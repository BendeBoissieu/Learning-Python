class Player:
    def __init__(self,pseudo,health,attack ):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def damage(self,damage):
        self.health -= damage
        print('Aie', self.pseudo,  '.... Vous venez de subir ', damage, 'dégats')

    def attack_player(self, target_player ):
        damage = self.attack
        if self.has_weapon():
            damage += self.weapon.get_damage_amount()
        target_player.damage(damage)

    def set_weapon(self,weapon):
        self.weapon = weapon
        return self.weapon.name

    # pour vérifier si le joueur a une arme
    def has_weapon(self):
        if self.weapon is not None:
            return self.weapon
