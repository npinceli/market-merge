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

    def entrar(self):
        """Pagina de login."""
        return self._entrar()

    def cadastrar(self):
        """Pagina de cadastro."""
        return self._cadastrar()

    def cadastrar_usuario(self):
        """Cadastrar usuario na plataforma."""
        dados = self.REQUEST.form

        senha_hash = pbkdf2_sha256.hash(dados['senha'])

        self._model_auth.inserir_usuario(dados['nome'], dados['usuario'],
                                         dados['email'], senha_hash)
