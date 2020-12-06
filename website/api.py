import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
from fastapi import FastAPI
import uvicorn
from portal.models import Discipline
from django.forms.models import model_to_dict


app = FastAPI()


@app.get("/")
async def read_item():
    return "Добро пожаловать. Для просмотра наберите {адрес сайта}/docs"


@app.get("/discipline/{id_disc}")
def read_item(id_disc):
    disc = Discipline.objects.get(pk=id_disc)
    return model_to_dict(disc)


@app.get("/group-st/{id_group}")
def read_item(id_group):
    disc = Discipline.objects.get(pk=id_group)
    return model_to_dict(disc)


@app.get("/kafedra/{id_kaf}")
def read_item(id_kaf):
    disc = Discipline.objects.get(pk=id_kaf)
    return model_to_dict(disc)


@app.get("/prepod/{id_prep}")
def read_item(id_prep):
    disc = Discipline.objects.get(pk=id_prep)
    return model_to_dict(disc)


@app.get("/result-of-midterms/{id_per}")
def read_item(id_per):
    disc = Discipline.objects.get(pk=id_per)
    return model_to_dict(disc)


@app.get("/semester/{id_sem}")
def read_item(id_sem):
    disc = Discipline.objects.get(pk=id_sem)
    return model_to_dict(disc)


@app.get("/student/{id_stud}")
def read_item(id_stud):
    disc = Discipline.objects.get(pk=id_stud)
    return model_to_dict(disc)


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000)

