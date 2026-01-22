# Function to sort the die values from highest to lowest


def insertion_sort1(numbers):
    # Variable to get the start time
    for i in range(1, len(numbers)):
        # To +1 every time it loops
        temp = numbers[i]  # Making the target element a temp to move to correct position
        j = i - 1  # Last element in sorted list
        # To move the numbers to the right one
        while j >= 0 and temp < numbers[j]:
            # To +1 every time it loops
            numbers[j + 1] = numbers[j]
            j = j - 1
        # Place the temp in correct sorted position
        numbers[j + 1] = temp
    return numbers