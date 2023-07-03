mydict = {
    "HTML" : 90,
    "CSS" : 80,
    "Python" : 60,
    "AI" : 20
}
print(f"HTML Progress Is {mydict['HTML']}%")
print(f"CSS Progress Is {mydict['CSS']}%")
print(f"Python Progress Is {mydict['Python']}%")
print(f"AI Progress Is {mydict['AI']}%")
mydict.setdefault("C++",90)
print(f"C++ Progress Is {mydict['C++']}%")
# Needed Output

"HTML Progress Is 90%"
"CSS Progress Is 80%"
"Python Progress Is 30%"
"AI Progress Is 20%"