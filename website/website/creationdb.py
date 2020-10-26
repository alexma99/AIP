from django.http import HttpResponse
import psycopg2

def page(request):
    con = psycopg2.connect(
        database="DataBase",
        user="postgres",
        password="admin",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()
    cur.execute('''CREATE TABLE kafedra (
	id_kaf BIGSERIAL NOT NULL PRIMARY KEY,
	zaved VARCHAR(20),
	name VARCHAR(30)
);

CREATE TABLE group_st(
	id_group BIGSERIAL NOT NULL PRIMARY KEY,
	course INT,
	id_kaf BIGINT REFERENCES kafedra (id_kaf)
);

CREATE TABLE student(
id_stud BIGSERIAL NOT NULL PRIMARY KEY,
first_name VARCHAR(20),
last_name VARCHAR(20),
otchestvo VARCHAR(20),
date_of_birth DATE,
id_group BIGINT REFERENCES group_st (id_group)
);

CREATE TABLE semester(
	id_sem BIGSERIAL NOT NULL PRIMARY KEY,
	year INT
);

CREATE TABLE discipline(
	id_disc BIGSERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(20),
	id_kaf BIGINT REFERENCES kafedra (id_kaf)
);

CREATE TABLE prepod (
	id_prep BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	otchestvo VARCHAR(20),
	degree VARCHAR(20),
	id_disc BIGINT REFERENCES discipline (id_disc)
);



CREATE TABLE result_of_midterms (
	id_per BIGSERIAL NOT NULL PRIMARY KEY,
	mark INT,
	date DATE,
	id_stud BIGINT REFERENCES student (id_stud),
	id_sem BIGINT REFERENCES semester (id_sem),
	id_disc BIGINT REFERENCES discipline (id_disc),
	id_prep BIGINT REFERENCES prepod (id_prep)
);''')
    cur.execute('''ALTER TABLE discipline ADD id_prep BIGINT REFERENCES prepod(id_prep);
    ALTER TABLE prepod ADD id_kaf BIGINT REFERENCES kafedra(id_kaf);''')
    con.commit()
    con.close()
    return HttpResponse('Таблицы созданы')