class Grandfather:
    def __init__(self, grandfather_property):
        self.grandfather_property = grandfather_property

    def display_grandfather_property(self):
        print(f"Grandfather's Property: {self.grandfather_property}")


class Father(Grandfather):
    def __init__(self, grandfather_property, father_property):
        # Call the constructor of the base class (Grandfather)
        super().__init__(grandfather_property)

        self.father_property = father_property

    def display_father_property(self):
        print(f"Father's Property: {self.father_property}")


class Child(Father):
    def __init__(self, grandfather_property, father_property, child_property):
        # Call the constructor of the intermediate class (Father)
        super().__init__(grandfather_property, father_property)

        self.child_property = child_property

    def display_child_property(self):
        print(f"Child's Property: {self.child_property}")


# Example usage:
grandfather_property = "Land and Assets"
father_property = "Business and Investments"
child_property = "Education and Hobbies"

child_object = Child(grandfather_property, father_property, child_property)

# Display properties inherited at different levels
child_object.display_grandfather_property()
print()
child_object.display_father_property()
print()
child_object.display_child_property()
