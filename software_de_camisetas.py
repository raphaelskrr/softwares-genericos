print("Bem vindo à loja de camisetas do Raphael Paiva Julio")

modelo_desejado = """
Entre com o modelo desejado:

MCS - Manga curta simples
MLS - Manga longa simples
MCE - Manga curta com estampa
MLE - Manga longa com estampa

-> """

modelos_de_camisetas = ["MCS", "MLS", "MCE", "MLE"]

modelos = {
  "MCS": 1.80,
  "MLS": 2.10,
  "MCE": 2.90,
  "MLE": 3.20
}

valor_unitario = 0
desconto = 0

def escolha_modelo():
  while True:
    escolha_do_modelo = input(modelo_desejado).strip().upper()
    if escolha_do_modelo in modelos_de_camisetas:
      return escolha_do_modelo
    else:
      print("Modelo inválido, tente novamente...")

def numero_de_camisetas():
  global desconto
  while True:
    try:
      escolha_de_quantidade_de_camisetas = int(input("Entre com o número de camisetas: "))
      if escolha_de_quantidade_de_camisetas > 20000:
        print("Não aceitamos esta quantidade de camisetas. Informe um valor abaixo de 20 mil.\n")
      else:
        break
    except ValueError:
      print("Esta entrada aceita somente números.\n")
  
  if escolha_de_quantidade_de_camisetas < 20:
    desconto = 0
  elif escolha_de_quantidade_de_camisetas < 200:
    desconto = 0.05
  elif escolha_de_quantidade_de_camisetas < 2000:
    desconto = 0.07
  elif escolha_de_quantidade_de_camisetas <= 20000:
    desconto = 0.12
  
  return escolha_de_quantidade_de_camisetas

def frete():
  while True:
    try:
      escolha_de_frete = int(input("""
Escolha o tipo de frete
1 - Frete por Transportadora - R$ 100.00
2 - Frete por Sedex - R$ 200.00
0 - Retirar pedido na fábrica - R$ 0.00
-> """))
      if escolha_de_frete == 1:
        return 100.00
      elif escolha_de_frete == 2:
        return 200.00
      elif escolha_de_frete == 0:
        return 0.00
      else:
        print("Escolha entre 1, 2 ou 0.")
    except ValueError:
      print("Entrada inválida, tente novamente...")

# Chama as funções para obter os valores
escolha_modelo = escolha_modelo()
quantidade_de_camisetas = numero_de_camisetas()
valor_frete = frete()

# Calcula o valor unitário baseado no modelo escolhido
valor_unitario = modelos[escolha_modelo]

# Calcula o desconto baseado na quantidade de camisetas
desconto_aplicado = valor_unitario * desconto

# Calcula o valor total (considerando desconto e frete)
valor_total = (valor_unitario * quantidade_de_camisetas) * (1 - desconto) + valor_frete

# Calcula a quantidade com desconto
quantidade_com_desconto = quantidade_de_camisetas * (1 - desconto)

# Imprime o valor total formatado
print(f"Total: R$ {valor_total:.2f} (Modelo: {modelos[escolha_modelo]:.2f} * Quantidade(com desconto): {quantidade_com_desconto} + frete: {valor_frete})")