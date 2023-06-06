from django.contrib import admin

# Register your models here.
from app.models import arvoreDetalhe , controleEntrega

class display(admin.ModelAdmin):
    list_display = ('cod_planta' ,'nome' , 'data_cadastro' ) #metodo de mostrar dados em display
    
    list_filter = ()

admin.site.register(arvoreDetalhe , display)
