"""
=============================================================================
 SOFTWARE FJ -  Registro de Ventas
=============================================================================
 Descripción : Gestiona las ventas confirmadas registradas en memoria.
=============================================================================
"""

import logging


class RegistroVentas:
    """
    Administra las ventas confirmadas del sistema.

    La lista _ventas es privada y solo se manipula mediante métodos públicos.
    """

    def __init__(self):
        """
        Inicializa el registro con una lista vacía de ventas.
        """
        self._ventas = []   # Lista privada de ventas confirmadas

    def registrar(self, reserva):
        """
        Registra una reserva confirmada como venta.

        Args:
            reserva: Objeto Reserva a registrar.
        """
        try:
            # Verificar estado de la reserva
            if reserva.estado != "CONFIRMADA":
                raise ValueError(
                    f"No se puede registrar la reserva '{reserva.id}' "
                    f"porque está en estado '{reserva.estado}'."
                )

            # Agregar reserva al registro
            self._ventas.append(reserva)

            logging.info(
                f"Venta registrada: reserva '{reserva.id}' "
                f"del cliente '{reserva.cliente.get_nombre()}'."
            )

            print(f"  ✔ Venta registrada: {reserva.id}")

        except ValueError as e:
            # Error por estado inválido
            logging.error(f"Error al registrar venta: {e}")
            print(f"  ⚠ No se pudo registrar la venta: {e}")

        except AttributeError as e:
            # Error por atributos faltantes
            logging.error(f"Objeto reserva inválido: {e}")
            print(f"  ⚠ Objeto de reserva inválido: {e}")

        except Exception as e:
            # Registrar errores inesperados
            logging.critical(f"Error crítico al registrar venta: {e}")
            print(f"  ✘ Error inesperado al registrar venta: {e}")

    def obtener_ventas(self) -> list:
        """
        Retorna una copia de las ventas registradas.

        Returns:
            list: Lista de ventas confirmadas.
        """
        return list(self._ventas)   # Copia protegida

    def total_ingresos(self) -> float:
        """
        Calcula el total de ingresos registrados.

        Returns:
            float: Suma total de las ventas.
        """
        total = 0.0   # Acumulador de ingresos

        for venta in self._ventas:
            try:
                # Sumar total de cada venta
                total += venta.total

            except AttributeError:
                # Omitir ventas sin atributo total
                logging.warning(
                    f"La venta '{getattr(venta, 'id', 'desconocida')}' "
                    f"no tiene atributo 'total'."
                )
                continue

        return total

    def cantidad_ventas(self) -> int:
        """
        Retorna la cantidad de ventas registradas.

        Returns:
            int: Número total de ventas.
        """
        return len(self._ventas)
