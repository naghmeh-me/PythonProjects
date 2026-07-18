car={'brand':'Ford','model':'Mustang','year':1964}

x=car.setdefault('model','Bronco')

print(x,'\n')

y=car.setdefault('color','white')

print(y,'\n')

car.update({'color':'white'})

print(car,'\n')

dict1={1:'one','two':'two',3:3}

dict2={5:'five',3:'three','two':2}

dict1.update(dict2)


print(dict1,'\n')

print(dict2)
