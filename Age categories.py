name=input("Please write your name")
print("Welcome ", name)
age = int(input('Please enter your age.'))
if age <= 1:
    print ('You are an infant.', name)
elif age > 1 and age < 10:
    print ('You are a child.', name)
elif age > 10 and age <= 19:
    print ('You are a adolescent.', name)
elif age >19:
    print ("You are an adult", name)