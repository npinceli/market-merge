INSERT INTO 
    usuarios (nome, usuario, email, senha_hash)
VALUES (
    <dtml-sqlvar nome type="string">,
    <dtml-sqlvar usuario type="string">,
    <dtml-sqlvar email type="string">,
    <dtml-sqlvar senha type="string">
)