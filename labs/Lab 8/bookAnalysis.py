# Ashlyn Croft
# 20JUL25
# Lab 8
# Book Analysis
# SO! It looks like we might do some of the stuff I was wondering about in the last one!
# Examining trends using this code structure
# I adore this part of learning, I wish I wasn't operating on a ton of caffine to offset 3 days without sleep, I'd enjoy this so much more, and could really experiment
# Around in the code

# Anyway




def analyzeBook(filename):
    """
    Analyzes a text file and counts word frequency.
    
    filename - name of the text file to analyze (string)
    
    Returns a dictionary with words as keys and counts as values
    """
    count = {}
    
    # Use with statement for safe handling
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                # Remove punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '').replace('{', '').replace('}', '')
                word = word.replace('+', '').replace('*', '').replace('&', '').replace('%', '')
                word = word.replace('#', '').replace('@', '').replace('$', '').replace('^', '')
                word = word.replace('=', '').replace('|', '').replace('\\', '').replace('/', '')
                word = word.replace('<', '').replace('>', '').replace('~', '').replace('`', '')
                
                # Ignore case
                word = word.lower()
                
                # Only count alphabetic words
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
    
    return count


# Omg, i'm so excited to see this one run!


def outputAnalysis(count_dict, filename):
    """
    Outputs word analysis results to a new file in sorted order.
    
    count_dict - dictionary containing word counts
    filename - original filename to base output name on (string)
    """
    # Create output filename by replacing .txt with _analysis.txt
    if filename.endswith('.txt'):
        output_filename = filename.replace('.txt', '_analysis.txt')
    else:
        output_filename = filename + '_analysis.txt'
    
    # Sort the dictionary
    keys = list(count_dict.keys())
    keys.sort()
    
    #with statement to write analysis to file
    with open(output_filename, 'w', encoding='utf-8') as out:
        for word in keys:
            out.write(word + " " + str(count_dict[word]))
            out.write('\n')
    
    print(f"Word analysis saved to: {output_filename}")
    print(f"Total unique words found: {len(keys)}")
    print(f"Total word occurrences: {sum(count_dict.values())}")




# I hope this runs...


def main():
    """
    Function that coordinates the book analysis process.
    """
    print("Book Word Frequency Analyzer")
    print("=" * 40)
    print("This program counts word frequency in text files.")
    print("It removes punctuation and ignores case and numbers.")
    print()
    
    # Get filename from user
    filename = input("Enter the filename (including .txt extension): ")
    
    try:
        print(f"\nAnalyzing '{filename}'...")
        
        # Analyze the book and get word counts
        word_counts = analyzeBook(filename)
        
        if len(word_counts) == 0:
            print("No words found in the file!")
            return
        
        print(f"Analysis complete! Found {len(word_counts)} unique words.")
        
        # Output the analysis to a new file
        outputAnalysis(word_counts, filename)
        
        # Show some interesting statistics   (I'm in a fucking book club for archaic books on statistics: interesting is literal. I LOVE this.)
        print("\nTop 10 most frequent words:")
        print("-" * 30)
        
        # Sort by count (descending) for top words display.
        sorted_by_count = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        for i, (word, count) in enumerate(sorted_by_count[:10]):
            print(f"{i+1:2d}. {word:<15} ({count} times)")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        print("Make sure the file exists in the same folder as this script.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


# ...testing

# shit... It's just the, and, i, a, of, to, in, was, my, her.
# Ugh. If I get time I'll go back and elimate more words. "the" 1415, not particularly interesting.