create database final_project;

create table if not exists "person"(
	"person_id"		serial 		primary key unique not null,
	"name"			varchar(45)	not null,
	"surname"		varchar(45)	not null,
	"username"		varchar(45)	not null,
	"password"		varchar(90)
);

create table if not exists "relationship"(
	"relationship_id"		serial		primary key unique not null,
	"relationship_type"		varchar(45)	not null,
	"note"				varchar(255),
	"person_id1"			integer		not null,
	"person_id2"			integer		not null,
	foreign key ("person_id1") references "person",
	foreign key ("person_id2") references "person"
);

create table if not exists "contact"(
	"contact_id"			serial		primary key unique not null,
	"phone_num"			varchar(45),
	"mail"				varchar(45),
	"social_networks"		varchar(45),
	"person_id"			integer		not null,
	foreign key ("person_id") references "person"
);

create table if not exists "waiting_list"(
	"waiting_list_id"		serial		primary key unique not null,
	"date"				date 		not null,
	"order_num"			integer		not null,
	"doctor_id"			integer		not null,
	"patient_id"			integer		not null,
	foreign key ("doctor_id") references "person",
	foreign key ("patient_id") references "person"
);

create table if not exists "diagnosis_list"(
	"diagnosis_id"		serial		primary key unique not null,
	"diagnose"			varchar(45)	not null
);

create table if not exists "medical_record"(
	"record_id"			serial		primary key unique not null,
	"birth_id_number"		varchar(45)	not null,
	"birth_date"			date		not null,
	"insurance"			varchar(45)	not null,
	"person_id"			integer		not null,
	foreign key ("person_id") references "person"
);

create table if not exists "persons_diagnoses"(
	"record_id"			integer		not null,
	"diagnosis_id"			integer		not null,
	foreign key ("record_id") references "medical_record",
	foreign key ("diagnosis_id") references "diagnosis_list"
);

create table if not exists "address"(
	"address_id"			serial			primary key unique not null,
	"city"				varchar(45)		not null,
	"street"			varchar(45)		not null,
	"state"				varchar(45)		not null,
	"house_number"			varchar(45)		not null,
	"zip_code"			varchar(45)		not null
);

create table if not exists "persons_address"(
	"person_id"			integer		not null,
	"address_id"			integer		not null,
	foreign key ("person_id") references "person",
	foreign key ("address_id") references "address"
);

create table if not exists "location"(
	"location_id"			serial			primary key unique not null,
	"location"			varchar(45)		not null,
	"address_id"			integer			not null,
	foreign key	("address_id") references "address"
);

create table if not exists "medical_examination"(
	"examination_id"		serial			primary key unique not null,
	"title"				varchar(45)		not null,
	"note"				varchar(255),
	"location_id"			integer			not null,
	foreign key ("location_id") references "location"
);

create table if not exists "person_has_examination"(
	"booked"			boolean			not null,
	"date"				date,
	"time"				time,
	"examination_id"		integer			not null,
	"person_id"			integer			not null,
	foreign key ("examination_id") references "medical_examination",
	foreign key ("person_id") references person
);

create table if not exists "role"(
	"role_id"			serial			primary key unique not null,
	"role"				varchar(45)		not null
);

create table if not exists "persons_role"(
	"person_id"			integer			not null,
	"role_id"			integer			not null,
	foreign key ("person_id") references "person",
	foreign key ("role_id") references "role" 
)



