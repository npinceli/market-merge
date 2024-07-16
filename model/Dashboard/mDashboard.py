from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL
from Globals import package_home
import os
global product_path
product_path = os.path.join(package_home(globals())) + '/'


class MDashboard(SimpleItem.SimpleItem):
    """Model de dashboard."""

    def buscar_todos_produtos(self):
        """Busca todos os produtos listados."""
        return self._zsql_sel_todos_produtos()

    def buscar_info_vendedor(self, id_usuario):
        """Buscar infos do vendedor pelo id."""
        return self._zsql_sel_info_vendedor(id_usuario=id_usuario)

    _zsql_sel_todos_produtos = SQL(
        id='zsql_sel_todos_produtos', title='', connection_id='connection',
        arguments='', template=open(
            product_path + 'sql/zsql_sel_todos_produtos.sql').read()
    )

    _zsql_sel_info_vendedor = SQL(
        id="zsql_sel_info_vendedor", title='', connection_id='connection',
        arguments='id_usuario\n', template=open(
            product_path + 'sql/zsql_sel_info_vendedor.sql').read()
    )
