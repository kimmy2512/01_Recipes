import re

# Ingredient has mixed fraction followed by unit and ingredient

full_recipe = [
    "1 1/2 ml flour",
    "3/4 cup milk",
    "1 cup flour",
    "2 tablespoons white sugar",
    "1.5 tsp baking powder",
    "pinch of cinammon"
]

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

for recipe_line in full_recipe:
    # Get amount...
    if re.match(mixed_regex, recipe_line):
        print("true")
        # Get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # Replace space with a + sign...
        amount = mixed_num.replace(" ", "+")
        # Change the string into a decimal
        amount = eval(amount)
        print(amount)

        # Get unit and ingredient...
        compile_regex = re.compile(mixed_regex)
        print(compile_regex)
        unit_ingredient = re.split(compile_regex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip()   # Remove extra white space from unit
        print(unit_ingredient)

   # Get unit and ingredient...
    get_unit = unit_ingredient.split(" ", 1)    # Splits text at first space
    unit = get_unit[0]
    ingredient = get_unit[1]

    print("{} {} {}".format(amount, unit, ingredient))