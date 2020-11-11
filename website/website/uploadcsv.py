from django.http import HttpResponse
from sqlalchemy import create_engine
import pandas as pd


def is_number(strng):
    try:
        float(strng)
        return True
    except ValueError:
        return False


def csv(filename, engine):
    filepath = r"./csv/"+filename
    df = pd.read_csv(filepath, header=None)
    n = df.iloc[:, 1].size
    m = df.iloc[1, :].size
    for k in range(0, n):
        string = ""
        for j in range(0, m):
            if is_number(df.iloc[k, j]):
                string += str(df.iloc[k, j]) + ", "
            else:
                string += "'" + str(df.iloc[k, j]) + "', "
        engine.execute('''INSERT INTO '''+filename+''' VALUES ('''+string[:-2]+''');''')
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

    csv('discipline', engine)
    csv('group_st', engine)
    csv('kafedra', engine)
    csv('prepod', engine)
    csv('semester', engine)
    csv('student', engine)
    engine.close()
    return HttpResponse('Данные загружены')
