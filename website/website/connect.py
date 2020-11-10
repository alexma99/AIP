from django.http import HttpResponse
import psycopg2

def page(request):

    con = psycopg2.connect(
        database="btj4y9qiryp7r9sizol0",
        user="uuugtksqbcxtzbutebat",
        password="VOLUCrmJtrbgdruOKPWw",
        host="btj4y9qiryp7r9sizol0-postgresql.services.clever-cloud.com",
        port="5432"
    )
    con.close()
    return HttpResponse('Связь есть!')