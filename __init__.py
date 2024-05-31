import marketconfig


def initialize(context):
    """Inicializa o produto."""
    context.registerClass(
        marketconfig.Market,
        constructors=(
            # Quando o produto eh adicionado
            marketconfig.manage_addMarketForm,
            marketconfig.manage_addMarket,
        )
    )
