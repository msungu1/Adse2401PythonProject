#python file to demonstarte creating multiple threads to display numbers and letters
#import the  required module

import  threading

#function to display numbers (to be run in  a separate thread )
def print_numbers():
    for n in range(1, 11):
        print(f"from thread1: n = {n}")

        #function to display letters(to be run in another separate thread)
        def print_letters():
            for letter in "ABCDEFG":
                print(f"from thread2: {letter}")

                #create thread objects and start them
                thread1 = threading.Thread(target=print_numbers())
                thread2 = threading.Thread(target=print_letters)
