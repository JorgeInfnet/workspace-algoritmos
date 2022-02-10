Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 03/02/2022

funcao calcularArea ():real
Inicio
retorne (base * altura)/2
fimfuncao

Var
// Seção de Declarações das variáveis 
   altura: real
   base: real
   area: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
       escreva("Entre com a Altura do Triâgulo:")
       leia (altura)
       escreva("Entre com a Base do Triâgulo:")
       leia (base)
       area <- calcularArea()
       escreva ("Area do Triangulo:", area)
Fimalgoritmo