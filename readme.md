# Book Nook Inventory System - version 2!
The Book Nook code-base needs some updates and you are up for the challenge! You are given starter code and need to incorporate a dictionary:

1. First, take 3 minutes to become familiar with the given code. Take note of the dictionary of books and the conditional statements.
2. Update each conditional statement to incorporate dictionary methods:
    * add
    * remove
    * show
    * author search
    * title search
    * Make sure to only print books if the author exists in the dictionary
    
There are extra challenges at the bottom.

### Sample Runs
```
Welcome to...
      ______ ______
    _/      Y      \_
   // ~Book | ~~ ~  \
  // ~ ~ ~~ |  Nook~ \
 //________.|.________\
`----------`-'----------' version 3!


----------- Menu ----------
Add book (add)
Remove book (remove)
Show inventory (show)
Search for an author (author)
Search for a title (title)
Quit (q)

What would you like to do? add
What book would you like to add?
Title: To Kill a Mockingbird
Author: Harper Lee
To Kill a Mockingbird was added successfully.
```
```
What would you like to do? remove
What title would you like to remove? fsdfds
Error: fsdfds not in inventory.
```
```
What would you like to do? author
Which author would you like to seach for? Stephenie Meyer
All books by Stephenie Meyer:
   1. New Moon
   2. Twilight

----------- Menu ----------
Add book (add)
Remove book (remove)
Show inventory (show)
Search for an author (author)
Search for a title (title)
Quit (q)

What would you like to do? show
There are 4 books in your inventory.
   1. New Moon by Stephenie Meyer
   2. Twilight by Stephenie Meyer
   3. The Hunger Games by Suzanne Collins
   4. Batman: Court of Owls by Scott Snyder
```

## Extra Challenge
* add: if the book is already in the dictionary, don't add it.
* remove: if the book isn't found, let the user know.
* Allow the title search feature to include any book containing the searched word(s).
### Extra Challenge Sample Run
```
Which title would you like to search for? batman

There are 3 book(s) found containing batman:
   Batman: Court of Owls by Scott Snyder
   Batman: Zero Year by Scott Snyder
   Superman/Batman by Jeph Loeb
```

