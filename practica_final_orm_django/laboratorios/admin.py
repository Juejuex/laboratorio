from django.contrib import admin
from .models import Laboratorio, Directorgeneral, Producto

admin.site.site_header = 'Laboratorios'


class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_per_page = 20
    ordering = ('id',)

class DirectorgeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    search_fields = ('nombre', 'laboratorio__nombre')
    list_filter = ('laboratorio',)  
    list_per_page = 20
    ordering = ('id',)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    search_fields = ('nombre', 'laboratorio__nombre')
    list_filter = ('laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')  
    list_per_page = 20
    ordering = ('id',)

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Directorgeneral, DirectorgeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
