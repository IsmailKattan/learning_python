my_friends = []
maxlsize = 4

while maxlsize > 0:
    friend = input("Enter a friend name: ").strip()
    if friend.isupper():
        print("Invalid Name")
    elif friend.islower():
        print(f"Friend {friend} Added => 1st Letter Become Capital")
        my_friends.append(friend.capitalize())
        maxlsize -= 1
        print(f"Names Left in List Is {maxlsize}")
    else :
        print("only lower case")
print(my_friends)
