dividendo = float(input().strip())
divisor = float(input().strip())
divisao = dividendo // divisor
resto = dividendo % divisor
print ('{:.4f}'.format(divisao))
print ('{:.4f}'.format(resto))