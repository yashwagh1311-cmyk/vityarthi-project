# Design Artefacts

## Architecture
CLI -> service layer -> repository layer -> SQLite.

## Workflow
Student selects a course and section -> course lookup -> duplicate check -> seat check -> prerequisite graph check -> section lookup -> interval overlap check -> registration saved -> personal timetable/report generated.

## Use Cases
Student: list courses, register, view timetable, inspect reports.
Academic coordinator/system: maintain course/section data and review seat/clash reports.

## Class Relationships
`RegistrationEngine` uses `CourseRepository`, `RegistrationRepository`, and `PrerequisiteGraph`. `ReportService` uses repositories. `Course` contains prerequisite course codes and `Section` contains a day/time interval.

## ER Diagram (text)
STUDENT 1---N REGISTRATION N---1 COURSE
COURSE 1---N SECTION
COURSE N---N COURSE through PREREQUISITES
REGISTRATION attempts that conflict are recorded in CLASH_LOGS.

## Algorithms
- Prerequisites: directed graph + Kahn topological sort.
- Timetable clashes: intervals overlap when `start1 < end2 && start2 < end1` on the same day.
- Seat utilization: registered count / course capacity.
