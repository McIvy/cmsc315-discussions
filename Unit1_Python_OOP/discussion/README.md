# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Files

- `unit1_discussion.py` contained the parent class, child class, namespace demo, copy demo, and `main()`.

## How to Run

```bash
cd Unit1_Python_OOP/discussion
python3 unit1_discussion.py
```

The script required no input. It printed the parent and child objects, the namespace demo, the shallow and deep copy demos, and the extension result.

## Student-Created Extension

`check_projected_budget()` was a method added to `ChildClass`. It counted every item across the nested lists, multiplied the count by an average item cost ($5.00 by default), and compared the estimate to the object's budget. It returned a budget alert when the estimate was over and the amount remaining when it was under. `main()` called it on the Suitland list. 

## What the Demos Showed

### Inheritance 
`ChildClass` inherited `name`, `budget`, and `get_summary()` from `ParentClass`. It then overrode `get_summary()` and added a department, nested item lists, and a specialty store.

### Namespaces 
Printing `__dict__` showed that each object stored its own data. The `coupon_code` attribute appeared only on the Smith object. Printing `ChildClass.__dict__` showed that the class stored the shared `specialty_store` variable and its methods.

### Copying 
After "apple pie" was added to the original list, the shallow copy showed it too because both objects pointed to the same nested lists in memory. The deep copy did not show it because it held its own separate lists. The `is` checks printed `True` for the shallow copy and `False` for the deep copy.

### Edge cases 
An over-budget list triggered the budget alert, with $15.00 projected against a $10.00 budget. An empty list counted as zero items and passed the budget check. A list with only one section would have raised an IndexError because `add_to_bakery_section` assumed the Bakery list sat at index 1, so a guard returned a message instead.

### Real-world use 
The same design could have supported a real shopping or inventory app. A parent class held the shared budget logic, and child classes added features for specific stores or trips.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## My Reflection

This assignment demonstrated how inheritance, namespaces, and object copying functioned in Python. A constructor with `self` gave each object its own data, and `super().__init__` reused the parent setup. Using `__dict__` showed what each object owned versus what the class shared. The `is` operator proved that a shallow copy shared nested lists while a deep copy stayed independent.

The main roadblocks stemmed from simple setup errors. A hanging Git push only resolved after switching to a personal access token. In the code, a typo (deparment) threw an AttributeError, and an incorrect format specifier broke the dollar amount in the budget line. Reading the terminal tracebacks made both bugs easy to fix.

Procedural code separated data from functions, forcing manual inputs into every routine. OOP bundled them together instead. This allowed the grocery list object to carry its own budget and item arrays.

This made maintainability easy since adding the `check_projected_budget` method to the child class was simple. It safely read the existing data the object already held without requiring new inputs, leaving the parent class and main demonstrations completely untouched. Classes required extra boilerplate setup like constructors and self. But reusability through inheritance made adding future features much cheaper in real applications.

Repo located at https://github.com/McIvy/cmsc315-discussions