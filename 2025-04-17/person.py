class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'<<{self.name}::{self.age}>>'

class Employee(Person):
    def __init__(self, name: str, age: int, id: str) -> None:
        # Let the superclass handle its part of the
        # initialization
        super().__init__(name, age)
        self.id_num = id



if __name__ == '__main__':
    p1 = Person('joe', 20)
    p2 = Person('judith', 23)
    print(p1)
    print(p2)
    p1.name = 'skip'
    print(p1)
    