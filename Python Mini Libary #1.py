#Question

# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

# Plan

# Make a class named libary. It should have 4 functions
# display book
# lend book - (who owns the book if not present)
# add book
# return book
# Add book and make a list display books if asked and check the avibility of the book asked
# if anyone wants to add a book so take his/her name and name of book and if anyone lends a
# book so ask name of person, name of book and save the time at which book was witdrawed and
# make a .txt file to save that details. I anyone returns the book take name of person, book
# and save time for the same !!

# Program:
import time
class Libary:

    def __init__(self,Listofbooks, nameoflib):
        self.Listofbooks = Listofbooks
        self.nameoflib = nameoflib

    def displaybook(self):
        with open("books.txt") as op:
            for i in op:
                print(i, end="")
        print("Hope you like them !!, If you want to lend a book from our libary so you can hit y for yes and n for no do so !!")
        print("If You want to lend a book from our libary so kindly mention your name and book's name which you want to lend And hit y for yes and n for no")
        yn = input()
        if yn == "y":
            print("Pls Enter Your Name:")
            lendn = input()
            f = open("Info.txt", "r+")
            f.read()
            f.write("\nName of the person: ")
            f.write(lendn)
            print("Pls Enter Book's Name:")
            lendb = input()
            f = open("Info.txt", "r+")
            f.read()
            f.write("\nName of the book: ")
            f.write(lendb)

            localtime = time.asctime(time.localtime(time.time()))
            f = open("Info.txt", "r+")
            f.read()
            f.write("\nThe time at which the book was lend from the libary: \n")
            f.write(localtime)
            f.close()
            return (f"Your Name is {lendn} And the Book you have lend from us Is {lendb}")

        else:
            return ("Ok")

    def lend(self):
        print("If You want to lend a book from our libary so kindly mention your name and book's name which you want to lend And hit y for yes and n for no")
        yn = input()
        if yn=="y":
            print("Pls Enter Your Name:")
            lendn = input()
            f = open("Info.txt", "r+")
            f.read()
            f.write("\nName of the person: ")
            f.write(lendn)
            print("Pls Enter Book's Name:")
            lendb = input()
            f = open("Info.txt", "r+")
            f.read()
            f.write("\nName of the book: ")
            f.write(lendb)

            localtime = time.asctime(time.localtime(time.time()))
            f = open("Info.txt", "r+")
            f.read()
            f.write("\nThe time at which the book was lend from the libary: \n")
            f.write(localtime)
            f.close()
            return (f"Your Name is {lendn} And the Book you have lend from us Is {lendb}")

        else:
            return ("Ok")


    def addbook(self):
        print("If Your wish is is to add a book to our libary then first a fall we would like to Thank you for your contribution\n" \
              "Please Mention Your name:")
        addn = input()
        print("Please Mention Your Book's name:")
        addb = input()
        print(f"Confirmation Your Name is {addn} And the Book Name Is {addb}\n"
         f"If You want to proceed further then press y to confirm the order and n for cancelling it.")
        yorn = input()
        if yorn=="y":
            print("Your Info and book is saved to our libary\n")
            f = open("Bookadd.txt", "r+")
            f.read()
            f.write(f"\nRecently A Book Was Added to our libary. Name Of Book Is *{addb}*, And Name of the person who had added the book is {addn}")
            localtime = time.asctime(time.localtime(time.time()))
            f.write("\nThe time at which the book was lend from the libary: \n")
            f.write(localtime)

            return "Thank You !!"

        else:
           return ("Your Order was Cancelled !!")




    def retbook(self):
        print("Hope you have enjoyed reading our book, And you have come here to return them so we request you to mention you name and the book's name")
        print("Please Mention Your name:")
        rnam = input()
        print("Please Mention Your Book's name:")
        rbok = input()
        print(f"Confirmation Your Name is {rnam} And the Book Name Is {rbok}")
        print("Press y to confirm the return or Press n to cancel")
        yorc = input()

        if yorc=="y":
            print("Your Info and book is saved to our libary\n")
            f = open("bookret.txt", "r+")
            f.read()
            f.write(f"\nRecently A Book Was Returned to our libary. Name Of Book Is *{rbok}*, And Name of the person who had returned the book is {rnam}")

            localtime = time.asctime(time.localtime(time.time()))
            f.write("\nThe time at which the book was returned to the libary: \n")
            f.write(localtime)
            return "Thank You !!"

        else:
            return ("Your Return was Cancelled !!")


    def finduser(self):
        print("Please Enter the Name of the book:")
        d1 = {"Harry Potter and the Sorcerer's Stone":"Aryan", "Harry Potter and the Chamber of Secrets":"Sarvesh",
        "Harry Potter and the Prisoner of Azkaban":"Vedant",
        "Harry Potter and the Goblet of Fire":"Vidhan",
        "Harry Potter and the Order of the Phoenix":"Yash",
        "Harry Potter and the Half-Blood Prince":"Awadh",
        "Harry Potter and the Deathly Hallows":"Ashwad"}
        xyz = input()
        return (d1[xyz])




if __name__ == '__main__':
    Aryan_Libary = Libary("books.txt", "Aryan Libary")


    while(True):
        print(f"Welcome to the {Aryan_Libary.nameoflib} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            Aryan_Libary.displaybook()

        elif user_choice == 2:

            Aryan_Libary.lend()

        elif user_choice == 3:
            Aryan_Libary.addbook()

        elif user_choice == 4:
            Aryan_Libary.retbook()

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue

