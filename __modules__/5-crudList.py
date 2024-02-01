class ListManipulator:
    def __init__(self):
        self.my_list = []

    def add_element(self, my_list, element):
        my_list.append(element)
        print(f"Added {element} to the list. Current list: {my_list}")

    def remove_element(self, my_list, element):
        if element in my_list:
            my_list.remove(element)
            print(f"Removed {element} from the list. Current list: {my_list}")
        else:
            print(f"{element} not found in the list.")


