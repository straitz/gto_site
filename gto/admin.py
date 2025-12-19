from django.contrib import admin
from .models import Standard, Document, News, Partner

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ("name", "age_group", "gold", "silver", "bronze")
admin.site.register(News)
admin.site.register(Partner)