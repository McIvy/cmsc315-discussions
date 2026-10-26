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

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

This week’s exercise showed how stacks and queues are built on lower-level structures. I wrapped a list and collections.deque in classes with simple interfaces. This taught me encapsulation, since users never touch the underlying data. I also learned about efficiency. Using collections.deque gives O(1) constant-time removal from the front of a queue. Exception handling was another skill sharpened, because I had to decide how each method behaves when the container is empty.

The main challenge was having to handle those empty calls gracefully. Raising IndexError from pop and dequeue kept the code from failing silently. In parallel, peek and front returned None so a quick look at an empty container did not crash. Another challenge was getting queue access right. A careless front() could have returned the entire container, so I limited it to returning only the first element.

The pancake and jet bridge scenarios showed me how the two structures differ in daily life. A stack served the newest item first, like eating the top pancake from a pile. A queue serves the oldest first, like passengers boarding a jet bridge in the order they arrived. Grounding the code in everyday examples helped me understand these concepts much better.