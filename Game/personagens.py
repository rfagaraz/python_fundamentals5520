# -*- coding: utf-8 -*-
from random import randint

class Personagem:
    def __init__(self):
        self.hp = 100
        self.xp = 0
        self.mp = 100
        self.nivel = 1
        self.esquiva = 0

    def subirNivel(self):
        if self.xp > (99 * self.nivel):
            self.nivel += 1
            print("Level UP!")

    
class Mago(Personagem):
    def __init__(self):
        super().__init__()
        self.inteligencia = True
        self.msg_atq = "Magia das Trevas!!"
        self.poderEspecial = 3

    def recuperacaoMana(self):
        if self.poderEspecial > 0:
            self.mp = 100
            print("Mana Recuperada!!")
            self.poderEspecial -= 1
        else:
            print("Sem Poder Especial")


class Guerreiro(Personagem):
    def __init__(self):
        super().__init__()
        self.forca = True
        self.msg_atq = "Estocada violenta!!"
        self.poderEspecial = 3

    def furia(self):
        if self.poderEspecial > 0:
            if self.hp < 100:
                self.hp += self.hp + (self.hp * 0.10)
                self.poderEspecial -= 1
            else:
                print("HP está cheio")
        else:
            print("Sem Poder Especial")


