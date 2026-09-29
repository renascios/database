import sqlite3
import database

database.criar_tabela()

while True:
    print("Menu Manipulação do Banco de Dados database.py")
    try:
        comando = int(input("1-Cadastrar,2-Listar,3-Buscar,4-Atualizar,5-Deletar,6-Sair"))
        if not comando:
            raise ValueError("string vazia")
    except ValueError:
        print("Insira um número válido")
        continue
    if comando == 1:
        try:
            nome = input("Digite o nome do produto: ").strip()
            if not nome:
                raise ValueError("string vazia")
        except ValueError:
            print("string não pode ser vazia")
            continue
        try:
            preco = float(input("Digite o preco do futuro: "))
            if not preco:
                raise ValueError("string vazia")
            if preco <= 0:
                raise ValueError("número menor que zero")
        except ValueError:
            print("o valor precisa ser numérico")
            continue
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            if not quantidade:
                raise ValueError("string vazia")
            if quantidade <= 0:
                raise ValueError("número menor que zero")
        except ValueError:
            print("o valor precisa ser um inteiro")
            continue
        database.criar_produto(nome,quantidade,preco)
        print("produto criado")
    elif comando == 2:
        lista = database.listar_produtos()
        for itens in lista:
            print(f"id: {itens[0]}, nome: {itens[1]}, quantidade: {itens[2]} preço: {itens[3]}")
    elif comando == 3:
        try:
            id_buscado = int(input("Digite o ID do produto: "))
            if not id_buscado:
                raise ValueError("string vazia")
            if id_buscado <= 0:
                raise ValueError("número menor que zero")
        except ValueError:
            print("o valor precisa ser numérico")
            continue
        resultado = database.buscar_produto(id_buscado)
        if not resultado == None:
            print(f"id: {resultado[0]}, nome: {resultado[1]}, quantidade: {resultado[2]} preço: {resultado[3]}")
        else:
            print("não foram encontrados ID's correspondentes a busca")
    elif comando == 4:
        try:
            id_atualizar = int(input("Digite o ID a ser atualizado: "))
            if not id_atualizar:
                raise ValueError("string vazia")
            if id_atualizar <= 0:
                raise ValueError("número menor que zero")
        except ValueError:
            print("Você precisa digitar um inteiro para o ID")
            continue
        try:
            quantidade_atualizada = int(input("Digite a quantidade: "))
            if not quantidade_atualizada:
                raise ValueError("string vazia")
            if quantidade_atualizada <= 0:
                raise ValueError("número menor que zero")
        except ValueError:
            print("Você precisa digitar um inteiro para a quantidade")
            continue
        try:
            nome_atualizado = str(input("Digite o nome à ser atualizado: ")).strip()
            if not nome_atualizado:
                raise ValueError("string vazia")
        except ValueError:
            print("problema com nome")
            continue
        try:
            preco_atualizado = float(input("Digite o novo preço: "))
            if not preco_atualizado:
                raise ValueError("string vazia")
            if preco_atualizado <= 0:
                raise ValueError("número menor que zero")
        except ValueError:
            print("Digite um valor númerico")
            continue
        final = database.atualizar_produto(id_atualizar, nome_atualizado, quantidade_atualizada, preco_atualizado)
        if final == True:
            print("produto atualizado")
        else:
            print("erro ao atualizar")
    elif comando == 5:
        try:
            id_deletar = int(input("Digite o ID do produto para ser deletado: "))
            if not id_deletar:
                raise ValueError("string vazia")
            if id_deletar <= 0:
                raise ValueError("número menor que zero")
        except ValueError:
            print("Digite um ID válido")
            continue
        resultado_deletar = database.deletar_produto(id_deletar)
        if resultado_deletar == True:
            print("produto deletado")
        else:
            print("erro ao deletar")
    elif comando == 6:
        break
    else:
        print("insira um número válido")

