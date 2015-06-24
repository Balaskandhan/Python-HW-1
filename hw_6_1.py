class Animal:
    
    def __init__(self,name):
        self.name = name
        
    def guess_who_am_i(self):
        print("I'll give you three hints, try to find who am i?")
        if self.name == 'elephant':
           ans = "not elephant"
           while ans:
               print("\n I have exceptional memory")
               answer = input("Who am i?: ")
               if answer == 'elephant':
                   print("You got it")
                   ans = answer
                   break
               else:
                   print("Nope, try again!")
                   print("\n I am the largest land-living mammal in the world")
                   answer = input("Who am i?: ")
                   if answer == 'elephant':
                       print("You got it")
                       ans = answer
                       break
                   else:
                       print("Nope, try again!")
                       print("\n I have Tusk")
                       answer = input("Who am i?: ")
                       if answer == 'elephant':
                           print("You got it")
                           ans = answer
                           break
                       else:
                            print("Nope, try again!")
                            print("I'm out of hits, I am :",self.name)
                        
                        
        if self.name == 'tiger':
           ans = "tiger"
           while ans:
               print("\n I am the biggest cat")
               answer = input("Who am i?: ")
               if answer == 'tiger':
                   print("You got it")
                   ans = answer
                   break
               else:
                   print("Nope, try again!")
                   print("\n I come in black and white or orange and black")
                   answer = input("Who am i?: ")
                   if answer == 'tiger':
                       print("You got it")
                       ans = answer
                       break
                   else:
                       print("Nope, try again!")
                       print("\n A group of us are known as an ambush or streak.")
                       answer = input("Who am i?: ")
                       if answer == 'tiger':
                           print("You got it")
                           ans = answer
                           break
                       else:
                            print("Nope, try again!")
                            print("I'm out of hits, I am :",self.name)
                            break
                        
        if self.name == 'bat':
           ans = "not dog"
           while ans:
               print("\n I use echo-location")
               answer = input("Who am i?: ")
               if answer == 'bat':
                   print("You got it")
                   ans = answer
                   break
               else:
                   print("Nope, try again!")
                   print("\n I can fly")
                   answer = input("Who am i?: ")
                   if answer == 'bat':
                       print("You got it")
                       ans = answer
                       break
                   else:
                       print("Nope, try again!")
                       print("\n I see well in dark")
                       answer = input("Who am i?: ")
                       if answer == 'bat':
                           print("You got it")
                           ans = answer
                           break
                       else:
                            print("Nope, try again!")
                            print("I'm out of hits, I am :",self.name)
                            break
                    
e = Animal('elephant')
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
