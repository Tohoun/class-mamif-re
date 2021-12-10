from abc import ABC, abstractmethod
class Mamifere:
    def __init__(self,locomotion,type) -> None:
        self.locomotion=locomotion
        self.type=type
    
    @abstractmethod
    def habitat(self):
        pass
        

class Humain(Mamifere):
    def habitat(self):
        print(f"j'habite dans une maison")

class Lemurien(Mamifere):
    def habitat(self):
        print(f"j'habite dans un terrier")

class Caractere(Mamifere):
    def __init__(self, locomotion, type,mdc) -> None:
        super().__init__(locomotion, type)
        self.__mdc=mdc
# mdc=mode de communication
#type=("herbivore","carnivore","omnivore")


p1 = Humain("pieds","omnivor")
p1.habitat()