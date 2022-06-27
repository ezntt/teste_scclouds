# A função deve receber um numero N >= 0 (deve validar o input para a função), 
# e retornar o valor correspondente desse número na sequencia fibonnaci. 
# EX. fib(0) = 0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.

# Criar uma função RECURSIVA que resolva fibonacci

"""
primeiros 10:

0 1 1 2 3 5 8 13 21 34  -> fib(n)
^ ^ ^ ^ ^ ^ ^ ^  ^  ^
0 1 2 3 4 5 6 7  8  9   -> n
"""

while True:  # validação

	n = int(input("N: "))  # pega input

	if n >= 0:  # número correto
		break;  # sai do loop

	else:  # número incorreto
		print("N deve ser maior ou igual a 0.")  # mensagem de erro + repete loop

def fib(value):
	
	if value == 0 or value == 1:  # número mínimo é 2 para realizar a operação, por isso 0 e 1 são tratados separadamente
		return value

	else:
		return fib(value - 1) + fib(value - 2)  # recursividade sendo aplicada (função chamando ela mesma)


print(f"fib({n}) = {fib(n)}")  # output