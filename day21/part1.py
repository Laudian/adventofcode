with open("input.txt") as file:
    data = [line.strip("\n").strip(")") for line in file]

# Maps allergens to all the ingredients they may be contained in
ingredient_count = {}
allergen_to_ingredient = {}
all_ingredients = []
for line in data:
    ingredients, allergens = line.split(" (contains ")
    ingredients = ingredients.split()
    allergens = allergens.split(", ")

    for allergen in allergens:
        if allergen not in allergen_to_ingredient:
            allergen_to_ingredient[allergen] = set(ingredients)
        else:
            allergen_to_ingredient[allergen] = allergen_to_ingredient[allergen].intersection(set(ingredients))

    all_ingredients += ingredients
    all_ingredients = list(set(all_ingredients))

    for ingredient in ingredients:
        ingredient_count[ingredient] = ingredient_count.get(ingredient, 0) + 1

unused_ingredients = set(all_ingredients)
for allergen, ingredients in allergen_to_ingredient.items():
    for ingredient in ingredients:
        unused_ingredients.discard(ingredient)

unused_count = sum([ingredient_count[ingredient] for ingredient in unused_ingredients])
print("Part 1: " + str(unused_count))

# Part 2
result = []
# As longs as we have not found the specific ingredient for one allergen:
while allergen_to_ingredient:
    # Check all allergens to find one that has only one possible ingredient listed
    for allergen, ingredients in allergen_to_ingredient.items():
        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            result.append((ingredient, allergen))
            # remove this allergen from the dict
            del allergen_to_ingredient[allergen]
            # Remove the ingredient we found from all other allergens
            for value in allergen_to_ingredient.values():
                value.discard(ingredient)
            break

# Sort result alphabetically by their allergen
result.sort(key=lambda x: x[1])
resultstring = "".join([ing + "," for ing, all in result]).strip(",")
print(resultstring)