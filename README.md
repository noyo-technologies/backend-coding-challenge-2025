# Employee Location Tracking System

## Overview
Welcome to the Employee Location Tracking System! This system helps companies manage and track where their employees are located over time, which is crucial for compliance, resource allocation, and workforce planning.

## Domain Context

### What are Segments?
A segment represents a period of time when an employee is located in a specific place. Think of it as a "stay" or "assignment" at a particular location. For example:
- An employee working from the San Francisco office from January to March
- A remote worker based in Houston starting from April
- A temporary assignment in New York for two weeks

Each segment has:
- A start date (when the employee arrived at the location)
- An optional end date (when they left)
- Location details (city, state, zip code)

### Why is this Important?
Companies need to track employee locations for various reasons:
- Tax compliance (different states have different tax rules)
- Resource allocation (knowing where talent is located)
- Emergency response (knowing who's in which office)
- Workforce planning (understanding mobility patterns)

## The Challenge

### Background
You're joining a fast-growing tech company that's rapidly expanding across multiple locations. The company has been manually tracking employee locations in spreadsheets, but this is becoming unsustainable as they:
- Open new offices
- Allow more remote work
- Need real-time location data
- Require better compliance reporting

### Your Mission
Build a robust system to manage employee location segments that can:
1. Track where employees are located over time
2. Handle complex scenarios like overlapping assignments
3. Provide insights about employee mobility
4. Scale as the company grows

## Take-Home Exercise (Optional)
To help you prepare for the interview, you can optionally implement the basic segment management system (see `BASIC.md`). This quick exercise (should take no more than 5 minutes) will help you understand the core domain concepts before the interview.

### Quick Start
1. Clone this repository
2. Implement the `PUT /api/persons/<person_id>/segment` endpoint
3. Follow the requirements in `BASIC.md`
4. Be ready to discuss your implementation

Note: This is an optional exercise. You can also come to the interview fresh and we'll work through the basic implementation together.

## Using Modern Tools

We embrace modern development tools and workflows. During your interview:

- **Feel free to use any tools you'd normally use** - Including Google, Stack Overflow, or documentation
- **We encourage the use of AI assistants** - We use Cursor at our company, and your interview will mirror how we actually collaborate on problems. We're interested in how you leverage these tools effectively as part of your workflow.
- **Be prepared to explain your approach** - The ability to effectively integrate modern tools while maintaining critical thinking and sound engineering judgment is a valuable skill. We want to see how you combine your expertise with the tools available to solve complex problems efficiently.

## Interview Structure
The interview will consist of four parts, each building upon the previous:
1. Basic Segment Management (pre-work)
2. Analytics and Validation
3. Multi-Person Relationships
4. Real-Time and Geospatial Features

Each part will test different aspects of system design, implementation, and problem-solving skills.

## Getting Started
1. Review the requirements in `BASIC.md`
2. Set up your development environment
3. Implement the basic segment management system
4. Be prepared to discuss your implementation and tackle more complex challenges during the interview

Good luck!
