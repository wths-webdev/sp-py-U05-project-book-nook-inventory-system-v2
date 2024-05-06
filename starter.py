books = {
        "New Moon": "Stephenie Meyer",
        "Twilight": "Stephenie Meyer",
        "The Hunger Games" : "Suzanne Collins",
        "Batman: Court of Owls": "Scott Snyder",
        "Game Dev Using Python": "James R. Parker",
        "Batman: Zero Year": "Scott Snyder",
        "Superman/Batman": "Jeph Loeb",
        "The Great Gatsby": "F. Scott Fitzgerald"
    } 

# Welcome message
print("\nWelcome to...") 
print("\nWelcome to...\n"
    "      ______ ______\n"
    "    _/      Y      \\_\n"
    "   // ~Book | ~~ ~  \\\n"
    "  // ~ ~ ~~ |  Nook~ \\\n"
    " //________.|.________\\\n"
    "`----------`-'----------'\n")

while True:
    # Display menu to user
    print()
    print("----------- Menu ----------")
    print("Add book (add)")
    print("Remove book (remove)")
    print("Show inventory (show)")
    print("Search for an author (author)")
    print("Search for a title (title)")
    print("Quit (q)\n")
    user_selection = input("What would you like to do? ").lower()

    # Use conditional statements to call dictionary methods based on user input
    if user_selection == "add":
        print("What book would you like to add?")
        title = input("Title: ")
        author = input("Author: ")
        # add your code below

    elif user_selection == "remove":
        book = input("What title would you like to remove? ")
        # add your code below
    
    elif user_selection == "show":
        # add your code below

    elif user_selection == "author":
        author = input("Which author would you like to seach for? ")

        print(f"All books by {author}:")
        # add your code below

    elif user_selection == "title":
        title = input("Which title would you like to search for? ")
        # add your code below

    elif user_selection == "q":
        print("Bye bye!")
        break # out of the loop
    else:
        print("Error: That was not an option.\n")

print("")