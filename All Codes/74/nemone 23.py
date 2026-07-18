#1
is_subset=lambda x,y:True if x&y else False

dairy={'milk','yugert','cheese','ice cream','cream'}

foodstuff={"rice",'bread','apple','milk','katchup','orange','cheese','eggs','meat','chips','ice crea,'}

if is_subset==True:
    print("dairy products are subset of food items.")
else:
    print("dairy product aren't subset of food items.")

#2
is_subset=lambda items:items.issubset(foodstuff)

dairy={'milk','cheese','ice cream'}

foodstuff={"rice",'bread','apple','milk','katchup','orange','cheese','eggs','meat','chips','ice cream'}

if is_subset(dairy):
    print("dairy products are subset of food items.")
else:
    print("dairy product aren't subset of food items.")

