CREATE TABLE Equipment ( 
 item_id INT PRIMARY KEY, 
 _name VARCHAR(100) NOT NULL, 
 _type VARCHAR(100) NOT NULL, 
 _manual TEXT 
); 
CREATE TABLE Device ( 
 item_id INT NOT NULL,
 device_number INT NOT NULL, 
 purchase_date DATE NOT NULL, 
 _status VARCHAR(20) NOT NULL, 
 PRIMARY KEY (item_id, device_number), 
 CONSTRAINT fk_device_item 
 FOREIGN KEY (item_id) REFERENCES Equipment(item_id) ON DELETE CASCADE, 
 CONSTRAINT chk_device__status
 CHECK (_status IN ('available', 'in_use', 'retired')) 
); 
CREATE TABLE LabMember ( -- self-foreign key revised.
 member_id INT PRIMARY KEY, 
 first_name VARCHAR(50) NOT NULL, 
 middle_name VARCHAR(50), 
 last_name VARCHAR(50) NOT NULL, 
 join_date DATE NOT NULL, 
 mentor_id INT,
 mentor_sdate DATE,
 mentor_edate DATE,
 CONSTRAINT chk_mentor_fk
 FOREIGN KEY (mentor_id) REFERENCES LabMember(member_id) ON DELETE SET NULL,
 CONSTRAINT chk_faculty_no_mentor
 CHECK (
  (mentor_id IS NULL AND mentor_sdate IS NULL AND mentor_edate IS NULL)
  OR
  (mentor_id IS NOT NULL AND mentor_sdate IS NOT NULL)
 ),
 CHECK (mentor_edate IS NULL OR mentor_sdate IS NULL OR mentor_edate >= mentor_sdate)
 
);

CREATE TABLE Faculty ( 
 member_id INT PRIMARY KEY, 
 department VARCHAR(100) NOT NULL, 
 CONSTRAINT fk_faculty_member 
 FOREIGN KEY (member_id) REFERENCES LabMember(member_id) ON DELETE CASCADE 
); 
CREATE TABLE Student ( 
 member_id INT PRIMARY KEY, 
 student_number VARCHAR(30) NOT NULL UNIQUE, 
 major VARCHAR(100) NOT NULL, 
 academic_level VARCHAR(30) NOT NULL, 
 CONSTRAINT fk_student_member 
 FOREIGN KEY (member_id) REFERENCES LabMember(member_id) ON DELETE CASCADE 
); 
CREATE TABLE Collaborator ( 
 member_id INT PRIMARY KEY, 
 institutional_affiliation VARCHAR(200) NOT NULL, 
 CV TEXT, 
 CONSTRAINT fk_collaborator_member 
 FOREIGN KEY (member_id) REFERENCES LabMember(member_id) ON DELETE CASCADE 
);
CREATE TABLE Publication ( 
 publication_id INT PRIMARY KEY, 
 title VARCHAR(300) NOT NULL, 
 publication_date DATE NOT NULL, 
 venue VARCHAR(200) NOT NULL, 
 doi VARCHAR(150) UNIQUE 
); 
CREATE TABLE Project ( 
 project_id INT PRIMARY KEY, 
 title VARCHAR(200) NOT NULL, 
 begin_date DATE NOT NULL, 
 end_date DATE, 
 duration INT, 
 _status VARCHAR(20) NOT NULL, 
 leader_id INT NOT NULL, 
 CONSTRAINT fk_project_leader 
 FOREIGN KEY (leader_id) REFERENCES Faculty(member_id) ON DELETE CASCADE, 
 CONSTRAINT chk_project__status
 CHECK (_status IN ('active', 'completed', 'paused')), 
 CONSTRAINT chk_project_dates 
 CHECK (end_date IS NULL OR end_date >= begin_date), 
 CONSTRAINT chk_project_duration 
 CHECK (duration IS NULL OR duration >= 0) 
); 
CREATE TABLE Grants ( 
 grant_id INT PRIMARY KEY, 
 funding_agency VARCHAR(200) NOT NULL, 
 budget DECIMAL(12,2) NOT NULL, 
 begin_date DATE NOT NULL, 
 planned_duration INT, 
 project_id INT UNIQUE NOT NULL, 
 CONSTRAINT fk_grant_project 
 FOREIGN KEY (project_id) REFERENCES Project(project_id) ON DELETE CASCADE, 
 CONSTRAINT chk_grant_budget 
 CHECK (budget > 0), 
 CONSTRAINT chk_grant_duration 
 CHECK (planned_duration IS NULL OR planned_duration >= 0) ); 
 
CREATE TABLE Works_On ( 
 project_id INT NOT NULL, 
 member_id INT NOT NULL, 
 hours_of_involvement DECIMAL(5,2) NOT NULL,
 _role VARCHAR(100) NOT NULL, 
 PRIMARY KEY (project_id, member_id), 
 CONSTRAINT fk_workson_project 
 FOREIGN KEY (project_id) REFERENCES Project(project_id) 
 ON DELETE CASCADE, 
 CONSTRAINT fk_workson_member 
 FOREIGN KEY (member_id) REFERENCES LabMember(member_id) ON DELETE CASCADE, 
 CONSTRAINT chk_workson_hours 
 CHECK (hours_of_involvement >= 0) 
); 
CREATE TABLE Uses ( 
 member_id INT NOT NULL, 
 item_id INT NOT NULL, 
 device_number INT NOT NULL, 
 begin_date DATE NOT NULL, 
 end_date DATE, 
 purpose_of_use VARCHAR(300) NOT NULL, 
 PRIMARY KEY (member_id, item_id, device_number), 
 CONSTRAINT fk_uses_member 
 FOREIGN KEY (member_id) REFERENCES LabMember(member_id) ON DELETE CASCADE, 
 CONSTRAINT fk_uses_device 
 FOREIGN KEY (item_id, device_number) REFERENCES Device(item_id, device_number) ON DELETE CASCADE, 
 CONSTRAINT chk_uses_dates 
 CHECK (end_date IS NULL OR end_date >= begin_date) 
);
CREATE TABLE Authors ( 
 member_id INT NOT NULL, 
 publication_id INT NOT NULL, 
 PRIMARY KEY (member_id, publication_id), 
 CONSTRAINT fk_authors_member 
 FOREIGN KEY (member_id) REFERENCES LabMember(member_id) 
 ON DELETE CASCADE, 
 CONSTRAINT fk_authors_publication 
 FOREIGN KEY (publication_id) REFERENCES Publication(publication_id) ON DELETE CASCADE 
); 