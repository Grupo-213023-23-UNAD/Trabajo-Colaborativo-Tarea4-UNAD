from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva, ErrorReserva

print("===== INICIO DEL SISTEMA =====\n")

# ==============================
# CASOS DE PRUEBA (10)
# ==============================

casos = [
    ("Alan", "alan@gmail.com", "3001234567", "Sala", 2),
    ("Maria", "maria@gmail.com", "3019876543", "Equipo", 3),
    ("Luis", "luis@gmail.com", "3025551234", "Asesoria", 1),

    ("", "correo_malo", "abc", "Sala", 2),
    ("Pedro", "pedro@gmail.com", "123", "Equipo", 2),
    ("Ana", "ana@gmail.com", "3001112222", "Otro", 1),

    ("Carlos", "carlos@gmail.com", "3009991111", "Sala", 2),
    ("Laura", "laura@gmail.com", "3008887777", "Asesoria", 2),
    ("Andres", "", "3001231234", "Equipo", 1),
    ("Sofia", "sofia@gmail.com", "abc", "Sala", 3),
]

print("Cantidad de casos:", len(casos), "\n")

# ==============================
# EJECUCIÓN
# ==============================

for i, caso in enumerate(casos, start=1):
    print(f"--- Caso {i} ---")

    try:
        nombre, correo, telefono, tipo, cantidad = caso

        # Crear cliente
        cliente = Cliente(nombre, correo, telefono)

        # Crear servicio
        if tipo == "Sala":
            servicio = ReservaSala("Sala VIP", 50)
        elif tipo == "Equipo":
            servicio = AlquilerEquipo("Proyector", 30)
        elif tipo == "Asesoria":
            servicio = Asesoria("Consultoría", 100)
        else:
            raise ErrorReserva("Tipo de servicio no válido")

        # Calcular costo
        costo = servicio.calcular_costo(cantidad)

        # Crear reserva
        reserva = Reserva(cliente, servicio)
        reserva.confirmar()

        # Mostrar resultado
        print(reserva.mostrar_reserva())
        print("Costo:", costo)

        # Cancelar en algunos casos (pares)
        if i % 2 == 0:
            reserva.cancelar()
            print("Reserva cancelada correctamente")

    except Exception as e:
        print("Error detectado:", e)

    finally:
        print("Proceso finalizado\n")


print("===== FIN DEL SISTEMA =====")
input("toque para cerrar el programa")
