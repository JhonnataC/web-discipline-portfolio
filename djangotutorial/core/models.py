from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    # Vincula o perfil a um usuario do Django
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil',
        null=True,
        blank=True,
    )

    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    course = models.CharField(max_length=100, verbose_name="Curso") 
    semester = models.CharField(max_length=50, verbose_name="Período")
    email = models.EmailField(verbose_name="Email")
    github_url = models.URLField(verbose_name="GitHub URL", blank=True, null=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True, null=True)
    image_url = models.URLField(verbose_name="URL da imagem", blank=True, null=True)

    def __str__(self):
        return self.name