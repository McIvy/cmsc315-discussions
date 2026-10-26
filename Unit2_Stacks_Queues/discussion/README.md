# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements Completed

1. Stack operations implemented (push, pop, peek, is_empty).
2. Queue operations implemented (enqueue, dequeue, front, is_empty).
3. LIFO behavior demonstrated with the book stack and the pancake stack.
4. FIFO behavior demonstrated with the customer line and the jet bridge.
5. Edge cases tested (empty removal, empty viewing, single item).
6. Real-world scenarios created (jet bridge and pancake stack).

## How It Works

Both classes wrap a built-in structure behind a small interface. Callers use the methods and never touch the underlying data.

Stack. A Python list holds the items. push appends to the end, and pop removes from the end, so the newest item always leaves first (LIFO). peek reads the last item without removing it, and is_empty checks whether the list has any items.

Queue. A collections.deque holds the items. enqueue appends to the back, and dequeue uses popleft to remove from the front, so the oldest item always leaves first (FIFO). A deque is used because removing from the front of a plain list is O(N), while popleft on a deque is O(1). front reads the first item without removing it.

## Edge cases tested
1. Raising an IndexError with a descriptive message during empty pop or dequeue attempts enables the system to handle empty states robustly. This prevents silent bugs from propagating through the program with built-in data integrity.
2. For empty viewing, peek and front return None, since looking at an empty structure is a harmless question.
3. The single items demo pushes or enqueues one item, removes it and confirms is_empty becomes True.

The program output prints each case, including the caught error message. Now the behavior can be read directly from the run.

## Real-World Scenarios
1. For queue chose a Jet bridge case. Passengers step onto the bridge in the order they arrive and enter the plane in that same order. The attendant checks the empty bridge at the end which triggers the empty-dequeue case.
2. The Pancake stack, stack example, has the last pancake placed on the pile is the first one eaten.

In software development, stacks power undo history and browser back buttons, while queues power print jobs and customer service lines.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

### Concepts & Skills
This week’s exercise showed how stacks and queues are built on lower-level structures. I wrapped a list and collections.deque in classes with simple interfaces, which taught me encapsulation, since users never touch the underlying data. I also learned about efficiency, because collections.deque gives O(1) removal from the front of a queue. Exception handling was another skill, since I had to decide how each method behaves when the container is empty.

### Challenges & Solutions
The main challenge was handling empty calls gracefully. pop and dequeue raise IndexError so failures are never silent, while peek and front return None so a quick look does not crash. Getting queue access right was another challenge. A careless front() could return the entire container, so I limited it to the first element.

### Stack vs Queue
The pancake and jet bridge scenarios showed how the two structures differ in daily life. A stack serves the newest item first, like eating the top pancake from a pile. A queue serves the oldest first, like passengers boarding a jet bridge in arrival order. Grounding the code in everyday examples helped me understand both.
