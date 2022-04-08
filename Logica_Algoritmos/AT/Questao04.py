#um montante financeiro inicial
#um percentual de rendimento por período
#um valor de aporte para cada período
#uma quantidade de períodos
import matplotlib.pyplot as graph

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
def formatCurrency (num):
    num = f'R$ {num:_.2f}'
    num = num.replace(".", ",").replace("_", ".")
    return num
def parseStrToFloat(num):
    try:
        num = num.replace(",", ".")
        num = float(num)
        return num
    except Exception as erroParse:
        print(f"Error: {erroParse}")
def CalculateIncome(Amount):
    Amount = float(Amount)
    InterestRate = float(fInterestRate)

    InvestmentIncome = Amount * (fInterestRate/100)
    AccumulatedAmount = Amount + InvestmentIncome
    return AccumulatedAmount
def CalculatePeriodicContribution(AccruedAmount):
    AccruedAmount = float(AccruedAmount)
    AccruedAmount = AccruedAmount + fContribution
    return AccruedAmount
def InvestmentReport():
    PaybackPerPeriod = []
    PaybackPerPeriod = CalculatePayback()
    PeriodCounter = 1
    PeriodList = []
    for period in PaybackPerPeriod:
        AmountFormated = formatCurrency(period)
        print(f"Após {PeriodCounter} períodos(s), o montante será de {AmountFormated}")
        PeriodList.append(PeriodCounter)
        PeriodCounter = PeriodCounter + 1

    graph.plot(PeriodList, PaybackPerPeriod)
    graph.xlabel('Períodos')
    graph.ylabel('Projeção de Acúmulo do Investimento.')
    graph.title('Relatório de Investimento')
    graph.show()

def CalculatePayback():
    PaybackPerPeriod=[]
    AccruedAmount = fStartAmount
    for period in range(iPeriod):
        AccruedAmount = CalculateIncome(AccruedAmount)
        AccruedAmount = CalculatePeriodicContribution(AccruedAmount)
        PaybackPerPeriod.append(AccruedAmount)
    return PaybackPerPeriod


fStartAmount = 0.00
fInterestRate = 0.00
fContribution = 0.00
iPeriod = 0

try:

    fStartAmount = input("Informe o aporte inicial do investimento: R$")
    if not is_numDecimal(fStartAmount) or parseStrToFloat(fStartAmount) < 0:
        raise Exception(f"Por favor entre com um valor válido!")
    else:
        fStartAmount = parseStrToFloat(fStartAmount)

    fInterestRate = input("Informe a taxa de rendimento por período: %")
    if not is_numDecimal(fInterestRate) or parseStrToFloat(fInterestRate) < 0:
        raise Exception(f"Por favor entre com uma taxa válida!")
    else:
        fInterestRate = parseStrToFloat(fInterestRate)

    fContribution = input("Informe o valor do aporte periódico: R$")
    if not is_numDecimal(fContribution) or parseStrToFloat(fContribution) < 0:
        raise Exception(f"Por favor entre com um valor válido!")
    else:
        fContribution = parseStrToFloat(fContribution)

    iPeriod = input("Informe o péríodo do investimento: ")
    if not is_numInt(iPeriod) or int(iPeriod) < 0:
        raise Exception(f"Por favor entre com um período válido!")
    else:
        iPeriod = int(iPeriod)

    InvestmentReport()

except Exception as erro:
    print(f"Error: {erro}")
