INSERT INTO
    produtos (id_vendedor, nome_produto, img_produto, preco, quantidade, data_anuncio)
VALUES
    (<dtml-sqlvar id_vendedor type="int">, <dtml-sqlvar nome_produto type="string">, <dtml-sqlvar img_produto type="string">,
    <dtml-sqlvar preco type="float">, <dtml-sqlvar quantidade type="int">, current_timestamp)