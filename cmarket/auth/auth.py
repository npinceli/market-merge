from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.marketmerge.model.Auth.mAuth import MAuth
from passlib.hash import pbkdf2_sha256


class Autenticacao(SimpleItem.SimpleItem):
    """Controller de autenticacao de usuarios."""
    _model_auth = MAuth()

    _entrar = PageTemplateFile("zpt/entrar.zpt", globals())
    _cadastrar = PageTemplateFile("zpt/cadastrar.zpt", globals())
    auth_css = PageTemplateFile("zpt/css/auth.css", globals())
    auth_js = PageTemplateFile("zpt/js/auth.js", globals())

    def entrar(self):
        """Pagina de login."""
        return self._entrar()

    def entrar_conta(self):
        """A."""
        dados = self.REQUEST.form

        for i in self._model_auth.busca_usuario(dados['usuario']):
            senha = i.senha_hash
            # Retorna true or false.
            compara_senha = pbkdf2_sha256.verify(dados['senha'], senha)

            if compara_senha:
                self.sessao.definir_sessao({'id_usuario': i.id_usuario})
                return self.REQUEST.RESPONSE.\
                    redirect('/m/market/dashboard/dash')
            else:
                raise Exception(3)
        raise Exception(2)

    def cadastrar(self):
        """Pagina de cadastro."""
        return self._cadastrar()

    def cadastrar_usuario(self):
        """Cadastrar usuario na plataforma."""
        dados = self.REQUEST.form

        # Verificar se o usuario ja existe
        duplicado = self._model_auth.busca_usuario(dados['usuario'])

        if duplicado:
            return self.REQUEST.RESPONSE.redirect('/m/market/auth/cadastrar')

        senha_hash = pbkdf2_sha256.hash(dados['senha'])

        self._model_auth.inserir_usuario(dados['nome'], dados['usuario'],
                                         dados['email'], senha_hash)

        return self.REQUEST.RESPONSE.redirect('/m/market/auth/entrar')
