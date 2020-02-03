from django.contrib import admin
from .models import Dogs, Curators, Costs

admin.site.register(Dogs)
admin.site.register(Curators)

#here we disable all CRUD operations with Costs
class CostsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Costs, CostsAdmin)
