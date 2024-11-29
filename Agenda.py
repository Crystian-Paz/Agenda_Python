def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"O Novo Contato '{nome_contato}' Foi Adicionado a Sua Agenda")
    return

contatos = []

def visualizar_contato(contatos):
    for index, contato in enumerate(contatos):
        print(f"{index}.{contato}")
    return

while True:
    print("\nMenu de Gerenciamento da Agenda:")
    print("1. Adicionar um Contato")
    print("2. Visualizar Lista de Contatos")
    print("3. Editar Lista de Contatos")
    print("4. Marcar/Desmarcar como Favorito")
    print("5. Ver Lista de Contatos Favoritos")
    print("6. Apagar um Contato")
    print("7. Sair.")
    
    opcao = input("Digite o Número da Ação: ")

    if opcao == "1":
        nome_contato = input("Digite o Nome do Contato: ")
        telefone_contato = input("Digite o Telefone do Contato: ")
        email_contato = input("Digite o Email do Contato: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
        print("Foi Adicionado um novo Contato a Agenda, Nome do Contato: {nome_contato}")
    elif opcao == "2":
        visualizar_contato(contatos)
    elif opcao == "3":
        print("A")
    elif opcao == "4":
        print("A")
    elif opcao == "5":
        print("A")
    elif opcao == "6":
        print("A")
    elif opcao == "7":
        print("A")
        break
    else:
        print("A")