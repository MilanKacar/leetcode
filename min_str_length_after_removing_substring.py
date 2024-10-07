# Problem: Minimum String Length After Removing Substrings

"""
You are given a string s consisting only of uppercase English letters.
You can apply some operations to this string where, in one operation, 
you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.
"""

# Basic Approach 🛠️
def minLength_basic(s: str) -> int:
    while "AB" in s or "CD" in s:
        s = s.replace("AB", "")
        s = s.replace("CD", "")
    return len(s)

# Use case for basic approach
if __name__ == "__main__":
    s1 = "ABFCACDB"
    s2 = "ACBBD"
    print("Basic Solution Results:")
    print(f"Input: {s1}, Result: {minLength_basic(s1)}")  # Output: 2
    print(f"Input: {s2}, Result: {minLength_basic(s2)}")  # Output: 5


# Optimized Stack Approach 🚀
def minLength_stack(s: str) -> int:
    stack = []
    for char in s:
        if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

# Use case for optimized stack approach
if __name__ == "__main__":
    s1 = "ABFCACDB"
    s2 = "ACBBD"
    print("\nOptimized Stack Solution Results:")
    print(f"Input: {s1}, Result: {minLength_stack(s1)}")  # Output: 2
    print(f"Input: {s2}, Result: {minLength_stack(s2)}")  # Output: 5


# Recursive Approach 🔄
def minLength_recursive(s: str) -> int:
    if "AB" not in s and "CD" not in s:
        return len(s)
    
    if "AB" in s:
        s = s.replace("AB", "", 1)
    if "CD" in s:
        s = s.replace("CD", "", 1)
    
    return minLength_recursive(s)

# Use case for recursive approach
if __name__ == "__main__":
    s1 = "ABFCACDB"
    s2 = "ACBBD"
    print("\nRecursive Solution Results:")
    print(f"Input: {s1}, Result: {minLength_recursive(s1)}")  # Output: 2
    print(f"Input: {s2}, Result: {minLength_recursive(s2)}")  # Output: 5


# Dynamic Programming Approach 🧠
def minLength_dp(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)  # DP array to store minimum lengths

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        
        if i > 1 and ((s[i - 2] == 'A' and s[i - 1] == 'B') or (s[i - 2] == 'C' and s[i - 1] == 'D')):
            dp[i] = min(dp[i], dp[i - 2])

    return dp[n]

# Use case for DP approach
if __name__ == "__main__":
    s1 = "ABFCACDB"
    s2 = "ACBBD"
    print("\nDynamic Programming Solution Results:")
    print(f"Input: {s1}, Result: {minLength_dp(s1)}")  # Output: 2
    print(f"Input: {s2}, Result: {minLength_dp(s2)}")  # Output: 5
