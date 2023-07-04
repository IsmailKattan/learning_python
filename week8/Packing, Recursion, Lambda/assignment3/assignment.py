def get_the_scores(name = "", **subjectsAndScores) :
    if name != "" and len(subjectsAndScores) != 0:
        print(f"Hello {name}, This Is Your Score Table:")
    if len(subjectsAndScores) == 0 :
        print(f"Hello {name}, You Have No Scores To Show")
    else :
        for subject, progress in subjectsAndScores.items() :
            print(f"{subject} => {progress}")
        print("-" * 15 + "ALL SCORES PRINTED" + "-" * 15)

scores_list = {
    "Math" : "90",
    "Science" : "80",
    "Language" : "70"

}
get_the_scores("Osama", **scores_list)
print("_" * 48)
get_the_scores("Osama")
print("_" * 48)
get_the_scores(**scores_list)