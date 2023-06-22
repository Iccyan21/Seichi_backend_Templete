from django.contrib import admin
from accounts.models import User,AccessToken
# Register your models here.

admin.site.register(AccessToken)
admin.site.register(User)