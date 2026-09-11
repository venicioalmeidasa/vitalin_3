
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views #Views nativas do django

app_name = 'autenticacao'

urlpatterns = [
    #Rotas genéricas nativa do django
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html', redirect_authenticated_user=True
        ), name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), 
        name='logout'
    ),
    path('alterarsenha/', auth_views.PasswordChangeView.as_view(
        template_name='registration/alterarsenhaform.html',
        success_url=reverse_lazy('autenticacao:alterarsenhasucesso')
        ), name='alterarsenha'
    ),
    path('alterarsenha/sucesso/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/alterarsenhasucesso.html'
        ), name='alterarsenhasucesso'
    ),
    #falta adicionar a recuperação da senha
]