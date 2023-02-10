def ex10():
    graus_celsius = int(input("Qual a temperatura em Celsius ? "))
    graus_fahrenheit = (graus_celsius * 1.8) + 32

    print("A temperatura em Fahrenheit é : {:.2f} ºF".format(graus_fahrenheit))


if(__name__ == '__main__'):
    ex10()