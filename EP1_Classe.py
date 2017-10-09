import turtle 

class Desenho:
    
    def  __init__ (self):
        self.tr = turtle.Turtle()
        self.tr.penup()
        self.tr.setpos(-160,160)
        self.tr.pendown()

    def direcaoE (self, grau):
        self.tr.left(grau)
        
    def direcaoD (self, grau):
        self.tr.right(grau)
        
    def frente (self, tamanho):
        self.tr.speed('fastest')
        self.tr.forward(tamanho)

print("inicial = 'F-F-F-F'")
print("regraP = 'F F+F-F-F+F'")
print("nr = 4")

inicial = str(input("Qual o str inicial? "))
regraP = str(input("Qual a regra de produção? "))
nr = int(input("Quantas vezes vai repetir? "))

final = ''
regraP = regraP.split()

i=0
while i < nr:
    final = inicial.replace(regraP[0], regraP[1])
    inicial = final
    i+=1
      
rodar = Desenho()

for i in final.upper():
    if i == 'F':
        rodar.frente(4)
    elif i == '-':
        rodar.direcaoD(90)
    elif i == '+':
        rodar.direcaoE(90)
