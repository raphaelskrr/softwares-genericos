print("Bem vindo à loja de Raphael Paiva Julio")

def calcular_parcela():
  valor_do_pedido = float(input("Entre com o valor do pedido: "))
  quantidade_de_parcelas = int(input("Entre com a quantidade de parcelas: "))
  try:
    if quantidade_de_parcelas < 4:
      juros = 0
    elif quantidade_de_parcelas >= 4 and quantidade_de_parcelas < 6:
      juros = 0.04
    elif quantidade_de_parcelas >= 6 and quantidade_de_parcelas < 9:
      juros = 0.08
    elif quantidade_de_parcelas >= 9 and quantidade_de_parcelas < 13:
      juros = 0.16
    else:
      juros = 0.32
  except ValueError:
    print("O sistema espera a entrada de números.")
  valor_da_parcela = valor_do_pedido * (1 + juros) / quantidade_de_parcelas
  valor_total_parcelado = valor_da_parcela * quantidade_de_parcelas
  print(f"O valor das parcelas é de: R$ {valor_da_parcela:.2f}")
  print(f"O valor total parcelado é de: R$ {valor_total_parcelado:.2f}")
    
calcular_parcela()
      