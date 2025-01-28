class OperasBas:
    #declaracion de propiedades, constructores de la clase, metodos de clase
    #guion bajo indica private, punto publico y doble guion bajo, protegido

    num=0
    num2=0
    res=0

    #constructores de la clase
    def __init__(self,a,b):
        self.num=a
        self.num2=b
        
    #metodos de clase
    def suma(self):
        self.res=self.num+self.num2
        print("r: {}".format(self.res))
    
def main():
    obj=OperasBas(3,5)
    obj.suma()

if __name__=="__main__":
        main()
        