from django.db import models

# Create your models here.
class Certificate(models.Model):
    description = models.TextField(verbose_name="Descrição do Certificado")

    def __str__(self):
        return self.description[:50]

class Project(models.Model):
    PROJECT_TYPES = [
        ('PERSONAL', 'Projeto Pessoal'),
        ('COURSE', 'Projeto de Disciplina'),
        ('FREELANCER', 'Freelancer'),
    ]

    project_type = models.CharField(
        max_length=20,
        choices=PROJECT_TYPES,
        default='PERSONAL',
        verbose_name="Tipo de Projeto"
    )
    name = models.CharField(max_length=100, verbose_name="Nome do Projeto")
    description = models.TextField(verbose_name="Descrição do Projeto")
    github_url = models.URLField(verbose_name="Link do GitHub")

    def __str__(self):
        return self.name