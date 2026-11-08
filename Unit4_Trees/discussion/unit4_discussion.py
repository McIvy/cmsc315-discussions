"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        #   to the left and right child nodes.
        
        self.value = value
        # Reference to the left child (smaller values). 
        self.left = None
        # Reference to the right child (larger values).
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        
        # Top node of tree if None then empty.
        self.root = None


    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        
        # Starts recursive insertion process.
        self.root = self._insert_recursive(self.root, value)

        # Insertion depended on value comparisons because the BST rule 
        # required everything in a left subtree to be smaller than its 
        # parent and everything in a right subtree to be larger. 
        # Comparing the new value to the current node determined which 
        # branch it belonged on. This evaluation ensured every value 
        # was placed in the exact location where subsequent searches 
        # expected to find it.

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        
        # Base case: If empty spot found insert new node.
        if node is None:
            return Node(value)

        # Choose which subtree to check next.
        if value < node.value:
            # Smaller values on left, recurse into that subtree.
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Larger values on right, recurse into that subtree.
            node.right = self._insert_recursive(node.right, value)
        
        # If value == node.value, neither branch runs. Duplicates were ignored on 
        # purpose so every value is stored once and the tree stays a set.

        # Return updated node reference so parent intact.
        return node


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        
        # Start recursive search process.
        return self._search_recursive(self.root, value)

        # A linear search checks items one by one so N items can take N checks. A 
        # BST search discards a whole subtree with every comparison. In a balanced 
        # tree that halves the remaining items each step, gives O(log N). 
        # The benefit depends on balance. A lopsided tree can need up to N checks, 
        # just like a linear search.

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        
        # Base cases: Value not found or value found
        if node is None:
            return False
        if node.value == value:
            return True

        # Choose which subtree to check next.
       
        # The BST rule means the target can only be on one side, so the other side 
        # is never visited.
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        
        # Create helper list to collect values.
        result = []
        self._inorder_recursive(self.root, result)
        return result


    def _inorder_recursive(self, node, result):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # The output is sorted because a BST stores smaller values in the left subtree 
        # and larger values in the right subtree. By visiting the left side, the 
        # current node, and then the right side, the algorithm naturally processes 
        # values from smallest to largest. This rule applies at every level so the 
        # entire tree prints out in ascending order.
        
        if node:
            # Visit left side.
            self._inorder_recursive(node.left, result)
            # Record current value.
            result.append(node.value)
            # Visit right side.
            self._inorder_recursive(node.right, result)

    def height(self):
        # Starts recursive height calculation.
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        # Base case: empty path has height of -1.
        if node is None:
            return -1

        # Count the longest path down either side
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

    def suggestions(self, prefix):
        # Return every stored word that starts with the prefix, in sorted order.
        results = []
        # Edge case guard. An empty prefix matches everything, so return nothing.
        if not prefix:
            return results
        self._suggest_recursive(self.root, prefix, results)
        return results

    def _suggest_recursive(self, node, prefix, results):
        # Base case: ran off the tree, nothing more to check.
        if node is None:
            return

        starts = node.value.startswith(prefix)

        # Words starting with the prefix sit together in sorted order. If this
        # node is larger than the prefix, smaller matches may be on the left.
        if node.value > prefix:
            self._suggest_recursive(node.left, prefix, results)

        # Record this word if matched. 
        # Left, node, right keeps results sorted.
        if starts:
            results.append(node.value)

        # Matches can be on the right only if this node is smaller than the prefix
        #   or is itself a match. Otherwise the whole right side is skipped.
        if node.value < prefix or starts:
            self._suggest_recursive(node.right, prefix, results)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    employee_tree = BST()

     # So 1050 is the root to create a perfectly balanced structure.
    inserted_ids = [1050, 1025, 1075, 1012, 1037, 1062, 1087]
    for emp_id in inserted_ids:
        employee_tree.insert(emp_id)

    # Show inserted values.
    print(f"Values inserted in order: {inserted_ids}")
    print(f"Resulting sorted tree (In-Order Traversal): {employee_tree.inorder()}")
    print(f"Tree structure height: {employee_tree.height()}")
    print("=" * 60)

    target_id = 1062
    print(f"Searching for ID {target_id}...")
    found = employee_tree.search(target_id)
    print(f"Search successful? {'Yes' if found else 'No'}")

    """
    Searching a BST dramatically reduces the search space through directional elimination. 
    When searching for employee ID 1062, the target is compared to the root, 1050. Since 
    1062 is greater, discarded the entire left subtree (1025, 1012, 1037), which cut the 
    search space in half. Next, the target is compared to the remaining right child (1075).
    Because 1062 is smaller, the right branch 1087 is eliminated and the 
    remaining options are halved again. Finally, the next left child (1062) is checked 
    and found the match in just three operations. Rather than scanning all 7 elements 
    sequentially like a linear search, each comparison discarded an entire branch. This 
    tree is balanced, height 2 for 7 nodes, so that yields O(log N) time.
    """ 

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # Perform traversal and display results
    sorted_elements = employee_tree.inorder()
    print(f"In-Order Traversal results: {sorted_elements}")
    print(f"Matches sorted(inserted_ids)? {sorted_elements == sorted(inserted_ids)}")

    """
    The inorder traversal of BST produced a sorted list because the BST rule puts every
    smaller value in a node's left subtree and every larger value in its right subtree.
    Visiting left, then the node, then right ensured that all smaller values are 
    processed before the current node and all larger values are processed after. This 
    property makes inorder traversal useful for tasks like finding the median or range 
    of values in the tree.
    """

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # Find values in the tree.
    existing_target_1 = 1012
    existing_target_2 = 1087

    found_1 = employee_tree.search(existing_target_1)
    found_2 = employee_tree.search(existing_target_2)
    
    print(f"Searching for existing ID {existing_target_1}... Found? {found_1}")
    print(f"Searching for existing ID {existing_target_2}... Found? {found_2}")
    
    # Find values that do not exist in the tree.
    missing_target_1 = 999
    missing_target_2 = 2000
    
    found_3 = employee_tree.search(missing_target_1)
    found_4 = employee_tree.search(missing_target_2)
    
    print(f"Searching for missing ID {missing_target_1}... Found? {found_3}")
    print(f"Searching for missing ID {missing_target_2}... Found? {found_4}")

    """
    The search tests confirmed the directional logic of the binary search tree. 
    When searching for an existing IDs like 1012 or 1087, the algorithm evaluates node 
    values at each step and traversed the matching branch. Once it found 
    node.value == value, it returned True. Conversely, when searching for missing IDs 
    like 999 or 2000, the path down the tree eventually leads to an empty leaf 
    reference None, without hitting a match. At this point, the base case handles the 
    miss gracefully and returns False.
    
    Both missing IDs ended at the edges of the tree. 999 is smaller than every ID, so
    the search went left at every node (1050, 1025, 1012) and fell off the left of 1012.
    2000 is larger than every ID, so it went right (1050, 1075, 1087) and fell off the
    right of 1087. Each miss still took only 3 comparisons, the same as a hit.
    """
    
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Create fresh, empty BST for demos.
    empty_tree = BST()

    # Edge Case 1: Search an empty tree.
    search_empty = empty_tree.search(1050)
    print(f"Searching for ID 1050 in an empty tree... Found? {search_empty}")
    
    # Edge Case 2: Traversing an empty tree
    traversal_empty = empty_tree.inorder()
    print(f"In-order traversal of an empty tree: {traversal_empty}")

    # Edge Case 3: Insert duplicate values.
    duplicate_tree = BST()
    for emp_id in [1050, 1025, 1050, 1025, 1075]:
        duplicate_tree.insert(emp_id)
    print(f"Inserted [1050, 1025, 1050, 1025, 1075] -> stored {duplicate_tree.inorder()}")

    # Edge Case 4: A tree with only one node.
    single_tree = BST()
    single_tree.insert(1050)
    print(f"Single node tree -> traversal {single_tree.inorder()}, height {single_tree.height()}")
    print(f"Empty tree height: {empty_tree.height()}")

    # ===============================
    # INSERTION ORDER MATTERS
    # ===============================
    # Same kind of IDs, different insertion order.

    print("\n=== INSERTION ORDER COMPARISON ===")

    sequential_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
    sequential_tree = BST()
    for emp_id in sequential_ids:
        sequential_tree.insert(emp_id)

    print(f"Sequential inserts {sequential_ids}")
    print(f"Sequential tree height: {sequential_tree.height()} vs balanced height: {employee_tree.height()}")
    print(f"Both still traverse in order: {sequential_tree.inorder() == sequential_ids}")

    """
    Sorted input made every new value larger than the one before it, so every insert
    went to the right and the tree became a chain, which behaves like a linked list.
    Its height grew to 6 for 7 nodes, while the balanced insert order kept the height
    at 2. Finding 1007 in the chain meant passing through all 7 nodes, so search fell
    back to O(N). Finding 1062 in the balanced tree meant passing through only 3.
    The BST rule held in both trees, but only the balanced shape delivered O(log N)
    search. Inserting a middle value first, or using a self-balancing tree such as
    AVL or red-black, prevents the chain.
    """


    """
    These edge cases demonstrated how the recursive algorithms gracefully handled empty 
    tree structures. When search() was called on a tree where self.root is None, the 
    recursive helper _search_recursive instantly triggered its first base case,
    if node is None: and safely returned False without crashing. Also, when 
    inorder() is called, the condition if node: in the helper method evaluated to 
    False immediately. The function bypassed the recursive loops entirely and returns 
    the empty list [] untouched. Properly defined base cases ensure the program 
    remained stable even when operating on empty data structures.

    Duplicate inserts were ignored because neither the less than branch nor the
    greater than branch ran for an equal value, so 1050 and 1025 were each stored
    once. The single node tree had a height of 0 because the node has no children,
    and the empty tree had a height of -1 because its base case returns -1.
    """

    # ===============================
    # REAL WORLD EXAMPLE: SPELL CHECKER
    # ===============================
    print("\n=== REAL WORLD EXAMPLE: SPELL CHECKER ===")

    # Helper that inserts the middle word first so the dictionary tree stays balanced.
    def insert_balanced(tree, words):
        if not words:
            return
        mid = len(words) // 2
        tree.insert(words[mid])
        insert_balanced(tree, words[:mid])
        insert_balanced(tree, words[mid + 1:])

    dictionary_words = sorted(
        ["apple", "apply", "apricot", "banana", "band", "bandage",
        "bank", "cat", "catalog", "catch", "dog", "door", "zebra"]
        )
    dictionary = BST()
    insert_balanced(dictionary, dictionary_words)
    print(
        f"Dictionary loaded: {len(dictionary_words)} words, " 
        f"tree height {dictionary.height()}"
        )

    for typed in ["band", "bandit", "ca"]:
        print(f"\nUser typed: '{typed}'")
        if dictionary.search(typed):
            print("  Spelled correctly (exact match found).")
        else:
            # Not a word, so shorten the input until some words still match.
            prefix = typed
            while prefix and not dictionary.suggestions(prefix):
                prefix = prefix[:-1]
            print(
                f"  Not found. Suggestions for '{prefix}': "
                f"{dictionary.suggestions(prefix)}")

    # Edge cases for the spell checker.
    print(f"\nEmpty input suggestions: {dictionary.suggestions('')}")
    print(f"No match ('xyz'): {dictionary.suggestions('xyz')}")
    print(f"Empty dictionary: {BST().suggestions('ban')}")

    """
    A spell checker is and example of BST because words compare in alphabetical
    order. The same left smaller and right larger rule applies here. Checking a word
    used search(), which discarded half the dictionary at each step. Suggestions used
    the in-order idea and matching words came out already sorted. Inserting the
    middle word first kept the tree balanced. This is why lookups stayed O(log N).
    Loading the same words in alphabetical order would have built a chain and made
    every lookup O(N), the same problem shown in the insertion order comparison.
    An empty prefix returned nothing then an unknown prefix returned. Then an empty 
    list and an empty dictionary returned an empty list without crashing.
    """


if __name__ == "__main__":
    main()