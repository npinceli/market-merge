from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL
from Globals import package_home
import os
global product_path
product_path = os.path.join(package_home(globals())) + '/'


class MAuth(SimpleItem.SimpleItem):
    """Model de autenticacao."""
    def busca_usuario(self, usuario):
        """Busca usuario na tabela."""
        return self._zsql_busca_usuario(usuario=usuario)

    def inserir_usuario(self, nome, usuario, email, senha):
        """Cria usuario na tabela"""
        return self._zsql_inserir_usuario(nome=nome, usuario=usuario,
                                          email=email, senha=senha)

    _zsql_busca_usuario = SQL(
        id='zsql_busca_usuario', title='', connection_id='connection',
        arguments='usuario', template=open(
            product_path + 'sql/zsql_busca_usuario.sql').read()
    )

    _zsql_inserir_usuario = SQL(
        id='zsql_inserir_usuario', title='', connection_id='connection',
        arguments='nome\nusuario\nemail\nsenha', template=open(
            product_path + 'sql/zsql_inserir_usuario.sql').read()
    )
