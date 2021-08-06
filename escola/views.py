from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = {"nome":"teste"}
        return JsonResponse(aluno)
