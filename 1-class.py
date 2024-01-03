import __modules__.crudList as crudList
# from crudList import ListManipulator

# def add_element(list,element):
#     l.append(element)
#     print(f"Add {element}.  list: {list}")

# def remove_element(list, element):
#     if element in list:
#         list.remove(element)
#         print(f"Remove {element}   . list: {list}")
#     else:
#         print(f"{element} pas dans list.")

# l = ['a','b']
# add_element(l, "added_corossol")
# remove_element(l, "added_corossol")



my_list = ['a', 'b']

# Create an instance of ListManipulator
list_manipulator = crudList.ListManipulator()

# Example usage
list_manipulator.add_element(my_list, "added_corossol")
list_manipulator.remove_element(my_list, "added_corossol")