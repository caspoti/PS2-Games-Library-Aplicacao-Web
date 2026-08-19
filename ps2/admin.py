from django.contrib import admin
from ps2.models import Game

# Register your models here.
class Gameadmin(admin.ModelAdmin):
    list_display = ['title','release_year','rating','review']

# Registrar dentro da pagina de ADM do django
admin.site.register(Game,Gameadmin)