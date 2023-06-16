class UF:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome

class Fabricante:
    def __init__(self, codigo, marca, site, telefone, uf):
        self.codigo = codigo
        self.marca = marca
        self.site = site
        self.telefone = telefone
        self.uf = uf

class Produto:
    def __init__(self, descricao, peso, valor_compra, valor_venda, fabricante):
        self.descricao = descricao
        self.peso = peso
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.fabricante = fabricante
        self.valor_lucro = valor_venda - valor_compra
        self.percentual_lucro = (self.valor_lucro / valor_compra) * 100

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# Unidades Federativas
ufs = [
    UF("AC", "Acre"),
    UF("AL", "Alagoas"),
    UF("AP", "Amapa"),
    UF("AM", "Amazonas"),
    UF("BA", "Bahia"),
    UF("CE", "Ceara"),
    UF("DF", "Distrito Federal"),
    UF("ES", "Espirito Santo"),
    UF("GO", "Goias"),
    UF("MA", "Maranhao"),
    UF("MT", "Mato Grosso"),
    UF("MS", "Mato Grosso do Sul"),
    UF("MG", "Minas Gerais"),
    UF("PA", "Para"),
    UF("PB", "Paraiba"),
    UF("PR", "Parana"),
    UF("PE", "Pernambuco"),
    UF("PI", "Piaui"),
    UF("RJ", "Rio de Janeiro"),
    UF("RN", "Rio Grande do Norte"),
    UF("RS", "Rio Grande do Sul"),
    UF("RO", "Rondonia"),
    UF("RR", "Roraima"),
    UF("SC", "Santa Catarina"),
    UF("SP", "Sao Paulo"),
    UF("SE", "Sergipe"),
    UF("TO", "Tocantins")
]
#  fabricantes
fabricantes = [
    Fabricante("908070", "Tortuga", "tortuga.com.br", "(41) 4141-4141", ufs[15]),
    Fabricante("123456", "Purina", "purina.com.br", "(11) 1111-1111", ufs[24]),
    Fabricante("789012", "Royal Canin", "royalcanin.com.br", "(22) 2222-2222", ufs[11]),
    Fabricante("080030", "Prupru", "prupru.com.br", "(82) 8282-8282", ufs[1]),
    Fabricante("654456", "Dory", "Dory.com.br", "(99) 9999-9999", ufs[10]),
    Fabricante("121012", "Esquifs", "Esquifs.com.br", "(61) 6161-6161", ufs[7])
]
# produtos
produtos = [
    Produto("Fosbovi Confinamento", "25kg", 100.0, 250.0, fabricantes[0]),
    Produto("Racao para Gatos", "5kg", 50.0, 100.0, fabricantes[1]),
    Produto("Racao para Caes", "10kg", 80.0, 150.0, fabricantes[2]),
    Produto("Racao para pombos", "2kg", 5.0, 8.0, fabricantes[3]),
    Produto("Racao para peixes", "8kg", 110.0, 240.0, fabricantes[4]),
    Produto("Racao para esquilos", "1kg", 4.0, 20.0, fabricantes[5])
]
# clientes
clientes = [
    Cliente("Maria", 45),
    Cliente("Pedro", 32),
    Cliente("Jorge", 41),
    Cliente("Joaquim", 94),
    Cliente("besvaldo", 85),
]
# Lista de clientes com idade superior a 60 anos
lista_60 = [
        Cliente("Renato", 99)
]



# Funcao para listar os produtos de um determinado fabricante em ordem alfabética
def listar_produtos_por_fabricante(codigo_fabricante):
    produtos_fabricante = []
    for produto in produtos:
        if produto.fabricante.codigo == codigo_fabricante:
            produtos_fabricante.append(produto)
    
    if len(produtos_fabricante) == 0:
        print("Nenhum produto encontrado para o fabricante com codigo", codigo_fabricante)
        return
    
    produtos_fabricante.sort(key=lambda x: x.descricao)
    for produto in produtos_fabricante:
        print("Descricao:", produto.descricao)
        print("Peso:", produto.peso)
        print("Valor de compra:", produto.valor_compra)
        print("Valor de venda:", produto.valor_venda)
        print("Valor do lucro:", produto.valor_lucro)
        print("Percentual do lucro:", produto.percentual_lucro)
        print("Fabricante:", produto.fabricante.marca)
        print()

# Funcao para apresentar os estados onde te, algum produto com o valor igual ao maior valor registrado no sistema
def listar_estados_com_maior_valor():
    maior_valor = max([produto.valor_venda for produto in produtos])
    estados = []
    for produto in produtos:
        if produto.valor_venda == maior_valor:
            estado = produto.fabricante.uf
            if estado not in estados:
                estados.append(estado)
    
    if len(estados) == 0:
        print("Nenhum estado encontrado com produtos de valor igual ao maior valor registrado")
    else:
        print("Estado(s) com produto(s) de valor igual ao maior valor registrado:")
        for estado in estados:
            print(estado.nome)

# Funcao para apresentar os fabricantes onde tem algum produto com o valor igual ao menor valor registrado no sistema
def listar_fabricantes_com_menor_valor():
    menor_valor = min([produto.valor_venda for produto in produtos])
    fabricantes_menor_valor = []
    for produto in produtos:
        if produto.valor_venda == menor_valor:
            fabricante = produto.fabricante
            if fabricante not in fabricantes_menor_valor:
                fabricantes_menor_valor.append(fabricante)
    
    if len(fabricantes_menor_valor) == 0:
        print("Nenhum fabricante encontrado com produtos de valor igual ao menor valor registrado")
    else:
        print("Fabricante(s) com produto(s) de valor igual ao menor valor registrado:")
        for fabricante in fabricantes_menor_valor:
            print("Codigo:", fabricante.codigo)
            print("Marca:", fabricante.marca)
            print()

# Funcao para listar todos os produtos em ordem crescente de valor
def listar_produtos_ordem_crescente_valor():
    produtos.sort(key=lambda x: x.valor_venda)
    for produto in produtos:
        print("Descricao:", produto.descricao)
        print("Peso:", produto.peso)
        print("Valor de compra:", produto.valor_compra)
        print("Valor de venda:", produto.valor_venda)
        print("Valor do lucro:", produto.valor_lucro)
        print("Percentual do lucro:", produto.percentual_lucro)
        print("Fabricante:", produto.fabricante.marca)
        print()

# Funcao para listar todos os produtos em ordem crescente de maior "valor do lucro"
def listar_produtos_ordem_crescente_lucro():
    produtos.sort(key=lambda x: x.valor_lucro)
    for produto in produtos:
        print("Descricao:", produto.descricao)
        print("Peso:", produto.peso)
        print("Valor de compra:", produto.valor_compra)
        print("Valor de venda:", produto.valor_venda)
        print("Valor do lucro:", produto.valor_lucro)
        print("Percentual do lucro:", produto.percentual_lucro)
        print("Fabricante:", produto.fabricante.marca)
        print()

# Funcao para cadastrar um novo cliente
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    cliente = Cliente(nome, idade)
    clientes.append(cliente)

# Funcao para verificar se existe algum cliente com idade superior a 60 anos
def verificar_cliente_maior_60():
    for cliente in clientes:
        if cliente.idade > 60:
            lista_60.append(cliente)
            clientes.remove(cliente)
    
    if len(lista_60) > 3:
        print("Existem mais de 3 clientes com idade igual ou superior a 60 anos.")
        print("Os clientes serao atendidos na ordem de chegada originalmente cadastrada.")
        print("Os clientes com idade igual ou superior a 60 anos serao removidos da lista original.")
    else:
        print("Nao existem mais de 3 clientes com idade igual ou superior a 60 anos.")

# Funcao para verificar se existe algum produto com o valor especificado pelo usuario (busca binaria)
def verificar_produto_valor():
    valor = float(input("Digite o valor do produto a ser verificado: "))
    produtos_valores = [produto.valor_venda for produto in produtos]
    produtos_valores.sort()
    found = False
    left = 0
    right = len(produtos_valores) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if produtos_valores[mid] == valor:
            found = True
            break
        elif produtos_valores[mid] < valor:
            left = mid + 1
        else:
            right = mid - 1
    
    if found:
        print("Existe pelo menos um produto com o valor especificado.")
    else:
        print("Nao existe nenhum produto com o valor especificado.")

# Funcao para realizar o atendimento dos clientes na lista original com ordem de acesso baseado em fila
def atender_clientes():
    if len(clientes) == 0:
        print("Nao ha clientes para atender.")
        return
    
    print("Atendendo clientes na ordem de chegada:")
    for cliente in clientes:
        print("Nome:", cliente.nome)
        print("Idade:", cliente.idade)
        print()

# Funcao para realizar o atendimento dos clientes na lista_60 com ordem de acesso baseado em pilha
def atender_clientes_60():
    if len(lista_60) == 0:
        print("Nao ha clientes com idade igual ou superior a 60 anos para atender.")
        return
    
    print("Atendendo clientes com idade igual ou superior a 60 anos:")
    while len(lista_60) > 0:
        cliente = lista_60.pop()
        print("Nome:", cliente.nome)
        print("Idade:", cliente.idade)
        print()

# Loop principal do programa
while True:
    print("\nMENU:")
    print("[a] Listar os produtos de um determinado fabricante")
    print("[b] Apresentar o(s) estado(s) onde tenha(m) algum produto com o valor igual ao maior valor registrado")
    print("[c] Apresentar o(s) fabricante(s) onde tenha(m) algum produto com o valor igual ao menor valor registrado")
    print("[d] Listar todos os produtos em ordem crescente de valor")
    print("[e] Listar todos os produtos em ordem crescente de maior 'valor do lucro'")
    print("[f] Cadastrar novo cliente para atendimento na lista")
    print("[g] Verificar se existe algum cliente para atendimento na lista com idade superior a 60 anos")
    print("[h] Verificar se existe algum produto com o valor especificado pelo usuario")
    print("[i] Atender clientes na lista original com ordem de acesso baseado em fila")
    print("[j] Atender clientes na lista_60 com ordem de acesso baseado em pilha")
    print("[s] Sair")
    
    opcao = input("Digite a opcao desejada: ")
    
    if opcao == "a":
        codigo_fabricante = input("Digite o codigo do fabricante: ")
        listar_produtos_por_fabricante(codigo_fabricante)
    elif opcao == "b":
        listar_estados_com_maior_valor()
    elif opcao == "c":
        listar_fabricantes_com_menor_valor()
    elif opcao == "d":
        listar_produtos_ordem_crescente_valor()
    elif opcao == "e":
        listar_produtos_ordem_crescente_lucro()
    elif opcao == "f":
        cadastrar_cliente()
    elif opcao == "g":
        verificar_cliente_maior_60()
    elif opcao == "h":
        verificar_produto_valor()
    elif opcao == "i":
        atender_clientes()
    elif opcao == "j":
        atender_clientes_60()
    elif opcao == "s":
        break
    else:
        print("Opcao invalida. Digite uma opcao valida.")




