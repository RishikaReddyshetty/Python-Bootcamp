data=[1,8,'apple','carrot','mango']
fruits=['banana','mango','orange','watermelon']
vegies=['tomato','beans','carrot','apple']
for i in data:
    if i in vegies and i not in fruits:
        print(i)
