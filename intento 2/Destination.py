class Destination:
    def __init__(self, destination:str, destination_cost:int) -> None:
        self.__destination = destination
        self.__destination_cost = destination_cost
    
    def get_destination(self):
        return self.__destination
    
    def get_destination_cost(self):
        return self.__destination_cost