import random

#create enemy list and import "current enemy into this one module"
#create current enemy 
#create current enemy with health


#weaponseffect

def pixie_dust(current_enemy):
    chance = random.random()
    success_threshold = 0.3
    
    if chance <= success_threshold:
        pixie_dust_effect = ["Exploded", "Imploded", "Turned to Stone", "Face Melted"]
        selected_effect = random.choice(pixie_dust_effect)
        enemy_health = 0
        print(f"The {current_enemy} {selected_effect}! The {current_enemy} is defeated.")
    else:
        print("A faint fizzle can be heard, nothing happened.")
        
def magical_brass_knuckles(current_enemy):
    magical_brass_knuckles_damage = (random.randrange(-10,30))
        if magical_brass_knuckles_damage == (1,30): 
            enemy_health 
            




def cast_spell(self, spell_name):
        if spell_name in self.attacks:
            if spell_name == "Fireball":
                min_damage, max_damage = self.attacks[spell_name]
                damage = random.randint(min_damage, max_damage)
                if damage == max_damage:
                    print(f"{self.name} casts {spell_name} for {damage} damage! CRITICAL HIT!")
    