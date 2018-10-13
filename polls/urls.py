from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
   	url(r'^cadastrar/cadastro/$', views.cadastrar_usuario),
   	url(r'^cadastrar/$', views.Cadastrar, name='cadastrar'),
   	url(r'^verificar/$', views.Verificar, name='verificar'),
   	url(r'^index/logar/$', views.logar_usuario),
   	url(r'^logar/$', views.logar_usuario),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]