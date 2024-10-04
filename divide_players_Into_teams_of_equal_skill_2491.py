class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        # If the number of players is odd, we can't form pairs
        if len(skill) % 2 != 0:
            return -1
        
        # Sort the skills in ascending order
        skill = sorted(skill)

        # Calculate the sum of the first and last player in the sorted array
        first_pair = skill[0] + skill[-1]
        chemistry = skill[0] * skill[-1]

        # Loop through the rest of the players and check if the sum is consistent
        for i in range(1, len(skill) // 2):
            if skill[i] + skill[-1 - i] != first_pair:
                return -1  # If any pair sum is different, return -1
            chemistry += skill[i] * skill[-1 - i]

        return chemistry


# Test cases to validate the solution
if __name__ == "__main__":
    # Example 1
    skill = [3, 2, 5, 1, 3, 4]
    print(Solution().dividePlayers(skill))  # Output: 22

    # Example 2
    skill = [3, 4]
    print(Solution().dividePlayers(skill))  # Output: 12

    # Example 3
    skill = [1, 1, 2, 3]
    print(Solution().dividePlayers(skill))  # Output: -1

    # Example 4
    skill = [6, 7, 2, 9, 8, 1]
    print(Solution().dividePlayers(skill))  # Output: 67

    # Example 5
    skill = [10, 10, 10, 10]
    print(Solution().dividePlayers(skill))  # Output: 200

    # Example 6
    skill = [5, 5, 5, 5, 5, 5]
    print(Solution().dividePlayers(skill))  # Output: 75

    # Example 7
    skill = [1, 2, 3, 4, 5, 6]
    print(Solution().dividePlayers(skill))  # Output: 28

    # Edge Case
    skill = [10, 20, 30]
    print(Solution().dividePlayers(skill))  # Output: -1
