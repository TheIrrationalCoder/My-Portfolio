import uuid
from django.db import models

class Person(models.Model):
    person_id   =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        =   models.CharField(max_length=100)
    age         =   models.PositiveIntegerField(default=0)
    exp         =   models.CharField(max_length=100)
    country     =   models.CharField(max_length=100)
    location    =   models.CharField(max_length=100)
    email       =   models.EmailField(max_length=200)
    phone       =   models.CharField(max_length=100)
    address     =   models.CharField(max_length=200)

class Skill(models.Model):
    skill_id    =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_id   =   models.ForeignKey("person", on_delete=models.CASCADE)
    skill_type  =   models.CharField(max_length=200)
    skill_desc  =   models.TextField()

class Education(models.Model):
    edu_id      =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_id   =   models.ForeignKey("person", on_delete=models.CASCADE)
    edu_name    =   models.CharField(max_length=200)
    edu_dur     =   models.CharField(max_length=200)
    edu_desc    =   models.TextField()

class Experience(models.Model):
    exp_id      =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_id   =   models.ForeignKey("person", on_delete=models.CASCADE)
    exp_name    =   models.CharField(max_length=200)
    exp_dur     =   models.CharField(max_length=200)
    exp_desc    =   models.TextField()

class Certification(models.Model):
    cert_id     =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_id   =   models.ForeignKey("person", on_delete=models.CASCADE)
    cert_name   =   models.CharField(max_length=200)
    cert_desc   =   models.TextField()

class Visitor(models.Model):
    visitor_id  =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        =   models.CharField(max_length=500)
    email       =   models.EmailField(max_length=500)
    linkedinh   =   models.CharField(max_length=1000, blank=True)

