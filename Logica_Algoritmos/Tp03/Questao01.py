def is_numDecimal(num):
    try:
        num = num.replace(",", ".")
        float(num)
        return True
    except:
        pass
    return False


def is_numInt(num):
    try:
        int(num)
        return True
    except:
        pass
    return False

def calculaConta(vlrConta, txServico):
    vlrConta = vlrConta.replace(",", ".")
    txServico = txServico.replace(",", ".")
    return (float(vlrConta)*(float(txServico)/100 +1))

def rateiaConta(vlrConta, qtdPessoas):
    return (float(vlrConta)/float(qtdPessoas))

def imprimeConta(vlrConta, qtdPessoas, percTxServico):
    vlrTotalConta = calculaConta(vlrConta, percTxServico)
    vlrRateio = rateiaConta(vlrTotalConta, qtdPessoas)

    vlrTotalConta = f'R$ {vlrTotalConta:_.2f}'
    vlrTotalConta = vlrTotalConta.replace(".", ",").replace("_", ".")

    vlrRateio = f'R$ {vlrRateio:_.2f}'
    vlrRateio = vlrRateio.replace(".", ",").replace("_", ".")

    print(f'O valor total da conta, com a taxa de serviço, será de {vlrTotalConta}.')
    print(f"Dividindo a conta por {qtdPessoas} pessoa(s), cada pessoa deverá pagar R$ {vlrRateio}.")

try:

    vlrTotConta = input("Informe o Valor da Total da Conta: ")
    if not is_numDecimal(vlrTotConta):
        raise Exception(f"Por favor entre com um valor válido!")

    qtdPessoas = input("Informe quantas pessoas dividirão a Conta: ")
    if not is_numInt(qtdPessoas):
        raise Exception(f"Por favor entre com uma quantidade de pessoas válida!")
    if int(qtdPessoas) <= 0:
        raise Exception(f"Deve haver ao menos uma pessoa para pagar a conta!")

    percTxServico = input("Informe o valor da taxa de serviço: ")
    if not is_numDecimal(percTxServico):
        raise Exception(f"Por favor informe um valor válido para Taxa de Serviço!")
    if float(percTxServico.replace(",", ".")) < 0 or float(percTxServico.replace(",", ".")) > 100:
        raise Exception(f"o valor da Taxa de Serviço é inválido!")

    imprimeConta(vlrTotConta,qtdPessoas,percTxServico)

except Exception as erro:
    print(f"Error: {erro}")
