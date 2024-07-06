print("Bem vindo à loja de Raphael Paiva Julio")
menu = """
---------Bem-vindo à loja de Marmitas do Raphael-----------
----------------------- Cardápio --------------------------
-----------------------------------------------------------
---| Tamanho | Bife Acebolado(BA) | Filé de Frango(FF) |---
---|    P    |      R$ 16.00      |      R$ 15.00      |---
---|    M    |      R$ 18.00      |      R$ 17.00      |---
---|    G    |      R$ 22.00      |      R$ 21.00      |---
-----------------------------------------------------------"""

lista_de_precos = {
  "bife_acebolado_pequeno": 16.00,
  "bife_acebolado_medio": 18.00,
  "bife_acebolado_grande": 22.00,
  "file_de_frango_pequeno": 15.00,
  "file_de_frango_medio": 17.00,
  "file_de_frango_grande": 21.00,
}

opcoes_de_marmitas = ["BA", "FF"]
opcoes_de_tamanhos = ["P", "M", "G"]

def escolher_marmita():
  while True:
    try:
      print(menu)
      escolha_da_marmita = str(input("Entre com o sabor desejado (BA/FF): ")).upper()
      if escolha_da_marmita not in opcoes_de_marmitas:
        print("Sabor inválido. Tente novamente.")
      else:
        return escolha_da_marmita
    except ValueError:
      print("O input espera somente letras.")
      
def escolher_tamanho():
  while True:
    escolha_do_tamanho = str(input("Entre com o tamanho desejado da marmita (P/M/G): ")).upper()
    if escolha_do_tamanho not in opcoes_de_tamanhos:
      print("Tamanho inválido. Tente novamente.")
    else:
      return escolha_do_tamanho

marmita = escolher_marmita()
tamanho = escolher_tamanho()

valor_a_pagar = 0

while True:
  if marmita == "BA" and tamanho == "P":
    print("\nVocê pediu um Bife Acebolado no tamanho P: R$ 16.00")
    valor_a_pagar += lista_de_precos["bife_acebolado_pequeno"]
  elif marmita == "BA" and tamanho == "M":
    print("\nVocê pediu um Bife Acebolado no tamanho M: R$ 18.00")
    valor_a_pagar += lista_de_precos["bife_acebolado_medio"]
  elif marmita == "BA" and tamanho == "G":
    print("\nVocê pediu um Bife Acebolado no tamanho G: R$ 22.00")
    valor_a_pagar += lista_de_precos["bife_acebolado_grande"]
  elif marmita == "FF" and tamanho == "P":
    print("\nVocê pediu um Filé de Frango no tamanho P: R$ 15.00")
    valor_a_pagar += lista_de_precos["file_de_frango_pequeno"]
  elif marmita == "FF" and tamanho == "M":
    print("\nVocê pediu um Filé de Frango no tamanho M: R$ 17.00")
    valor_a_pagar += lista_de_precos["file_de_frango_medio"]
  elif marmita == "FF" and tamanho == "G":
    print("\nVocê pediu um Filé de Frango no tamanho G: R$ 21.00")
    valor_a_pagar += lista_de_precos["file_de_frango_grande"]

  adicional = str(input("Deseja mais alguma coisa? (S/N): ")).upper()
  if adicional == "S":
    marmita = escolher_marmita()
    tamanho = escolher_tamanho()
  elif adicional == "N":
    break

print(f"O valor total a ser pago: R$ {valor_a_pagar:.2f}")
