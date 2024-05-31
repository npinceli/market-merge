from OFS import SimpleItem
from Globals import DTMLFile
from Products.marketmerge.market import MarketMerge


class Market(SimpleItem.SimpleItem):
    """Classe raiz para iniciar o produto."""

    meta_type = 'Market'

    market = MarketMerge()

    def __init__(self, id, connection):
        """Inicia a instancia."""
        self.id = id
        self.connection = connection

    def get_database_connection(self):
        """Conexao com o banco."""
        return self.connection


def manage_addMarket(self, id, connection):
    """Cria a instancia do produto."""
    conn = getattr(self, connection)
    self._setObject(id, Market(id, conn))


manage_addMarketForm = DTMLFile('config/addMarketForm', globals())
