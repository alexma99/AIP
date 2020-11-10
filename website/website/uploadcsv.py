from django.http import HttpResponse
import pandas as pd
import psycopg2


def is_number(strng):
    try:
        float(strng)
        return True
    except ValueError:
        return False


def csv(filename, cur):
    filepath = r"D:\PycharmProjects\StudBase\csv\/"+filename
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
        cur.execute('''INSERT INTO '''+filename+''' VALUES ('''+string[:-2]+''');''')
    return


def page(request):
    con = psycopg2.connect(
        database="btj4y9qiryp7r9sizol0",
        user="uuugtksqbcxtzbutebat",
        password="VOLUCrmJtrbgdruOKPWw",
        host="btj4y9qiryp7r9sizol0-postgresql.services.clever-cloud.com",
        port="5432"
    )
    cur = con.cursor()
    cur.execute('''SET session_replication_role = 'replica';''')  # откл проверку ключей
    csv('discipline', cur)
    csv('group_st', cur)
    csv('kafedra', cur)
    csv('prepod', cur)
    csv('semester', cur)
    csv('student', cur)
    cur.execute('''SET session_replication_role = 'origin';''')  # вкл проверку ключей
    con.commit()
    con.close()
    return HttpResponse('Данные загружены')
