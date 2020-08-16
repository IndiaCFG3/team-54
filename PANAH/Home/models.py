from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

# Create your models here.

State = (
        ("1", "ANDHRA PRADESH"),
        ("2", "TAMIL NADU"),
        ("3", "TELANGANA"),
        ("4", "MAHARASHTRA"),
        ("5", "WEST BENGAL"),
        ("6", "UTTAR PRADESH"),
        ("7", "KARNATAKA"),
        ("8", "KERALA"),
    )
Living = (
        ("1","OWN HOUSE"),
        ("2","RENT"),
        ("3","Other")
    )
Organization = (
        ("1","Organised "),
        ("2","UnOrganised"),
        ("3","Other"),
    )
class Schema(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=50)
    income_max = models.IntegerField()
    income_min = models.IntegerField()
    state = models.CharField(
        max_length = 20,
        choices = State,
        default = '1'
        )
    max_fam = models.IntegerField()
    min_fam = models.IntegerField()
    living = models.CharField(
        max_length =20,
        choices = Living,
        default = '1'
    )
    organization = models.CharField(
        max_length =20,
        choices = Organization,
        default = '1'
    )
