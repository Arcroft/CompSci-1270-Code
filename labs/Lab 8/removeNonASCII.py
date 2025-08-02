# Ashlyn Croft
# 20Jul25
# Lab 8
# Remove non ASCII
# Remove non-ASCII characters: I'm assuming this is likely standard practice to strip input files to prevent runtime errors.



def readFile(filename):
    """
    Opens and reads the text file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def removeNonASCII(text):
    """
    Removes all non-ASCII characters
    
    """
    clean = ""
    
    # Iterate through each character
    for character in text:
        # Check if character is ASCII
        if ord(character) <= 127:
            clean += character
    
    return clean

def writeCleanFile(content, original_filename):
    """
    Writes stripped content to a new file with '_clean.txt' suffix.

    """
    if original_filename.endswith('.txt'):
        new_filename = original_filename.replace('.txt', '_clean.txt')
    else:
        new_filename = original_filename + '_clean.txt'
    
    # Write the cleaned content
    with open(new_filename, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Cleaned file saved as: {new_filename}")





def main():
    """
    Main function - file cleaning process.
    """
    print("ASCII File Cleaner")
    print("=" * 30)
    print("This program removes non-ASCII characters from text files.")
    print("ASCII characters have decimal values 0-127.")
    print()
    
    # Get filename from user
    filename = input("Enter the filename (including .txt extension): ")
    
    try:
        # Read the original file contents
        file_content = readFile(filename)
        
        print(f"\nOriginal file content:")
        print("-" * 40)
        print(file_content)
        print("-" * 40)
        
        # Remove non-ASCII characters
        cleaned_content = removeNonASCII(file_content)
        
        print(f"\nCleaned content (ASCII only):")
        print("-" * 40)
        print(cleaned_content)
        print("-" * 40)
        
        # Write cleaned content to new file
        writeCleanFile(cleaned_content, filename)
        
        # Show character count comparison
        original_count = len(file_content)
        cleaned_count = len(cleaned_content)
        removed_count = original_count - cleaned_count
        
        print(f"\nSummary:")
        print(f"Original characters: {original_count}")
        print(f"Cleaned characters: {cleaned_count}")
        print(f"Non-ASCII characters removed: {removed_count}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        print("Make sure the file exists in the same folder as this script.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


# Is this similar to something used in the backend of like... Idk how to describe. Version edit changes? Comparisons?
# You could strip everything from two files that are shared relative to some metric. See how much text is left in either. 
# E.g, you test one student paper against another and after stripping there is 10% of original characters left in either paper.
# Or, maybe, treat sentences and paragraphs as lists and sub lists and sub sub lists and stuff?
# So you can pinpoint minor revisions like changing a single word to a synonym.

# I suppose for the plagarism check.
# strip all filler words and punctuation. The, and, but, ;, .. Etc
# Use a nested list structure to determine if some % of words within a list(paragraph, sentence, etc) are similar.
# You could set different thresholds. So, a sentence might need to share at least 60% of words, but a paragraph might need to share 70%. 
# This would quickly hint at whether the content was written once: and then jumbled slightly to avoid detection.
# You could include a dictionary that contained synonyms for the checks: so simply right clicking in word with synonym wouldn't pass the filter.
# Run an after analysis descriptive statistic block.
# Total Paper Similarity: 70%.
# Paper1 - 7 paragraphs. Paper2 - 8 paragraphs.  Check every pairing: 5 paragraphs meet the threshold for flagging at >60% similarity
# Flagged paragraphs, 1-5: comparison at sentence level. Accounting for synonyms, 75% of sentences contain the same words and their variations.

# So, I ...admittedly don't love coding. I'm drowning. I havnt slept in 2 days. The workload isnt sustainable, and I've spent all night in the animal hospital.
# BUT, moments like this are something I always find impactful. Like learning an instrument. Even if I never played/coded again(lol, I'll be coding R eternally): 
# I have a deeper appreciation for backend code/orchestra.

# Expanding out from this: for stylometry. You'd use more depth than this, but you could expand out to build a model for how sentences are typically structured early on, 
# and then move into how they change over time.

# Building a model that essentially does the plagiarism check at a deeper level. You're just examining the evolution of writing over a 
# temporal space for the same author.

# This actually might be one of the more interesting files. This is foundational building blocks for many systems of writing analysis
# FBI writing sample checks against database. Examining the progression of Plato's work over time without being able to 100% date them. 
# To rapidly check for "micro" plagarism beyond the macro: author's lifting significant sentences from other works.

# Expanding further: I don't know how the parameters of LLMs are structured: but is it just a sort of inverse stylometry?
# Instead of examining for similarity for anaylsis: you use a model with broken down sentence structures and vocabularies to generate predictive text
# That then could self anaylsis its own work against what it was fed, to determine how similar(facilitating the function of probablility)
# Its generative output is to input samples. 
# Huh.


# Neat