# Public vs. Private attributes and methods

class Person:
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name # private attribute

class Dog:
    def __init__(self, name: str) -> None:
        self.__name = name  # Private attribute

    def set_name(self, name: str) -> None:  
        # Setter method
        self.__name = name

    def get_name(self) -> str:  
        # Getter method
        return self.__name

