from abc import ABC, abstractmethod
class Mamifere:
    def __init__(self,locomotion,milieu_de_vie) -> None:
        self.locomotion=locomotion
        self.milieu_de_vie=milieu_de_vie
    
    @abstractmethod
    def habitat(self):
        pass
        

class Humain(Mamifere):
    def habitat(self):
        print(f"j'habite dans une maison")

class Lemurien(Mamifere):
    def habitat(self):
        print(f"j'habite dans un terrier")


p1 = Humain("pieds","omnivor")
p1.habitat()