"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # DONE: Created the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # DONE: Added value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Append to end for LIFO behavior.
        self.items.append(value)

    def pop(self):
        # DONE: Removed and returned the most recently added value.
        # What should happen if the stack is empty?
        """Removes from the end, the same end push adds to, so the newest item leaves first (LIFO)."""
        # Prevent silent bugs by raising IndexError when empty.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        # DONE: Returned the top value without removing it.
        # Inspects top item without removing it.
        # Returns None if empty.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # DONE: Returned True since the stack had no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # DONE: Created the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # DONE: Added value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Adding to the back ensures older elements at the front are processed first.
        self.items.append(value)

    def dequeue(self):
        # DONE: Removed and returned the value from the front of the queue.
        # Prevents silent bugs by raising IndexError when queue is empty.
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def front(self):
        # DONE: Returned the front value without removing it.
        # Inspects the front item without removing it.
        # Returns None if empty.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # DONE: Returned True since the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")


    # ===============================
    # DONE: STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")

    # Create a stack object.
    my_stack = Stack()

    # Edge Case: peek() on an empty stack.
    print(f"Initial empty stack peek: {my_stack.peek()}")

    # Add at least 4 values to the stack.
    print("\nPushing 4 elements onto the stack...")
    for item in ["Book A", "Book B", "Book C", "Book D"]:
        my_stack.push(item)

        # Print statements clearly explain what is happening.
        print(f" -> Pushed: {item}")

    print(f"\nCurrent top of the stack (peek): {my_stack.peek()}")

    # Demonstrate LIFO behavior.
    print("\nPopping elements off the stack (LIFO Order):")
    while not my_stack.is_empty():
        print(f" -> Popped: {my_stack.pop()}")

    # Show what happens when pop() is used on an empty stack.
    print("\nAttempting to pop from an empty stack:")
    try:
        my_stack.pop()
    except IndexError as e:
        print(f" -> Caught expected error: {e}")

    # Single item stack lifecycle and verification.
    print("\nTesting single-item lifecycle:")
    single_stack = Stack()
    single_stack.push("Only Item")
    print(f" -> Pushed: {single_stack.peek()}")
    print(f" -> Removed: {single_stack.pop()}")
    print(f" -> Is the stack empty now? {single_stack.is_empty()}")


    # ===============================
    # DONE: QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.")

    # Create a Queue object.
    my_queue = Queue()

    # Edge Case: front() on an empty queue.
    print(f"Initial empty queue front: {my_queue.front()}")

    # Add at least 4 values to the queue.
    print("\nEnqueueing 4 elements onto the queue...")
    for item in ["Customer A", "Customer B", "Customer C", "Customer D"]:
        my_queue.enqueue(item)
        # Print statements clearly explain what is happening.
        print(f" -> Enqueued: {item}")

    print(f"\nCurrent front of the queue: {my_queue.front()}")

    # Demonstrate FIFO behavior.
    print("\nDequeuing elements off the queue (FIFO Order):")
    while not my_queue.is_empty():
        print(f" -> Dequeued: {my_queue.dequeue()}")

    # Show what happens when dequeue() is used on an empty queue.
    print("\nAttempting to dequeue from an empty queue:")
    try:
        my_queue.dequeue()
    except IndexError as e:
        print(f" -> Caught expected error: {e}")

    # Single item queue lifecycle and verification.
    print("\nTesting single-item lifecycle:")
    single_queue = Queue()
    single_queue.enqueue("Only Item")
    print(f" -> Enqueued: {single_queue.front()}")
    print(f" -> Removed: {single_queue.dequeue()}")
    print(f" -> Is the queue empty now? {single_queue.is_empty()}")

    # ===============================
    # QUEUE SCENARIO: Airplane Jet Bridge Boarding
    # ===============================
    print("\n=== SCENARIO QUEUE DEMO ===")
    jet_bridge = Queue()

    # Edge Case: Checking the bridge before boarding begins.
    print(f"Checking jet bridge before boarding: {jet_bridge.front()}")  # None

    # Passengers scan tickets then step onto the bridge.
    print("\nPassengers scan boarding passes and enter the jet bridge...")
    for passenger in ["Seat 12A (Elena)", "Seat 12B (Marcus)", "Seat 14C (Sarah)", "Seat 15F (David)"]:
        jet_bridge.enqueue(passenger)
        print(f" -> Stepped onto jet bridge: {passenger}")

    print(f"\nPassenger currently at the front of the bridge line: {jet_bridge.front()}")

    # Flight attendants welcome passengers into the cabin in arrival order.
    print("\nPassengers stepping into the airplane cabin (FIFO Order):")
    while not jet_bridge.is_empty():
        print(f" -> Entered the plane cabin: {jet_bridge.dequeue()}")

    # Edge Case: Attendant checks the bridge after boarding concludes.
    print("\nAttendant looks down the bridge after everyone has boarded:")
    try:
        jet_bridge.dequeue()
    except IndexError as e:
        print(f" -> Gate Alert: Jet bridge is completely clear ({e})")


    # ===============================
    # STACK SCENARIO: Stack of Pancakes
    # ===============================
    print("\n=== SCENARIO STACK DEMO ===")
    pancake_stack = Stack()

    # Edge Case: Checking plate before cooking starts.
    print(f"Checking plate before breakfast: {pancake_stack.peek()}")

    # Chef makes pancakes and stacks them up.
    print("\nChef is cooking pancakes...")
    for pancake in ["Bottom Pancake (Plain)", "Middle Pancake (Blueberry)", "Top Pancake (Chocolate Chip)"]:
        pancake_stack.push(pancake)
        print(f" -> Placed on stack: {pancake}")

    print(f"\nNext pancake to be eaten (peek): {pancake_stack.peek()}")

    # Customer eats from top to bottom.
    print("\nCustomer starts eating (LIFO Order):")
    while not pancake_stack.is_empty():
        print(f" -> Ate: {pancake_stack.pop()}")

    # Edge Case: Trying to eat from an empty plate.
    print("\nCustomer tries to take another pancake:")
    try:
        pancake_stack.pop()
    except IndexError as e:
        print(f" -> Plate Warning: No more pancakes left! ({e})")


if __name__ == "__main__":
    main()
