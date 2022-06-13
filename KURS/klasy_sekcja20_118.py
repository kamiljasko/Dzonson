class User:

    def __int__(self, age, name):
        print(
            "jestem inicjatorem, który wywołuje sie zawsze podczas konstrukcji obiektu")
        self.age = age
        self.name = name

    def print_age(self):
        print("wiek: ", self.age, "imie: ", self.name)


user1 = User(30, "kurwa")
user2 = User(50, "mac")

user1.print_age()
user2.print_age()
# user1 = User(20,  "CHuj")
