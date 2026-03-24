import os

print("hello world  ,.welcome to the new class of python ")

# if 7 > 5:
#  print("7 is greater than 5")
#
#  if 5 < 7:
#      print("5 is less than 7")
#
#      # python variable
#      x = 90
#      y = "christian "
#
# print(x)
# print(y)
# print("hello have a good fun today", end="")
# print("hello dont forget to call me today ")
# print("hello edulink  international collegue")
# print("hello God bless me ")
# print("hello friend")
#
# print("=================print/ displaying numbers=============================================")
# x= 50
# y= 90
# z= 600
# t = 900
#
# print(x)
# print(y)
# print(z)
# print(t)
#
# sum = x + y + z + t
# product = x * y * z * t
# sub=  x - y - z - t
#
#
# print ("================================adding the numbers up=======================================")
# print("the total sum is " ,sum)
# print(y + x + z + t)
# print ("================================multiplying the numbers up=======================================")
# print ("the product of all the numbers is ", product)
# print(y * x * z * t)
# print ("================================dividing  the numbers up=======================================")
# print("the numbers when substracted is ", sub)
# print (y - x - z - t)
#
# print("i am thinking the ",sum, "is many  than" , sub, "but ", product,"is way higher that all of them")
#
#
# print ("================================PYTHON VARIABLES=======================================")
# b = 6
# a ="john"
# c = "mzungu"
# print(b)
# print(a)
# print(c)
# print ("================================PYTHON casting=======================================")
#
# bb = str(3)
# bc = int(3)
# ba = float(3)
# print(type(bb))
# print(type(bc))
# print(type(ba))
# print(bb)
# print(bc)
# print(ba)
#
# print ("================================GET THE TYPE =======================================")
# X = 5
# Y = "john"
# print(type(X))
# print(type(Y))
#
# print ("================================Assign Multiple values =======================================")
#
# x, y, t = "orange", "pine", "cherry"
# print(x)
# print(y)
# print(t)
# print(x,y,t)
#
# print ("================================Assign one value to  Multiple variable =======================================")
#
# x = y= z= t = r ="migori"
# print(X)
# print(y)
# print(z)
# print(t)
# print(r)
#
# print ("================================output variable =======================================")
#
# # printing numnbers in string s
# c = 67890
# y = "pintrest"
#
# print(c,y )
#
# print ("================================global  variable =======================================")
# # createv  avariable outside of a function and use it inside the function
#
# x = "awsome"


# def myfunc():
#     print("python is " + x)
#     myfunc()


def create_file(path, content):
    with open(path, "w") as f:
        f.write(content)
        print("file created")

    currentdirectory = os.getcwd()
    print (f"the current directory is: {currentdirectory}")
create_file("file1.txt", "hello world")