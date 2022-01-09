from django.contrib import admin
from appTwo.models import User

"""
Username (leave blank to use 'zenbook'): Gabriel
Email address: name_last@email.com
Password: ABC$2345
"""

# Register your models here.
admin.site.register(User)