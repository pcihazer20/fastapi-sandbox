

last_name = 'hernandez'

def test_data_types():
    x = 123
    my_string = 'hazor'
    siblings_list = ['Carina', 'Hugo']
    cousins_tuple = ('Yair','Bambi','Campa')
    cars_set = {"pontiac fierro","chevy celebrity","nissan altima"}
    my_prefs_dictionary = {
                           "favorite_color": "navy",
                           "favorite_drink": "arnold_palmer",
                           "favorite_vacation" : "hawaii"}


    print(my_string)
    print(x)
    print(siblings_list)
    print(cousins_tuple)
    print(my_prefs_dictionary)
    print(cars_set)



def test_conditionals()->None:
    is_correct = 1 == 2
    if(is_correct == 1):
        print("is_correct")
    else:
        print("is_correct")





def say_hello(name: str)-> str:
    return f"Hello {name}"

#a single line test comment

"""
This is a test multi-line comment
"""

if __name__ == '__main__':
    print("Hello World")
    print(say_hello("rafa"))
    test_data_types()
