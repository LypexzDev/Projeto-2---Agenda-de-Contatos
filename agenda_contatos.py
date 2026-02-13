import json, os

def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def adicionar_contato():
    contatos = carregar_dados("contatos.json")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contato = {"id": len(contatos)+1, "nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)
    salvar_dados("contatos.json", contatos)
    print("Contato adicionado!")

def listar_contatos():
    contatos = carregar_dados("contatos.json")
    for c in contatos:
        print(c)

def atualizar_contato():
    contatos = carregar_dados("contatos.json")
    listar_contatos()
    id_c = int(input("ID do contato para atualizar: "))
    contato = next((c for c in contatos if c["id"]==id_c), None)
    if contato:
        contato["nome"] = input(f"Nome ({contato['nome']}): ") or contato["nome"]
        contato["telefone"] = input(f"Telefone ({contato['telefone']}): ") or contato["telefone"]
        contato["email"] = input(f"Email ({contato['email']}): ") or contato["email"]
        salvar_dados("contatos.json", contatos)
        print("Contato atualizado!")
    else:
        print("Contato não encontrado!")

def remover_contato():
    contatos = carregar_dados("contatos.json")
    listar_contatos()
    id_c = int(input("ID do contato para remover: "))
    contatos = [c for c in contatos if c["id"] != id_c]
    salvar_dados("contatos.json", contatos)
    print("Contato removido!")

def menu():
    while True:
        print("\n1- Adicionar contato\n2- Listar contatos\n3- Atualizar contato\n4- Remover contato\n5- Sair")
        opcao = input("Escolha: ")
        if opcao=="1": adicionar_contato()
        elif opcao=="2": listar_contatos()
        elif opcao=="3": atualizar_contato()
        elif opcao=="4": remover_contato()
        elif opcao=="5": break
        else: print("Opção inválida!")

if __name__=="__main__":
    menu()
