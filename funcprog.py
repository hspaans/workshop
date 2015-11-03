numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odds = list(filter(lambda i: i % 2 == 1, numbers))
squares = list(map(lambda i: i * i, numbers))

from functools import reduce
sum_num = reduce(lambda x, y: x + y, numbers) 
fact5 = reduce(lambda x, y: x * y, range(1,6))

squares2 = [ i * i for i in numbers ]
odds2 = [ i for i in numbers if i % 2 == 1 ]

pyth_triple = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]


