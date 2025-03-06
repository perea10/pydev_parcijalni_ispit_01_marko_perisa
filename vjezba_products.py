


class Product:
    def __init__(self, 
                 name: str, 
                 price: float,
                 description=''):
        self.name = name
        self.price = price
        self.description = description 

    def display(self) -> str:
        print(f'Naziv: {self.name}')
    
    def __repr__(self):
        return f'repr Naziv: {self.name}'