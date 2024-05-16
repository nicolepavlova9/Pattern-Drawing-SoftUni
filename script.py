def ui_controller():
    print('1. Right-angled Triangle')
    print('2. Square with Hollow Center')
    print('3. Diamond')
    print('4. Left-angled Triangle')
    print('5. Hollow Square')
    print('6. Pyramid')
    print('7. Cancel')
    user_choice_input = int(input('Choose your option: '))
    if user_choice_input == 7:
        exit()
    if user_choice_input < 1 or user_choice_input > 7:
        is_choice_valid = False
        while is_choice_valid is False:
            user_choice_input = int(input('Please make a valid choice: '))
            if 1 <= user_choice_input <= 7:
                is_choice_valid = True
    user_size_input = int(input('Choose your size: '))
    if user_size_input < 1:
        is_size_valid = False
        while not is_size_valid:
            user_size_input = int(input('Please enter a valid size: '))
            if user_size_input >= 1:
                is_size_valid = True
    return user_choice_input, user_size_input


pattern_choice, user_size = ui_controller()


def pattern_solver(choice, size):
    print('-------------------------')
    print()
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
    print()
    print('-------------------------')


pattern_solver(pattern_choice, user_size)
