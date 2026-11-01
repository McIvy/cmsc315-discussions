"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""

# Use a global constant to define a master reusable baseline list.
# It is a static list that will go untouched with further operaton.
BASE_LIST = [10, 20, 30, 40]


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Use the built-in list insert method. 
    # Add the value at the specific index.
    lst.insert(index, value)

    # After an insertion, existing elements have to shift right.
    # Insertions at the beginning are the most costly as all elements move.
    # Insertions in the middle are faster but still has element shift cost till end.
    # The fastest insertion happens at the end as there are no shifts. 


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Index validation prevents the program from crashing when index out of range. 
    # Safe deletion provides graceful error handling.
    # A negative index counts from the end.
    try:
        return lst.pop(index)
    except IndexError:
        # If the index does not exist, catch the exception and return None.
        return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because it checks items in the list one by one.
    # It must scan sequentially because the list is unsorted. Without any order, 
    #   we have no clue as to where the item is.
    for i in range(len(lst)):
        if lst[i] == value:
            return i 
            
    return -1 


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # Make a fresh copy so mutations don't ruin future tests
    ins_list = BASE_LIST.copy()
    print(f"Original list baseline: {ins_list}")
    
    # Test and display insertion at index 0.
    insert_at(ins_list, 0, 5)
    print(f"After inserting 5 at the beginning: {ins_list}")
    
    # Test and display middle insertion.
    insert_at(ins_list, 2, 15)
    print(f"After inserting 15 in the middle: {ins_list}")
    
    # Test and display end insertion.
    insert_at(ins_list, len(ins_list), 50)
    print(f"After inserting 50 at the end: {ins_list}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Make a fresh copy starting right from the baseline again
    del_list = BASE_LIST.copy()
    print(f"Original list baseline: {del_list}")

    # Delete beginning index, display and print updated list. 
    deleted = delete_at(del_list, 0)
    print(f"Removed value from beginning: {deleted}")
    print(f"List after first deletion: {del_list}")
    
    # Delete middle index, display and print updated list. 
    deleted = delete_at(del_list, 2)
    print(f"Removed value from middle: {deleted}")
    print(f"List after middle deletion: {del_list}")
    
    # Delete from end index, and print updated list.
    deleted = delete_at(del_list, len(del_list) - 1)
    print(f"Removed value from end: {deleted}")
    print(f"List after end deletion: {del_list}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Copying the base list guarantees 20 is exactly at index 1
    search_list = BASE_LIST.copy()
    print(f"Using pristine baseline for search: {search_list}")

    # Search for a value that is present in the list.
    # Using value 20 here. 
    found_index = search_value(search_list, 20)
    print(f"Searching for 20... Result: {found_index}")
    # Sequential scan stopped at index 1 because 20 is located there.
    
    # Search for a missing value. 
    # Using value 99 below.
    missing_index = search_value(search_list, 99)
    print(f"Searching for 99... Result: {missing_index}")
    # Scans checked every item, found no match and returned -1.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    edge_list = BASE_LIST.copy()

    # Edge Case 1: Attempt deletion of an invalid index.
    print("\nEdge Case 1: Delete using an invalid index")
    # Reusing delete_at() catches IndexError internally.
    # It returns None gracefully instead of crashing.
    print("Attempting to delete index 100...")
    edge_deleted = delete_at(edge_list, 100)
    print(f"Result of invalid deletion: {edge_deleted}")
    print(f"List remains safely unchanged: {edge_list}")
    
    # Edge case 2: Search for a missing value
    print("\nEdge Case 2: Search for a missing value")
    # Searching for an item not inside a collection checks all slots
    #   safely before returning -1 to signal a missing result.
    print("Searching for missing value 999...")
    missing_search = search_value(edge_list, 999)
    print(f"Result of missing value search: {missing_search}")

    # Edge case 3: Insert into empty list. 
    print("\nEdge Case 3: Insert into an empty list")
    # Even though the list size is 0, inserting at index 0 is valid. 
    # The first item is setup and increases list length to 1.
    empty_list_for_ins = []
    print(f"Starting state: {empty_list_for_ins}")
    print("Inserting 99 into index 0...")
    insert_at(empty_list_for_ins, 0, 99)
    print(f"Resulting list: {empty_list_for_ins}")

    # Edge Case 4: Delete from an empty list.
    print("\nEdge Case 4: Delete from an empty list")
    # An empty list has no valid elements at all. 
    # Use try/except method to catch structural IndexError immediately.
    empty_list_for_del = []
    print(f"Starting state: {empty_list_for_del}")
    print("Attempting to delete index 0...")
    empty_deleted = delete_at(empty_list_for_del, 0)
    print(f"Result of deleting from empty list: {empty_deleted}")
     
    # Edge Case 5: Auto removal of out-of-stock item.
    print("\nEdge Case 5: Out-of-stock auto-removal from middle of cart")
    
    # Simulate a 50-item cart using item IDs, 100 to 149.
    cart_list = list(range(100, 150))   
    print(
        f"Cart initialized with {len(cart_list)} items. Simulating out-of-stock check..."
        )
    
    # Demo found branch.
    out_of_stock_id = 125

    # Search: Linearly scan to locate the out-of-stock item in the middle.
    target_idx = search_value(cart_list, out_of_stock_id)
    
    # Delete: Safe deletion check to protect the cart from bad removals.
    if target_idx != -1:
        removed_id = delete_at(cart_list, target_idx)
        print(f"Item {removed_id} found at index {target_idx} and successfully auto-removed.")
        print(f"New cart size: {len(cart_list)} items (subsequent items shifted left).")
    else:
        print(f"Search returned -1. Item {out_of_stock_id} not in cart; deletion skipped.")

    # Demo else branch.
    missing_id = 999  # Item that does not exist in the cart
    print(f"\nSimulating inventory check for missing item: {missing_id}...")
    
    # Search again to locate missing item.
    target_idx_missing = search_value(cart_list, missing_id)
    
    # Do another safe deletion that triggers the protection branch
    if target_idx_missing != -1:
        removed_id = delete_at(cart_list, target_idx_missing)
        print(
            f"-> Success: Item {removed_id} found at index {target_idx_missing} \
            and auto-removed.")
    else:
        print(f"-> Protection triggered: Search returned {target_idx_missing}.")
        print(f"   Item {missing_id} was not inside the cart; bad deletion safely skipped.")
        print(f"   Cart remains safely unchanged at {len(cart_list)} items.")

if __name__ == "__main__":
    main()