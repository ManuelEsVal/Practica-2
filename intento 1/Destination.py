
class Destination:
    def __init__(self, destination:str, destination_complete_cost:int, ticket_types:list) -> None:
        self.destination = destination
        self.destination_complete_cost = destination_complete_cost
        self.ticket_types = ticket_types
               
    def tickets_cost_per_unit(self, first_ticket_porcentaje:int, second_porcentaje_porcentaje:int):
        self.first_ticket_porcentaje = first_ticket_porcentaje
        self.second_porcentaje_porcentaje = second_porcentaje_porcentaje
        
        self.ticket_1 = self.ticket_types[0]
        self.ticket_2 = self.ticket_types[1]
        
        self.ticket_value_1 = (self.destination_complete_cost * (1 + self.first_ticket_porcentaje))
        self.ticket_value_2 = (self.destination_complete_cost * (1 + self.second_ticket_porcentaje))
        
        print(self.ticket_1,self.ticket_value_1)
        print(self.ticket_2,self.ticket_value_2)
        
    def destiny_list(self, first_option:str, second_option:str, third_option:str):
        self.first_option = first_option
        self.second_option = second_option
        self.third_option = third_option
        
        self.destination_list = [self.first_option, self.second_option, self.third_option]
        pass