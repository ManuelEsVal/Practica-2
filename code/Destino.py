class Destino:
    def __init__(self, nombre, precio_base, num_asientos):
        """
        Crea un nuevo objeto Destino con los datos del destino.

        Args:
        nombre (str): El nombre del destino.
        precio_base (float): El precio base de un asiento en este destino.
        num_asientos (int): El número total de asientos disponibles en este destino.
        """
        self.nombre = nombre
        self.precio_base = precio_base
        self.num_asientos = num_asientos
        self.asientos_disponibles = {'T': [], 'V': []}
        self._crear_asientos()

    def _crear_asientos(self):
        """
        Crea y asigna los asientos al objeto destino.
        """
        for i in range(1, 31):
            self.asientos_disponibles['T'].append('T{:02d}'.format(i))
        for i in range(31, 51):
            self.asientos_disponibles['V'].append('V{:02d}'.format(i))

    def calcular_precio(self, tipo_asiento):
        """
        Calcula el precio total de un asiento, dada su categoría.

        Args:
        tipo_asiento (str): La categoría del asiento ('T' para tradicional o 'V' para VIP).

        Returns:
        float: El precio total del asiento, incluyendo el precio base y el porcentaje adicional.
        """
        if tipo_asiento == 'T':
            porcentaje_adicional = 0.1
        elif tipo_asiento == 'V':
            porcentaje_adicional = 0.5
        return self.precio_base * (1 + porcentaje_adicional)

    def reservar_asiento(self, tipo_asiento):
        """
        Reserva un asiento en el destino, dada su categoría.

        Args:
        tipo_asiento (str): La categoría del asiento ('T' para tradicional o 'V' para VIP).

        Returns:
        str: El número del asiento reservado, o None si no hay asientos disponibles.
        """
        if self.num_asientos <= 0:
            return None

        if not self.asientos_disponibles[tipo_asiento]:
            return None

        num_asiento = self.asientos_disponibles[tipo_asiento].pop(0)
        self.num_asientos -= 1
        return num_asiento

    def cancelar_asiento(self, tipo_asiento, num_asiento):
        """
        Cancela un asiento en el destino, dada su categoría y número.

        Args:
        tipo_asiento (str): La categoría del asiento ('T' para tradicional o 'V' para VIP).
        num_asiento (str): El número del asiento a cancelar.
        """
        self.asientos_disponibles[tipo_asiento].append(num_asiento)
        self.num_asientos += 1

