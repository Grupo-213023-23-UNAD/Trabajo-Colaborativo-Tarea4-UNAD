from abc import ABC, abstractmethod


# ==============================
# CLASE ABSTRACTA
# ==============================

class Servicio(ABC):
    def __init__(self, nombre, precio):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del servicio no puede estar vacío")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    def descripcion(self):
        return f"Servicio: {self.nombre} | Precio base: {self.precio}"


# ==============================
# CLASES HIJAS (POLIMORFISMO)
# ==============================

class ReservaSala(Servicio):
    def calcular_costo(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero")
        return self.precio * cantidad


class AlquilerEquipo(Servicio):
    def calcular_costo(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero")
        return self.precio * cantidad


class Asesoria(Servicio):
    def calcular_costo(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero")
        return self.precio * cantidad * 1.2


# ==============================
# PRUEBAS DEL MÓDULO
# ==============================

if __name__ == "__main__":
    print("=== PRUEBAS DE SERVICIOS ===")

    try:
        s1 = ReservaSala("Sala VIP", 50)
        print(s1.descripcion())
        print("Costo:", s1.calcular_costo(2))

        s2 = AlquilerEquipo("Proyector", 30)
        print(s2.descripcion())
        print("Costo:", s2.calcular_costo(3))

        s3 = Asesoria("Consultoría", 100)
        print(s3.descripcion())
        print("Costo:", s3.calcular_costo(2))

        # Error intencional
        s4 = ReservaSala("", -10)

    except Exception as e:
        print("Error en Servicio:", e)
