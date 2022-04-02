def is_numDecimal(num):
    try:
        num = num.replace(",", ".")
        float(num)
        return True
    except:
        pass
    return False

participantes=dict([])

try:
    notaMaior = 0
    ganhador =" "
    for num in range(5):
        contador = num + 1
        participante = input("Entre com o nome do participante nº" + str(contador) + " : ")

        nota = input(f"Entre com a nota do participante nº{contador} : ")
        if not is_numDecimal(nota) or float(nota.replace(",", ".")) <= 0 or float(nota.replace(",", ".")) > 10:
            raise Exception(f"Por favor entre com uma nota válida!")

        participantes[participante] = nota
        if float(nota.replace(",", ".")) > float(notaMaior):
            notaMaior = float(nota.replace(",", "."))
            ganhador = participante
        print("_________________________________________________")

        contador = contador + 1

    print(f"O(a) vencedor(a) foi {ganhador} com nota {notaMaior}!")


except Exception as erro:
    print(f"Error: {erro}")

