import math
print("Seja bem vindo a calculadora de equacoes de segundo grau! ela funciona da seguinte forma: \n a calculadora vai te pedir para escrever de forma isolada cada item da equacao no formato ax2+bx+c e apos isso te dara o resultado")

a=float(input('Digite o termo a '))
b=float(input('Digite o termo b '))
c=float(input('Digite o termo c '))

delta=(b*b) - (4*a*c)
if(delta<0):
    print("nao existem raizes reais")
    
else:

    rzdelta=math.sqrt(delta)

    x1=((b*-1)+rzdelta)/(2*a)
    x2=((b*-1)-rzdelta)/(2*a)
    print(f"A primeira raiz {x1:.2f} a segunda {x2:.2f}")
