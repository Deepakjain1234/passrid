from django.db import models

class Activity(models.Model):
    login_no = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=9)
    webiste_id = models.CharField(max_length=9)
    ip = models.GenericIPAddressField(unpack_ipv4=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=True)
    secure_status = [
        ('secured', 'Secured'),
        ('unsecured', 'Unsecured'),
    ] 
    security_status = models.CharField(max_length=10, choices=secure_status , default='secured')
    via = [
        ('web' , 'Website'),
        ('app' , 'Application'),
    ]
    medium = models.CharField(max_length=4 , choices=via , default='web')
