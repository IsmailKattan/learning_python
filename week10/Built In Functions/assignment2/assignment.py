# v = ??
v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

# the result must be like this: 
# v*(v+1)/2 + v**v % v = 820
# v*(v+1)/2 +    0     = 820 
# v*(v+1) = 1640
# 40*41 = 1640 
