from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from . import models



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["user_name", "type", "phone", "email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("اطلاعات شخصی", {"fields": ["f_name", "l_name", "phone"]}),
        ("طلاعات کاربر", {"fields": ["user_name", "email", "type"]}),
        ("مجوزهای کاربر", {"fields": ["is_admin", "is_active"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["user_name", "phone", "email", "type"]
    ordering = ["type", "date_joined"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(models.User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


@admin.register(models.SimpleUser)
class SimpleUserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'email']
    fieldsets = [
        ("اطلاعات شخصی", {"fields": ["f_name", "l_name", "phone"]}),
        ("طلاعات کاربر", {"fields": ["user_name", "email", "type"]}),
        ("مجوزهای کاربر", {"fields": ["is_admin", "is_active"]}),
    ]
    search_fields = ['user_name', 'phone', 'email']
    list_filter = ['phone', 'email']
    ordering = ['date_joined']


@admin.register(models.Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'type', 'status', 'artist_name', 'phone', 'email']
    fieldsets = [
        ("اطلاعات شخصی", {"fields": ["f_name", "l_name", "phone", "artist_name"]}),
        ("طلاعات کاربر", {"fields": ["user_name", "email", "type"]}),
        ("مجوزهای کاربر", {"fields": ["is_admin", "is_active"]}),
        ("پروفایل کاربر", {"fields": ["bio", "image"]}),
        ("وضعیت کاربر", {"fields": ["status"]})
    ]
    search_fields = ['user_name', 'phone', 'email', 'artist_name']
    list_filter = ['status', 'artist_name']
    ordering = ['date_joined', 'status']


@admin.register(models.Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'email', 'status', 'artist_name']
    fieldsets = [
        ("اطلاعات شخصی", {"fields": ["f_name", "l_name", "phone", "artist_name"]}),
        ("طلاعات کاربر", {"fields": ["user_name", "email", "type"]}),
        ("مجوزهای کاربر", {"fields": ["is_admin", "is_active"]}),
        ("پروفایل کاربر", {"fields": ["bio", "image"]}),
        ("وضعیت کاربر", {"fields": ["status", "persentage"]})
    ]
    search_fields = ['user_name', 'phone', 'email', 'artist_name']
    list_filter = ['status', 'artist_name']
    ordering = ['date_joined', 'status']



@admin.register(models.Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = [ 'phone', 'email', 'status', 'artist_name']
    fieldsets = [
        ("اطلاعات شخصی", {"fields": ["f_name", "l_name", "phone", "artist_name"]}),
        ("طلاعات کاربر", {"fields": ["user_name", "email", "type"]}),
        ("مجوزهای کاربر", {"fields": ["is_admin", "is_active"]}),
        ("پروفایل کاربر", {"fields": ["bio", "image"]}),
        ("وضعیت کاربر", {"fields": ["status", "persentage"]})
    ]
    search_fields = ['user_name', 'phone', 'email', 'artist_name']
    list_filter = ['status', 'artist_name']
    ordering = ['date_joined', 'status']



@admin.register(models.Supporter)
class SupporterAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'type', 'phone', 'email']
    fieldsets = [
        ("اطلاعات شخصی", {"fields": ["f_name", "l_name", "phone" ]}),
        ("طلاعات کاربر", {"fields": ["user_name", "email", "Supporter_id"]}),
        ("مجوزهای کاربر", {"fields": ["is_admin", "is_active"]})
    ]
    search_fields = ['user_name', 'type', 'phone', 'email']
    list_filter = ['type', 'phone', 'email']
    ordering = ['date_joined']