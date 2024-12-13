from pprint import pprint

with open('recipes.txt', encoding='utf-8') as f:
    data = f.read().split('\n')
    data.append('')

cook_book = {}
recipe = []
ingredients=[]

for line in data:
    if line:
        recipe.append(line)
    else:
        for ingredient in recipe[2:]:
            ingredients_data = ingredient.split('|')
            ingredients.append(
                {'ingredient_name': ingredients_data[0],
                 'quantity': int(ingredients_data[1]),
                 'measure': ingredients_data[2]}
            )
            cook_book[recipe[0]] = ingredients
        ingredients =[]
        recipe =[]

pprint(cook_book)

def get_shop_list_by_dishes(dishes:list, person_count=1):
    result = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name in result:
                    quantity = ingredient['quantity'] + result[ingredient_name]['quantity'] // person_count
                else:
                    quantity = ingredient['quantity']
                result[ingredient_name] = ({'quantity': quantity * person_count,
                                            'measure': ingredient['measure']}
                )
        else:
            raise ValueError(f"{dish} нет в поваренной книге")
            break
    return result

pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
