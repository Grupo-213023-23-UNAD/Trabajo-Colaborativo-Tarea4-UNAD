from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva, ErrorReserva

print("===== INICIO DEL SISTEMA =====\n")

casos = [
    ("Alan", "alan@gmail.com", "3001234567", "Sala", 2),
    ("Maria", "maria@gmail.com", "3019876543", "Equipo", 3),
    ("Luis", "luis@gmail.com", "3025551234", "Asesoria", 1),
    ("", "correo_malo", "abc", "Sala", 2),
    ("Pedro", "pedro@gmail.com", "123", "Equipo", 2),
    ("Ana", "ana@gmail.com", "3001112222", "Otro", 1),
]

print("Cantidad de casos:", len(casos), "\n")

for i, caso in enumerate(casos, start=1):
    print(f"--- Caso {i} ---")

    try:
        nombre, correo, telefono, tipo, cantidad = caso

        cliente = Cliente(nombre, correo, telefono)

        if tipo == "Sala":
            servicio = ReservaSala("Sala VIP", 50)
        elif tipo == "Equipo":
            servicio = AlquilerEquipo("Proyector", 30)
        elif tipo == "Asesoria":
            servicio = Asesoria("Consultoría", 100)
        else:
            raise ErrorReserva("Tipo de servicio no válido")

        costo = servicio.calcular_costo(cantidad)

        reserva = Reserva(cliente, servicio)
        reserva.confirmar()

        print(reserva.mostrar_reserva())
        print("Costo:", costo)

    except Exception as e:
        print("Error detectado:", e)

    finally:
        print("Proceso finalizado\n")

print("===== FIN DEL SISTEMA =====")
input("toque para cerrar el programa")
