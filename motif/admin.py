from django.contrib import admin
from .models import Person, TextMsg

motif_models = [Person, TextMsg]

admin.site.register(motif_models)
