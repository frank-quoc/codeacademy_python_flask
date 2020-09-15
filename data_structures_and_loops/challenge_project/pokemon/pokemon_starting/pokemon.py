class Pokemon:
    """Class to create Pokemon"""

    poke_types = {
        'Fire': {
            'Water': 0.5,
            'Grass': 2,
        },
        'Water': {
            'Grass': 0.5,
            'Fire': 2,
        },
        'Grass': {
            'Fire': 0.5,
            'Water': 2,
        },
    }

    def __init__(self, name, lvl, type):
        self.name = name
        self.lvl = lvl
        self.type = type
        self.max_health = lvl*5
        self.curr_health = lvl*5
        self.koed = False
        self.base_dmg = 5

    def lose_health(self, dmg):
        self.curr_health -= dmg
        
        if self.curr_health <= 0:
            self.knocked_out()
        else:
            self.print_health()
    
    def knocked_out(self):
        self.koed = True
        self.curr_health = 0
        print(f"{self.name} fainted!")
    
    def gain_health(self, heal):
        self.curr_health += heal

        if self.curr_health > self.max_health:
            self.curr_health = self.max_health
        self.print_health()
    
    def print_health(self):
        print(f"{self.name} now has {self.curr_health} health.")

    def revive(self, max_revive=True, revive=False):
        if max_revive:
            self.curr_health = self.max_health
        elif revive:
            self.curr_health = 0.5*self.max_health
        print(f"{self.name} has been revived to {self.curr_health} health.")

    def attack(self, other):
        dmg_mult = self.poke_types[self.type].get(other.type, 1)
        dmg = self.base_dmg * dmg_mult
        print(f"{self.name} attacked {other.type} for {dmg} damage.")

        other.lose_health(dmg)

class Trainer:
    """Class to represent our trainer."""

    def __init__(self, trainer_name, num_pots, pokemon_list):
        self.trainer = trainer_name
        self.num_pots = num_pots
        self.pokemon_lst = pokemon_list[:6] if len(pokemon_list) > 6 else pokemon_list
        self.active_pokemon = 0

    def use_pot(self, idx_healed_pokemon):
        if self.num_pots > 0:
            print(f"You used a potion on {self.pokemon_lst[idx_healed_pokemon].name}")
            self.pokemon_lst[idx_healed_pokemon].gain_health(20)
            self.num_pots -= 1
        else:
            print("You have no potions left.")

    def atk_trainer(self, opponent):
        trainer_pokemon = self.pokemon_lst[self.active_pokemon]
        opp_pokemon = opponent.pokemon_lst[opponent.active_pokemon]

        print(f"{self.trainer}'s {trainer_pokemon} attacked {opp_pokemon}.")
        trainer_pokemon.attack(opp_pokemon)

    def switch(self, new_active):
        chk_active = self.pokemon_lst[new_active]

        if (new_active < len(self.pokemon_lst)) and (new_active >= 0):
            if chk_active.koed:
                print(f"{chk_active.name} is KTFO! Pick another one.")
            elif new_active == self.active_pokemon:
                print("They are the same Pokemon, you NOOB! It's {chk_active.name}")
            else: 
                self.active_pokemon = new_active
                print(f"Go {self.pokemon_lst[self.active_pokemon].name}! Get 'em, SON!'")
