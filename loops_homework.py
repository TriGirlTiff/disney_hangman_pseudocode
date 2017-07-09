books = ["Dune", "Pride and Prejudice"]



# Welcome message

print "Brighticorn's Books"
print "-------------------"
print

use_library = True
while use_library:
    
    print "You can add/ view/ check/ exit"
    print "There are {} books in list.".format(len(books))
    print "******************************"
    command = raw_input("What action do you want to take? ")
    command = command.lower()
    print "Action: ", command
    print "*******************"
    if command == "exit":
        print "Goodbye!"
        use_library = False
    elif command == "add":
        print "Add Book"
        new_book = raw_input("What is the title of the new book? ")
        if new_book in books:
            print "Book is already in list."
        else:
            books.append(new_book)
            print "Added: ", new_book

    elif command == "view":
        print "View Books"        
        for book in books:
            print book
        print "End of list"

    elif command == "check":
        print "Checks for a Book"

        to_check = raw_input("What book do you want to check for? ")

        if to_check in books:
            print "Found: ", to_check
        else:
            print "Book not found."

    else:
        print "Sorry, that's not an option."