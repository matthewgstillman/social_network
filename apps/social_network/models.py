from django.db import models
import re, os, binascii, bcrypt
# import md5

NAME_REGEX =re.compile('^[A-z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def register(self, postData):
            print (" In the registration process")
            messages = []
            first_name = postData['first_name']
            if len(str(first_name)) < 1:
                messages.append("Error! First name must not be blank!")
            if len(str(first_name)) < 2:
                messages.append("Error! First name must be at least 2 characters long!")

            last_name = postData['last_name']
            if len(str(last_name)) < 1:
                messages.append("Error! Last name must not be blank!")
            if len(str(last_name)) < 2:
                messages.append("Error! Last name must be at least 2 characters long!")

            email = postData['email']
            if len(str(email)) < 1:
                messages.append("Error! Email must not be blank!")
            if len(str(email)) < 2:
                messages.append("Error! Email must be at least 2 characters long!")
            if not EMAIL_REGEX.match(email):
                messages.append("Error! Email must be in a valid format!")

            password = postData['password']
            if len(str(password)) < 1 :
                messages.append("Error! Password must not be blank!")
            if len(str(password)) < 8 :
                messages.append("Error! Password must be at least 8 characters long!")

            password_confirm = postData['password_confirm']
            if password_confirm != password:
                messages.append("Error! Passwords must match")
            user_list = User.objects.filter(email=email)
            for user in user_list:
                print(user.email)
            if user_list:
                messages.append("Error! Email is alread y in the system!")
            if not messages:
                print("No messages")
                password = password.encode()
                salt = bcrypt.gensalt()
                hashed_pw = bcrypt.hashpw(password, salt)
                # password = password
                print("Create User")
                print(hashed_pw)
                #Added Picture field for user
                User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed_pw)
                print(User.objects.all())
                return None
            return messages

class User(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    email = models.CharField(max_length=38)
    password = models.CharField(max_length=38)
    password_confirm = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

def __unicode__(self):
    return(first_name, last_name, email, password)

