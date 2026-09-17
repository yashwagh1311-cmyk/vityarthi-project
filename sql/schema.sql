CREATE TABLE students(id TEXT PRIMARY KEY,name TEXT,program TEXT,semester INTEGER);
CREATE TABLE courses(code TEXT PRIMARY KEY,name TEXT,credits INTEGER,capacity INTEGER);
CREATE TABLE prerequisites(course TEXT,prereq TEXT,PRIMARY KEY(course,prereq));
CREATE TABLE sections(course TEXT,section TEXT,day TEXT,start INTEGER,end INTEGER,room TEXT,PRIMARY KEY(course,section));
CREATE TABLE registrations(student TEXT,course TEXT,section TEXT,PRIMARY KEY(student,course));
CREATE TABLE clash_logs(student TEXT,course TEXT,message TEXT,created_at DATETIME DEFAULT CURRENT_TIMESTAMP);
