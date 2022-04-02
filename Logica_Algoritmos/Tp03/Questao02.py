def is_numInt(num):
    try:
        int(num)
        return True
    except:
        pass
    return False

def imprimeSituacaoEleitoral(idade):

    idade = int(idade)

    if idade >= 16 and idade < 18 or idade >= 70:
        return "Não tem obrigação de votar."
    elif idade >= 18 and idade < 70:
        return "Tem obrigação de votar."
    elif idade < 16:
        return "Não tem direito a voto."


try:
    idadePessoa = input("Informe a sua idade: ")
    if not is_numInt(idadePessoa) or int(idadePessoa) <= 0:
        raise Exception(f"Informe uma idade válida!")

    print (imprimeSituacaoEleitoral(idadePessoa))


except Exception as erro:
    print(f"Error: {erro}")