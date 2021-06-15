#Challenge One
def sum_to(num):
    sum = 0
    for n in range(1, num+1):
        sum += n
    return sum

print(sum_to(5)) #15

#Challenge Two
def largest(nums):
    nums.sort()
    return nums[-1]

print(largest([1,2,3])) #3

#Challenge Three
def occurances(string, substr):
    return string.count(substr)


print(occurances('Fleep Floop', 'o')) #2

#Challenge Four
def product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

print(product(1, 2, 3)) #6