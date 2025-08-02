# AShlyn croft
# 20JUL25
# Lab 8
# WOrd swap
# Swap words from user input





import random

def main():
    """
    Main function
    """
    print("Word Swap Generator")
    print("=" * 30)
    print("This program randomly reassigns words in your sentence.")
    print("Each unique word gets a consistent random replacement.")
    print()
    
    # complete sentence from user
    sentence = input("Enter a complete sentence: ")
    words = sentence.split()
    

    unique_words = list(set(words))
    


    word_mapping = {}
    for word in unique_words:
        replacement_word = random.choice(words)
        word_mapping[word] = replacement_word

    
    # Dictionary
    print()
    print("Word Mapping Dictionary:")
    print("-" * 25)
    print(word_mapping)
    

    # Create new sentence
    new_sentence_words = []
    for word in words:
        new_sentence_words.append(word_mapping[word])
    



    # Print
    new_sentence = " ".join(new_sentence_words)
    print()
    print("Original sentence:")
    print(f'"{sentence}"')
    print()
    print("New sentence with word swaps:")
    print(f'"{new_sentence}"')
    
    # Breakdown
    print()
    print("Word-by-word breakdown:")
    print("-" * 25)
    for i, original_word in enumerate(words):
        replacement = word_mapping[original_word]
        print(f"{i+1}. '{original_word}' → '{replacement}'")

if __name__ == "__main__":
    main()


# I'm... unsure what this extrapolates to.
# Seeding? Generative content? 