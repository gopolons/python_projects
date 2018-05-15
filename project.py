#so I've gotta start writing something
#how about a short game perhaps

inv = []
#inventory list - empty

def new_room_centre():
    print()
    print("""You find youself in a room that is dimly lit by a lamp that hangs from a ceiling. 
There is a table, toilet and a bookshelf in a room.""")
    print()
    player_move = input("Where do you want to go? ").lower()
    if player_move == "table" or player_move == "go to table":
        new_table_seq()
    elif player_move == "toilet" or player_move == "go to toilet":
        toilet_seq()
    elif player_move == "bookshelf" or player_move == "shelf" or player_move == "go to bookshelf" or player_move == "go to shelf":
        bookshelf_seq()
    elif player_move == "door" or player_move == "go to door":
        print()
        print("The door is locked.")
        room_centre()
    else:
        print()
        print("I don't know how to do that")
        new_room_centre()

def new_table_seq():
    print()
    player_move = input("You see an empty table. ").lower()
    if player_move == "table" or player_move == "look at the table" or player_move == "look at table":
        print()
        print("There is nothing here.")
        new_table_seq()
    elif player_move == "go back" or player_move == "back" or player_move == "b":
        new_room_centre()
    else:
        print("I don't know how to do that.")
        new_table_seq()

def letter_seq():
    print()
    player_move = input("Do you wish to take the letter? ").lower()
    if player_move == "yes" or player_move == "y":
        inv.append("letter")
        new_table_seq()
    elif player_move == "no" or player_move == "n":
        print()
        print("You leave the letter on the table")
        table_seq()
    else:
        print("I do not know how to do that")
        letter_seq()

def room_centre():
    print()
    print("""You find youself in a room that is dimly lit by a lamp that hangs from a ceiling. 
There is a table, toilet and a bookshelf in a room. There is a letter on a table.""")
    print()
    player_move = input("Where do you want to go? ").lower()
    if player_move == "table" or player_move == "go to table":
        table_seq()
    elif player_move == "toilet" or player_move == "go to toilet":
        toilet_seq()
    elif player_move == "bookshelf" or player_move == "shelf" or player_move == "go to bookshelf" or player_move == "go to shelf":
        bookshelf_seq()
    elif player_move == "door" or player_move == "go to door":
        print()
        print("The door is locked.")
        room_centre()
    else:
        print()
        print("I don't know how to do that")
        room_centre()
#start of the game sequence

def table_seq():
    print()
    player_move = input("You see a letter on the table... ").lower()
    if player_move == "letter" or player_move == "pick up the letter" or player_move == "take the letter" or player_move == "pick up letter" or player_move == "take letter" or player_move == "read the letter" or player_move == "read letter" or player_move == "read":
        print()
        print("""Welcome to the Dark Room! Your goal is to get out of here! 
Use commands to order your character what to do. Use hints in the room in order to get out of it! Good luck!""")
        letter_seq()
    elif player_move == "go back" or player_move == "back" or player_move == "b":
        room_centre()
    else:
        print("I don't know how to do that.")
        table_seq()
        
def toilet_seq():
    print("You see a toilet")

def bookshelf_seq():
    print()
    print("You see a bookshelf")

room_centre()