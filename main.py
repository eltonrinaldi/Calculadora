## Calculadora Simples

operador = ''
operador_str = ''
operador_int = 0
operador_symb = ''
num1_int = 0
num2_int = 0
resultado = 0

while True:
      print(f'{'-'*30}\n')
      print("""Bem-vindo a Calculadora Simples \n
      1. Soma 
      2. Subtração
      3. Multiplicação
      4. Divisão
            """)
      
      operador_input = input("Escolha uma operação: ")

      try:
            operador_int = int(operador_input)
            
      except Exception as Erro:
            print('Isso não é um número válido!: ', Erro)
            continue
            

      if operador_int < 1 or operador_int > 4:
            print(f'*** O número {operador_int} não é válido,\nDigite um número que está na tabela ***')
            continue

      elif operador_int == 1:
            operador = 'Soma'
            operador_str = 'Somado'
            operador_symb = '+'
      
      elif operador_int == 2:
            operador = 'Subtração'
            operador_str = 'Subtraído'
            operador_symb = '-'

      elif operador_int == 3:
            operador = 'Multiplicação'
            operador_str = 'Multiplicado'
            operador_symb = '*'

      elif operador_int == 4: 
            operador = 'Divisão'
            operador_str = 'Dividido'
            operador_symb = '/'
      
      else:
            print('voce não deveria está aqui')

      print(f'Você escolheu {operador}')

      num1 = input('Agora escolha um número: ')
      num2 = input(f'Escolha o segundo número que será {operador_str} com o primeiro: ')

      try:
            num1_int = int(num1)
            num2_int = int(num2)
      except:
            print('Isso não é um número')
            continue

      if operador == 'Soma':
            resultado = num1_int + num2_int

      elif operador == 'Subtração':
            resultado = num1_int - num2_int
      
      elif operador == 'Multiplicação':
            resultado = num1_int * num2_int
      
      elif operador == 'Divisão':
            resultado = num1_int / num2_int

      else:
            print('Erro de operador desconhecido')

      print(f'A {operador} entre o número {num1_int} e o número {num2_int} é {resultado}')
      print('Segue abaixo a formula da conta')
      print(f'{num1_int} {operador_symb} {num2_int} = {resultado}')

      sair = input('\n\nDeseja sair? [s]im').lower()
      sair = sair.startswith('s')

      if sair == 's':
            break
      else:
            continue