import sqlite3

con = sqlite3.connect("exemplo.db")
cur = con.cursor()

##cur.execute("CREATE TABLE IF NOT EXISTS itens(" \
#"               id INTEGER PRIMARY KEY AUTOINCREMENT," \
#"               nome TEXT NOT NULL," \
#"               preco FLOAT," \
#"               quantidade INTEGER)")

#carrinho = [("biscoito", 2.50, 40),("brigadeiro", 1.50, 50)]
#cur.executemany("INSERT INTO itens (nome, preco, quantidade) VALUES (?,?,?)", carrinho)
#con.commit()
teste=int("string")
print(teste)