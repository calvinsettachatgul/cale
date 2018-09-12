# lena calvin 082418
my_arr = [1,2,3,4]

person1 = {
    'first': 'calvin',
    'last': 'callast',
    'email': 'calemail',
}
person2 = {
    'first': 'lena',
    'last': 'lenalast',
    'email': 'callemail',
}
person3 = {
    'first': 'per3',
    'last': 'per3last',
    'email': 'per3email',
}

# def isLena(person):
#     return person['first'] === 'lena'

people = [ person1, person2, person3]

def isLena(person):
    return person['first']=='lena'
    
def changePerson(person):
    person['first'] += 'abc'
    person['last'] += 'abc'
    person['email'] += 'abc'
    return person

transformedPerson = map(changePerson, people)

print(transformedPerson)
    
    
    
# map1 = map(isLena,people)
# print(map1)



# for num in my_arr:
#     print(num)
    
# final_list = []
# i=0
# while i<len(people):
#     final_list.append(people[i]['email'])
#     i+=1

# k = 0
# while k < len(people):
#     print("{} {} {}".format(people[k]['first'], people[k]['last'], people[k]['email']))
#     k += 1


    
# print(final_list)

