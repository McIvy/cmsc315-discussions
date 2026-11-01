# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Real-World Scenario

A Python list keeps items in order by index. Inserting an item shifts every item after it to the right and deleting an item shifts the items after it to the left to close the gap. Searching an unsorted list means checking items one at a time until a match is found. An online shopping cart shows all three. The newest item is often shown at the top, so adding it is an insertion at index 0 and every other item shifts right. Suppose a product in the middle of a 50-item cart goes out of stock. The system first finds it using a linear search and then deletes it then every item after it shifts left. Edge case 5 in this script models both steps with search_value and delete_at. If the product is no longer in the cart, the search returns -1 and nothing is deleted, which protects the cart from a bad removal.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Reflection
In this assignment I learned how Python lists handle insertion, deletion, and searching, and why position matters. Inserting at index 0 forced every later element to shift right, an O(n) cost. Inserting at the end was amortized O(1). Searching an unsorted list required a linear scan, so a missing value meant checking every item.

My biggest challenge was list mutability. My insertion and deletion tests changed the same list in place, so 20 was gone before the search ran and the search returned -1. I fixed it by keeping a constant baseline list and using copy() to give each test section a fresh list. I also fixed NameError problems by moving variables into the right scope, and I learned that code placed after a return statement never runs. I chose try/except (EAFP) in delete_at so a bad index returned None instead of crashing.

In real applications these costs add up. In a shopping cart, adding an item at the top or removing an out-of-stock item from the middle shifts the items after it. Finding that item takes a linear search. With large carts, that work slows the system. My own long Amazon cart made me wonder how much work each customer’s cart creates at that scale. The work grows with every item added, so a very large cart slows the system.
