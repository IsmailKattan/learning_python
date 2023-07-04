def show_skills (name , *skills) :
    if len(skills) == 0 :
        print(f"Hello {name} You Have No Skills To Show")
    else :
        print(f"Hello {name} Your Skills Is")
        for skill in skills :
            print(f"- {skill}")

            
show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")