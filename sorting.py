# Python code to sort a word in order of frequency

# Take input string from user
string = input("Enter a string: ")

def most_frequent():

    # Create an empty dictionary
    freq_dict = {}

    # Count frequency of each character in the string
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Sort the dictionary by values in descending order
    sorted_dict = sorted(freq_dict.items(), key=get_frequency, reverse=True)

    # Print the letters in decreasing order of frequency
    for item in sorted_dict:
        print(item[0], item[1])

def get_frequency(item):
    return item[1]

x= most_frequent()