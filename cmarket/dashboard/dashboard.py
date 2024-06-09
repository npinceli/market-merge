from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile


class Dashboard(SimpleItem.SimpleItem):
    """Classe controller do dashboard."""

    # html
    header = PageTemplateFile('zpt/header.zpt', globals())
    _dashboard = PageTemplateFile('zpt/dash.zpt', globals())

    # css
    header_css = PageTemplateFile('zpt/css/header.css', globals())
    dash_css = PageTemplateFile('zpt/css/dash.css', globals())

    def dash(self):
        """View principal do dashboard."""
        teste = self.sessao.obter_sessao()

        a = teste.get('id_usuario')

        raise Exception(a)

        return self._dashboard()
