CREATE TABLE IF NOT EXISTS public.jobs
(
    id integer NOT NULL,
    job character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT jobs_pkey PRIMARY KEY (id)
)
