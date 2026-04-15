def cocktail_sort(arr):
    n = len(arr)    # Get the total number of elements
    swapped = True  # Flag to indicate if any swap has occurred
    start = 0       # Starting index of the unsorted portion
    end = n - 1     # Ending index of the unsorted portion


    # Continue looping until no swaps occur in both directions
    while swapped:
        swapped = False

        # Forward pass: move the largest unsorted element to the end
        for i in range(start, end):
            # Compare adjacent pairs
            if arr[i] > arr[i + 1]:
                # Swap if elements are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If no swaps occurred in the forward pass,
        # the list is already sorted
        if not swapped:
            break
        
        # Reset swapped flag for the backward pass
        swapped = False
        # Reduce the upper boundary since the last element is now sorted
        end -= 1

        # Backward pass: move the smallest unsorted element to the start
        for i in range(end - 1, start - 1, -1):
             # Compare and swap adjacent pairs in reverse direction
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Increment the lower boundary since the first element is sorted
        start += 1

    # Return the fully sorted array
    return arr
