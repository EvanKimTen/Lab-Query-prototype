-- LabMember
INSERT INTO LabMember (member_id, first_name, middle_name, last_name, join_date, mentor_id, mentor_sdate, mentor_edate)
VALUES (1, 'John', NULL, 'Kim', '2022-01-10', NULL, NULL, NULL);
INSERT INTO LabMember VALUES (2, 'Alice', NULL, 'Lee', '2022-02-15', NULL, NULL, NULL);
INSERT INTO LabMember VALUES (3, 'Brian', NULL, 'Park', '2022-03-20', NULL, NULL, NULL);
INSERT INTO LabMember VALUES (4, 'Sarah', NULL, 'Xiang', '2022-04-05', 1, '2023-03-01', NULL);
INSERT INTO LabMember VALUES (5, 'David', NULL, 'Zhang', '2023-01-12', 1, '2023-04-01', NULL);
INSERT INTO LabMember VALUES (6, 'Emma', NULL, 'Brown', '2023-02-18', 2, '2023-05-01', NULL);
INSERT INTO LabMember VALUES (7, 'John', NULL, 'Johnson', '2023-03-25', 2, '2023-06-01', NULL);
INSERT INTO LabMember VALUES (8, 'Micheal', NULL, 'Miller', '2023-04-14', 1, '2023-07-01', NULL);
INSERT INTO LabMember VALUES (9, 'Daniel', NULL, 'Wilson', '2023-05-09', 2, '2023-08-01', NULL);
INSERT INTO LabMember VALUES (10, 'Andrej', NULL, 'Zarzycki', '2023-06-01', 3, '2023-09-01', NULL);
INSERT INTO LabMember VALUES (11, 'Robert', 'Tappan', 'Morris', '2023-02-03', 3, '2023-09-01', NULL);
INSERT INTO LabMember VALUES (12, 'Eric', NULL, 'Green', '2023-06-01', 3, '2023-09-01', NULL);

INSERT INTO Faculty (member_id, department)
VALUES (1, 'Computer Science');
INSERT INTO Faculty VALUES (2, 'Data Science');
INSERT INTO Faculty VALUES (3, 'CyberSecurity');

INSERT INTO Student (member_id, student_number, major, academic_level)
VALUES (4, 'S1001', 'CS', 'MS');
INSERT INTO Student VALUES (5, 'S1002', 'CS', 'MS');
INSERT INTO Student VALUES (6, 'S1003', 'DS', 'MS');
INSERT INTO Student VALUES (7, 'S1004', 'DS', 'PhD');
INSERT INTO Student VALUES (11, 'S1005', 'Security', 'PhD');
INSERT INTO Student VALUES (12, 'S1006', 'Security', 'PhD');

INSERT INTO Collaborator (member_id, institutional_affiliation, CV)
VALUES (8, 'Stanford University - Visiting Researcher', 'Short CV: AI researcher with 3 years of lab collaboration experience.');
INSERT INTO Collaborator VALUES (9, 'MIT - External Advisor', 'Short CV: Database systems researcher focused on query optimization.');
INSERT INTO Collaborator VALUES (10, 'Google Research - Industry Collaborator', 'Short CV: Applied ML engineer working on privacy-preserving analytics.');

INSERT INTO Project (project_id, title, begin_date, end_date, duration, _status, leader_id)
VALUES (1, 'Automata Project', '2024-01-01', NULL, 12, 'active', 1);
INSERT INTO Project VALUES (2, 'Data Management Project', '2024-01-02', NULL, 12, 'active', 2);
INSERT INTO Project VALUES (3, 'Applied ML Project', '2024-01-03', NULL, 12, 'active', 3);
INSERT INTO Project VALUES (4, 'Clickjacking Defense Project', '2024-01-04', NULL, 12, 'active', 3);
INSERT INTO Project
VALUES
(10, 'Cancer Cell Imaging', '2022-01-01', '2023-06-30', 18, 'completed', 1),
(11, 'AI Drug Discovery', '2023-01-15', '2023-12-15', 11, 'completed', 2),
(12, 'Quantum Sensor Lab', '2023-05-01', '2024-03-01', 10, 'active', 1),
(13, 'Protein Folding Study', '2021-09-01', '2022-12-20', 15, 'completed', 3);
INSERT INTO Project
VALUES
(20, 'Completed AI Lab', '2022-01-01', '2023-06-30', 18, 'completed', 1),
(21, 'Completed Security Lab', '2022-05-01', '2023-12-15', 19, 'completed', 2),
(22, 'Still Active Robotics Lab', '2023-01-01', '2024-05-30', 16, 'active', 1);

INSERT INTO Works_On(project_id, member_id, hours_of_involvement, _role)
VALUES (1, 1, 15, 'Leader');
INSERT INTO Works_On VALUES (1, 4, 15, 'Researcher');
INSERT INTO Works_On VALUES (1, 5, 15, 'Researcher');
INSERT INTO Works_On VALUES (1, 8, 20, 'Researcher');
INSERT INTO Works_On VALUES (2, 2, 10, 'Leader');
INSERT INTO Works_On VALUES (2, 6, 20, 'Researcher');
INSERT INTO Works_On VALUES (2, 7, 20, 'Researcher');
INSERT INTO Works_On VALUES (3, 3, 20, 'Leader');
INSERT INTO Works_On VALUES (3, 11, 20, 'Researcher');
INSERT INTO Works_On VALUES (3, 12, 20, 'Researcher');

------------------------------------------------------------------------------------------------------------------------------------------------

INSERT INTO Equipment(item_id, _name, _type, _manual)
VALUES (1, 'GPU Workstation', 'Computer', 'Manual for GPU workstation');
INSERT INTO Equipment VALUES (2, '3D Printer', 'Manufacturing', 'Manual for 3D printer');
INSERT INTO Equipment VALUES (3, 'Microscope', 'Optical', 'Manual for microscope');
INSERT INTO Equipment VALUES (4, 'Sensor Kit', 'IoT', 'Manual for sensor kit');
INSERT INTO Equipment VALUES (5, 'Network Analyzer', 'Networking', 'Manual for network analyzer');
INSERT INTO Equipment VALUES (6, 'Raspberry Pi Kit', 'Embedded System', 'Manual for Raspberry Pi kit');

INSERT INTO Device(item_id, device_number, purchase_date, _status)
VALUES (1, 1, '2022-01-01', 'available');
INSERT INTO Device VALUES (1, 2, '2022-03-01', 'in_use');
INSERT INTO Device VALUES (2, 1, '2021-09-15', 'available');
INSERT INTO Device VALUES (2, 2, '2022-10-10', 'in_use');
INSERT INTO Device VALUES (3, 1, '2020-05-20', 'available');
INSERT INTO Device VALUES (3, 2, '2021-06-25', 'retired');
INSERT INTO Device VALUES (4, 1, '2023-03-12', 'in_use');
INSERT INTO Device VALUES (4, 2, '2023-04-01', 'available');
INSERT INTO Device VALUES (5, 1, '2022-11-30', 'available');
INSERT INTO Device VALUES (6, 1, '2023-07-18', 'in_use');

INSERT INTO Uses(member_id, item_id, device_number, begin_date, end_date, purpose_of_use)
VALUES (3, 1, 1, '2024-04-01', NULL, 'Experiment');
INSERT INTO Uses VALUES (4, 1, 1, '2024-02-01', NULL, 'Training automata detection model');
INSERT INTO Uses VALUES (5, 1, 2, '2024-02-05', NULL, 'Running ML experiments');
INSERT INTO Uses VALUES (6, 2, 1, '2024-03-01', NULL, 'Printing lab prototype');
INSERT INTO Uses VALUES (7, 2, 2, '2024-03-10', '2024-03-20', 'Completed prototype casing print');
INSERT INTO Uses VALUES (8, 3, 1, '2024-04-01', NULL, 'Collecting image data');
INSERT INTO Uses VALUES (11, 4, 1, '2024-04-05', NULL, 'Sensor data collection');
INSERT INTO Uses VALUES (12, 6, 1, '2024-04-10', NULL, 'Embedded system testing');


------------------------------------------------------------------------------------------------------------------------------------------------

INSERT INTO Publication(publication_id, title, publication_date, venue, doi)
VALUES (1, 'Automata-Based Pattern Detection', '2024-02-10', 'ACM Computing Survey', '10.1000/pub001');
INSERT INTO Publication VALUES (2, 'Efficient Database Management for Research Labs', '2024-03-15', 'VLDB Workshop', '10.1000/pub002'); 
INSERT INTO Publication VALUES (3, 'Applied Machine Learning for Student Data', '2024-04-20', 'IEEE Access', '10.1000/pub003'); -- 2
INSERT INTO Publication VALUES (4, 'Clickjacking Defense in Modern Web Systems', '2024-05-12', 'USENIX Security Poster', '10.1000/pub004'); -- 3
INSERT INTO Publication VALUES (5, 'Privacy-Aware Data Analytics', '2023-11-05', 'PETS Workshop', '10.1000/pub005'); -- 3
INSERT INTO Publication VALUES (6, 'Secure Authorization Models for Lab Systems', '2023-09-18', 'ACM SACMAT', '10.1000/pub006'); -- 3
INSERT INTO Publication VALUES (7, 'InContext Model agianst the Clickjacking attacks', '2022-08-22', 'ICML Workshop', '10.1000/pub007'); -- 3
INSERT INTO Publication VALUES (8, 'Database Query Optimization in Academic Systems', '2022-10-30', 'SIGMOD Demo', '10.1000/pub008'); -- 2

INSERT INTO Grants(grant_id, funding_agency, budget, begin_date, planned_duration, project_id)
VALUES (1, 'NSF', 75000.00, '2024-01-01', 12, 1);
INSERT INTO Grants VALUES (2, 'NIH', 50000.00, '2024-01-02', 12, 2);
INSERT INTO Grants VALUES (3, 'DARPA', 120000.00, '2024-01-03', 12, 3);
INSERT INTO Grants VALUES (4, 'Google Research', 45000.00, '2024-01-04', 12, 4);
INSERT INTO Grants
VALUES
(301, 'NSF', 50000, '2022-01-01', 18, 20),
(302, 'NIH', 70000, '2022-05-01', 19, 21),
(303, 'DOE', 90000, '2023-01-01', 16, 22);

INSERT INTO Authors(member_id, publication_id)
VALUES (1, 1);
INSERT INTO Authors VALUES (4, 1);
INSERT INTO Authors VALUES (5, 1);

INSERT INTO Authors VALUES (2, 2);
INSERT INTO Authors VALUES (6, 2);
INSERT INTO Authors VALUES (7, 2);

INSERT INTO Authors VALUES (2, 3);
INSERT INTO Authors VALUES (7, 3);

INSERT INTO Authors VALUES (3, 4);
INSERT INTO Authors VALUES (11, 4);
INSERT INTO Authors VALUES (12, 4);

INSERT INTO Authors VALUES (3, 5);
INSERT INTO Authors VALUES (10, 5);

INSERT INTO Authors VALUES (10, 6);
INSERT INTO Authors VALUES (11, 6);

INSERT INTO Authors VALUES (3, 7);
INSERT INTO Authors VALUES (10, 7);
INSERT INTO Authors VALUES (11, 7);
INSERT INTO Authors VALUES (12, 7);

INSERT INTO Authors VALUES (2, 8);
INSERT INTO Authors VALUES (6, 8);
INSERT INTO Authors VALUES (9, 8);