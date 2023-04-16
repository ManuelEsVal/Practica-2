class Asiento:
    """
    Clase para representar un asiento en un vuelo.
    """

    def __init__(self, numero: str, tipo: str, precio_adicional: float):
        """
        Constructor de la clase.

        :param numero: str, el número de asiento.
        :param tipo: str, el tipo de asiento (tradicional o VIP).
        :param precio_adicional: float, el precio adicional basado en el tipo de asiento y el destino.
        """
        self.numero = numero
        self.tipo = tipo
        self.estado = True  # True si el asiento está disponible, False si está reservado
        self.precio_adicional = precio_adicional
