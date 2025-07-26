def format_indian_currency(number):
    """
    Converts a number into Indian currency format with commas.
    Example: 123456.7891 => '1,23,456.7891'
    """
    num_str = str(number)

    # Separate integer and decimal parts
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
        decimal_part = '.' + decimal_part
    else:
        integer_part = num_str
        decimal_part = ''

    # If the number is less than or equal to 3 digits, no formatting needed
    if len(integer_part) <= 3:
        return integer_part + decimal_part

    # Last 3 digits are grouped together
    last_three_digits = integer_part[-3:]
    remaining_digits = integer_part[:-3]

    # Add commas after every two digits in the remaining part
    formatted_parts = []
    while len(remaining_digits) > 2:
        formatted_parts.insert(0, remaining_digits[-2:])
        remaining_digits = remaining_digits[:-2]
    if remaining_digits:
        formatted_parts.insert(0, remaining_digits)

    # Combine all parts with commas
    formatted_integer = ','.join(formatted_parts + [last_three_digits])

    return formatted_integer + decimal_part

# --- Input from user ---
try:
    user_input = input("Enter a number to format as Indian currency (e.g., 123456.7891): ")
    number = float(user_input)
    formatted = format_indian_currency(number)
    print(f"Formatted Indian currency: {formatted}")
except ValueError:
    print("Invalid input. Please enter a valid number (e.g., 123456.7891).")
