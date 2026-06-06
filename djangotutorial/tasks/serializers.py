from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Tarefa.
    ModelSerializer gera automaticamente os campos
    com base no modelo, incluindo validacao.
    """

    responsible = serializers.StringRelatedField(read_only=True)

    class Meta:
        # Qual modelo este serializer representa
        model = Task

        # Quais campos incluir na API
        # '__all__' inclui todos, mas e melhor ser explicito:
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'responsible']

        # Campos que so podem ser lidos (nao aceitar no POST/PUT)
        read_only_fields = ['id', 'created_at', 'responsible']