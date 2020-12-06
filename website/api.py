from sqlalchemy import create_engine
from fastapi import FastAPI
import pandas as pd
import time
import uvicorn


def connect():
    database = "btj4y9qiryp7r9sizol0"
    user = "uuugtksqbcxtzbutebat"
    pwd = "VOLUCrmJtrbgdruOKPWw"
    host = "btj4y9qiryp7r9sizol0-postgresql.services.clever-cloud.com"
    port = "5432"

    conn_string = "{driver}://{user}:{pwd}@{host}:{port}/{database}".format(
        driver="postgresql+psycopg2",
        user=user,
        pwd=pwd,
        host=host,
        port=port,
        database=database,
    )
    engine = create_engine(conn_string)
    return engine


def discipline_get(id_disc, engine=connect()):
    df = pd.read_sql_query("SELECT * FROM discipline WHERE id_disc = %s" % id_disc, engine, index_col='id_disc')
    return df.to_dict(orient='index')


def group_st_get(id_group, engine=connect()):
    df = pd.read_sql_query("SELECT * FROM group_st WHERE id_group = %s" % id_group, engine, index_col='id_group')
    return df.to_dict(orient='index')


def kafedra_get(id_kaf, engine=connect()):
    df = pd.read_sql_query("SELECT * FROM kafedra WHERE id_kaf = %s" % id_kaf, engine, index_col='id_kaf')
    return df.to_dict(orient='index')


def prepod_get(id_prep, engine=connect()):
    df = pd.read_sql_query("SELECT * FROM prepod WHERE id_prep = %s" % id_prep, engine, index_col='id_prep')
    return df.to_dict(orient='index')


def result_of_midterms_get(id_per, engine=connect()):
    df = pd.read_sql_query("SELECT * FROM result_of_midterms WHERE id_per = %s" % id_per, engine, index_col='id_per')
    return df.to_dict(orient='index')


def semester_get(id_sem, engine=connect()):
    df = pd.read_sql_query("SELECT * FROM semester WHERE id_sem = %s" % id_sem, engine, index_col='id_sem')
    return df.to_dict(orient='index')


def student_get(id_stud, engine=connect()):
    df = pd.read_sql_query("SELECT * FROM student WHERE id_stud = %s" % id_stud, engine, index_col='id_stud')
    return df.to_dict(orient='index')


app = FastAPI()


@app.get("/")
async def read_item():
    return "Добро пожаловать. Для просмотра наберите {адрес сайт}/docs"


@app.get("/discipline/{id}")
async def read_item(id):
    return discipline_get(id)


@app.get("/group-st/{id}")
async def read_item(id):
    return group_st_get(id)


@app.get("/kafedra/{id}")
async def read_item(id):
    return kafedra_get(id)


@app.get("/prepod/{id}")
async def read_item(id):
    return prepod_get(id)


@app.get("/result-of-midterms/{id}")
async def read_item(id):
    return result_of_midterms_get(id)


@app.get("/semester/{id}")
async def read_item(id):
    return semester_get(id)


@app.get("/student/{id}")
async def read_item(id):
    return student_get(id)


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000)

