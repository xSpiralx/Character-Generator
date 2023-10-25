import random


def generate_character_name(race, gender, character_class):
    # Sample character name generation logic (you can customize this)
    race_names = {
        "human": ["John", "Mary", "Richard", "Eliza"],
        "elf": ["Lorien", "Arwen", "Legolas"],
        "dwarf": ["Thorin", "Gimli", "Kili"],
    }
    gender_names = {
        "male": ["John", "Richard", "Thorin"],
        "female": ["Mary", "Eliza", "Arwen"],
    }
    class_names = {
        "warrior": ["Conan", "Aragorn", "Brienne"],
        "wizard": ["Gandalf", "Merlin", "Elminster"],
    }
    
    

    generated_name = random.choice(race_names.get(race, []))
    generated_name += " " + random.choice(gender_names.get(gender, []))
    generated_name += " the " + random.choice(class_names.get(character_class, []))

    return generated_name
