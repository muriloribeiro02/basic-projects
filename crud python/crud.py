import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MUrilo022!!',
    database='bdteste',
)


#DELETE

#cursor = conexao.cursor()

#nome_produto = "todynho"
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

# -------------------------------------------------------------------------

# UPDATE

#cursor = conexao.cursor()
#nome_produto = "todynho"
#valor = 6
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}" '
#cursor.execute(comando)
#conexao.commit()

# -------------------------------------------------------------------------
# READ

# cursor = conexao.cursor()
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

# ------------------------------------------------------------------------
# CREATE

# cursor = conexao.cursor()
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit()
# resultado = cursor.fetchall()

# cursor.close
# conexao.close


cursor = conexao.cursor()
nome_produto = "caqui"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" '
cursor.execute(comando)
conexao.commit()