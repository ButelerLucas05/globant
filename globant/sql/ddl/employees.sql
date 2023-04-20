CREATE TABLE IF NOT EXISTS public.employees
(
    id integer NOT NULL,
    name character varying(200) COLLATE pg_catalog."default",
    datetime timestamp with time zone,
    department_id integer,
    job_id integer,
    CONSTRAINT employees_pkey PRIMARY KEY (id)
)