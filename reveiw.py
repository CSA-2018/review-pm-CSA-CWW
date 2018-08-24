
class person:
    def __init__(self,name,age,city,phone):
        self.name = name
        self.age = age
        self.city = city
        self.phone = phone
        
    def register(self):
        print('Name, "%s" registerd!' %self.name)
        print('Age, "%s" registerd!' %self.age)
        print('City, "%s" registerd!' %self.city)
        print('Phone, "%i" registerd!' %self.phone)
    
def ask():
    name = input('What is your name?').title() ; print('')
    age = input('What is your age') ; print('')
    city = input('What is your city').title() ; print('')
    while True:
        try:
            phone = int(input('What is your phone')) ; print('')
            break
        except ValueError:        #try and accept checking for a number#
            print ('\nDont use letters.\n')
    you = person(name,age,city,phone)
    you.register()
ask()

#cameron#
#comp prog#
#2018/22/8#


