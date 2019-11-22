from django.contrib import admin
from website.models import Produto, Pedido

# Register your models here.
admin.site.register(Produto)
admin.site.register(Pedido)