print("Bem-vindo à Lista de Compras Simples!")
print("-------------------------------------------------")

# Lista para armazenar os produtos
produtos = []
id_produto = 1  # ID único que será atribuído a cada produto

# Função para exibir os produtos
def listar_produtos():
    if not produtos:
        print("Não há produtos na lista de compras.")
    else:
        print("Produtos na lista:")
        for produto in produtos:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Quantidade: {produto['quantidade']} {produto['unidade']} | Descrição: {produto['descricao']}")
    print()

# Função para adicionar um produto
def adicionar_produto():
    global id_produto
    
    nome = input("Digite o nome do produto: ")
    unidade = input("Digite a unidade de medida (Quilograma, Grama, Litro, Mililitro, Unidade, Metro, Centímetro): ").capitalize()
    quantidade = input("Digite a quantidade: ")
    descricao = input("Digite a descrição do produto: ")
    
    # Validação da unidade
    unidades_validas = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]
    if unidade not in unidades_validas:
        print("Unidade de medida inválida!")
        return
    
    try:
        quantidade = float(quantidade)
    except ValueError:
        print("Quantidade inválida! Digite um número válido.")
        return
    
    produto = {
        "id": id_produto,
        "nome": nome,
        "unidade": unidade,
        "quantidade": quantidade,
        "descricao": descricao
    }
    
    produtos.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso! (ID: {id_produto})")
    
    id_produto += 1  # Incrementa o ID para o próximo produto

# Função para remover um produto
def remover_produto():
    try:
        id_remover = int(input("Digite o ID do produto que deseja remover: "))
    except ValueError:
        print("ID inválido! Digite um número inteiro.")
        return
    
    produto_removido = False
    for produto in produtos:
        if produto["id"] == id_remover:
            produtos.remove(produto)
            print(f"Produto ID {id_remover} removido com sucesso!")
            produto_removido = True
            break
    
    if not produto_removido:
        print("Produto com o ID informado não encontrado.")

# Função para pesquisar produtos por nome
def pesquisar_produto():
    nome_pesquisa = input("Digite o nome ou parte do nome do produto para pesquisa: ").lower()
    resultados = [produto for produto in produtos if nome_pesquisa in produto['nome'].lower()]
    
    if resultados:
        print(f"{len(resultados)} produto(s) encontrado(s):")
        for produto in resultados:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Quantidade: {produto['quantidade']} {produto['unidade']} | Descrição: {produto['descricao']}")
    else:
        print("Nenhum produto encontrado com esse nome.")

# Função principal para controlar o menu
def menu():
    while True:
        # Exibindo lista de produtos e o menu
        listar_produtos()
        
        print("Menu de Opções:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Pesquisar Produtos")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            pesquisar_produto()
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")
            
# Iniciando o programa
menu()