--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

ALTER TABLE IF EXISTS ONLY public.question DROP CONSTRAINT IF EXISTS pk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS pk_answer_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS fk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS pk_comment_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS fk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS fk_answer_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS pk_question_tag_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS fk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.tag DROP CONSTRAINT IF EXISTS pk_tag_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS fk_tag_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.question DROP CONSTRAINT IF EXISTS fk_user_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS fk_user_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS fk_user_id CASCADE;


DROP TABLE IF EXISTS public.question;
DROP SEQUENCE IF EXISTS public.question_id_seq;
CREATE TABLE question (
    id serial NOT NULL,
    submission_time timestamp without time zone,
    view_number integer,
    vote_number integer,
    title text,
    message text,
    image text,
    user_id integer
);

DROP TABLE IF EXISTS public.answer;
DROP SEQUENCE IF EXISTS public.answer_id_seq;
CREATE TABLE answer (
    id serial NOT NULL,
    submission_time timestamp without time zone,
    vote_number integer,
    question_id integer,
    message text,
    image text,
    user_id integer
);

DROP TABLE IF EXISTS public.comment;
DROP SEQUENCE IF EXISTS public.comment_id_seq;
CREATE TABLE comment (
    id serial NOT NULL,
    question_id integer,
    answer_id integer,
    message text,
    submission_time timestamp without time zone,
    edited_count integer,
    user_id integer
);


DROP TABLE IF EXISTS public.question_tag;
CREATE TABLE question_tag (
    question_id integer NOT NULL,
    tag_id integer NOT NULL
);

DROP TABLE IF EXISTS public.tag;
DROP SEQUENCE IF EXISTS public.tag_id_seq;
CREATE TABLE tag (
    id serial NOT NULL,
    name text
);

DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.users_seq;
create table users
(
	id serial
		constraint users_pk
			primary key,
	name text NOT NULL,
	password text
);


ALTER TABLE ONLY answer
    ADD CONSTRAINT pk_answer_id PRIMARY KEY (id);

ALTER TABLE ONLY comment
    ADD CONSTRAINT pk_comment_id PRIMARY KEY (id);

ALTER TABLE ONLY question
    ADD CONSTRAINT pk_question_id PRIMARY KEY (id);

ALTER TABLE ONLY question_tag
    ADD CONSTRAINT pk_question_tag_id PRIMARY KEY (question_id, tag_id);

ALTER TABLE ONLY tag
    ADD CONSTRAINT pk_tag_id PRIMARY KEY (id);

ALTER TABLE ONLY comment
    ADD CONSTRAINT fk_answer_id FOREIGN KEY (answer_id) REFERENCES answer(id);

ALTER TABLE ONLY answer
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES question(id);

ALTER TABLE ONLY question_tag
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES question(id);

ALTER TABLE ONLY comment
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES question(id);

ALTER TABLE ONLY question_tag
    ADD CONSTRAINT fk_tag_id FOREIGN KEY (tag_id) REFERENCES tag(id);

ALTER TABLE ONLY question
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE ONLY answer
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE ONLY comment
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);

INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (0, '2017-04-28 08:29:00.000000', 29, 7, 'Who is your favourite mentor at Codecool?', 'Who was the most helpful and friendly? Who has the most hardskills?', null);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (6, '2019-11-15 08:00:39.000000', null, null, 'I have a database with all the countries in it. I need every country which starts with the letter ''E''.', 'Which should I use?
SELECT name FROM countries
WHERE name LIKE ''E_'';
or rather
SELECT name FROM countries
WHERE name LIKE ''E%'';
?', null);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (7, '2019-11-15 09:04:51.000000', null, null, 'What is the difference between the SCRUM Master and the Product Owner?', 'Could someone please specify the differences between their roles?', null);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (8, '2019-11-15 09:23:56.000000', null, null, 'How long does it take to climb the Mt. Everest?', 'Can you guys give me an estimation?', null);
SELECT pg_catalog.setval('question_id_seq', 8, true);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (16, '2019-11-15 00:58:59.000000', null, 0, 'Gábor and Rudi from the green room are awesome!', null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (18, '2019-11-15 01:02:56.000000', null, 0, 'One of the Terray brothers helped me a lot once, but as I can''t tell them apart, I don''t know which one :(', null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (17, '2019-11-15 01:00:13.000000', null, 0, 'I enjoyed being in the white room with Árpi and Laci.', null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (19, '2019-11-15 08:57:15.000000', null, 6, 'You should use the second one.
SELECT name FROM countries
WHERE name LIKE ''E%'';', null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (20, '2019-11-15 09:24:20.000000', null, 8, 'I would get there in 2 days.', null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (21, '2019-11-15 09:24:35.000000', null, 8, 'A month, if you are properly trained.', null);
SELECT pg_catalog.setval('answer_id_seq', 21, true);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (32, 0, 16, 'Do you say that only because your answer is in the presentation?', null, null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (33, 6, null, 'The second one.', null, null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (34, 6, 19, 'Thank you, it is working.', null, null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (35, 8, null, 'Could you please specify? From where do you start? Which route do you take? What''s your training level?', null, null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (36, 8, 21, '1 day.', null, null);
SELECT pg_catalog.setval('comment_id_seq', 36, true);
INSERT INTO public.tag (id, name) VALUES (1, 'python');
INSERT INTO public.tag (id, name) VALUES (2, 'sql');
INSERT INTO public.tag (id, name) VALUES (3, 'css');
SELECT pg_catalog.setval('tag_id_seq', 3, true);
