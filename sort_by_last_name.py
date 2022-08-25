#A program to sort a list of names (ex. John Smith, Halle Berry) by last name alphabetical order
#Created with tremendous help from the example at https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-names-by-last-name/
#Program by Michael Cummings
#8.25.22

def sort_by_last_name(name_list): #Accepts a list of strings as an argument
    new_list = [] #Declaring and initializing an empty list
    
    for i in name_list: #Copying the contents of name_list to new_list, split() is used to produce a 2D array
        new_list.append(i.split()) #.split() method is called on i to split the names by spaces, "John Smith" becomes ["John", "Smith"]
    name_list = [] #Emptying the initial list passed as an argument? Wonder why
    
    #Next step: sorting by last name
    #This next line sorts the newly created 2D array new_list in alphabetical order, with the key being a lambda method that selects the last subindex for each index in the list
    for n in sorted(new_list, key=lambda x: x[-1]):
        name_list.append(' '.join(n)) #Repopulating the list we emptied earlier! Makes sense to me!
    
    return name_list

example_names = ["Bruce Wayne", "Selina Kyle", "Oswald Cobblepot", "Harvey Dent"]

print("\nList of names:", example_names)
print("\nSorted by last name: ", sort_by_last_name(example_names))