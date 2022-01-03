CREATE VIEW person_contact AS
SELECT p.person_id, p.name, p.surname , c.phone_num, c.mail, m.birth_id_number FROM person p
JOIN contact c
ON p.person_id = c.person_id
JOIN medical_record m
ON p.person_id = m.person_id;

GRANT SELECT ON person_contact to spravca;
