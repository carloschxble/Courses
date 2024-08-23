names = input("¿Cual es tu nombre?: ")
sales = int(input("¿Cuanto vendiste este mes?: "))
print(f"Hola {names}, este mes \nvendiste ${sales}, por lo \ntanto, el monto de tu \ncomisión es: ${round(sales * 13 / 100, 2) }")