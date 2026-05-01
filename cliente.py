# cliente.py

# ==============================
# EXCEPCIONES PERSONALIZADAS
# ==============================

class NombreInvalidoError(Exception):
    pass


class CorreoInvalidoError(Exception):
    pass


class TelefonoInvalidoError(Exception):
    pass


# ==============================
# CLASE CLIENTE
# ==============================

class Cliente:
    def __init__(self, nombre, correo, telefono):
        try:
            self.__nombre = self.__validar_nombre(nombre)
            self.__correo = self.__validar_correo(correo)
            self.__telefono = self.__validar_telefono(telefono)
        except Exception as e:
            self.__registrar_error(e)
            raise

    # ==============================
    # VALIDACIONES
    # ==============================

    def __validar_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise NombreInvalidoError("El nombre no puede estar vacío")
        return nombre.strip()

    def __validar_correo(self, correo):
        if "@" not in correo or "." not in correo:
            raise CorreoInvalidoError("El correo no es válido")
        return correo

    def __validar_telefono(self, telefono):
        if not telefono.isdigit():
            raise TelefonoInvalidoError(
                "El teléfono debe contener solo números")
        if len(telefono) < 7:
            raise TelefonoInvalidoError("El teléfono es demasiado corto")
        return telefono

    # ==============================
    # GETTERS (ENCAPSULACIÓN)
    # ==============================

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # ==============================
    # MÉTODOS
    # ==============================

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo} | Teléfono: {self.__telefono}"

    def __str__(self):
        return self.mostrar_info()

    # ==============================
    # LOG DE ERRORES
    # ==============================

    def __registrar_error(self, error):
        try:
            with open("logs.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"[CLIENTE ERROR] {str(error)}\n")
        except Exception:
            pass


# ==============================
# PRUEBAS BÁSICAS
# ==============================

if __name__ == "__main__":
    print("=== Pruebas de Cliente ===")

    # Caso válido
    try:
        c1 = Cliente("Jeisson", "jeisson@gmail.com", "3001234567")
        print(c1)
    except Exception as e:
        print("Error:", e)

    # Caso inválido
    try:
        c2 = Cliente("", "correo_invalido", "abc")
    except Exception as e:
        print("Error detectado:", e)
