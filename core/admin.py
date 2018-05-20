from django.contrib import admin
from .models import Alerts, Time, Kassa
# Register your models here.


class KassaInline(admin.TabularInline):
    model = Kassa
    extra = 0


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    inlines = [KassaInline, ]


admin.site.register(Alerts)