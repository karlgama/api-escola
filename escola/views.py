from django.https import JsonResponse

def alunos(resquest):
    if request.method == 'GET':
        aluno = {"nome":"teste"}
        return JsonResponse(aluno)
