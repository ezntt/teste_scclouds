# Copyright [2022] Eduardo Zanetta

# A função deve receber um numero N > 1 (validar o input), 
# e retornar todos os números primos até o numero N. 
# EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

# Criar uma função RECURSIVA que resolva p

from operator import is_


while True:  # validação

	n = int(input("N: "))  # pega input

	if n > 1:  # número correto
		break;  # sai do loop

	else:  # número incorreto
		print("N deve ser maior do que 1.")  # mensagem de erro + repete loop

prime_nums = []  # declarando lista de números primos

def is_prime(a, b):  # verifica se número é primo ou não
						   # argumentos: a = a, b = b

	if a == b:	# é igual (chegou a ser) e não foi divisível em nenhuma repetição?
		return True

	elif b % a == 0:  # é divisível?
		return False

	else:  # não é divisível nem igual?
		return is_prime(a + 1, b)  # incrementa +1 ao primeiro argumento

for i in range(2, n + 1):  # loop começando em 2 pois 1 não é primo

	if is_prime(2, i):  # se retornar True (linha 26)
	
		prime_nums.append(i)  # adiciona i na lista de números primos

print(f"p({n}) = {prime_nums}")  # output


"""
para N = 10

i = 3  | j = 2 | i % j = 1
i = 4  | j = 2 | i % j = 0  -> return False
i = 5  | j = 2 | i % j = 1
i = 5  | j = 3 | i % j = 2
i = 5  | j = 4 | i % j = 1
i = 6  | j = 2 | i % j = 0  -> return False
i = 7  | j = 2 | i % j = 1
i = 7  | j = 3 | i % j = 1
i = 7  | j = 4 | i % j = 3
i = 7  | j = 5 | i % j = 2
i = 7  | j = 6 | i % j = 1
i = 8  | j = 2 | i % j = 0  -> return False
i = 9  | j = 2 | i % j = 1
i = 9  | j = 3 | i % j = 0  -> return False
i = 10 | j = 2 | i % j = 0  -> return False
"""
