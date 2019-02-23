from model.Players import Player, Warrior
from model.weapon import Weapon

knife = Weapon('knife', 6)
player1 = Player('Ben', 20, 3)
player2 = Player('Rene', 15, 4)
warrior = Warrior('Dark warrior', 30, 4)
warrior.damage(4)
print('warrior vie ', warrior.get_health(), 'armure ', warrior.get_points_armor())

print(player1.get_pseudo(), ' attacks ', player2.get_pseudo())
player1.attack_player(player2)
print(player1.get_pseudo(), ' || ', player1.get_health(), ' points de vie')
print(player2.get_pseudo(), ' || ', player2.get_health(), ' points de vie')

print(player2.get_pseudo(), 'recupere', knife.get_name())
player2.set_weapon(knife)
print(player2.get_pseudo(), ' || ', player2.set_weapon(knife))

print(player2.get_pseudo(), ' attacks ', player1.get_pseudo())
player2.attack_player(player1)
print(player1.get_pseudo(), ' || ', player1.get_health(), ' points de vie')
print(player2.get_pseudo(), ' || ', player2.get_health(), ' points de vie')

# print(player1.get_pseudo())
# player1.damage(3)
# print('Vous possedez désormais ', player1.get_health(), ' points de vie')

# to check if the parent class is Player
if issubclass(Warrior, Player):
    print('Le guerrier est bien une specialisation de Player')