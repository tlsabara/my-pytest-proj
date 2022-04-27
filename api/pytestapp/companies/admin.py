from django.contrib import admin

from .models import Company, Operadores


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Operadores)
class OperadoresAdmin(admin.ModelAdmin):
    pass
