def ex09():
    
    graus_fahrenheit = int(input("Qual a temperatura em graus Fahrenheit ?"))
    graus_celsius = (graus_fahrenheit - 32) / 1.8

    print("A temperatura em graus Celsius é: {:.2f} ºC".format(graus_celsius))

if(__name__ == '__main__'):
    ex09()