# Copyright [2022] Eduardo Zanetta

# A função deve receber um numero N > 1 (validar o input), 
# e retornar todos os números primos até o numero N. 
# EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

# Criar uma função LINEAR que resolva p

# números primos positivos = divisíveis apenas por 1 e por ele mesmo

while True:  # validação

	n = int(input("N: "))  # pega input	

	if n > 1:  # número correto
		break;  # sai do loop

	else:  # número incorreto
		print("N deve ser maior do que 1.")  # mensagem de erro + repete loop


prime_nums = []  # declarando lista de números primos


# for-else loop -> else ocorre quando o break não é acionado

for i in range(2, n + 1):  # loop começando em 2 pois 1 não é primo
	
	for j in range(2, i):  # loop dentro de outro, para repetir em cada valor de i

		# print(f"i = {i} | j = {j} | i % j = {i % j}")  # debug

		if i % j == 0:  # verifica se é i divisível por j
			break  # se sim, encerra loop
	
	else:
		prime_nums.append(i)  # se não, adiciona i na lista de números primos

print(f"p({n}) = {prime_nums}")  # output

"""
para N = 10

i = 3  | j = 2 | i % j = 1
i = 4  | j = 2 | i % j = 0 -> break, pula para proximo i
i = 5  | j = 2 | i % j = 1
i = 5  | j = 3 | i % j = 2
i = 5  | j = 4 | i % j = 1
i = 6  | j = 2 | i % j = 0 -> break
i = 7  | j = 2 | i % j = 1
i = 7  | j = 3 | i % j = 1
i = 7  | j = 4 | i % j = 3
i = 7  | j = 5 | i % j = 2
i = 7  | j = 6 | i % j = 1
i = 8  | j = 2 | i % j = 0 -> break
i = 9  | j = 2 | i % j = 1
i = 9  | j = 3 | i % j = 0 -> break
i = 10 | j = 2 | i % j = 0 -> break
"""