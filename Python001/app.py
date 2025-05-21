from functions.funções import adicionar
from functions.funções import deletar
from functions.funções import info
from functions.funções import exportar_txt

# execute as funções aqui: 
adicionar("exemplo1", 14, "exemplo1@gmail.com") # adicionando login
adicionar("exemplo2", 23, "exemplo2@email.com") # adicionando login

info() # mostrando todos os logins

deletar("exemplo1") # deletou o primeiro login (deleta por nome)

info() # mostra os logins atualizados

exportar_txt() # exporta para um arquivo .txt