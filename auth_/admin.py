from django.contrib import admin
from auth_.models import MyUser, Profile


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('gender',)

