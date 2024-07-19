#Dictionary collection of items
# It is a mutable data structure
#SYNTAX:
    #dict={'key1':value1,'key2':value2........'keyn':value3}



'''menu={
    'roti':30,
    'butter roti':70,
    'paneer':250,
    'cold drink':50
    }
print(menu)'''#normal dictionary
    




'''menu={
    'roti':30,
    'butter roti':70,
    'paneer':250,
    'cold drink':50
    }
menu.pop('cold drink')
print(menu)'''#pop


'''menu={
    'roti':30,
    'butter roti':70,
    'paneer':250,
    'cold drink':50
    }
menu['butter roti']=60
print(menu)'''# To update


'''menu={
    'roti':30,
    'butter roti':70,
    'paneer':250,
    'cold drink':50
    }
menu['fruit_salad']=30
print(menu)'''# Add


'''menu={
    'roti':30,
    'butter roti':70,
    'paneer':250,
    'cold drink':50
    }
print(menu.keys())
print(menu)'''#To print keys(rates)



menu={
    'roti':30,
    'butter roti':70,
    'paneer':250,
    'cold drink':50
    }
print(menu.values())
for k,v in menu.items():
    print(k,'->',v)#To print values

