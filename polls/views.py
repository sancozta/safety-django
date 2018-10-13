from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.template import RequestContext
from django.shortcuts import redirect
import requests
import json

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Mostra novamente o formulário de votação das perguntas.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Sempre retorna um HttpResponseRedirect depois de lidar com sucesso
        # com dados via POST. Isso impede que os dados sejam postados duas vezes se
        # o usuário clicar no botão voltar.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def get_deteccoes(id):
    try:
        url = 'https://safetycc.herokuapp.com/logs/'+'1'
        dados = {"id": id}

        headers = {'Authorization': 'Basic YWRtaW46c2VjcmV0'}
        r = requests.get(url, headers=headers)
        print(r.content)
        dicionario = json.loads(r.content)
        return dicionario
    except:
        return ['erro']



@require_POST
def logar_usuario(request):
    try:
        url = 'https://safetycc.herokuapp.com/login'
        dados = {
            "email": request.POST['email'],
            "password": request.POST['senha']
        }

        headers = {'Authorization': 'Basic YWRtaW46c2VjcmV0'}
        r = requests.post(url, data=dados, headers=headers)
        print(r.content)
        dicionario = json.loads(r.content)
        #return redirect('http://127.0.0.1:8000/polls/verificar')
        return HttpResponse([dicionario, get_deteccoes(1)])
    except Exception as e:
        return HttpResponse(e)





@require_POST
def cadastrar_usuario(request):
    # https://safetycc.herokuapp.com/users
    # POST

    # name email password arduino


    try:
        url = 'https://safetycc.herokuapp.com/users'
        dados = {
           "email": request.POST['email'],
            "password": request.POST['senha'],
           "name": request.POST['nome'],
           "arduino": request.POST['arduino']
        }

        

        headers = {'Authorization': 'Basic YWRtaW46c2VjcmV0'}
        r = requests.post(url, data=dados, headers=headers)
        #print(r.content)
        #dicionario = json.loads(r.content)
        #return dicionario
        return redirect('http://127.0.0.1:8000/polls/index')
    except Exception as e:
        return HttpResponse(e)



    '''
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux:
            return HttpResponse("Já existe esse email.")

    except User.DoesNotExist:
        nome_usuario = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']

        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()
        return redirect('http://127.0.0.1:8000/polls/')
    '''
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def Cadastrar(request):
    return render(request, 'polls/cadastrar.html')

def Verificar(request):
    try:
        url = 'https://safetycc.herokuapp.com/logs/'+'1'
        dados = {"id": id}
        headers = {'Authorization': 'Basic YWRtaW46c2VjcmV0'}
        r = requests.get(url, headers=headers)
        print("conteudo")
        print(r.content)
        dicionario = json.loads(r.content)
        usuario = {"nome":"Marcos","id":2}
        return render(request, 'polls/verificar.html',{
            "dic": dicionario,
            "teste": 1,
            "nome": usuario["nome"],
            "id": usuario["id"]
            })
    except:
        return ['erro']
    