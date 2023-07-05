values = (0, 1, 2)

if any(values):

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
#         1                  0                   0      = 1
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")

else:

  print("Bad")


# the output is Good