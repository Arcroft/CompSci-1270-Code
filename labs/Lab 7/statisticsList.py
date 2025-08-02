# Ashlyn Croft
# 16Jul25
# Lab 7
# Statistics list
# Basic descriptive statistics

# Its weird to have done pro-bono statistical consulting, and be citing a mean
# Like asking a contractor to cite what a shovel is

import random



def generateInput():
    """
    Generates a list of random integers for statistical analysis.
    """
    list_length = random.randint(200, 500)
    random_list = []
    for i in range(list_length):
        random_number = random.randint(1, 2000)
        random_list.append(random_number)
    
    return random_list

def findMean(data_list):
    """
    Calculates the statistical mean of a list of numbers.
    
    Statistical mean: "The arithmetic mean is the sum of all values divided 
    by the number of values in the dataset" (Moore, McCabe, & Craig, 
    Introduction to the Practice of Statistics, 8th ed.).
    """
    # Sum all values
    total = 0
    for number in data_list:
        total = total + number
    
    # Calculate mean
    mean_value = total / len(data_list)
    
    return mean_value




def findMedian(data_list):
    """
    Calculates the statistical median of a list of numbers.
    
    Statistical median: "The median is the middle value when the data 
    values are arranged in order from smallest to largest" (Moore, McCabe, 
    & Craig, Introduction to the Practice of Statistics, 8th ed.).
    """
    # Sort the list to find middle value(s)
    sorted_list = data_list.copy()
    sorted_list.sort()
    
    list_length = len(sorted_list)
    
    # Check if list length is odd or even
    if list_length % 2 == 1:
        middle_index = list_length // 2
        median_value = sorted_list[middle_index]
    else:
        middle_index1 = (list_length // 2) - 1
        middle_index2 = list_length // 2
        median_value = (sorted_list[middle_index1] + sorted_list[middle_index2]) / 2
    
    return median_value





def main():
    """
    Main function that generates random data and calculates descrptive statistics.
    """
    print("Random Data Statistical Analysis")
    print("=" * 40)
    print("Generating random dataset and calculating mean and median...")
    print()
    
    # random list of integers
    data = generateInput()
    
    print(f"Generated list with {len(data)} random numbers")
    print(f"Range: {min(data)} to {max(data)}")
    print()
    
    # mean and median
    mean = findMean(data)
    median = findMedian(data)
    

    print("Statistical Results:")
    print("-" * 25)
    print("Mean: {0} Median: {1}".format(mean, median))
    print()
    print("Additional Info:")
    print(f"Mean (rounded): {round(mean, 2)}")
    print(f"Median (rounded): {round(median, 2)}")
    print(f"Dataset size: {len(data)} values")

if __name__ == "__main__":
    main()