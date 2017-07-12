
CREATE TABLE reading (
    value text,
    createdon timestamp without time zone DEFAULT now(),
    name text
);

ALTER TABLE public.reading OWNER TO pi;

