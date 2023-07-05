# n = ??

n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

#--------------------------------------------------------
n = 21

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# Output => Good


# (n-1)*n/2/n = 10
#  9.5 <= (n-1)/2 <= 10.4
#  19 <= n-1 <= 20.8    
#  20 <=  n  <= 21.8    
#  n = 20 , n = 21