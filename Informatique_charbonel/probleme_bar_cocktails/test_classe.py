#!/bin/env python3

class Verb():
    def __init__(self,nv):
        self.nv = nv
    def __str__(self):
        return f"{[self.__class__.__name__]}"

class Accessoire(Verb):
    def __init__(self,Verb1):
        super().__init__(Verb1.nv)
        self.list= []

    
Verb1 = Verb(3)
Accesoire1 = Accessoire(Verb1)

print(f"Verb1.nv = {Verb1.nv}")
print(Accesoire1)
print(f"Accesoire1.nv = {Accesoire1.nv}")