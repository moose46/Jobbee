from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from datetime import timedelta, datetime

import geocoder

import os

# Create your models here.


class JobType(models.TextChoices):
    Permanent = "Permanent"
    Temporary = "Temporary"
    Internship = "Intership"


class Education(models.TextChoices):
    Bachelors = "Bachelors"
    Masters = "Masters"
    Phd = "Phd"


class Industry(models.TextChoices):
    Business = "Business"
    IT = "Information Technology"
    Banking = "Banking"
    Education = "Education/Training"
    Telecommunications = "Telecommunications"
    Other = "Others"


class Experience(models.TextChoices):
    NO_EXPERIENCE = "No Experience"
    ONE_YEAR = "1 Year"
    TWO_YEARS = "2 Years"
    THREE_YEAR_PLUS = "3 Years or more"


def return_date_time():
    now = datetime.now()
    return now + timedelta(days=10)


class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    jobType = models.CharField(
        max_length=16, choices=JobType.choices, default=JobType.Permanent
    )
    education = models.CharField(
        max_length=30, choices=Education.choices, default=Education.b
    )
    industry = models.CharField(
        max_length=20, choices=Industry.choices, default=Industry.Business
    )
    experience = models.CharField(
        max_length=20, choices=Experience.choices, default=Experience.NO_EXPERIENCE
    )
    salary = models.IntegerField(
        default=1, validators=[MaxValueValidator(1e6), MinValueValidator(1)]
    )
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0, 0.0))
    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapquest(self.address, key=os.environ.get("GEODOCDER_API"))
        print(g)
        lng = g.lng
        lat = g.lat
        self.point(lng, lat)
        super(Job, self).save(*args, **kwargs)
