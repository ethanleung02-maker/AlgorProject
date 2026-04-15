from matrix import Matrix        # your Matrix class (from matrix.py)
from cocktail_sort import cocktail_sort  # your sorting algorithm (from cocktail_sort.py)
import time

def demonstrate_matrix_operations():
    """
    Demonstrates creation, filling, and transposing of a Matrix.
    """
    print("=== Matrix Demonstration ===")
    
    # Create a 3x3 matrix
    matrix = Matrix(3, 3)
    
    # Fill matrix with values from 1 to 9
    count = 1
    for i in range(3):
        for j in range(3):
            matrix.set_value(i, j, count)
            count += 1  

    print("Original Matrix:")
    matrix.display()
    
    # Transpose the matrix (rows becomes columns)
    transposed = matrix.transpose()
    print("\nTransposed Matrix:")
    transposed.display()
    
    return matrix


def demonstrate_cocktail_sort():
    """
    Demonstrates the Cocktail Sort algorithm on a simple list.
    """
    print("\n=== Cocktail Sort Demonstration ===")

    # Example input list 
    arr = [5, 1, 4, 2, 8, 0, 3]
    print("Original array:", arr)
    
    # Sort the array using cocktail_sort function 
    sorted_arr = cocktail_sort(arr)

    # Print the sorted array
    print("Sorted array:  ", sorted_arr)


def demonstrate_matrix_row_sort(matrix):
    """
    Demonstrates sorting each row of a matrix using Cocktail Sort.
    """
    print("\n=== Sorting Each Row in a Matrix with Cocktail Sort ===")
    import random

    # Fill the matrix with random integers between 1 and 99
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            matrix.set_value(i, j, random.randint(1, 99))
    
    print("Matrix before Sorting:")
    matrix.display()

    # Sort each row using cocktail sort 
    for row in matrix.data:
        cocktail_sort(row)
    
    print("\nMatrix after Sorting Each Row:")
    matrix.display()


def main():
    # Step 1: Matrix operations
    matrix = demonstrate_matrix_operations()

    # Step 2: Simple cocktail sort on list
    demonstrate_cocktail_sort()

    # Step 2.1: Cocktail sort with execution time measurement
    demonstrate_cocktail_sort_with_time()

    # Step 3: Sorting rows of a matrix using cocktail sort
    demonstrate_matrix_row_sort(matrix)


def demonstrate_cocktail_sort_with_time():
    arr = [5, 1, 4, 2, 8, 0, 3]
    print("\nOriginal array:", arr)

    start = time.perf_counter()
    sorted_arr = cocktail_sort(arr)
    end = time.perf_counter()

    print("Sorted array:", sorted_arr)
    print(f"Execution time: {(end - start) * 1000:.3f} ms")

# Entry point of the program
if __name__ == "__main__":
    main()