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
    ("1", "OWN HOUSE"),
    ("2", "RENT"),
    ("3", "Other")
)
Organization = (
    ("1", "Organised "),
    ("2", "UnOrganised"),
    ("3", "Other"),
)

Gender = (("1","Female"),("2","Male"),("3","Other"))
class Schema(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=50)
    income_max = models.IntegerField()
    income_min = models.IntegerField()
    state = models.CharField(
        max_length=20,
        choices=State,
        default='1'
    )
    max_fam = models.IntegerField()
    min_fam = models.IntegerField()
    living = models.CharField(
        max_length=20,
        choices=Living,
        default='1'
    )
    organization = models.CharField(
        max_length=20,
        choices=Organization,
        default='1'
    )
    gender = models.CharField(
        max_length=20,
        choices=Gender,
        default='1'
    )
    def __str__(self):
        return self.title
class EndUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    income = models.IntegerField()
    family_size = models.IntegerField()
    address = models.TextField()
    pin_code = models.IntegerField()
    state = models.CharField(
        max_length=20,
        choices=State,
        default='1'
    )
    gender = models.CharField(
        max_length=20,
        choices=Gender,
        default = "1"
    )
class Employee(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    full_Name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 20)
    ngo_id = models.CharField(max_length =10)
    location= models.CharField(max_length =20)
class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length =12)
    location = models.TextField()
