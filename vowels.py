class StringDetails:
    def __init__(self):
        self.upperCount=0
        self.lowerCount=0
        self.constantCount=0
        self.ovwelCount=0
        self.specialCharCount=0

    def uppercase(self,string):
        for i in range(len(string)):
            if string[i]>='A' and string[i]<='Z' :
                self.upperCount+=1

    def Lowercase(self,string):
        for i in range(len(string)):
            if string[i]>='a' and string[i]<='z' :
                self.lowerCount+=1

    def constants(self,string):
        ovwel = ['a','e','i','o','u']
        for i in range(len(string)):
            if string[i].lower() not in ovwel and string[i].upper()>='A' and string[i].upper()<='Z' :
                self.constantCount+=1                            

    def ovwels(self,string):
        ovwel = ['a','e','i','o','u']
        for i in range(len(string)):
            if string[i].lower() in ovwel :
                self.ovwelCount+=1

    def space(self,string):
        for i in range(len(string)):
            if string[i]==" ":
                self.specialCharCount+=1

    def status(self,string):
        self.ovwels(string)
        self.constants(string)
        self.space(string)
        self.uppercase(string)
        self.Lowercase(string)

        print(f"The no of upper case characters in a string is {self.upperCount}")
        print(f"The no of lower case characters in a string is {self.lowerCount}")
        print(f"The no of ovwels in a string is {self.ovwelCount}")
        print(f"The no of constants in a string is {self.constantCount}")
        print(f"The no of spaces in a string is {self.specialCharCount}")


s = input("Enter a string : ")
s1 = StringDetails()
s1.status(s)



