def ui_controller():
    print('1. Right-angled Triangle')
    print('2. Square with Hollow Center')
    print('3. Diamond')
    print('4. Left-angled Triangle')
    print('5. Hollow Square')

    user_choice = int(input('Choose your pattern: '))
    user_size = int(input('Choose your size: '))

    return user_choice, user_size


pattern_choice, size = ui_controller()
print("Pattern choice:", pattern_choice)
print("Size:", size)


def solver(choice, usr_size):
    while True:
        match choice:
            case 1:
                for i in range(1, usr_size + 1):
                    print('*' * i)
            case 2:
                for i in range(usr_size):
                    for j in range(usr_size):
                        if i == 0 or i == usr_size - 1 or j == 0 or j == usr_size - 1:
                            print("*", end="")
                        else:
                            print(" ", end="")
                    print()
            case 3:
                for i in range(1, usr_size + 1, 2):
                    print(" " * ((usr_size - i) // 2) + "*" * i + " " * ((usr_size - i) // 2))
                for i in range(usr_size - 2, 0, -2):
                    print(" " * ((usr_size - i) // 2) + "*" * i + " " * ((usr_size - i) // 2))

            case 4:
                pass
            case 5:
                pass
        break


solver(pattern_choice, size)
