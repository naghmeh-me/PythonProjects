#1
current_fruits={'apple','banana','kiwi','watermelon','pitch','mango','bluberry','strawberry','orange'}

new_fruits={'kiwi','watermelon','pitch','strawberry','bluberry','mango'}

print("common fruits :" , current_fruits & new_fruits)


#2
fruits_in_stock={'apple','banana','kiwi','orange'}

new_arrivls={'banana','watermelon','kiwi','mango','bluberry'}

common_fruits=fruits_in_stock.intersection(new_arrivls)
common=new_arrivls & fruits_in_stock

print("common fruits between stock ana new arrivals:")
print(common_fruits)
print(common)
