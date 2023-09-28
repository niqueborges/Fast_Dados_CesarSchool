# Ao tentar colocar um Voltorb em uma piscina, Biu acabou levando um choque do trovão. 
# Curioso de saber qual foi a intensidade do choque que levou, ele pesquisou e descobriu que existia uma relação entre o level do voltorb e a potência de seu choque.
# Escreva um programa que, dado o level do voltorb, imprima de quanto foi o choque em W segundo a tabela: 

level = int(input('Digite o level do Voltorb: '))

if level >=1 and level <= 20:
    potencia = 20 + level**3
    
elif level >=21 and level <= 40:
    potencia = 8000 + (level - 10)**2
    
elif level >=41 and level <= 60:
    potencia = 9000 + (5*level)
    
elif level >=61 and level <= 80:
    potencia = 9300 + (2*level)
    
elif level >=81 and level <= 100:
    potencia = 9500 + level
    
else:
    print('valor inválido!')
    
    
print('A intensidade do choque foi: ', potencia, 'W')