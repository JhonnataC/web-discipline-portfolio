from django.db import models
from django.conf import settings


class Task(models.Model):
    """
    Modelo que representa uma tarefa.
    Cada tarefa tem um titulo, descrição, status de conclusão
    e a data em que foi criada.
    """

    # Campo de texto curto (max 200 caracteres) — obrigatorio
    title = models.CharField(max_length=200)

    # Campo de texto longo — opcional (blank=True permite vazio no formulario)
    description = models.TextField(blank=True)

    # Campo booleano — por padrao, a tarefa nao esta concluida
    is_completed = models.BooleanField(default=False)

    # Data e hora automatica — preenchido automaticamente ao criar
    created_at = models.DateTimeField(auto_now_add=True)

    # Responsavel pela tarefa
    # null=True e blank=True para nao quebrar tarefas ja existentes
    responsible = models.ForeignKey(
        settings.AUTH_USER_MODEL,       # Referencia o modelo User do Django
        on_delete=models.CASCADE,       # Se o usuario for excluido, exclui as tarefas dele
        related_name='tasks',           # Permite acessar: user.tasks.all()
        null=True,
        blank=True,
    )

    class Meta:
        # Ordena por data de criacao (mais recente primeiro)
        ordering = ['-created_at']

    def __str__(self):
        # Representacao em texto da tarefa (aparece no admin)
        return self.title
