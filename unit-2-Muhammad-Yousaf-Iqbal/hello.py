"""
program for hello.py that has two functions.
program made by yousaf.
"""
"""
function for hello_world that prints hello world.
"""
def hello_world():
    #print a message that says hello world.
    print('Hello, World!')
"""
function for hello_you that uses name as an input from user that prints hello name.
"""
def hello_you():
    #name is set as input from user
    name = input("Enter your name: ")
    #print a message that uses name input and says hello name
    print("Hello,",name,"!")
"""
function for main/program to run/execute.
"""
def main():
    #run/execute hello_world function
    hello_world()
    #run/execute hello_you function
    hello_you()
#run/execute main function
main()