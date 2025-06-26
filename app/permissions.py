from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    # Essa função é chamada sempre que alguém tenta acessar a API
    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )
        # Se não conseguir gerar o nome da permissão, nega o acesso
        if not model_permission_codename:
            return False

        # Verifica se o usuario tem a permissão necessária para a ação/modelo
        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        try:
            # Obtem o nome do modelo relacionado a view
            model_name = view.queryset.model._meta.model_name

            # Obtem o nome do app relacionado a view
            app_label = view.queryset.model._meta.app_label

            # Define a ação (view, add, change, delete) baseada no método HTTP
            action = self.__get_action_sufix(method)

            # Monta o nome da permissão no padrão django: app_label.action_modelname
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            # Caso a view não tenha queryset/model definido
            return None

    # Retorna o sufixo da ação de acordo com o método HTTP da requisição
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }

        # Retorna a ação correspondente ao método HTTP, ou string vazia se não encontrar
        return method_actions.get(method, '')
