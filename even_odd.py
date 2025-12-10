print("=== Even/Odd Checker – start ===")

# 1. Helper function: decides if a number is even
def is_even(n: int) -> bool:
    """
    Return True if n is even, False otherwise.
    """
    return n % 2 == 0


# 2. Main program logic wrapped in a function
def main() -> None:
    # Ask the user for a number as text
    number_str = input("Enter an integer: ").strip()

    # Handle negative numbers
    if number_str.startswith("-"):
        num_part = number_str[1:]
    else:
        num_part = number_str

    # Validate that what's left is all digits
    if not num_part.isdigit():
        print("That is not a valid integer.")
        return  # stop the function early

    # Convert the string to an actual integer
    number = int(number_str)

    # Use our helper function instead of writing the logic inline
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    print("Thanks for using the even/odd checker!")


# 3. Only run main() if this file is executed directly
if __name__ == "__main__":
    main()
    print("=== Even/Odd Checker – done ===")


