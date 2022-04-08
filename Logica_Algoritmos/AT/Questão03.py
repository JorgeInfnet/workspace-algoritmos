# dados um valor de renda mensal total
# gastos totais com moradia,
# gastos totais com educação e
# gastos totais com transporte

def is_numDecimal(num):
    try:
        num = num.replace(",", ".")
        float(num)
        return True
    except:
        pass
    return False
def parseStrToFloat(num):
    try:
        num = num.replace(",", ".")
        num = float(num)
        return num
    except Exception as erroParse:
        print(f"Error: {erroParse}")
def getPercentual(vlrRenda, vlrDespesa):
    vlrRenda = parseStrToFloat(vlrRenda)
    vlrDespesa = parseStrToFloat(vlrDespesa)
    return (vlrDespesa/vlrRenda*100)
def getVlrIdeal(vlrRenda, percIdeal):
    vlrRenda = parseStrToFloat(vlrRenda)
    return (vlrRenda * (percIdeal/100))
def formatCurrency (num):
    num = f'R$ {num:_.2f}'
    num = num.replace(".", ",").replace("_", ".")
    return num
def getMessageDefault( area, percCalc, vlrIdeal, estaDentroLimite):
    if estaDentroLimite:
        return (f"Seus gastos totais com {area} comprometem um total de {percCalc:.1f}% de sua renda total, Seus gastos estão dentro da margem recomendada.")
    else:
        return (f"Seus gastos totais com {area} comprometem um total de {percCalc:.1f}% de sua renda total, Portanto, idealmente, o máximo de sua renda comprometida com {area} deveria ser de {vlrIdeal}.")
def printDiagnostico(vlrRenda, vlrMoradia, vlrEduc, vlrTrans):
    print("Diagnóstico:")
    percMoradia = getPercentual(vlrRenda, vlrMoradia)
    if float(percMoradia) <= percIdealMoradia:
        print(getMessageDefault("moradia", percMoradia, "", True))

    else:
        vlrIdeal = formatCurrency(getVlrIdeal(vlrRenda, percIdealMoradia))
        print(getMessageDefault("moradia", percMoradia, vlrIdeal, False))

    percEducacao = getPercentual(vlrRenda, vlrEduc)
    if float(percEducacao) <= percIdealEduc:
        print(getMessageDefault("educação", percEducacao, "", True))

    else:
        vlrIdeal = formatCurrency(getVlrIdeal(vlrRenda, percIdealEduc))
        print(getMessageDefault("educação", percEducacao, vlrIdeal, False))

    percTransporte = getPercentual(vlrRenda, vlrTrans)
    if float(percTransporte) <= percIdealTrans:
        print(getMessageDefault("transporte", percTransporte, "", True))

    else:
        vlrIdeal = formatCurrency(getVlrIdeal(vlrRenda, percIdealTrans))
        print(getMessageDefault("transporte", percTransporte, vlrIdeal, False))

percIdealMoradia = 30.0
percIdealEduc = 20.0
percIdealTrans = 15.0

try:

    vlrRendaMensal = input("Informe o valor total da sua renda mensal: R$")
    if not is_numDecimal(vlrRendaMensal) or parseStrToFloat(vlrRendaMensal) < 0:
        raise Exception(f"Por favor entre com um valor válido!")

    vlrMoradia = input("Informe o valor gasto mensalmente com moradia: R$")
    if not is_numDecimal(vlrMoradia) or parseStrToFloat(vlrMoradia) < 0:
        raise Exception(f"Por favor entre com um valor válido!")

    vlrEduc = input("Informe o valor gasto mensalmente com educação: R$")
    if not is_numDecimal(vlrEduc) or parseStrToFloat(vlrEduc) < 0:
        raise Exception(f"Por favor entre com um valor válido!")

    vlrTrans = input("Informe o valor gasto mensalmente com transporte: R$")
    if not is_numDecimal(vlrTrans) or parseStrToFloat(vlrTrans) < 0:
        raise Exception(f"Por favor entre com um valor válido!")

    printDiagnostico(vlrRendaMensal, vlrMoradia, vlrEduc, vlrTrans)

except Exception as erro:
    print(f"Error: {erro}")
