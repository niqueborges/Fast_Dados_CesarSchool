# Desenvolva um programa que pergunte a velocidade de um carro. 
# Caso a velocidade ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por cada Km acima da velocidade permitida.
# Duas ações possíveis:
# 1. Emitir a mensagem “Você foi multado e pagará R$ ….”
# 2. Encerrar o programa.

velocidade = float(input('Digite a velocidade do carroem Km/h? '))

if velocidade > 80:
    velocidade_acima = velocidade - 80
    valor_multa = velocidade_acima * 5
    print('Você foi multado!')
    print(f'Você pagará R$ {valor_multa:.2f} de multa. ')

