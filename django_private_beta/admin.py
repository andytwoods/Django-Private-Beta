from django.contrib import admin
from private_beta.models import PrivateBetaModel


class PrivateBetaModelAdmin(admin.ModelAdmin):
    pass



admin.site.register(PrivateBetaModel, PrivateBetaModelAdmin)

