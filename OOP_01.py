

class Computer:

    def __init__(self, cpu, ram):

        self.cpu = cpu
        self.ram = ram

        print("This is a auto printed")


    def config(self):
        print("This is a computer machine")
        print("Config is: " + self.cpu, self.ram)




com1 = Computer('i15', 8)
#print(type(com1)) # this is an object of the computer class.
com2 = Computer('ryzen 3', 16)


#These both give the same output and function in the same way
com1.config()
#Computer.config(com1)
com2.config()
#Computer.config(com2) # we will not be using this format


# Prints the address in the heap memory
print(id(com1))
print(id(com2))


