from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.marketmerge.model.Dashboard.mDashboard import MDashboard


class Dashboard(SimpleItem.SimpleItem):
    """Classe controller do dashboard."""

    # model
    _model_dashboard = MDashboard()

    # html
    _dashboard = PageTemplateFile('zpt/dash.zpt', globals())
    header = PageTemplateFile('zpt/header.zpt', globals())
    _anuncios = PageTemplateFile('zpt/anuncios.zpt', globals())
    _adc_produto = PageTemplateFile('zpt/adc_produto.zpt', globals())

    # css
    dash_css = PageTemplateFile('zpt/css/dash.css', globals())
    header_css = PageTemplateFile('zpt/css/header.css', globals())

    def dash(self):
        """Pagina principal do dashboard."""
        sessao = self.sessao.obter_sessao()
        logado = sessao.get('logado')

        produtos = self._model_dashboard.buscar_todos_produtos()
        for p in produtos:
            id_vendedor = p.id_vendedor

        info_vendedor = self._model_dashboard.buscar_info_vendedor(
            id_usuario=id_vendedor)

        if not logado:
            return self.REQUEST.RESPONSE.redirect('/m/market/auth/entrar')

        return self._dashboard(
            dados={
                "produtos": produtos,
                "info_vendedor": info_vendedor
            }
        )

    def anuncios(self):
        """Pagina de anuncios do usuario."""
        return self._anuncios()

    def adicionar(self):
        """Form de adicionar produto."""
        sessao = self.sessao.obter_sessao()
        logado = sessao.get('logado')

        return self._adc_produto(dados=logado)

    def adicionar_saida(self):
        """Insere o produto no banco."""
        produto = self.REQUEST.form

        raise Exception(produto)
