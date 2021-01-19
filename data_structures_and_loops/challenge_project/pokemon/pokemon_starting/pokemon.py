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
        self.max_health = lvl*20
        self.curr_health = self.max_health
        self.koed = False
        self.base_dmg = lvl * 0.5
        self.curr_exp = 1
        self.exp_to_lvl = 4/5 * lvl**3
    
    def __repr__(self):
        return f"{self.name} is level {self.lvl} {self.type} type." 

    def lose_health(self, dmg):
        self.curr_health -= dmg
        
        if self.curr_health <= 0:
            self.knocked_out()
        else:
            self.print_health()
    
    def knocked_out(self):
        self.koed = True
        self.curr_health = 0
        print(f"{self.name} fainted!\n")
    
    def gain_health(self, heal):
        self.curr_health += heal

        if self.curr_health > self.max_health:
            self.curr_health = self.max_health
        self.print_health()
    
    def print_health(self):
        print(f"{self.name} now has {self.curr_health} health.\n")

    def revive(self, max_revive=True, revive=False):
        if max_revive:
            print("Used Max Revive")
            self.curr_health = self.max_health
        elif revive:
            print("Used Revive")
            self.curr_health = round(0.5*self.max_health)

    def attack(self, other):
        dmg_mult = self.poke_types[self.type].get(other.type, 1)
        dmg = round(self.base_dmg * dmg_mult)
        print(f"{dmg} damage was dealt.")
        if dmg_mult == 2:
            print("It's super effective!")
        elif dmg_mult == 0.5:
            print("It's not very effective.")

        other.lose_health(dmg)

    def gain_exp(self, other):
        exp_to_gain = other.curr_exp * other.lvl * 1.5 / 7
        self.curr_exp += exp_to_gain

        while (self.curr_exp >= self.exp_to_lvl) and self.lvl < 100:
            self.lvl += 1
            self.curr_exp = exp_to_gain - self.exp_to_lvl
            print(f"{self.name} leveled up to {self.lvl}!")
            if self.lvl == 100:
                print(f"{self.name} has reached maxed level.\n")
            

class Charmander(Pokemon):
    stats = {
        'base_hp': 44,
        'base_atk': 52,
        'base_def': 43,
        'base_sp_atk': 60,
        'base_sp_def': 50,
        'base_speed': 65,
    }
    def __init__(self, lvl = 5):
        super().__init__("Charmander", lvl, "Fire")
        self.max_health += self.stats['base_hp']
        self.curr_health = self.max_health
        self.base_dmg += self.stats['base_atk']

    def gain_exp(self, other):
        exp_to_gain = other.curr_exp * other.lvl * 1.5 / 7
        self.curr_exp += exp_to_gain

        while (self.curr_exp >= self.exp_to_lvl) and self.lvl < 16:
            self.lvl += 1
            self.curr_exp = exp_to_gain - self.exp_to_lvl
            print(f"{self.name} leveled up to {self.lvl}!")
            if self.lvl == 16:
                print(f"\n{self.name} evolved to...")
                self.__class__ = Wartortle
                self.__init__()
                print(f"{self.name}! Congrats!!!\n")

class Charmeleon(Charmander):
    stats = {
        'base_hp': 58,
        'base_atk': 64,
        'base_def': 58,
        'base_sp_atk': 80,
        'base_sp_def': 65,
        'base_speed': 80,
    }
    def __init__(self, lvl = 16):
        super().__init__(lvl)
        self.name = 'Charmeleon'
        self.max_health += self.stats['base_hp']
        self.curr_health = self.max_health
        self.base_dmg += self.stats['base_atk']

class Squirtle(Pokemon):
    stats = {
        'base_hp': 44,
        'base_atk': 48,
        'base_def': 65,
        'base_sp_atk': 50,
        'base_sp_def': 64,
        'base_speed': 43,
    }
    def __init__(self, lvl = 5):
        super().__init__("Squirtle", lvl, "Water")
        self.max_health += self.stats['base_hp']
        self.curr_health = self.max_health
        self.base_dmg += self.stats['base_atk']

    def gain_exp(self, other):
        exp_to_gain = other.curr_exp * other.lvl * 1.5 / 7
        self.curr_exp += exp_to_gain

        while (self.curr_exp >= self.exp_to_lvl) and self.lvl < 16:
            self.lvl += 1
            self.curr_exp = exp_to_gain - self.exp_to_lvl
            print(f"{self.name} leveled up to {self.lvl}!")
            if self.lvl == 16:
                print(f"{self.name} evolved to...")
                self.__class__ = Wartortle
                self.__init__()
                print(f"...{self.name}! Congrats!!!\n")

class Wartortle(Squirtle):
    stats = {
        'base_hp': 59,
        'base_atk': 63,
        'base_def': 80,
        'base_sp_atk': 65,
        'base_sp_def': 80,
        'base_speed': 58,
    }

    def __init__(self, lvl=16):
        super().__init__(lvl)
        self.name = 'Wartortle'
        self.max_health += self.stats['base_hp']
        self.curr_health = self.max_health
        self.base_dmg += self.stats['base_atk']

class Bulbasaur(Pokemon):
    stats = {
        'base_hp': 45,
        'base_atk': 49,
        'base_def': 49,
        'base_sp_atk': 65,
        'base_sp_def': 65,
        'base_speed': 45,
    }
    def __init__(self, lvl = 5):
        super().__init__("Bulbasaur", lvl, "Grass")
        self.max_health += self.stats['base_hp']
        self.curr_health = self.max_health
        self.base_dmg += self.stats['base_atk']

    def gain_exp(self, other):
        exp_to_gain = other.curr_exp * other.lvl * 1.5 / 7
        self.curr_exp += exp_to_gain

        while (self.curr_exp >= self.exp_to_lvl) and self.lvl < 16:
            self.lvl += 1
            self.curr_exp = exp_to_gain - self.exp_to_lvl
            print(f"{self.name} leveled up to {self.lvl}!")
            if self.lvl == 16:
                print(f"\n{self.name} evolved to...")
                self.__class__ = Wartortle
                self.__init__()
                print(f"{self.name}! Congrats!!!\n")

class Ivysaur(Bulbasaur):
    stats = {
        'base_hp': 60,
        'base_atk': 62,
        'base_def': 63,
        'base_sp_atk': 80,
        'base_sp_def': 80,
        'base_speed': 60,
    }

    def __init__(self, lvl=16):
        super().__init__(lvl)
        self.name = 'Ivysaur'
        self.max_health += self.stats['base_hp']
        self.curr_health = self.max_health
        self.base_dmg += self.stats['base_atk']

class Trainer:
    """Class to represent our trainer."""

    def __init__(self, trainer_name, num_pots, pokemon_list):
        self.trainer = trainer_name
        self.num_pots = num_pots
        self.pokemon_lst = pokemon_list[:6] if len(pokemon_list) > 6 else pokemon_list
        self.active_pokemon = 0

    def __repr__(self):
        print(f"Introducing... {self.trainer}'s team: ")
        for i in self.pokemon_lst:
            print(i)
        return f"{self.pokemon_lst[self.active_pokemon].name} is currently in battle.\n"

    def use_pot(self, idx_healed_pokemon):
        pokemon_to_heal = self.pokemon_lst[idx_healed_pokemon]
        if pokemon_to_heal.curr_health == pokemon_to_heal.max_health:
            print(f"{pokemon_to_heal.name} already has max health. Please pick another pokemon to heal.\n")
            return
        if self.num_pots > 0:
            print(f"You used a potion on {pokemon_to_heal.name}")
            pokemon_to_heal.gain_health(20)
            self.num_pots -= 1
        else:
            print("You have no potions left.")

    def use_revive(self, idx_revived_pokemon, max_revive=True, revive=False):
        pokemon_to_revive = self.pokemon_lst[idx_revived_pokemon]
        if not pokemon_to_revive.koed:
            print(f"Can't use revive on a pokemon that hasn't fainted.")
        else:
            pokemon_to_revive.revive(max_revive, revive)
            print(f"{self.trainer}'s {pokemon_to_revive.name} has been revived to {pokemon_to_revive.curr_health} health.")

    def atk_trainer(self, opponent):
        trainer_pokemon = self.pokemon_lst[self.active_pokemon]
        opp_pokemon = opponent.pokemon_lst[opponent.active_pokemon]

        if trainer_pokemon.koed == True:
            print(f"{trainer_pokemon.name} has no hp left and can't attack. Pokemon is passed out; time to swap.\n")
        else:
            print(f"{self.trainer}'s {trainer_pokemon.name} attacked {opponent.trainer}'s {opp_pokemon.name}.")
            trainer_pokemon.attack(opp_pokemon)
            if opp_pokemon.koed:
                trainer_pokemon.gain_exp(opp_pokemon)

    def switch(self, new_active):
        chk_active = self.pokemon_lst[new_active]

        if (new_active < len(self.pokemon_lst)) and (new_active >= 0):
            if chk_active.koed:
                print(f"{chk_active.name} is KTFO! Pick another one.\n")
            elif new_active == self.active_pokemon:
                print(f"Can't swap. They are the same Pokemon! It's {chk_active.name}.\n")
            else: 
                print(f"{self.pokemon_lst[self.active_pokemon].name}, return.")
                self.active_pokemon = new_active
                print(f"Go {self.pokemon_lst[self.active_pokemon].name}! Get 'em!\n")

# Six pokemon are made with different levels. (If no level is given, it is level 5)
a = Charmander(7)
b = Squirtle(5)
c = Squirtle(1)
d = Bulbasaur(10)
e = Charmander(5)
f = Squirtle(2)


#Two trainers are created. The first three pokemon are given to trainer 1, the second three are given to trainer 2.
trainer_1 = Trainer("Ash", 3, [a,b,c])
trainer_2 = Trainer("Gary", 5, [d,e,f])

print(trainer_1)
print(trainer_2)



# Testing attacking, giving potions, and switching pokemon.
trainer_1.atk_trainer(trainer_2)
trainer_2.atk_trainer(trainer_1)
trainer_2.use_pot(2)
trainer_1.switch(2)
trainer_1.atk_trainer(trainer_2)
trainer_2.use_revive(0, max_revive=False, revive=True)

# Testing to see Pokemon Evolution Changing Classes
trainer_1.atk_trainer(trainer_2)
trainer_1.atk_trainer(trainer_2)
trainer_1.atk_trainer(trainer_2)
trainer_1.atk_trainer(trainer_2)
print(type(trainer_1.pokemon_lst[trainer_1.active_pokemon]),"\n")
trainer_1.atk_trainer(trainer_2)
print(type(trainer_1.pokemon_lst[trainer_1.active_pokemon]),"\n")

# Testing to see methods on fainted pokemon
trainer_2.switch(0)
trainer_2.use_revive(0, max_revive=True, revive=False)



