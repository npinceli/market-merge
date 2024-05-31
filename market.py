from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile


class MarketMerge(SimpleItem.SimpleItem):
    """Controller principal do produto."""

    _index = PageTemplateFile('zpt/index.zpt', globals())
    main_css = PageTemplateFile('zpt/css/main.css', globals())

    def index(self):
        """Pagina inicial do MarketMerge"""
        return self._index()
