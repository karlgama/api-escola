from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome','RG','CPF','data_nascimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

class Cursos(admin.ModelAdmin):
    list_display = ('id','descricao','codigo_curso')
    list_display_links = ('id','codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Aluno, Alunos)
admin.site.register(Curso, Cursos)
