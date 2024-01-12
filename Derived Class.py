class LU:
    def __init__(self, lu_code, lu_name):
        self.lu_code = lu_code
        self.lu_name = lu_name

    def display_lu_info(self):
        print(f"LU Code: {self.lu_code}")
        print(f"LU Name: {self.lu_name}")


class ITM:
    def __init__(self, itm_code, itm_name):
        self.itm_code = itm_code
        self.itm_name = itm_name

    def display_itm_info(self):
        print(f"ITM Code: {self.itm_code}")
        print(f"ITM Name: {self.itm_name}")


class DerivedClass(LU, ITM):
    def __init__(self, lu_code, lu_name, itm_code, itm_name, derived_info):
        # Call constructors of both base classes
        LU.__init__(self, lu_code, lu_name)
        ITM.__init__(self, itm_code, itm_name)

        # Additional information specific to the derived class
        self.derived_info = derived_info

    def display_derived_info(self):
        print("Derived Information:", self.derived_info)


# Example usage:
lu_code = "LU001"
lu_name = "LU Department"
itm_code = "ITM001"
itm_name = "ITM Department"
derived_info = "Additional information for the derived class."

derived_object = DerivedClass(lu_code, lu_name, itm_code, itm_name, derived_info)

# Display information using methods from base classes and the derived class
derived_object.display_lu_info()
print()
derived_object.display_itm_info()
print()
derived_object.display_derived_info()
