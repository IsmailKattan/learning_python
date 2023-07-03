friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
people = []
people.extend(friends)
people.extend(employees)
people.extend(school)
print(people)


# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]