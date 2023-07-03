friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
ignored_count = 0
index = 0

while index < len(friends):
    friend = friends[index]
    if friend[0].isupper():
        print(friend)
    else:
        ignored_count += 1

    index += 1

print(f"Friends Printed And Ignored Names Count Is {ignored_count}")

# Needed Output
#"Mohamed"
#"Shady"
#"Sherif"
#"Friends Printed And Ignored Names Count Is 2"