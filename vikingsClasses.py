import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def battleCry(self):
        return f"Odin Owns You All!."

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has receiver {damage} points of damage."
        else:
            return f"{self.name} has died in act of combat."

# Saxon
#delete

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage."
        else:
            return "A Saxon has died in combat."

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!."
        elif len(self.vikingArmy) == 0:
            return "Saxon have fought for their lives and survived another day."
        else:
            return "Vikings and Saxon are still in the thick of battle."
    """    
    pass

#yop
class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass
    """

