# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Real World Scenario

I used a binary search tree to model a spell checker dictionary. Words compare alphabetically so the same rule applied. Smaller words went left and larger words went right. I loaded 13 words by inserting the middle word first which kept the tree balanced at height 3.

Checking a typed word used the search method. Each comparison discarded half of the remaining dictionary, so a lookup stayed O(log N). When a word was not found, such as "bandit", the program shortened it one letter at a time until stored words matched. It found "band" and returned "band" and "bandage" as suggestions. These came out in sorted order because the suggestion method followed the left-node-right pattern of an inorder traversal.

The edge cases behaved safely. An empty input returned no suggestions, a prefix with no match returned an empty list and an empty dictionary returned an empty list without crashing. Loading the same words in alphabetical order would have created a chain and made every lookup O(N) like in the insertion order comparison problem.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Reflection
In this assignment I learned how a binary search tree keeps its values ordered by sending every smaller value left and every larger value right. Writing the recursive insert, search and inorder methods showed me that one comparison at each node decides where a value belongs and where to look for it later. The first challenge I ran into was explaining why inorder traversal returns sorted output instead of just stating that it does. I overcame it by tracing the seven employee IDs through the tree. Through this process, I saw that the left subtree is always smaller and the right subtree is always larger. My second challenge was seeing that tree shape matters. When I inserted 1001 through 1007 in order, the tree became a chain with a height of 6 when starting with 1050 kept height 2.

A BST discards a whole subtree with each comparison, so a balanced tree searches in O(log N) time. A list checks items one by one in O(N). A sorted array can use binary search but inserting means shifting elements, while a BST inserts without shifting. The tradeoff is that an unbalanced BST falls back to O(N).