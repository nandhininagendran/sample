def reverse_number(N):
    # Convert the number to a string, reverse it, and convert back to integer
    reversed_number = int(str(N)[::-1])
    return reversed_number

# Sample Input
N = int(input())

# Check if input is within constraints
if N <= 1000:
    # Call the function to reverse the number
    reversed_number = reverse_number(N)
    # Print the reversed number
    print(reversed_number)
else:
    print("Input is out of constraints.")
