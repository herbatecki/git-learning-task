shopping_dict_list1 = ["chleb", "pączek", "bułki"]
shopping_dict_list1 = [word.capitalize() for word in shopping_dict_list1]
shopping_dict_list2 = ["marchew", "seler", "rukola"]
shopping_dict_list2 = [word.capitalize() for word in shopping_dict_list1]
shopping_dict = {
"piekarnia" : shopping_dict_list1,
"warzywniak" : shopping_dict_list2
}
# shopping_dict_iterator = iter(shopping_dict)
# print(shopping_dict_iterator)
for shop, product in shopping_dict.items():
        print(f'idę do {shop.capitalize()}, kupuję tam następujące rzeczy: {product}')
print ("W sumie kupię",len(shopping_dict_list1+shopping_dict_list2),"produktów")
for numbers in range (0,101):
        if numbers%5==0:
                pass
                if numbers!=0:
                        print(numbers)
list_numbers = [numbers **3 for numbers in range(0,101) if numbers%5==0]
list_numbers.remove(0)
print(list_numbers)