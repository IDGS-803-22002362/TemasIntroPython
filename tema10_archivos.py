from io import open
"""manejo de archivos python"""
texto="une line"
archivo=open("archivo.txt","w")
archivo.write(texto)
texto="deux line"
archivo.write(texto)
archivo.close