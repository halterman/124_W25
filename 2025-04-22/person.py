class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'<<{self.name}::{self.age}>>'
    
    def get_name(self) -> str:
        return f'*** Name is {self.name} ***'


class Employee(Person):
    def __init__(self, name: str, age: int, id: str) -> None:
        # Let the superclass handle its part of the
        # initialization
        super().__init__(name, age)
        self.id_num = id

class Tool:
    def __init__(self, serial_no: int) -> None:
        self.serial_number = serial_no

    def get_serial_number(self) -> int:
        return self.serial_number


class Hammer(Tool):
    def __init__(self):
        super().__init__(-999)
        print('Just made a hammer object')


if __name__ == '__main__':
    p1 = Person('joe', 20)
    p2 = Person('judith', 23)
    print(p1.get_name())

    e1 = Employee('Fred', 35, '34123')
    print(e1)
    print(e1.get_name())

    t1 = Tool(423)

    print(t1)
    print('Tool t1 serial number:', t1.get_serial_number())

    h1 = Hammer()
    print('Hammer h1 serial number:', h1.get_serial_number())