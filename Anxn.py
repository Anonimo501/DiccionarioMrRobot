#!/usr/bin/env python
#_*_ coding: utf8 _*_

#MIT License

#Copyright (c) [2021] [Anonimo501]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

def dicnumerico(v1,v2):
    pass
    
def dicmrrobot(v1,v2,v3):
    pass

def diccompleto(v1,v2,v3,v4,v5,v6):
    pass
    
def main():
    while True:     ### Bucle - Menu
        print ("\n Bienvenid@ \n")
        print ("""
                /\  |\ | \/ |\ |
               /  \ | \| /\ | \|
        """)

        print("\n 1. - Cree su Dicionario de numeros")
        print(" 2. - Dicionario Mr Robot - Numerico")
        print(" 3. - Dicionario Mr Robot - Completo")
        print(" 5. - Salir\n")
        opcion = int(raw_input("Anonimo501$ - Opcion : "))
        
            ### Dicionario Numerico
            
        if opcion == 1:     ## opcion1
            archivo = open('DiccNumeros.txt','w')       ### Crea y abre un archivo de texto
            print ("\n [+] Cree su Dicionario de numeros [+] \n")       ### Titulo
            v1 = int(raw_input("Digite un Numero inicial - [Ejemplo] 3259000 : "))      ### Pide info al usuario
            v2 = int(raw_input("Digite un Numero Final - [Ejemplo] 3259099 : "))        ### Pide info al usuario
            dicnumerico(v1,v2)      ### envia las variables a def

            for n in range(v1,v2):      ### Bucle
                print ("{}".format(n))      ### Imprime en pantalla el bucle
                archivo.write(str(n))       ### Escribe sobre el archivo 
                archivo.write("\n")     ### Cambio de linea o Enter
                
            if v2 < v1:     ### Si la variable 1 es menor a la variable 2 ejecute la siguiente linea
                print ("\n [+] Digite el numero MAYOR PRIMERO! [+]")
            elif v1 == v2:      ### si la variable 1 y 2 son iguales imprima la siguiente linea
                print ("\n [+] Son iguales - Digite numeros diferentes[+]")

            archivo.close()     ### Cierra el archivo que se creo
            
                ### Diccionario Mr Robot Numerico

        if opcion == 2:     ### opcion 2
            archivo = open('DiccMrRobotNumerico.txt','w')   ### Crea y abre un archivo de texto
            print ("\n [+] Dicionario Mr Robot - Nombre Numerico[+] \n")        ### Titulo

            v1 = raw_input("Digite un Nombre - [Ejemplo] Arturo : ")        ### Pide info al usuario
            v2 = int(raw_input("Digite #1 en Numero - [Ejemplo] 1900 : "))      ### Pide info al usuario
            v3 = int(raw_input("Digite  el Numero Final - [Ejemplo] 2021 : "))      ### Pide info al usuario
            dicmrrobot(v1,v2,v3)        ### envia las variables a def

            for n in range(v2,v3):      ### Bucle
                print ("{}{}".format(v1,n))     ### Imprime en pantalla el bucle
                archivo.write(str(v1))      ### Escribe sobre el archivo
                archivo.write(str(n))       ### Escribe sobre el archivo
                archivo.write("\n")     ### Cambio de linea o Enter
            
            if v2 < v1:     ### Si la variable 1 es menor a la variable 2 ejecute la siguiente linea
                print ("\n [+] Digite el numero MAYOR PRIMERO! [+]")
            elif v2 == v3:      ### si la variable 1 y 2 son iguales imprima la siguiente linea
                print ("\n [+] Son iguales - Digite numeros diferentes[+]")
                
            archivo.close()     ### Cierra el archivo que se creo

            ### Dicionario Mr Robot - Completo
            
        elif opcion == 3:       ### opcion 3
            archivo = open('DiccMrRoboCompleto.txt','w')        ### Crea y abre un archivo de texto
            print ("\n [+] Dicionario Mr Robot  - Completo [+] \n")     ### Titulo
            
            v1 = raw_input("\nIngrese el nombre : ")        ### Pide info al usuario
            v2 = int(raw_input("Ingrese Fecha de Inicio : "))       ### Pide info al usuario
            v3 = int(raw_input("Ingrese Fecha Final : "))       ### Pide info al usuario
            v4 = raw_input("Ingrese el Nombre de la Mascota : ")        ### Pide info al usuario
            v5 = raw_input("Ingrese el Nombre del barrio donde vive : ")        ### Pide info al usuario
            v6 = raw_input("Ingrese el Nombre del Dios  en el que Cree : ")     ### Pide info al usuario
            diccompleto(v1,v2,v3,v4,v5,v6)      ### envia las variables a def
            
            for n in range(v2,v3):      ### Bucle
                print("{}{}".format(v1,n))       ### Imprime en pantalla el bucle
                print("{}{}".format(v4,n))       ### Imprime en pantalla el bucle
                print("{}{}".format(v5,n))       ### Imprime en pantalla el bucle
                print("{}{}".format(v6,n))       ### Imprime en pantalla el bucle
                
                archivo.write(str(v1))      ### Escribe sobre el archivo
                archivo.write(str(n))       ### Escribe sobre el archivo
                archivo.write("\n")     ### Cambio de linea o Enter
                archivo.write(str(v4))      ### Escribe sobre el archivo
                archivo.write(str(n))       ### Escribe sobre el archivo
                archivo.write("\n")     ### Cambio de linea o Enter
                archivo.write(str(v5))      ### Escribe sobre el archivo
                archivo.write(str(n))       ### Escribe sobre el archivo
                archivo.write("\n")     ### Cambio de linea o Enter
                archivo.write(str(v6))      ### Escribe sobre el archivo
                archivo.write(str(n))       ### Escribe sobre el archivo
                archivo.write("\n")     ### Cambio de linea o Enter
                
            archivo.close()     ### Cierra el archivo que se creo
        
        elif opcion == 5:       ### opcion 3
            exit()      ### Cierra el programa
    
if __name__ == '__main__':
    main()      ### main