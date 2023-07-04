def get_people_scores(name = "", **subjectsAndScores) :
    if name != "" :
        print(f"Hello {name} This Is Your Score Table:")
    for subject, progress in subjectsAndScores.items() :
        print(f"{subject} => {progress}")
    print("-" * 15 + "ALL SCORES PRINTED" + "-" * 15)

get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")