# LeetCode
Problems solved

|        |   Arrays |   Back Tracking |   Binary |   Dynamic Programming |   Graph |   Heap |   Linked List |   String |   Tree |   Two Pointers |   Union Find |   total |
|:-------|---------:|----------------:|---------:|----------------------:|--------:|-------:|--------------:|---------:|-------:|---------------:|-------------:|--------:|
| easy   |       30 |               0 |        2 |                     4 |       0 |      1 |             3 |       16 |     14 |              0 |            0 |      70 |
| medium |      122 |               3 |        2 |                    25 |      24 |      4 |            10 |       38 |     44 |              5 |            2 |     279 |
| hard   |       21 |               1 |        0 |                    12 |      12 |      5 |             1 |        5 |      5 |              1 |            3 |      66 |
| total  |      173 |               4 |        4 |                    41 |      36 |     10 |            14 |       59 |     63 |              6 |            5 |     415 |

Problems worth resolving 

1. Arrays
>* Easy
>    * 169 Majority Element : Solve with using O(1) extra space.
>* Medium
>    * 1314 Matrix Block Sum : Prefix sum with 2D array
>    * 56 Merge Intervals : Not sorted input & take care of all cases
>    * 152 Maximum Product Subarray
>    * 334 Increasing Triplet Subsequence
>    * 347 Top K Frequent Elements : The idea of bucket sort.
>    * 435 Non-overlapping Intervals : Sorting intervals. 
>    * 526 Beautiful Arrangement
>    * 1014 Best Sightseeing Pair
>    * 406 Queue Reconstruction by Height
>    * 739 Daily Temperatures
>    * 18 4Sum
>    * 932 Beautiful Array
>    * 1424 Diagonal Traverse II
>    * 525 Contiguous Array
>    * 2054 Two Best Non-Overlapping Events
>    * 740 Delete and Earn
>* Hard
>    * 239 Sliding Window Maximum : A typical monotonic queue problem. 
>    * 862 Shortest Subarray with Sum at Least K, 1499 Max Value of Equation : Monotonic queue problems(very simillar).
>    * 84 Largest Rectangle in Histogram
>    * 330 Patching Array : A greedy solution with the interval.
>    * 352 Data Stream as Disjoint Intervals : Stream processing using heap.
>    * 1526 Minimum Number of Increments on Subarrays to Form a Target Array
>    * 1074 Number of Submatrices That Sum to Target : prefix by row
>    * 42 Trapping Rain Water
2. Dynamic Programming
>* Easy
>    * 121,122 : Best Time to Buy and Sell Stock series
>* Medium
>    * 1567 Maximum Length of Subarray With Positive Product
>    * 322 Coin Change, 518 Coin Change 2 : Basic dynamic programming problems. 
>    * 576 Out of Boundary Paths
>    * 837 New 21 Game : Brilliant DP. 
>    * 1155 Number of Dice Rolls With Target Sum
>    * 1143 Longest Common Subsequence
>    * 123,188 : Best Time to Buy and Sell Stock series
>    * 1277 Count Square Submatrices with All Ones
>    * 795 Number of Subarrays with Bounded Maximum
>* Hard
>    * 879 Profitable Schemes : 2D dp.
>    * 1416 Restore The Array
>    * 309,714 : Best Time to Buy and Sell Stock series
>    * 312 Burst Balloons : 2D DP
>    * 1866 Number of Ways to Rearrange Sticks With K Sticks Visible
3. Linked List
>* Medium
>    * 19 Remove Nth Node From End of List : Solve with only one pass.
4. Priority Queue
>* Hard
>    * 23 Merge k Sorted Lists : A typical heap problem. 
>    * 295 Find Median from Data Stream
>    * 1439 Find the Kth Smallest Sum of a Matrix With Sorted Rows
>    * 1675 Minimize Deviation in Array
5. Tree
>* Medium
>    * 105 Construct Binary Tree from Preorder and Inorder Traversal, 889 Construct Binary Tree from Preorder and Postorder Traversal : Nice recursion solution exists. 
>    * 437 Path Sum III : Prefix method on the binary tree. 
>    * 729 My Calendar I : Sorting intervals using Binary Search Tree.
>    * 307 Range Sum Query - Mutable : Segmented Tree
>    * 1367 Linked List in Binary Tree : KMP algorithm with tree.
>* Hard
>    * 1028 Recover a Tree From Preorder Traversal : Nice usage of stack. 
>    * 968 Binary Tree Cameras : Greedy DFS
>    * 732 My Calendar III : Segmentation tree with lazy propagation.
6. Graph
>* Medium
>    * 207 Course Schedule : A typical topological sorting problem. 
>    * 417 Pacific Atlantic Water Flow : The idea of reverse flow.
>    * 1631 Path With Minimum Effort : A typical Dijkstra Algorithm problem. DFS would cause TLE. 
>    * 1584 Min Cost to Connect All Points : Minimum Spanning Tree
>    * 1091 Shortest Path in Binary Matrix : A problem that DFS gives TLE but BFS passes.
>    * 1334 Find the City With the Smallest Number of Neighbors at a Threshold Distance : Floyd Algorithm. 
>* Hard
>    * 773 Sliding Puzzle
>    * 127 Word Ladder : A problem that DFS gives TLE but BFS passes.
7. Binary
>* Easy
>    * 191 Number of 1 Bits : The idea of n&-n.   
>* Medium
>    * 1442 Count Triplets That Can Form Two Arrays of Equal XOR : Time O(n) using the properties of XOR. 
8. String
>* Easy
>    * 28 Implement strStr() : KMP algorithm
>* Medium
>    * 648 Replace Words : The idea of Trie. 
>    * 966 Vowel Spellchecker
>    * 1209 Remove All Adjacent Duplicates in String 
>* Hard
>    * 1209 Remove All Adjacent Duplicates in String II
>    * 1032 Stream of Characters
>    * 1312 Minimum Insertion Steps to Make a String Palindrom : Longetst Common Subsequencee
9. Union Find
>* Hard
>    * 1627 Graph Connectivity With Threshold : A typical union find problem. 
>    * 1697 Checking Existence of Edge Length Limited Paths
10. Backtracking
>* Medium
>    * 39 Combination Sum
>    * 698 Partition to K Equal Sum Subsets
>* Hard
>    * 37 Sudoku Solver
11. Two Pointers
>    * 1004 Max Consecutive Ones III
