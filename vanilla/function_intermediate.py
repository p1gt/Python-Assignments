import random
def randInt(min=0,max=100):
    if max < min or max < 0:
        return "maximum must be greater than minimum and 0"
    num = random.random() * (max - min) + min
    return round(num)

print(randInt()) 
print(randInt(max=-1))
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))