from OFS import SimpleItem


class Sessao(SimpleItem.SimpleItem):
    """Classe controller de sessao."""

    def obter_sessao(self):
        """Obter sessao do usuario."""
        return self.REQUEST.SESSION

    def definir_sessao(self, data):
        """Definir sessao do usuario."""
        sessao = self.obter_sessao()
        for chave, valor in data.items():
            sessao[chave] = valor
