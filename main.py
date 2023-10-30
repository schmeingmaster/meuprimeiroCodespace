 O mercado 'seu Jose ' está com uma promoção de 10% para seus clentes  
 maiores de 18 anos. Faça um progama em Python  que pergunte  a idade, o valor do total e mostre 
 ele pode ou não ter desconto, qual o desconto e o valor final
 idade =int (input("16:\n"))
 total = float(input("R$50:\n"))

if(idade>=18):
    print("pode ter o desconto")
    desconto = total * 0.1
    final = total - desconto
    print (f"O desconto foi de R${desconto:2f.} e o total é de R${final}")
    else:
        print(f" Não tem direito ao desconto e o seu valor fina é de R${total}")
