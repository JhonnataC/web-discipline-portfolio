from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Colunas exibidas na listagem
    list_display = ['title', 'is_completed', 'created_at']

    # Filtro lateral por status
    list_filter = ['is_completed']

    # Campo de busca
    search_fields = ['title', 'description']