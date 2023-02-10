def ex08():
    
    valor_hora = float(input("Quanto você ganha por hora ?"))
    quantidade_horas = int(input("Quantas horas você trabalha ?"))

    total_salario = (quantidade_horas * valor_hora) * 30

    print("O total do seu salário por mês é: {} ".format(total_salario))

if(__name__ == '__main__'):
    ex08()