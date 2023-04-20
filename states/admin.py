from django.contrib import admin
from .models import State, Activity
# Register your models here.
class StateAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(State, StateAdmin)
admin.site.register(Activity)