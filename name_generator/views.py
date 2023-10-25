from django.shortcuts import render
from .forms import CharacterForm
from .models import Character
from .name_generator import generate_character_name

def generate_name(request):
    generated_name = ""  # Define a default value for generated_name

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            generated_name = generate_character_name(character.race, character.gender, character.character_class)
            character.generated_name = generated_name  # Update generated_name here
            character.save()
    else:
        form = CharacterForm()

    print(f"Generated Name: {generated_name}")

    return render(request, 'name_generator/generate_name.html', {'form': form,})
