print("Bem vindo ao software de Raphael Paiva Julio")

lista_de_funcionarios = []
id_global = 4763917

ESCOLHAS_DO_MENU_PRINCIPAL = [1, 2, 3, 4]
ESCOLHAS_DO_MENU_CONSULTA = [1, 2, 3, 4]

MENU_PRINCIPAL = """
-----------------------------------------------------------
-------------------- MENU PRINCIPAL -----------------------
Escolha a opção desejada:
1 - Cadastrar funcionários
2 - Consultar funcionários
3 - Remover funcionários
4 - Sair
-> """

MENU_CADASTRAR_FUNCIONARIO = """
-----------------------------------------------------------
---------------- MENU CADASTRAR FUNCIONÁRIO ---------------
"""

MENU_CONSULTAR_FUNCIONARIO = """
-----------------------------------------------------------
---------------- MENU CONSULTAR FUNCIONÁRIO ---------------
1 - Consultar todos os funcionários
2 - Consultar funcionário por ID
3 - Consultar funcionário por setor
4 - Retornar
-> """

def menu_cadastrar_funcionarios():
    nome_do_funcionario = input("Por favor entre com o nome do funcionário: ").capitalize()
    setor_do_funcionario = input("Por favor entre com o setor do funcionário: ").capitalize()
    salario_do_funcionario = float(input("Por favor entre com o salário do funcionário: "))
    global id_global
    id_global += 1
    
    funcionario = {
        "Id": id_global,
        "Nome": nome_do_funcionario,
        "Setor": setor_do_funcionario,
        "Salario": salario_do_funcionario
    }
    
    lista_de_funcionarios.append(funcionario.copy())

def consultar_funcionarios():
    while True:
        try:
            opcao_de_consulta = int(input(MENU_CONSULTAR_FUNCIONARIO))       
            if opcao_de_consulta not in ESCOLHAS_DO_MENU_CONSULTA:
                print("Opção inválida. Digite uma opção válida dentro do menu de opções.")
                continue
            if opcao_de_consulta == 1:
                print("Lista de todos os funcionários: ")
                for funcionario in lista_de_funcionarios:
                    print(funcionario)
            elif opcao_de_consulta == 2:
                id_consulta = int(input("Digite o ID do funcionário: "))
                funcionario_encontrado = False
                for funcionario in lista_de_funcionarios:
                    if funcionario['Id'] == id_consulta:
                        print(f"Funcionário encontrado:\nID: {funcionario['Id']}\nNome: {funcionario['Nome']}\nSetor: {funcionario['Setor']}\nSalário: {funcionario['Salario']}")
                        funcionario_encontrado = True
                        break
                if not funcionario_encontrado:
                    print("Funcionário não encontrado.")
            elif opcao_de_consulta == 3:
                consulta_do_setor = input("Digite o setor que deseja consultar: ").capitalize()
                setor_encontrado = False
                for funcionario in lista_de_funcionarios:
                    if funcionario["Setor"].lower() == consulta_do_setor.lower():
                        print(f"ID: {funcionario['Id']}\nNome: {funcionario['Nome']}\nSetor: {funcionario['Setor']}\nSalário: {funcionario['Salario']}\n")
                        setor_encontrado = True
                if not setor_encontrado:
                    print("Nenhum funcionário encontrado neste setor.")
            elif opcao_de_consulta == 4:
                return
            else:
                print("Opção inválida.")
        except ValueError:
            print("Opção inválida, tente novamente.")

def remover_funcionario():
  while True:
      try:
        remover_id_do_funcionario = int(input("Digite o ID do funcionário que deseja remover, digite '0' para retornar: "))
        funcionario_encontrado = False
        if remover_id_do_funcionario == 0:
            break
        for funcionario in lista_de_funcionarios:
            if funcionario['Id'] ==  remover_id_do_funcionario:
                lista_de_funcionarios.remove(funcionario)
                print("Funcionário removido com sucesso.")
                funcionario_encontrado = True
                break
            if not funcionario_encontrado:
                print("ID inválido. Funcionário não encontrado.")
      except ValueError:
          print("Opção inválida, tente novamente.")
    
while True:
    try:
        opcao = int(input(MENU_PRINCIPAL))
        if opcao not in ESCOLHAS_DO_MENU_PRINCIPAL:
            print("Opção inválida. Digite uma opção válida dentro do menu de opções.")
            continue
    except ValueError:
        print("Opção inválida. O input espera somente números dentro do menu de opções.")
        continue
    if opcao == 1:
        menu_cadastrar_funcionarios()
    elif opcao == 2:
        consultar_funcionarios()
    elif opcao == 3:
        remover_funcionario()
    elif opcao == 4:
        print("Encerrando o programa...")
        break