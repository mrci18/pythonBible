numbers[1,2,3,4,5]
print(*numbers)

def add(*numbers)
    total = 0
    for number in numbers
        total = total + number 
    return(total)

add(1,2,3)

#numbers = (1,2,3)
dictionary = {"name": "Charles", "age": 23 "likes": "wrestling"}

def about(name,age,likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name,age,likes)
    return sentence

about(**dictionary)

def foo(**kwags):
    for key, value in kwards.items():
        print("{}:{}".format(key,value))

foo(alice = "female", bob = "male", jerry = "male")