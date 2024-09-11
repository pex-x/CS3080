test = {'1111' : {'First Name': 'James', 'Last Name': 'Robert', 'Email': 'james.robert@gmail.com', 'Favorite Color': 'Red'},
        '1112' : {'First Name': 'John', 'Last Name': 'Michael', 'Email': 'john.michael@gmail.com', 'Favorite Color': 'Blue'},
        '1113' : {'First Name': 'David', 'Last Name': 'William', 'Email': 'david.william@gmail.com', 'Favorite Color': 'Green'}
}

for personID in (test.keys()) :
    print()
    print(personID)
    for attribute in test[personID].keys():
     print(attribute, '=', test[personID][attribute])
