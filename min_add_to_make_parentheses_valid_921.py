# Solution for LeetCode problem #921: Minimum Add to Make Parentheses Valid

def minAddToMakeValid(s: str) -> int:
    open_count = 0  # Count of unmatched '('
    close_needed = 0  # Count of ')' needed

    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1  # Match with an open '('
            else:
                close_needed += 1  # No matching '('

    # Total moves: unmatched '(' + unmatched ')'
    return open_count + close_needed

# Test cases
test_cases = [
    # Test case 1: minimal mismatch
    ("())", 1), 
    # Test case 2: all open parentheses
    ("(((", 3), 
    # Test case 3: already valid
    ("()", 0), 
    # Test case 4: alternating valid parentheses
    ("()()", 0), 
    # Test case 5: closing parentheses before any opening
    (")))", 3), 
    # Test case 6: nested parentheses with an extra closing parenthesis
    ("(()))", 1), 
    # Test case 7: empty string
    ("", 0), 
    # Test case 8: mix of unmatched and matched parentheses
    ("(()))(()", 2), 
    # Test case 9: multiple unmatched parentheses
    ("))((", 4), 
    # Test case 10: one closing without opening
    (")", 1)
]

# Run test cases
for i, (input_str, expected) in enumerate(test_cases, 1):
    result = minAddToMakeValid(input_str)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
