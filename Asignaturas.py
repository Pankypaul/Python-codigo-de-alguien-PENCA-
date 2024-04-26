
import os
print("Ingreso asignaturas")
edades=0
hombres=0
cantalumnos=0
alumnos1=0
alumnos2=0
alumnos3=0
alumnos4=0
mujeres=0
menores=0
sumedad=0
totalalumnos=0
promedad1=0
promedad2=0
promedad3=0
promedad4=0

while True:
    print("""
    Ingrese una asignatura a ingresar:
    1. Historia del Artes (HH)
    2. Sociedad y derechos de las mujeres (SM)
    3. Estadísticas y Probabilidad poblacionales (EE)
    4. Educación cívica (EC)
    5. Salir
    """)
    opc=int(input())
    if opc==1:
        alumnos1+=1
        cantalumnos+=1
        print("Ingrese su edad")
        edad=int(input())
        edades+=1
        sumedad+=edad
        promedad1=sumedad/edades
        print("Ingrese su género: (V/F)")
        género=input()
        if género=="V":
            hombres+=1
            
    if opc==2:
        alumnos2+=1
        cantalumnos+=1
        print("Ingrese su edad")
        edad=int(input())
        edades+=1
        sumedad+=edad
        promedad2=sumedad/edades
        print("Ingrese su género: (M/F)")
        género=input()
        if género=="M" or género=="m":
            hombres+=1
        elif género=="f" or género=="F":
            mujeres+=1
            
    if opc==3:
        alumnos3+=1
        cantalumnos+=1
        print("Ingrese su edad")
        edad=int(input())
        edades+=1
        sumedad+=edad
        promedad3=sumedad/edades
        print("Ingrese su género: (V/M)")
        género=input()
        if género=="M" or género=="m":
            hombres+=1
        elif género=="f" or género=="F":
            mujeres+=1
            
    if opc==4:
        alumnos4+=1
        cantalumnos+=1
        print("Ingrese su edad")
        edad=int(input())
        if edad >=18 and edad <=20:
            menores+=1
        edades+=1
        sumedad+=edad
        promedad4=sumedad/edades
        print("Ingrese su género: (F/M)")
        género=input()
        if género=="M" or género=="m":
            hombres+=1
        elif género=="f" or género=="F":
            mujeres+=1
            
    if opc==5:
        totalalumnos+=totalalumnos+cantalumnos
        if totalalumnos == 0:
            print("No hya ningún alumno registrado")
        else:
            
            print(f"""
                *************************************************************************************************************
                * Cantidad de alumnos que tomaron una asignatura extra:{totalalumnos}                                       *
                *************************************************************************************************************
                * Cantidad de hombres por cada asignatura:{hombres}                                                         *
                *************************************************************************************************************
                * Promedio de edad alumnos por cada asignatura: Historia del Artes (HH): {promedad1}                        *
                *                                              Sociedad y derechos de las mujeres (SM): {promedad2}         *
                *                                              Estadísticas y Probabilidad poblacionales (EE): {promedad3}  *
                *                                              Educación cívica (EC): {promedad4}                           *
                *************************************************************************************************************
                * Cantidad de alumnos por cada asignatura extra: Historia del Artes (HH): {alumnos1}                        *
                *                                                Sociedad y derechos de las mujeres (SM): {alumnos2}        *
                *                                                Estadísticas y Probabilidad poblacionales (EE): {alumnos3} *
                *                                                Educación cívica (EC): {alumnos4}                          *
                *************************************************************************************************************
                * Cantidad de mujeres que tomaron SM: {mujeres}                                                             *
                *************************************************************************************************************
                * Cantidad de hombres entre 18 y 20 años que tomaron EC: {menores}                                          *
                *************************************************************************************************************
                """)
    
