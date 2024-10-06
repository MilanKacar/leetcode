def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    """
    Determines if two sentences can be made identical by inserting 
    an arbitrary sentence into one of them.
    
    Args:
    - sentence1 (str): The first sentence.
    - sentence2 (str): The second sentence.
    
    Returns:
    - bool: True if the sentences are similar, otherwise False.
    """
    s1_words = sentence1.split()  # Split sentence1 into words
    s2_words = sentence2.split()  # Split sentence2 into words
    
    # Step 1: Find the longest common prefix
    i = 0
    while i < len(s1_words) and i < len(s2_words) and s1_words[i] == s2_words[i]:
        i += 1  # Move forward as long as words match at the start
    
    # Step 2: Find the longest common suffix
    j = 0
    while j < len(s1_words) - i and j < len(s2_words) - i and s1_words[-1 - j] == s2_words[-1 - j]:
        j += 1  # Move backward as long as words match at the end
    
    # Step 3: Check if i + j covers the entire shorter sentence
    return i + j == min(len(s1_words), len(s2_words))


# Test cases
def test_areSentencesSimilar():
    # Test case 1
    sentence1 = "My name is Haley"
    sentence2 = "My Haley"
    assert areSentencesSimilar(sentence1, sentence2) == True, "Test case 1 failed"

    # Test case 2
    sentence1 = "of"
    sentence2 = "A lot of words"
    assert areSentencesSimilar(sentence1, sentence2) == False, "Test case 2 failed"

    # Test case 3
    sentence1 = "Eating right now"
    sentence2 = "Eating"
    assert areSentencesSimilar(sentence1, sentence2) == True, "Test case 3 failed"

    # Test case 4
    sentence1 = "Hello"
    sentence2 = "Hello World"
    assert areSentencesSimilar(sentence1, sentence2) == True, "Test case 4 failed"

    # Test case 5
    sentence1 = "I love programming"
    sentence2 = "I programming"
    assert areSentencesSimilar(sentence1, sentence2) == True, "Test case 5 failed"

    # Test case 6
    sentence1 = "one word"
    sentence2 = "another word"
    assert areSentencesSimilar(sentence1, sentence2) == False, "Test case 6 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_areSentencesSimilar()
