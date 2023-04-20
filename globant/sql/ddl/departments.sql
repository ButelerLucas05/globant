CREATE TABLE IF NOT EXISTS public.departments
(
    id integer NOT NULL,
    department character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT departments_pkey PRIMARY KEY (id)
)
