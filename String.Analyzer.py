"""
String Analyzer

Prompts the user for a sentence and demonstrates
string transformation, searching, slicing, and analysis.
"""

while True:
    sentence = input("Enter a sentence (1-200 characters): ").strip()

    if not sentence:
        print("Your sentence cannot be empty. Try again.")
    elif len(sentence) > 200:
        print("Please keep your sentence under 200 characters.")
    else:
        break

try:
    print("\n--- String Analysis ---")

    # Transformation
    print("Uppercase:", sentence.upper())
    print("Lowercase:", sentence.lower())
    print("Reversed:", sentence[::-1])

    # Analysis
    words = sentence.split()
    print("Word count:", len(words))
    print("Character count:", len(sentence))
    print("First three words:", words[:3])

    search_word = input("\nEnter a word to search for: ").strip()

    if not search_word:
        print("You did not enter a search word.")
    else:
        count = sentence.lower().count(search_word.lower())
        print(f"'{search_word}' appears {count} time(s).")

    # Palindrome check
    cleaned = "".join(character.lower() for character in sentence if character.isalnum())

    if cleaned == cleaned[::-1]:
        print("The sentence is a palindrome.")
    else:
        print("The sentence is not a palindrome.")

except (ValueError, IndexError) as error:
    print(f"Something went wrong while analyzing the text: {error}")
