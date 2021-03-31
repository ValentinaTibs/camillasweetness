from django.contrib import admin

from main.models import Pagina

class PaginaAdmin(admin.ModelAdmin):

	model = Pagina
	list_display = ('nome','slug')

admin.site.register(Pagina,PaginaAdmin)

