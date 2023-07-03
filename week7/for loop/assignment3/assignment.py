# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
total = 0
for sub in my_ranks:
    if my_ranks[sub] == 'A':
        print(f"My Rank in {sub} Is {my_ranks[sub]} And This Equal 100 Points")
        total += 100
    if my_ranks[sub] == 'B':
        print(f"My Rank in {sub} Is {my_ranks[sub]} And This Equal 80 Points")
        total += 80
    if my_ranks[sub] == 'C':
        print(f"My Rank in {sub} Is {my_ranks[sub]} And This Equal 40 Points")
        total += 40
print(f"Total Points Is {total}")
# Needed Output
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320"