import random


def generate_character_name(race, gender, character_class):
    # Name Logic
    race_names = {
        "human": ["Robb", "Mary", "Richard", "Eliza"],
        "elf": ["Lorien", "Arwen", "Legolas"],
        "dwarf": ["Thorin", "Gimli", "Kili"],
    }
    gender_names = {
        "male": ["Red", "Black", "Green"],
        "female": ["Blue", "White", "Yellow"],
    }
    class_names = {
        "warrior": ["Conan", "Aragorn", "Brienne"],
        "wizard": ["Gandalf", "Merlin", "Elminster"],
    }
    
    

    generated_name = random.choice(race_names.get(race, []))
    generated_name += " " + random.choice(gender_names.get(gender, []))
    generated_name += " the " + random.choice(class_names.get(character_class, []))

    return generated_name
