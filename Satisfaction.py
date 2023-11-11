'''MÉTODO 5 Q`s = analise o problema e descubra:
#Atuaizando o codigo
1. Quais são os dados de entradas necessários ? fazer perguntas de satisfação dos nossos Funcionários

2. O que devo fazer com estes dados ? Armazenar as respostas e elaborar um grafico simples, visualizar os campos a serem melhorados

3. Quais são as restrições deste problema ? Todo o processo deve ser de forma anonima para quem prencher as perguntas.

4. Qual é o resultado esperado ? Um gráfico mostrando o quanto nossos funcionários estão contentes ou não ...

5. Qual é a sequência de passos a ser feita para chegar ao resultado?
# Fazer perguntas aos nossos funcionários 
# Armazenar as respostas 
# Somar as notas (SIM , NÂO)
# Elaborar um gráfico para melhor visualizar as respostas.
# Elaborar um plano de melhoria para cada nota 'NÂO' 
'''''
import os
from rich import print
votos_sim = 0
votos_nao = 0

while True:

    print(f"total sim:{votos_sim}{os.linesep}total nao:{votos_nao}" )
    try:
        voto = int(input(f"Você está satisfeito com a empresa?{os.linesep}1- sim {os.linesep}2- nao{os.linesep}seu voto: "))
        if voto == 1:
            votos_sim += 1
        elif voto == 2:
            votos_nao += 1
        else:
            pass
    except:
        print("Digite somente 1 ou 2 !!!")
os.system(cls)