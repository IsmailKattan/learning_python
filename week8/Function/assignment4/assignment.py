def say_hello(name = "Unknown", age = "Unknown", country = "Unknown") :
    if type(name) != str :
        print("unvalid name")
        return ""
    elif type(age) != int and age != "Unknown" :
        print("unvalid age")
        return ""
    elif type(country) != str :
        print("unvalid country name")
        return ""
    else :
        return f"Hello {name} Your Age Is {age} And You Live In {country}"
    

print(say_hello("Osama", 38, "Egypt"))
print(say_hello())