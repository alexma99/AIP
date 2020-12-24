from django.db import models


class Discipline(models.Model):
    id_disc = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    id_kaf = models.ForeignKey('Kafedra', models.CASCADE, db_column='id_kaf', blank=True, null=True)

    class Meta:
        db_table = 'discipline'


class GroupSt(models.Model):
    id_group = models.BigAutoField(primary_key=True)
    course = models.IntegerField(blank=True, null=True)
    id_kaf = models.ForeignKey('Kafedra', models.CASCADE, db_column='id_kaf', blank=True, null=True)

    class Meta:
        db_table = 'group_st'


class Kafedra(models.Model):
    id_kaf = models.BigAutoField(primary_key=True)
    zaved = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'kafedra'


class Prepod(models.Model):
    id_prep = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    otchestvo = models.CharField(max_length=20, blank=True, null=True)
    degree = models.CharField(max_length=20, blank=True, null=True)
    id_disc = models.ForeignKey(Discipline, models.CASCADE, db_column='id_disc', blank=True, null=True)

    class Meta:
        db_table = 'prepod'


class ResultOfMidterms(models.Model):
    id_per = models.BigAutoField(primary_key=True)
    mark = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_stud = models.ForeignKey('Student', models.CASCADE, db_column='id_stud', blank=True, null=True, )
    id_sem = models.ForeignKey('Semester', models.CASCADE, db_column='id_sem', blank=True, null=True)
    id_disc = models.ForeignKey(Discipline, models.CASCADE, db_column='id_disc', blank=True, null=True)
    id_prep = models.ForeignKey(Prepod, models.CASCADE, db_column='id_prep', blank=True, null=True)

    class Meta:
        db_table = 'result_of_midterms'


class Semester(models.Model):
    id_sem = models.BigAutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'semester'


class Student(models.Model):
    id_stud = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    otchestvo = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    id_group = models.ForeignKey(GroupSt, models.CASCADE, db_column='id_group', blank=True, null=True)

    class Meta:
        db_table = 'student'
