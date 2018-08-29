from django.contrib.auth import get_user_model
from lib.repos import AutenticarUsuarioRepositories


User = get_user_model()


class AuthBackend:
    def __init__(self):
        pass

    def authenticate(self, request, username=None, password=None):
        au = AutenticarUsuarioRepositories()
        result = au.consultarConveniada({
            'Login': username, 
            'Senha': password, 
            'Versao': '1.0.0'
        })
        print('*'*80)
        print('*'*80)
        print('*'*80)
        print('*'*80)
        print('*'*80)
        print(result)
        print('*'*80)
        print('*'*80)
        print('*'*80)
        print('*'*80)
        if result['CODRETORNO'] != '0':
            return None

        user, created = User.objects.get_or_create(username=result['CODIGO'])
        user.is_staff = True
        user.is_superuser = True
        user.save()
        if created:
            user.nome =  result['NOME']
            user.localidade = result['LOCALIDADE']
            user.saudacao = result['SAUDACAO']
            user.cnpj = result['CGC_CPF']
            user.filial_conveniada = result['FILIAL_CONVENIADA']
            user.conveniada = result['CONVENIADA']
            user.sequencia_conveniada = result['SEQUENCIA_CONVENIADA']
            user.contato_empresa = result['CONTATO_EMPRESA']
            user.codigo_portal = result['CODIGO']
            user.save()

        return user
    
    def get_user(self, user_id):
        try:
            return User._default_manager.get(id=user_id)
        except User.DoesNotExist:
            return None