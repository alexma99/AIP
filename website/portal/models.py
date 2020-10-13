from django.db import models


class Discip(models.Model):
    id_disc = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    id_kaf = models.BigIntegerField()
    id_prep = models.BigIntegerField()


class GroupSt(models.Model):
    id_group = models.AutoField(primary_key=True)
    course = models.BigIntegerField()
    id_kaf = models.BigIntegerField()


class Kafedra(models.Model):
    id_kaf = models.AutoField(primary_key=True)
    zaved = models.BooleanField()
    name = models.CharField(max_length=30)


class Prepod(models.Model):
    id_prep = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    otchestvo = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    id_disc = models.BigIntegerField()
    id_kaf = models.BigIntegerField()


class MidTerm(models.Model):
    id_per = models.AutoField(primary_key=True)
    mark = models.CharField(max_length=30)
    date = models.DateTimeField()
    id_stud = models.BigIntegerField()
    id_sem = models.BigIntegerField()
    id_disc = models.BigIntegerField()
    id_prep = models.BigIntegerField()


class Sem(models.Model):
    id_sem = models.AutoField(primary_key=True)
    year = models.BigIntegerField()


class Student(models.Model):
    id_stud = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    otchestvo = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField()
    id_group = models.BigIntegerField()
