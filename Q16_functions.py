# Q16. Write functions to organize a program that performs basic operations on strings and lists.

# --- String Functions ---

def reverse_string(s):
    """Returns the reversed string."""
    return s[::-1]

def count_vowels(s):
    """Counts the number of vowels in a string."""
    return sum(1 for ch in s.lower() if ch in "aeiou")

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def count_words(s):
    """Counts words in a string."""
    return len(s.split())

# --- List Functions ---

def list_stats(lst):
    """Returns basic statistics of a numeric list."""
    return {
        "length"  : len(lst),
        "sum"     : sum(lst),
        "max"     : max(lst),
        "min"     : min(lst),
        "average" : sum(lst) / len(lst)
    }

def remove_duplicates(lst):
    """Removes duplicates from a list preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def flatten_list(nested):
    """Flattens a nested list by one level."""
    return [item for sublist in nested for item in sublist]


# --- Main Program ---

print("=== String Functions ===")
word = "racecar"
print(f"reverse_string('{word}')  : {reverse_string(word)}")
print(f"count_vowels('{word}')    : {count_vowels(word)}")
print(f"is_palindrome('{word}')   : {is_palindrome(word)}")
print(f"is_palindrome('hello')    : {is_palindrome('hello')}")
print(f"count_words('Hello World'): {count_words('Hello World')}")

print("\n=== List Functions ===")
numbers = [4, 2, 8, 2, 5, 4, 9, 1, 7]
print(f"List: {numbers}")
stats = list_stats(numbers)
for k, v in stats.items():
    print(f"  {k}: {v}")
print(f"remove_duplicates : {remove_duplicates(numbers)}")

nested = [[1, 2], [3, 4], [5, 6]]
print(f"flatten_list({nested}): {flatten_list(nested)}")
