from django.http import HttpResponse
from django.db import IntegrityError
from sqlalchemy import create_engine
import pandas as pd
import time


def csv(filename, engine):
    filepath = r"./csv/"+filename+".csv"
    df = pd.read_csv(filepath, sep=';', index_col=0)
    df.to_sql(filename, engine, if_exists="append")
    time.sleep(3)
    return


def page(request):
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
    try:
        csv('semester', engine)
        csv('kafedra', engine)
        csv('discipline', engine)
        csv('prepod', engine)
        csv('group_st', engine)
        csv('student', engine)
        csv('result_of_midterms', engine)
    except IntegrityError:
        return HttpResponse('Данные не удалось загрузить')
    return HttpResponse('Данные успешно загружены')
