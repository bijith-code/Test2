username=input("Please enter your name")

userage=input("Please enter your age")

def age100(userage):

   turn=100-userage+2017

   return turn

turn = age100(userage)

message= 'Hello %s, your age is %d and you will turn 100 in the year %d' %(username,userage, turn)

print(message)
