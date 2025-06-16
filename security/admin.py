from django.contrib import admin
from security.models import User

from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'is_admin',)