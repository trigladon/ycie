from django.contrib import admin
from django.contrib.auth.admin import \
    UserAdmin as BaseUserAdmin,\
    UserCreationForm as BaseUserCreationForm, \
    UserChangeForm as BaseUserChangeForm

from .models import User


class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(BaseUserChangeForm):

    class Meta:
        model = User
        fields = '__all__'


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')


admin.site.register(User, UserAdmin)
