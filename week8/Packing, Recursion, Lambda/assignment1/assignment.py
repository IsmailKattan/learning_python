def get_score(**subjects) : 
    for subject, score in subjects.items() :
        print(f"{subject} => {score}")

get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)