from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.marketmerge.cmarket.auth.auth import Autenticacao


class MarketMerge(SimpleItem.SimpleItem):
    """Controller principal do produto."""

    auth = Autenticacao()

    _index = PageTemplateFile('zpt/index.zpt', globals())
    lp_css = PageTemplateFile('zpt/css/landingpage.css', globals())
    main_css = PageTemplateFile('zpt/css/main.css', globals())

    def index(self):
        """Pagina inicial do MarketMerge"""
        return self._index()
