from abc import ABC, abstractmethod
class Mamifere:
    def __init__(self,locomotion,type) -> None:
        self.locomotion=locomotion
        self.type=type
        
    @abstractmethod
    def habitat(self):
        pass
    @abstractmethod
    def mdc(self):
        pass
        

class Humain(Mamifere):
    def habitat(self):
        print("Habite dans une maison")
    def mdc(self):
        print("Parle")


class Lemurien(Mamifere):
    def habitat(self):
        print("Vit dans un terrier")
    def mdc(self):
        print("Fait un bruit de lémurien")

#type=("herbivore","carnivore","omnivore")


p1 = Humain("pieds","omnivor")
p1.habitat()
p1.mdc()