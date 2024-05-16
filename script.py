# TODO - UI

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
