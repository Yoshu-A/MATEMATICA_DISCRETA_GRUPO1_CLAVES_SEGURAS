from combinatoria import conteo_total, entropia_combinatoria, combinacion
from validador_claves import validar_clave
from generador_claves import generar_clave_segura


def menu():
    while True:
        print("\n--- SISTEMA DE CLAVES SEGURAS ---")
        print("1. Calcular número total de claves posibles")
        print("2. Calcular entropía combinatoria")
        print("3. Validar una clave")
        print("4. Generar clave segura")
        print("5. Calcular combinación C(n,r)")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alfabeto = int(input("Tamaño del alfabeto: "))
            longitud = int(input("Longitud de la clave: "))
            total = conteo_total(alfabeto, longitud)
            print(f"Total de claves posibles: {total}")

        elif opcion == "2":
            alfabeto = int(input("Tamaño del alfabeto: "))
            longitud = int(input("Longitud de la clave: "))
            entropia = entropia_combinatoria(alfabeto, longitud)
            print(f"Entropía combinatoria: {entropia:.2f} bits")

        elif opcion == "3":
            clave = input("Ingrese la clave a validar: ")
            if validar_clave(clave):
                print("La clave cumple la política de seguridad.")
            else:
                print("La clave NO cumple la política de seguridad.")

        elif opcion == "4":
            longitud = int(input("Longitud de la clave segura: "))
            clave = generar_clave_segura(longitud)
            print(f"Clave generada: {clave}")

        elif opcion == "5":
            n = int(input("Valor de n: "))
            r = int(input("Valor de r: "))
            resultado = combinacion(n, r)
            print(f"C({n},{r}) = {resultado}")

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
