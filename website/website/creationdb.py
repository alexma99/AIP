from django.http import HttpResponse
import psycopg2

def page(request):
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="admin",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()
    """ 
	cur.execute('''CREATE TABLE TestTable  
             (ADMISSION INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL);''') 
    """
    con.commit()
    con.close()
    return HttpResponse('Базы данных загружены')