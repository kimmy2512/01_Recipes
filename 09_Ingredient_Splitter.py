import re

# Ingredient has mixed fraction followed by unit and ingredient
recipe_line ="1 1/2 ml flour"  # Change to input statement in due course

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

if re.match(mixed_regex, recipe_line):
    print("true")
else:
    print("false")