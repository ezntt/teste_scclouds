# A função deve receber um numero N >= 0 (deve validar o input para a função), 
# e retornar o valor correspondente desse número na sequencia fibonnaci. 
# EX. fib(0) = 0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.

# Criar uma função LINEAR que resolva fibonacci

"""
primeiros 10:

0 1 1 2 3 5 8 13 21 34  -> fib(n)
^ ^ ^ ^ ^ ^ ^ ^  ^  ^
0 1 2 3 4 5 6 7  8  9   -> n
"""
# lógica de fibonacci -> f(n) = f(n-1) + f(n-2)

while True:  # validação

	n = int(input("N: "))  # pega input

	if n >= 0:  # número correto
		break;  # sai do loop

	else:  # número incorreto
		print("N deve ser maior ou igual a 0.")  # mensagem de erro + repete loop

fib_arr = [0, 1]  # primeiros números da sequência (tratados separadamente)

if n < 2:
	print(f"fib({n}) = {n}")  # caso seja digitado 0 ou 1

else:
	for i in range(2, n + 1):  # começa em 2 pois envolve operações com i - 2, evitando o erro de "list index out of range"
		fib_arr.append((fib_arr[i - 1]) + (fib_arr[i - 2]))  # adiciona próximo número da sequência na lista
	
	print(f"fib({n}) = {fib_arr[n]}")  # output
	
	# print(fib_arr)  # debug