import random, os, time

NAMES = [
  "Jogador",
  "Dealer"
]

CARTAS = [
  "AS",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "10",
  "VALETE",
  "DAMA",
  "REI"
]


class Jogador:
  def __init__(self, name=None) -> None:
    random_name = f"{random.choice(NAMES)} {random.choice(NAMES)}"

    self.name = random_name if name == None else name
    self.cartas = CARTAS.append(random.randint(2,11))
    self.soma = sum(self.cartas)
    self.resultado = (21 - self.soma)

  def print(self):
    print("----------")
    print(f"nome: {self.name}")
    print(f"Cartas: {self.cartas}")
    print(f"Soma: {self.soma}")
    print(f"Resultado: {self.resultado}")
    print("----------")

  @staticmethod
  def dealer_pega_uma_carta(player_to_pick: "Player"):
    carta_name = random.choice(CARTAS)
    carta_message = f"{player_to_pick.name} pega a carta {carta_name}!"
    pick_effectiveness = random.choice(pick_CHANCES)
    pick_damage = (player_to_pick.pick / dealer_to_pick.defense) * pick_CHANCES.index(pick_effectiveness) * (1 + random.random() / 2)
    
    dodged = random.random() >  (player_to_pick.speed / dealer_to_pick.speed)
    if dodged: pick_damage = 0

    print(pick_message)
    print(pick_effectiveness)
    if dodged: print(f"{dealer_to_pick.name} desviou!")
    print(f"{dealer_to_pick.name} tomou {pick_damage:.2f} de dano!")
    dealer_to_pick.health_points -= pick_damage

    if (dealer_to_pick.health_points < 0):
      print(f"{dealer_to_pick.name} foi pro saco!")
    
  @staticmethod
  def player_pega_uma_carta(player_to_pick: "Player"):
    carta_name = random.choice(CARTAS)
    carta_message = f"{player_to_pick.name} pega a carta {carta_name}!"
    pick_effectiveness = random.choice(pick_CHANCES)
    pick_damage = (player_to_pick.pick / dealer_to_pick.defense) * pick_CHANCES.index(pick_effectiveness) * (1 + random.random() / 2)
    
    dodged = random.random() >  (player_to_pick.speed / dealer_to_pick.speed)
    if dodged: pick_damage = 0

    print(pick_message)
    print(pick_effectiveness)
    if dodged: print(f"{dealer_to_pick.name} desviou!")
    print(f"{dealer_to_pick.name} tomou {pick_damage:.2f} de dano!")
    dealer_to_pick.health_points -= pick_damage

    if (dealer_to_pick.health_points < 0):
      print(f"{dealer_to_pick.name} foi pro saco!")

  @staticmethod
  def battle(player_1: "Player"):
    
    turn_number = 0
    while player_1.health_points > 0 and player_2.health_points > 0:
      turn_number += 1
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f"Turno: {turn_number}")
      player_1.print()
      player_2.print()
      print("\n\n")
      Player.pick_player(player_1, player_2)
      print("\n\n")
      Player.pick_player(player_2, player_1)
      time.sleep(2)