# reserva.py

# ==============================
# EXCEPCIÓN PERSONALIZADA
# ==============================

class ErrorReserva(Exception):
    pass


# ==============================
# CLASE RESERVA
# ==============================

class Reserva:
    def __init__(self, cliente, servicio):
        try:
            if cliente is None:
                raise ErrorReserva("El cliente no es válido")

            if servicio is None:
                raise ErrorReserva("El servicio no es válido")

            self.cliente = cliente
            self.servicio = servicio
            self.estado = "Pendiente"

        except Exception as e:
            self.__registrar_error(e)
            raise

    # ==============================
    # MÉTODOS PRINCIPALES
    # ==============================

    def confirmar(self):
        try:
            if self.estado == "Confirmada":
                raise ErrorReserva("La reserva ya está confirmada")

            self.estado = "Confirmada"

        except Exception as e:
            self.__registrar_error(e)
            raise

    def cancelar(self):
        try:
            if self.estado == "Cancelada":
                raise ErrorReserva("La reserva ya está cancelada")

            self.estado = "Cancelada"

        except Exception as e:
            self.__registrar_error(e)
            raise

    def mostrar_reserva(self):
        return f"Reserva de {self.cliente.get_nombre()} | Estado: {self.estado}"

    # ==============================
    # LOG DE ERRORES
    # ==============================

    def __registrar_error(self, error):
        try:
            with open("logs.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"[RESERVA ERROR] {str(error)}\n")
        except Exception:
            pass


# ==============================
# PRUEBAS DEL MÓDULO
# ==============================

if __name__ == "__main__":
    from cliente import Cliente
    from servicio import ReservaSala

    print("=== PRUEBAS DE RESERVA ===")

    try:
        cliente = Cliente("Alan", "alan@gmail.com", "3001234567")
        servicio = ReservaSala("Sala VIP", 50)

        reserva = Reserva(cliente, servicio)
        reserva.confirmar()

        print(reserva.mostrar_reserva())

        # Error intencional
        reserva.confirmar()

    except Exception as e:
        print("Error detectado:", e)

input("\nPresiona Enter para salir...")