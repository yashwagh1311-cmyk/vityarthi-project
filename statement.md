# Problem Statement
Campus course registration becomes difficult when students must satisfy prerequisites, compete for limited seats, and avoid timetable clashes. Manual checking can cause invalid registrations and conflicting schedules.

# Scope
The project provides command-line student/course management, prerequisite validation, seat-limit enforcement, timetable interval conflict detection, personal timetable generation, and reporting. SQLite is used for persistence.

# Target Users
Students, academic coordinators, and evaluators demonstrating registration algorithms.

# High-Level Features
- Student and course records
- Course sections and capacities
- Graph-based prerequisite checking using topological sort
- Interval overlap detection
- Custom registration exceptions
- Seat utilization and clash logs
- CLI execution and automated tests
