class TipoAsiento:
    def __init__(self, ticket_type:str, porcent:float):
        self.ticket_type = ticket_type
        self.__porcent = porcent

    def get_tipo(self):
        return self.ticket_type
    
    def get_porcentaje(self):
        return self.__porcent