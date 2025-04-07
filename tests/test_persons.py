import pytest

from noyo import create_app
from noyo.extensions import db
from noyo.models.person import Person


@pytest.fixture
def client():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()


def test_create_person(client):
    response = client.put(
        "/api/persons", json={"first_name": "John", "last_name": "Doe"}
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"
    assert "id" in data
    assert "created_at" in data


def test_get_person(client):
    # Create a person first
    with client.application.app_context():
        person = Person(first_name="John", last_name="Doe")
        db.session.add(person)
        db.session.commit()
        person_id = person.id

    response = client.get(f"/api/persons/{person_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"


def test_get_persons(client):
    # Create multiple persons
    with client.application.app_context():
        db.session.add(Person(first_name="John", last_name="Doe"))
        db.session.add(Person(first_name="Jane", last_name="Smith"))
        db.session.commit()

    response = client.get("/api/persons")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]["first_name"] in ["John", "Jane"]
    assert data[1]["first_name"] in ["John", "Jane"]


def test_get_nonexistent_person(client):
    response = client.get("/api/persons/999")
    assert response.status_code == 404
