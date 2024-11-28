# Initialize an empty dictionary
data_dict = {}

# Function to add a new list to the dictionary
def add_list_to_dict(new_list):
    # Generate a unique key(maybe we want to use the date and time as the list? idk)
    key = len(data_dict)  # Using the length of the dictionary as a simple key
    data_dict[key] = new_list
    return data_dict

# Example usage
new_list1 = [1, 2, 3]
new_list2 = ['a', 'b', 'c']

# Add new lists to the dictionary
add_list_to_dict(new_list1)
add_list_to_dict(new_list2)

print(data_dict)