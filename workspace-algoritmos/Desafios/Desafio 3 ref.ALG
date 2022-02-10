Algoritmo "CalculoIdadeEmDias"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Elberth Moraes
// Descrição   : Cálcula em dias a idade de uma pessoa
// Autor(a)    : Jorge Nascimento
// Data atual  : 06/02/2022

funcao ConverteAnoEmDias(ano:inteiro):inteiro
 Inicio
 retorne ((2022 - ano)-1)*365)
fimfuncao

funcao ConverteMesesEmDias(mes, mesAtual:inteiro):inteiro
Inicio
   retorne (((12 - mes)+ mesAtual)-1)*30
fimfuncao

funcao CalculaDataEmDias():inteiro
var dia, diaAtual, mes, mesAtual, ano, idadeEmDias:inteiro
Inicio
escreva("Entre com o Ano de Nascimento:")
leia(ano)
idadeEmDias <- ConverteAnoEmDias(ano)

escreva("Entre com o Mês de Nascimento:")
leia(mes)
escreva("Entre com o Mês Atual:")
leia(mesAtual)
idadeEmDias <- idadeEmDias + ConverteMesesEmDias(mes,mesAtual)

escreva("Entre com o Dia de Nascimento:")
leia(dia)
escreva("Entre com o Dia Atual:")
leia(diaAtual)

se (mes <= mesAtual) e (dia <= diaAtual) entao
   idadeEmDias <- idadeEmDias +((30 - dia) + diaAtual + 5)
senao
   idadeEmDias <- idadeEmDias +(30 - dia) + diaAtual
fimse
retorne idadeEmDias
fimfuncao



procedimento imprimeIdadeEmDias()
Inicio
escreval("Você tem ", CalculaDataEmDias(), " dias de idade.")
fimprocedimento

Var
// Seção de Declarações das variáveis

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...

imprimeIdadeEmDias()

Fimalgoritmo