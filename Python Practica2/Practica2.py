
frase = input("Ingresa una frase: ")

lista_palabras = frase.split()
print("\nLista de palabras:", lista_palabras)

for palabra in lista_palabras:
    print(palabra.upper())

palabra_contar = input("\nQue palabra quieres contar en la frase?: ")
cantidad = lista_palabras.count(palabra_contar)
print(f"La palabra {palabra_contar} aparece {cantidad} veces.")


palabra_o = input("\nQue palabra quieres reemplazar?: ")
palabra_n = input("Por cual palabra la quieres reemplazar?: ")
frase_m = frase.replace(palabra_o, palabra_n)
print("Frase modificada: ", frase_m)
