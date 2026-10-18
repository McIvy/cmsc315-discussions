"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented
programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections.
Your task is to complete, modify, and nalyze the code to
demonstrate understanding of inheritance, namespaces, and object
copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information
# about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    list_type = "Household Groceries"

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def get_summary(self):
        return (
            f"List Owner: {self.name}\n"
            f"Budget: ${self.budget:.2f}\n"
            f"Category: {self.list_type}"
        )


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    specialty_store = "Whole Foods"

    def __init__(self, name, budget, department, nested_items):
        super().__init__(name, budget)
        self.department = department
        self.nested_items = nested_items

    def add_to_bakery_section(self, item):
        if len(self.nested_items) < 2:
            return (
                "Could not add item because this list has no "
                "Bakery section."
            )
        self.nested_items[1].append(item)
        return f"Added '{item}' to the Bakery section list."

    # TODO 6: create custom extension
    def check_projected_budget(self, average_item_cost=5.00):
        """Counts all items and alerts Mom if the total estimate
        exceeds the budget."""
        total_items = 0

        # Loop through each nested sub-list (Pantry,
        # Bakery, Produce)
        for category_list in self.nested_items:
            total_items += len(category_list)

        # Calculate a projected total cost estimate
        projected_cost = total_items * average_item_cost

        # Check if the projection exceeds the instance budget set
        # in the constructor
        if projected_cost > self.budget:
            return (
                f"BUDGET ALERT: Your list has {total_items} items. "
                f"Projected cost is ${projected_cost:.2f}, "
                f"which exceeds your ${self.budget:.2f} budget!"
            )

        remaining = self.budget - projected_cost
        return (
            f"Budget Safe: {total_items} items on list. \n"
            f"Projected cost is ${projected_cost:.2f} "
            f"(${remaining:.2f} under budget)."
        )

    def get_summary(self):
        parent_text = super().get_summary()
        return (
            "[MOM APP] SPECIALTY TRIP ALERT: \n"
            f"Specialty Store: {self.specialty_store}\n"
            f"{parent_text}\n"
            f"Department: {self.department}\n"
            f"Nested Items: {self.nested_items}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and
# instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    items_list1 = [["honey"], ["bread"], ["spinach"]]
    items_list2 = [["oats"], ["muffins"], ["apples"]]

    mom1_list = ChildClass("Smith", 150.00, "Bakery", items_list1)
    mom2_list = ChildClass("Jones", 50.00, "Produce", items_list2)

    # access class variable through class and instance references
    print(f"Class variable via Class: {ChildClass.specialty_store}")
    print(
        f"Class variable via Instance (mom1_list): "
        f"{mom1_list.specialty_store}"
        )

    # adding attribute directly to specific object at runtime
    mom1_list.coupon_code = "ORGANIC20"
    print(
        "\nAdded dynamic 'coupon_code' attribute specifically to "
        "mom1_list."
        )

    # displyaing individual instance namespaces to check variables
    print(f"\nmom1_list Namespace: {mom1_list.__dict__}")
    print(f"mom2_list Namespace: {mom2_list.__dict__}")

    # insepct shared class namespace attributes
    class_keys = list(ChildClass.__dict__.keys())
    print(f"\nChildClass Namespace Keys: {class_keys}")

# TODO 4:
# Create a function that demonstrates shallow copying and deep
# copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and
# deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    whole_foods_items = [
        ["organic honey", "almond butter"], #pantry
        ["sourdough loaf", "croissants"],   #bakery
        ["avocados", "organic spinach"]     #produce
    ]

    original_list = ChildClass(
        "Davis", 100.00, "Bakery", whole_foods_items
    )

    # shallow copy creates an independent outer ChildClass object
    # shell. it still shares the same memory references for
    # internal nested lists.
    shallow_list = copy(original_list)

    # deep copy clones every layer recursively. it creates an
    # independent outer shell. it also creates independent
    # internal nested lists though nothing is shared.
    deep_list = deepcopy(original_list)

    print(
        "Mom updates the original list by adding 'apple pie' "
        "to the bakery section..."
    )
    original_list.add_to_bakery_section("apple pie")

    print(
        f"\nOriginal List Complete Sections: "
        f"{original_list.nested_items}"
    )
    print(
        f"Shallow Copy Complete Sections : "
        f"{shallow_list.nested_items}"
    )
    print(
        f"Deep Copy Complete Sections    : "
        f"{deep_list.nested_items}\n"
    )

    print(
        "Identity Check: Does Shallow Copy share the nested list?"
        )
    print(
        f"{shallow_list.nested_items is original_list.nested_items}"
        )

    print("Identity Check: Does Deep Copy share the nested list?")
    print(f"{deep_list.nested_items is original_list.nested_items}")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Mom's Streamlined Grocery Organizer ===")

    print("\n=== Testing Parent Object ===")
    household_list = ParentClass("Garcia", 200.00)
    print(household_list.get_summary())

    print("\n=== Testing Child Object (Plain Inheritance) ===")
    test_items = [["honey"], ["bagels"], ["kale"]]
    mom_app_list = ChildClass(
        "Suitland", 120.00,
        "Bakery", test_items
        )
    print(mom_app_list.get_summary())
    print(mom_app_list.add_to_bakery_section("blueberry muffins"))

    print(
        "\n=== Testing Extension (Branch 1: Budget Safe Pass) "
        "===")
    print(mom_app_list.check_projected_budget())

    print(
        "\n=== Testing Extension (Branch 2: Triggering Budget "
        "Alert) ==="
        )
    over_budget_items = [["organic milk"], ["cereal"], ["bananas"]]
    low_budget_list = ChildClass(
        "Lee", 10.00,
        "Grocery Aisle", over_budget_items
        )
    print(low_budget_list.get_summary())
    print(low_budget_list.check_projected_budget())

    print(
        "\n=== Testing Extension (Edge Case: Zero-Item Empty "
        "List Verification) ==="
        )
    empty_items = [[], [], []]
    empty_list = ChildClass(
        "Patel", 50.00, "Bakery", empty_items
        )

    print(empty_list.get_summary())
    print(empty_list.check_projected_budget())

    print(
        "\n=== Testing Edge Case (List Missing a Bakery Section) "
        "===")
    short_list = ChildClass(
        "Kim", 40.00, "Bakery Counter", [["Rice"]]
        )
    print(short_list.add_to_bakery_section("Bagels"))

    # Run demonstrations
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()