Algoritmo "Relat�rio de Funcion�rio"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Elberth Moraes
// Descri��o   : Imprime Nome e Sobrenome e Sal�rio Liquido
// Autor(a)    : Jorge Nascimento
// Data atual  : 06/02/2022
procedimento imprimeRelatorio()
var nome, sobrenome: caracter
salario: real
idade, anoNascimento:inteiro

Inicio

escreva("Entre com o nome do funcion�rio:")
leia(nome)

escreva("Entre com o sobrenome do funcion�rio:")
leia(sobrenome)

escreva("Qual a idade do funcion�rio?")
leia(idade)
anoNascimento <- CalculaAno(idade)

escreva("Qual o Sal�rio Bruto desse funcion�rio?")
leia(salario)

salario <- CalculaDesconto(salario)

escreva("O funcion�rio ", nome, " ", sobrenome, " nasceu em ", anoNascimento, " e ganha R$", salario)

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
// Se��o de Declara��es das vari�veis 
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
imprimeRelatorio()

Fimalgoritmo