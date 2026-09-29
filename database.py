import sqlite3

def criar_tabela():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS produtos (" \
    "               id INTEGER PRIMARY KEY AUTOINCREMENT," \
    "               nome TEXT NOT NULL," \
    "               quantidade INT," \
    "               preco FLOAT)")
    con.close()

def criar_produto(nome, quantidade, preco):
    if not isinstance(nome, str):
        raise TypeError("o nome deve estar em formato de string")
    if not isinstance(quantidade, int) or quantidade <=0:
        raise ValueError("a quantidade deve ser um número inteiro maior que zero")
    if not isinstance(preco,(float, int)) or preco <= 0:
        raise ValueError("o preço deve ser um número inteiro ou float e maior que zero")

    data = (nome,quantidade,preco)
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO produtos (nome,quantidade,preco) VALUES (?,?,?)",data)
    con.commit()
    con.close()

def buscar_produto(produto_id):
    if not isinstance(produto_id, int) or produto_id <= 0:
        raise ValueError("id precisa ser um número inteiro maior que zero")
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM produtos WHERE id = ?",(produto_id,))
    result = res.fetchone()
    con.close()
    return result

def atualizar_produto(produto_id, nome, quantidade, preco):
    if not isinstance(nome, str):
        raise TypeError("o nome deve estar em formato de string")
    if not isinstance(quantidade, int) or quantidade <=0:
        raise ValueError("a quantidade deve ser um número inteiro maior que zero")
    if not isinstance(preco,(float, int)) or preco <= 0:
        raise ValueError("o preço deve ser um número inteiro ou float e maior que zero")
    if not isinstance(produto_id, int) or produto_id <= 0:
        raise ValueError("id precisa ser um número inteiro maior que zero")

    data = (nome,preco,quantidade,produto_id)
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("UPDATE produtos" \
    "            SET nome=?," \
    "                preco=?," \
    "                quantidade=?" \
    "            WHERE id=?",data)
    
    con.commit()
    con.close()
    if cur.rowcount <= 0:
        return False
    else:
        return True

def deletar_produto(produto_id):
    if not isinstance(produto_id, int) or produto_id <= 0:
        raise ValueError("id precisa ser um número inteiro maior que zero")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("DELETE FROM produtos WHERE id=?",(produto_id,))
    con.commit()
    con.close()
    if cur.rowcount <= 0:
        return False
    else:
        return True

def listar_produtos():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM produtos")
    result = res.fetchall()
    con.close()
    return result
