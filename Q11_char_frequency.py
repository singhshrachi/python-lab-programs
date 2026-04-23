# Q11. Program to count frequency of characters in a string.

text = input("Enter a string: ")

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("\nCharacter Frequencies:")
print("-" * 25)
for char, count in sorted(freq.items()):
    print(f"  '{char}' : {count}")
