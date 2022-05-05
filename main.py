import os

cont=0
count=0

for i in range(50):
  
  cont = cont +1 
  print("***",cont,"ºAluno"***)
 # nome = str(input("Digite o nome do aluno: "))
  idade = int(input("Digite a idade do aluno: "))
  os.system('clear')
  
  if (idade > 15):
    count = count + 1
    
else:
  print("Total de Alunos Acima de 15 Anos: ",count)
    
  