class TipoAsiento:

    def __init__(self , tipo = 1 , porcentaje = .10 ):
      
        self.__nombre = str
        self.__tipo = tipo
        self.__porcentaje = porcentaje

        self.set_nombre() 

    def set_nombre(self):
        
        if self.__tipo == 1:
            self.__nombre = "Asiento tradicional"
        else:
            self.__tipo == 2: 
            self.__nombre = "Asiento VIP"
        

    def get_nombre(self):

        return self.__nombre

# Este lo podemos modificar o quitar al final  

    def get_tipo(self):

        return self.__tipo
    

    def get_porcentaje(self):
       
        return self.__porcentaje

