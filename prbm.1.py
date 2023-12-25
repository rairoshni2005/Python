from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()

    def calculate_age(self):
        current_date = datetime.now().date()
        age = current_date.year - self.date_of_birth.year - ((current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def display_info(self):
        print("Person Information:")
        print(f"Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')}")
        print(f"Age: {self.calculate_age()} years")

# Example usage:
person1 = Person(name="John Doe", country="USA", date_of_birth="1990-05-15")
person1.display_info()
