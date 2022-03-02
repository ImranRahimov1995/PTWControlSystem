from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


class CustomAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email",
                           'first_name', 'last_name'),
            },
        ),
    )


admin.site.register(User, CustomAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'user', 'code', 'duty', 'company', 'phone', 'created')
    list_filter = ('duty', 'sex', 'company',)

    search_fields = ('email',)
    ordering = ('-created',)


admin.site.register(Profile, ProfileAdmin)
