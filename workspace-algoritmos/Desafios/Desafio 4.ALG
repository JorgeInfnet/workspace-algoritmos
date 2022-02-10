Algoritmo "Relatório de Funcionário"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Elberth Moraes
// Descrição   : Imprime Nome e Sobrenome e Salário Liquido
// Autor(a)    : Jorge Nascimento
// Data atual  : 06/02/2022
procedimento imprimeRelatorio()
var nome, sobrenome: caracter
salario: real
idade, anoNascimento:inteiro

Inicio

escreva("Entre com o nome do funcionário:")
leia(nome)

escreva("Entre com o sobrenome do funcionário:")
leia(sobrenome)

escreva("Qual a idade do funcionário?")
leia(idade)
anoNascimento <- CalculaAno(idade)

escreva("Qual o Salário Bruto desse funcionário?")
leia(salario)

salario <- CalculaDesconto(salario)

escreva("O funcionário ", nome, " ", sobrenome, " nasceu em ", anoNascimento, " e ganha R$", salario)

fimprocedimento

funcao CalculaAno(idade:inteiro):inteiro
Inicio
retorne (2022-idade)
fimfuncao

funcao CalculaDesconto(salario:real):real
var desconto:real

Inicio
escreva("Qual o valor descontado em folha?")
leia(desconto)
retorne(salario-desconto)
fimfuncao

Var
// Seção de Declarações das variáveis 
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
imprimeRelatorio()

Fimalgoritmo