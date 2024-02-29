from ListaCircular import ListaCircularDoble
polinomio_a = ListaCircularDoble()
polinomio_b = ListaCircularDoble()
lista_a = []
lista_b = []

print('Parcial 1')
while True:
    #Se pregunta a que polinomio se desea ingresar o mostrar
    print('¿Para que polinomio desea ingresar numeros?')
    print('1- Polinomio a')
    print('2- Polinomio b')
    print('3- Mostrar los 2 polinomios ')
    print('4- Sumar los polinomios')
    op = int(input('Ingrese su opción: '))
    #Si se elije la opcion 1 se ingresa al polinomio a
    if op == 1:
        #Se pregunta que se desea realizar
        print('Ingreso al POLINOMIO A')
        print('¿Qué desea realizar para el polinomio a?')
        print('1- Ingresar números')
        print('2- Reemplazar números')
        print('3- Evaluar valor')
        a = int(input('Ingrese su opción: '))
        #Opcion para agregar los numeros y constuir polinomio
        if a == 1:
            #grado del polinomio
            print('¿Cuántos números desea ingresar? El máximo es de 5 numeros')
            pol_a = int(input('Ingrese la cantidad de numeros: '))
            if pol_a == 1:
                #se pide que se ingrese el numero y se inserta al inicio
                num1 = int(input('Ingrese su numero: '))
                polinomio_a.insertar_inicio(num1)
                lista_a.append(num1)
                print(lista_a)

            elif pol_a == 2:
                #se piden dos numeros y se añaden
                num1 = int(input('Ingrese su primer numero: '))
                num2 = int(input('Ingrese su segundo número: '))
                polinomio_a.insertar_inicio(num1)
                polinomio_a.insertar_inicio(num2)
                lista_a.append(num1)
                lista_a.append(num2)
            elif pol_a == 3:
                num1 = int(input('Ingrese su primer numero: '))
                num2 = int(input('Ingrese su segundo número: '))
                num3 = int(input('Ingrese su tercer número: '))
                polinomio_a.insertar_inicio(num1)
                polinomio_a.insertar_inicio(num2)
                polinomio_a.insertar_inicio(num3)
                lista_a.append(num1)
                lista_a.append(num2)
                lista_a.append(num3)
            elif pol_a == 4:
                num1 = int(input('Ingrese su primer número: '))
                num2 = int(input('Ingrese su segundo número: '))
                num3 = int(input('Ingrese su tercer número: '))
                num4 = int(input('Ingrese su cuarto número: '))
                polinomio_a.insertar_inicio(num1)
                polinomio_a.insertar_inicio(num2)
                polinomio_a.insertar_inicio(num3)
                polinomio_a.insertar_inicio(num4)
                lista_a.append(num1)
                lista_a.append(num2)
                lista_a.append(num3)
                lista_a.append(num4)

            elif pol_a == 5:
                num1 = int(input('Ingrese su primer número: '))
                num2 = int(input('Ingrese su segundo número: '))
                num3 = int(input('Ingrese su tercer número: '))
                num4 = int(input('Ingrese su cuarto número: '))
                num5 = int(input('Ingrese su quinto número: '))
                polinomio_a.insertar_inicio(num1)
                polinomio_a.insertar_inicio(num2)
                polinomio_a.insertar_inicio(num3)
                polinomio_a.insertar_inicio(num4)
                polinomio_a.insertar_inicio(num5)
                lista_a.append(num1)
                lista_a.append(num2)
                lista_a.append(num3)
                lista_a.append(num4)
                lista_a.append(num5)
        #opcion para actualizar el polinomio
        elif a == 2:
            print('Desa actualizar el polinomio a')
            if polinomio_a.vacio():
                print('Esta vacío')
            else:
                #se pregunta por el dato que se desea reeemplazar
                dato_viejo = int(input('Ingrese su dato viejo: '))
                dato_nuevo = int(input('Ingrese su dato nuevo: '))
                polinomio_a.actualizar(dato_viejo, dato_nuevo)
                print('Se remplazo el numero', dato_viejo, 'por', dato_nuevo)

        elif a == 3:
            valor = int(input('¿Qué valor desea evaluar?: '))
            print(polinomio_a.imprimir_lista_con_valor(valor))
    elif op == 2:
        #lo mismo que el polinomio a
        print('Ingreso al POLINIOMIO B')
        print('1- Ingresar números')
        print('2- Reemplazar números')
        print('3- Evaluar valor')
        b = int(input('Ingrese su opción: '))
        if b == 1:
            print('Desea ingresar numeros para el polinomio b')
            print('¿Cuántos números desea ingresar? El máximo es de 5 numeros')
            pol_b = int(input('Ingrese la cantidad de numeros: '))
            if pol_b == 1:
                num1 = int(input('Ingrese su numero: '))
                polinomio_b.insertar_inicio(num1)
                lista_b.append(num1)

            elif pol_b == 2:
                num1 = int(input('Ingrese su primer numero: '))
                num2 = int(input('Ingrese su segundo número: '))
                polinomio_b.insertar_inicio(num1)
                polinomio_b.insertar_inicio(num2)
                lista_b.append(num1)
                lista_b.append(num2)
            elif pol_b == 3:
                num1 = int(input('Ingrese su primer numero: '))
                num2 = int(input('Ingrese su segundo número: '))
                num3 = int(input('Ingrese su tercer número: '))
                polinomio_b.insertar_inicio(num1)
                polinomio_b.insertar_inicio(num2)
                polinomio_b.insertar_inicio(num3)
                lista_b.append(num1)
                lista_b.append(num2)
                lista_b.append(num3)
            elif pol_b == 4:
                num1 = int(input('Ingrese su primer número: '))
                num2 = int(input('Ingrese su segundo número: '))
                num3 = int(input('Ingrese su tercer número: '))
                num4 = int(input('Ingrese su cuarto número: '))
                polinomio_b.insertar_inicio(num1)
                polinomio_b.insertar_inicio(num2)
                polinomio_b.insertar_inicio(num3)
                polinomio_b.insertar_inicio(num4)
                lista_b.append(num1)
                lista_b.append(num2)
                lista_b.append(num3)
                lista_b.append(num4)

            elif pol_b == 5:
                num1 = int(input('Ingrese su primer número: '))
                num2 = int(input('Ingrese su segundo número: '))
                num3 = int(input('Ingrese su tercer número: '))
                num4 = int(input('Ingrese su cuarto número: '))
                num5 = int(input('Ingrese su quinto número: '))
                polinomio_b.insertar_inicio(num1)
                polinomio_b.insertar_inicio(num2)
                polinomio_b.insertar_inicio(num3)
                polinomio_b.insertar_inicio(num4)
                polinomio_b.insertar_inicio(num5)
                lista_b.append(num1)
                lista_b.append(num2)
                lista_b.append(num3)
                lista_b.append(num4)
                lista_b.append(num5)
        elif b == 2:
            print('Desa actualizar el polinomio b')
            if polinomio_b.vacio():
                print('Esta vacío')
            else:
                dato_viejo = int(input('Ingrese su dato viejo: '))
                dato_nuevo = int(input('Ingrese su dato nuevo: '))
                polinomio_b.actualizar(dato_viejo, dato_nuevo)

                print('Se remplazo el numero', dato_viejo,'por', dato_nuevo)

        elif b == 3:
            valor = int(input('¿Qué valor desea evaluar?: '))
            print(polinomio_b.imprimir_lista_con_valor(valor))

    elif op == 3:
        print(polinomio_a.imprimir_lista_con_valor(4))
        print(polinomio_b.imprimir_lista())
        exit()

