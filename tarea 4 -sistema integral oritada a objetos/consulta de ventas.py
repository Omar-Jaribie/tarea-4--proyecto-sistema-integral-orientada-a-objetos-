"""
=============================================================================
 SOFTWARE FJ - Consulta de Ventas
=============================================================================
 Descripción : Métodos estáticos para consultar y mostrar ventas registradas.
=============================================================================
""" 


import logging

# consulta de ventas y errores de acceso a atributos de reserva 
class ConsultaVentas:

    @staticmethod
    def total_ventas(ventas: list) -> float:
        """
        Calcula el total acumulado de las ventas.

        Args:
            ventas (list): Lista de reservas.

        Returns:
            float: Total de ventas.
        """
        total = 0.0

        for v in ventas:
            try:
                # Sumar total de cada reserva 
                total += v.total

            except AttributeError:
                # Omitir reservas sin total
                logging.warning(
                    f"La reserva '{getattr(v, 'id', 'desconocida')}' "
                    f"no tiene total calculado."
                )
                continue

            except Exception as e:
                # Registrar errores inesperados y continuar
                logging.error(
                    f"Error al sumar venta "
                    f"'{getattr(v, 'id', 'desconocida')}': {e}"
                )
                continue

        return total

    @staticmethod
    def mostrar_resumen(ventas: list):
        """
        Muestra un resumen de las ventas.

        Args:
            ventas (list): Lista de reservas.
        """
        print("\n" + "=" * 55)
        print("         RESUMEN DE VENTAS - SOFTWARE FJ")
        print("=" * 55)

        # Verificar si hay ventas registradas antes de mostrar el resumen 
        if not ventas:
            print("  No hay ventas registradas aún.")
        else:
            # Encabezado
            print(f"  {'ID':<12} {'CLIENTE':<22} {'ESTADO':<15} {'TOTAL'}")
            print("  " + "-" * 51)

            for v in ventas:
                try:
                    # Obtener datos de la reserva 
                    id_reserva = getattr(v, 'id', 'N/A')
                    nombre = v.cliente.get_nombre()
                    estado = getattr(v, 'estado', 'DESCONOCIDO')
                    total = getattr(v, 'total', 0.0)

                    print(
                        f"  {id_reserva:<12} "
                        f"{nombre:<22} "
                        f"{estado:<15} "
                        f"${total:.2f}"
                    )

                except Exception as e:
                    # Continuar si ocurre un error
                    logging.error(f"Error al mostrar reserva: {e}")
                    print(f"  [Error al leer esta reserva: {e}]")

        # Mostrar total general
        total_general = ConsultaVentas.total_ventas(ventas)
        print("  " + "-" * 51)
        print(f"  {'TOTAL GENERAL':<35} ${total_general:.2f}")
        print("=" * 55)
            
