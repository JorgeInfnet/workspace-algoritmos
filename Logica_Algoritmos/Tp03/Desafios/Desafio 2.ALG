Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 03/02/2022

funcao calcularArea ():real
Inicio
retorne (base * altura)/2
fimfuncao

Var
// Se��o de Declara��es das vari�veis 
   altura: real
   base: real
   area: real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
       escreva("Entre com a Altura do Tri�gulo:")
       leia (altura)
       escreva("Entre com a Base do Tri�gulo:")
       leia (base)
       area <- calcularArea()
       escreva ("Area do Triangulo:", area)
Fimalgoritmo