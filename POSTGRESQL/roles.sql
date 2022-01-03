CREATE USER spravca WITH PASSWORD 'root';

GRANT SELECT, DELETE, INSERT, UPDATE ON public.person TO spravca;
GRANT SELECT, DELETE, INSERT, UPDATE ON public.contact TO spravca;
GRANT UPDATE ON SEQUENCE public.contact_contact_id_seq to spravca;
GRANT UPDATE ON SEQUENCE public.person_person_id_seq to spravca;
