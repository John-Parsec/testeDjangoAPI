from django.contrib import admin

# Register your models here.
from api_app.models import Produto
from api_app.models import Nivel
from api_app.models import Relacao

admin.site.register(Produto)
admin.site.register(Nivel)
admin.site.register(Relacao)