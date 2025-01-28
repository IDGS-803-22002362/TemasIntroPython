import os
from io import open
class Tfr:
    def __init__(self, archivoNom):
        self.archivoNom=archivoNom
        self.palabras=[]
        self.cargarArchivo()

    
    def cargarArchivo(self):
        if not os.path.exists(self.archivoNom):
            return
        archivo=open(self.archivoNom,"r", encoding="utf-8")
        for linea in archivo:
            linea=linea.strip()
            if not linea:
                continue
            partes=linea.split(",")
            if len(partes)==3:
                esp,ing,fran=partes
                self.palabras.append((esp,ing,fran))
        archivo.close()
    
    def garderMot(self):
        archivo=open(self.archivoNom,"w",encoding="utf-8")
        for esp,ing,fran in self.palabras:
            texto=f"{esp},{ing},{fran}\n"
            archivo.write(texto)
        archivo.close()
    
    def ajouterMots(self, espanol, ingles, frances):
        self.palabras.append((espanol, ingles, frances))
        self.garderMot()

    
    def chercherMotsEspagnol(self,motEspagnol):
        for esp,ing,fran in self.palabras:
            if esp.lower()==motEspagnol.lower():
                return (ing,fran)
        return None
    
    def chercherMotsAnglais(self,motAnglais):
        for esp,ing,fran in self.palabras:
            if ing.lower()==motAnglais.lower():
                return (esp,fran)
        return None
    
    def chercherMotsFrancais(self,motFrancais):
        for esp,ing,fran in self.palabras:
            if fran.upper()==motFrancais.upper():
                return (esp,ing)
        return None
    
def run():
        traductor=Tfr("FRdicctionary.txt")
        while True:
            os.system('cls')
            print("=====Diccionario=====")
            print("1-BUSQUEDA")
            print("2-REGISTRO")
            print("3-SALIR")
            respuesta=int(input("Elige una opcion: "))
            if respuesta==1:
                os.system('cls')
                print("1-PALABRA ESPAÑOL")
                print("2-PALABRA INGLES")
                print("3-PALABRA FRANCES")
                palabra=int(input("Elige una opcion: "))
                if palabra==1:
                    pEsp=input("Introduzca palabra: ")
                    traduccion=traductor.chercherMotsEspagnol(pEsp)
                    if traduccion:
                        ing, fran = traduccion
                        print(f"Traducción Ingles: {ing}, FRANCÉS: {fran}")
                    else:
                        print("error no exite tal palabra")
                    input("Presiona Enter para continuar...")
                elif palabra==2:
                    pIng=input("Introduzca palabra: ")
                    traduccion=traductor.chercherMotsAnglais(pIng)
                    if traduccion:
                        esp, fran = traduccion
                        print(f"Traducción ESPAÑOL: {esp}, FRANCÉS: {fran}")
                    else:
                        print("error no exite tal palabra")
                    input("Presiona Enter para continuar...")
                elif palabra==3:
                    pFr=input("Introduzca palabra: ")
                    traduccion=traductor.chercherMotsFrancais(pFr)
                    if traduccion:
                        esp, ing = traduccion
                        print(f"Traducción ESPAÑOL: {esp}, Ingles: {ing}")
                    else:
                        print("error no exite tal palabra")
                    input("Presiona Enter para continuar...")
                else:
                    print("opcion no valida")
                    input("Presiona Enter para continuar...")



            elif respuesta==2:
                motEsp=input("palabra español")
                motAng=input("palabra ingles")
                motFran=input("palabra frances")
                traductor.ajouterMots(motEsp,motAng,motFran)
            
            elif respuesta==3:
                break


if __name__ == "__main__":
    run()     