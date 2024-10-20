from django.db import models

# Create your models here.
class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50, null=True)
    password=models.TextField(null=True)
    Usertype=models.CharField(max_length=50, null=True)
    status=models.CharField(max_length=50, null=True)
    class Meta:
        db_table='tbl_login'

class user_register(models.Model):
    user_id=models.AutoField(primary_key=True)
    login_id=models.IntegerField()
    firstname=models.CharField(max_length=50, null=True)
    lastname=models.CharField(max_length=50, null=True)
    phone_number=models.BigIntegerField(null=True)
    address=models.TextField(blank=True, null=True)
    mail_id=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_user_register'
class adoption_center_register(models.Model):
    aid_id=models.AutoField(primary_key=True)
    login_id=models.IntegerField()
    agency_name=models.CharField(max_length=50, null=True)
    phone_number=models.BigIntegerField(null=True)
    address=models.TextField(blank=True, null=True)
    mail_id=models.CharField(max_length=50)
    place_id=models.IntegerField()
    class Meta:
        db_table='tbl_agency_register'
class country(models.Model):
    country_id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_country'
        
class state(models.Model):
    state_id=models.AutoField(primary_key=True)
    country_id=models.ForeignKey('country', on_delete=models.CASCADE)
    state=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_state'



class district(models.Model):
    district_id=models.AutoField(primary_key=True)
    state_id=models.ForeignKey('state', on_delete=models.CASCADE)
    district=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_district'
class place(models.Model):
    place_id=models.AutoField(primary_key=True)
    district_id=models.ForeignKey('district', on_delete=models.CASCADE)
    place=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_place'
class pets(models.Model):
    pname=models.CharField(max_length=50)
    breed=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    description=models.TextField(max_length=50)
    age=models.IntegerField()
    image=models.CharField(max_length=50)
    user_login_id=models.IntegerField()
    class Meta:
        db_table='tbl_pets'
class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    feedback_subject=models.CharField(max_length=50)
    feedback=models.CharField(max_length=150)
    Ac_login_id=models.IntegerField()
    user_login_id=models.IntegerField()
    reply=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_feedback'
class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    complaint_subject=models.CharField(max_length=50)
    complaint=models.CharField(max_length=150)
    user_login_id=models.IntegerField()
    reply=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_complaint'

class Rescue_info(models.Model):
    rescue_id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    date=models.DateField()
    Ac_login_id=models.IntegerField()
    user_login_id=models.IntegerField()
    reply=models.CharField(max_length=50)
    photo=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_rescue'
class adoption_info(models.Model):
    adoption_id=models.AutoField(primary_key=True)
    pet_type=models.CharField(max_length=50)
    tag_name=models.CharField(max_length=50)
    breed=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    date=models.DateField()
    photo=models.CharField(max_length=50)
    Ac_login_id=models.IntegerField()
    status=models.CharField(max_length=50,default="Not Adopted")
    adopted_user_login_id=models.IntegerField(default=0)
    rescue_id=models.IntegerField(default=0)
    class Meta:
        db_table='tbl_adoption'

class boarding_service(models.Model):
    b_service_id=models.AutoField(primary_key=True)
    pet_type=models.CharField(max_length=50)
    cost=models.IntegerField(default=0)
    Ac_login_id=models.IntegerField(default=0)
    class Meta:
        db_table='tbl_boarding_service'
class grooming_service(models.Model):
    g_service_id=models.AutoField(primary_key=True)
    service_name=models.CharField(max_length=50)
    pet_type=models.CharField(max_length=50)
    description=models.TextField()
    cost=models.IntegerField(default=0)
    Ac_login_id=models.IntegerField(default=0)
    class Meta:
        db_table='tbl_grooming_service'
class booking_boarding(models.Model):
    boarding_booking_id=models.AutoField(primary_key=True)
    starting_date=models.DateField()
    ending_date=models.DateField()
    pet_id=models.IntegerField()
    b_service_id=models.IntegerField()
    user_login_id=models.IntegerField()
    status=models.CharField(max_length=50,default='Not Accepted')
    class Meta:
        db_table='tbl_booking_boarding'
class booking_grooming(models.Model):
    grroming_booking_id=models.AutoField(primary_key=True)
    date=models.DateField()
    pet_id=models.IntegerField()
    g_service_id=models.IntegerField()
    user_login_id=models.IntegerField()
    status=models.CharField(max_length=50,default='Not Accepted')
    class Meta:
        db_table='tbl_booking_grooming'

