from django.db import models

import re



# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}

        if len(post_data['first']) < 1:
            errors['first']='First name cannot be blank.'

        if len(post_data['first']) < 1:
            errors['last']= 'Last name cannot be blank.'

        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']= 'Invalid Email.'

        if len(post_data['password']) < 8:
            errors['password']='Password cannot be less than eight characters.'   

        if post_data['password'] != post_data['confirm_pw']:
            errors['password'] = 'Passwords must match.'

        if not errors:
            User.objects.create(first_name = post_data['first'], 
                            last_name = post_data['last'],
                            email = post_data['email'], 
                            password = post_data['password'])
        else:
            return errors

        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
