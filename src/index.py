import random
from typing import List

my_list = []


def generate_new_id(id_list: List[int]) -> int:
    new_id = random.randint(100, 999)

    if not id_list:
        id_list.append(new_id)
        return new_id

    if new_id not in id_list:
        id_list.append(new_id)
        return new_id
    else:
        return generate_new_id(id_list)


while True:
    print("1 - Register a new password")
    print("2 - List passwords")
    print("3 - Get next password")
    print("4 - Exit")

    option = int(input("Choose one of the options above: "))

    if option == 1:
        print("Registering a new password")
        my_list.append(generate_new_id([]))

    elif option == 2:
        print(my_list)

    elif option == 3:
        if len(my_list) == 0:
            print("There are no passwords registered")
        else:
            print(f"Selected password: {my_list[0]}")
            my_list.pop(0)

    elif option == 4:
        break

    else:
        print("Invalid option")
