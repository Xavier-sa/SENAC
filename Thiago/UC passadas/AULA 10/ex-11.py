'''11. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é: F=(9*C+160) / 5, sendo F a temperatura em Fahrenheit e C
a temperatura em Celsius.'''

temperatura_celsius = float(input("Insira a temperatura em graus Celsius: "))
temperatura_fahrenheit = (9 * temperatura_celsius + 160) / 5

print(f"A temperatura convertida em graus Fahrenheit é: {temperatura_fahrenheit:.2f}")

