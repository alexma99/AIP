import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
from fastapi import FastAPI
import uvicorn
from portal.models import *
from django.forms.models import model_to_dict


app = FastAPI()


@app.get("/")
async def read_item():
    return "Добро пожаловать. Для просмотра наберите {адрес сайта}/docs"


@app.get("/disc/{id_disc}")
def read(id_disc):
    return model_to_dict(Discipline.objects.get(pk=id_disc))


@app.delete("/del-disc/{id_disc}")
def delete(id_disc):
    Discipline.objects.filter(pk=id_disc).delete()
    Kafedra.objects.filter(id_disc=id_disc).delete()
    ResultOfMidterms.objects.filter(id_disc=id_disc).delete()
    return "Deleted"


@app.put("/changeDisc/{oldname}")
def update(oldname: str, newname: str):
    b = Discipline.objects.get(name=oldname)
    b.name = newname
    b.save()
    b = Kafedra.objects.get(name=oldname)
    b.name = newname
    b.save()
    return "oldname: "+oldname+" -> newname: "+newname


@app.get("/group-st/{id_group}")
def read(id_group):
    return model_to_dict(GroupSt.objects.get(pk=id_group))


@app.delete("/del-group/{id_group}")
def delete(id_group):
    GroupSt.objects.filter(pk=id_group).delete()
    Student.objects.filter(id_group=id_group).delete()
    return "Deleted"


@app.get("/kafedra/{id_kaf}")
def read(id_kaf):
    return model_to_dict(Kafedra.objects.get(pk=id_kaf))


@app.delete("/del-kaf/{id_kaf}")
def delete(id_kaf):
    Kafedra.objects.filter(pk=id_kaf).delete()
    Discipline.objects.filter(id_kaf=id_kaf).delete()
    GroupSt.objects.filter(id_kaf=id_kaf).delete()
    return "Deleted"


@app.get("/prepod/{id_prep}")
def read(id_prep):
    return model_to_dict(Prepod.objects.get(pk=id_prep))


@app.delete("/del-prep/{id_prep}")
def delete(id_prep):
    Kafedra.objects.filter(pk=id_prep).delete()
    return "Deleted"


@app.put("/disc-for-prep/{id_prep}")
def update(id_prep: int, old_id_disc: int, new_id_disc: int):
    b = Prepod.objects.get(pk=id_prep, id_disc=old_id_disc)
    b.id_disc = new_id_disc
    b.save()
    return "id_disc: "+old_id_disc+" -> newdisc: "+new_id_disc


@app.put("/degree/{id_prep}")
def update(id_prep: int, degree: str):
    b = Prepod.objects.get(pk=id_prep)
    c = b.degree
    b.degree = degree
    b.save()
    return "degree: "+c+" -> "+degree


@app.get("/result-of-midterms/{id_per}")
def read(id_per):
    return model_to_dict(ResultOfMidterms.objects.get(pk=id_per))


@app.delete("/del-res-mid/{id_per}")
def delete(id_per):
    Kafedra.objects.filter(pk=id_per).delete()
    return "Deleted"


@app.put("/changeMark/{id_stud}")
def update(id_stud: int, id_sem: int, nmark: int):
    b = ResultOfMidterms.objects.get(id_stud=id_stud,id_sem=id_sem)
    b.mark = nmark
    b.save()
    return "mark for student ("+id_stud+"): "+nmark


@app.get("/semester/{id_sem}")
def read(id_sem):
    return model_to_dict(Semester.objects.get(pk=id_sem))


@app.delete("/del-sem/{id_sem}")
def delete(id_sem):
    Semester.objects.filter(pk=id_sem).delete()
    ResultOfMidterms.objects.filter(id_sem=id_sem).delete()
    return "Deleted"


@app.get("/student/{id_stud}")
def read(id_stud):
    return model_to_dict(Student.objects.get(pk=id_stud))


@app.delete("/del-stud/{id_stud}")
def delete(id_stud):
    Student.objects.filter(pk=id_stud).delete()
    ResultOfMidterms.objects.filter(id_stud=id_stud).delete()
    return "Deleted"


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000)

