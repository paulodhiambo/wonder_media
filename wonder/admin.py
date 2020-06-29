from django.contrib import admin
from django.contrib.auth.models import User, Group

from wonder.models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "latitude", "longitude",)
    list_filter = ("created_at", "last_modified",)
    search_fields = ("name",)


admin.site.register(Users, UsersAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
