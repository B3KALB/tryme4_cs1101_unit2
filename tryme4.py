def new_line():

    print('.')

def three_lines():

    new_line()

    new_line()

    new_line()

def nine_lines():

    three_lines()

    three_lines()

    three_lines()

def clear_screen():

    new_line()
    
    three_lines()
    
    nine_lines()

print("Printing nine lines"), nine_lines(), print("Calling clearScreen()"), clear_screen()
