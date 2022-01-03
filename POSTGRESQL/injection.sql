CREATE TABLE injection(
    injection_id			 SERIAL	 PRIMARY KEY 	NOT NULL,
    injection varchar(100) 					NOT NULL
);

GRANT SELECT, INSERT ON injection TO spravca;

GRANT UPDATE ON SEQUENCE injection_injection_id_seq to spravca;

insert into injection(injection) values ('ABCD');
insert into injection(injection) values ('ABCD');
insert into injection(injection) values ('ABCD');
insert into injection(injection) values ('ABCD');
insert into injection(injection) values ('ABCD');
insert into injection(injection) values ('ABCD');
insert into injection(injection) values ('ABCD');
insert into injection(injection) values ('ABCD');
insert into injection(injection) values ('ABCD');
insert into injection(injection) values ('ABCD');
