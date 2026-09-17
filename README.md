# Campus Course Registration & Timetable Conflict Resolver

A command-line Java application that manages students and courses, checks prerequisites and seat limits, detects timetable clashes, and generates personal timetables.

## Requirements
- Java 17+
- Maven 3.8+

## Run from terminal
```bash
mvn clean test
mvn package
java -jar target/campus-course-registration-1.0.0.jar
```

No GUI or external database server is required. SQLite is created at `data/campus.db` on first execution.

## Features
1. Student/course/section management
2. Registration engine with seat limits
3. Graph-based prerequisite validation with topological sort
4. Interval overlap detection for timetable clashes
5. Custom `SeatFullException`, `PrerequisiteNotMetException`, and `TimetableConflictException`
6. Personal timetable generation
7. Seat-utilization and clash-log reports
8. SQLite persistence through JDBC
9. JUnit 5 tests

## CLI
The program starts with sample data and student `S1001`. Use the menu to list courses, register, view the timetable, inspect seat utilization, inspect clash logs, and display prerequisite order.

## Structure
```text
src/main/java/com/campus/registration
├── Main.java
├── model
├── exception
├── repository
├── service
├── report
└── util
src/test/java/com/campus/registration
docs/design.md
sql/schema.sql
statement.md
```

## Test Cases
`mvn test` validates interval overlap, topological prerequisite order, and seat-full handling. The CLI also demonstrates prerequisite and clash rejection.

## Design
The architecture is CLI -> services -> repositories -> SQLite. Prerequisites form a directed graph. A registration is accepted only after course existence, duplicate, capacity, prerequisite, section, and timetable constraints pass.

## Submission Notes
Keep this repository public and submit the repository root URL only: `https://github.com/yashwagh1311-cmyk/vityarthi-project`.
