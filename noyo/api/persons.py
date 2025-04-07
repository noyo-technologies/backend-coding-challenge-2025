from flask import Blueprint, abort, jsonify, request
from sqlalchemy import and_

from noyo.extensions import db
from noyo.models.person import Person
from noyo.models.segment import Segment

persons_bp = Blueprint("persons", __name__)


@persons_bp.route("/api/persons", methods=["GET"])
def get_persons():
    persons = Person.query.all()
    return jsonify(
        [
            {
                "id": p.id,
                "first_name": p.first_name,
                "last_name": p.last_name,
                "created_at": p.created_at,
                "updated_at": p.updated_at,
            }
            for p in persons
        ]
    )


@persons_bp.route("/api/persons/<int:person_id>", methods=["GET"])
def get_person(person_id):
    person = Person.query.get_or_404(person_id)
    return jsonify(
        {
            "id": person.id,
            "first_name": person.first_name,
            "last_name": person.last_name,
            "created_at": person.created_at,
            "updated_at": person.updated_at,
        }
    )


@persons_bp.route("/api/persons", methods=["PUT"])
def create_person():
    data = request.get_json()
    person = Person(**data)
    db.session.add(person)
    db.session.commit()
    return (
        jsonify(
            {
                "id": person.id,
                "first_name": person.first_name,
                "last_name": person.last_name,
                "created_at": person.created_at,
                "updated_at": person.updated_at,
            }
        ),
        201,
    )


@persons_bp.route("/api/persons/<int:person_id>/segment", methods=["PUT"])
def create_segment(person_id):
    # TODO: Gone fishing, this code is not ready for production yet

    data = request.get_json()

    new_segment = Segment(
        person_id=person_id,
        start_date=data.get("start_date"),
        end_date=data.get("end_date"),
        city=data.get("city"),
        state=data.get("state"),
        zip_code=data.get("zip_code"),
    )

    db.session.add(new_segment)
    db.session.commit()

    return jsonify({"message": "Segment created"}), 201
