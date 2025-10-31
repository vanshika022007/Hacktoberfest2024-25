"""
linear_and_binary_search.py
----------------------------
Program: Demonstrates Linear Search and Binary Search algorithms.

Problem Statement:
Given a sorted list of numbers, search for a given number using both
Linear Search and Binary Search techniques.

Input / Output Example:
-----------------------
Input:
Enter a number to search: 5

Output:
[Linear Search] 5 found at position 4
[Binary Search] 5 found at position 4

Complexity:
------------
Linear Search: O(n)
Binary Search: O(log n)

Compile / Run:
--------------
python3 linear_and_binary_search.py
"""

def linear_search(num, array):
    """Performs a linear search to find `num` in `array`."""
    for i in range(len(array)):
        if array[i] == num:
            print(f"[Linear Search] {num} found at position {i}")
            return
    print(f"[Linear Search] {num} not found in the list.")


def binary_search(num, array):
    """Performs binary search to find `num` in a sorted `array`."""
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] < num:
            low = mid + 1
        elif array[mid] > num:
            high = mid - 1
        else:
            print(f"[Binary Search] {num} found at position {mid}")
            return

    print(f"[Binary Search] {num} not found in the list.")


if __name__ == "__main__":
    array = [n + 1 for n in range(10)]  # Sorted array [1,2,3,...,10]
    print("Array:", array)
    try:
        num = int(input("Enter a number to search: "))
        linear_search(num, array)
        binary_search(num, array)
    except ValueError:
        print("Please enter a valid integer.")
