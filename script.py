def ui_controller():
    print('1. Right-angled Triangle')
    print('2. Square with Hollow Center')
    print('3. Diamond')
    print('4. Left-angled Triangle')
    print('5. Hollow Square')
    print('6. Pyramid')
    print('7. Exit')
    user_choice_input = int(input('Choose your option: '))
    if user_choice_input == 7:
        exit()
    user_size_input = int(input('Choose your size: '))
    return user_choice_input, user_size_input


pattern_choice, user_size = ui_controller()
print("Pattern choice:", pattern_choice)
print("Size:", user_size)


def pattern_solver(choice, size):
    while True:
        match choice:
            case 1:
                for i in range(1, size + 1):
                    print('*' * i)
            case 2:
                for i in range(size):
                    for j in range(size):
                        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                            print("*", end="")
                        else:
                            print(" ", end="")
                    print()
            case 3:
                for i in range(1, size + 1, 2):
                    print(" " * ((size - i) // 2) + "*" * i + " " * ((size - i) // 2))
                for i in range(size - 2, 0, -2):
                    print(" " * ((size - i) // 2) + "*" * i + " " * ((size - i) // 2))
            case 4:
                for i in range(size, 0, -1):
                    print('*' * i)
            case 5:
                for i in range(size):
                    if i == 0 or i == size - 1:
                        print("*" * size)
                    else:
                        print("*" + " " * (size - 2) + "*")
            case 6:
                for i in range(1, size + 1):
                    print(" " * (size - i), end="")
                    print("*" * (2 * i - 1))
        ui_controller()


pattern_solver(pattern_choice, user_size)
