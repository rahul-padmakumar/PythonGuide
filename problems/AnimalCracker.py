
def animal_crackers(animal_name):
    individual_words = animal_name.split(" ")
    print(individual_words)
    if len(individual_words) == 2:
        return individual_words[0][0].lower() == individual_words[1][0].lower()
    else:
        return False


print(animal_crackers("Levelheaded llama"))

print(animal_crackers('Crazy Kangaroo'))