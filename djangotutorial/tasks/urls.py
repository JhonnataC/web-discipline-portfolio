from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # ─── Usando versão com Generic Views (v3) ───
    path(
        'v3/',
        views.TaskListCreate.as_view(),
        name='lista-generic',
    ),
    path(
        'v3/<int:pk>/',
        views.TaskDetail.as_view(),
        name='detalhe-generic',
    ),
]