# Sistema de Reservas en Python

## Descripción

Este proyecto consiste en el desarrollo de un sistema de reservas utilizando Python y aplicando los principios de la Programación Orientada a Objetos (POO), como encapsulación, herencia y polimorfismo.

El sistema permite gestionar clientes, servicios y reservas, además de manejar errores y validar datos ingresados.

## Integrantes

* Alan Kenneth Gonzalez Cohecha
* Leonardo isaias Gonzalez Cohecha
* Jeisson Alexander Tamayo Rueda

## Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

* `cliente.py`: Maneja la información del cliente con validaciones y registro de errores.
* `servicio.py`: Contiene la clase abstracta Servicio y sus implementaciones (ReservaSala, AlquilerEquipo, Asesoria).
* `reserva.py`: Gestiona la creación, confirmación y estado de las reservas.
* `main.py`: Archivo principal que ejecuta el sistema mediante simulaciones.

## Funcionalidades

* Creación de clientes con validación de datos.
* Manejo de diferentes tipos de servicios.
* Creación y confirmación de reservas.
* Cálculo automático de costos.
* Manejo de errores mediante excepciones.
* Registro de errores en archivo `logs.txt`.

## Ejecución del programa

El programa puede ejecutarse de dos formas:

### Opción 1 (Recomendada)

Abrir una terminal en la carpeta del proyecto y ejecutar:

python main.py

### Opción 2

También se puede ejecutar dando doble clic sobre el archivo `main.py` desde el explorador de Windows.
En este caso, el programa mostrará los resultados y esperará una entrada del usuario para cerrarse.

## Notas

* El sistema ejecuta automáticamente varios casos de prueba (correctos y con errores).
* No es necesario ingresar datos manualmente.
* La carpeta `__pycache__` es generada automáticamente por Python y no afecta la ejecución.

## Autor

Trabajo realizado como parte del curso de Programación – UNAD.
