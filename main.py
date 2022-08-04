#Calculadora para realizar o procedimento do rateio do gás.

registroDoMesAnterior = "sem valor digitado do registro do mes anterior"
registroDoMesVigente = "sem valor digitado do registro do mes anterior"
valorDosDoisBotijoes = "sem valor digitado dos botijões"
constanteDeConversao = 2.3

valorDosDoisBotijoes = float(input("Informar o valor dos dois botijões somados: "))
registroDoMesAnterior = float(input("Informar o valor registrado no relogio do mês anterior: "))
registroDoMesVigente = float(input("Informar o valor registrado no relogio do mês vigente: "))
print(" ")
print(" ")

#calculos
resultadoSubtratidoDoMesVigenteEmRelacaoAoMesAnterior = registroDoMesVigente - registroDoMesAnterior

gastoNoMesEmMetrosCubicos = round(resultadoSubtratidoDoMesVigenteEmRelacaoAoMesAnterior * constanteDeConversao, 2)

valorDoMetroPagoNaCarga = round(valorDosDoisBotijoes / 90, 2)

resultadoDoValorDaParaPagar = round(((gastoNoMesEmMetrosCubicos * valorDoMetroPagoNaCarga) / 1000), 2)

print("---------------------------------------Descrição dos valores-------------------------------- ")

print(f"Valor da carga: R$ {valorDosDoisBotijoes}")
print(f"Valor por kg pago na carga comprada: R$ {round(valorDoMetroPagoNaCarga, 2)}")
print(f"Valor gasto em metros/cubicos no mês: {round(gastoNoMesEmMetrosCubicos, 2)}")
print(f"Valor a pagar: R$ {resultadoDoValorDaParaPagar}")



