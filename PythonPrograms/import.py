import useful_functions as uf
import math

scores=[88,92,79,93,85]
mean = uf.mean(scores)
curved = uf.add_five(scores)
mean_c=uf.mean(curved)
print("Scores: ", scores)
print("Original Mean: ",mean, " New mean: ", mean_c)

print(__name__)
print(uf.__name__)
print(math.factorial(4))
