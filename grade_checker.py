# this script will ask user to input a number from 0 - 100 
# and will return the corresponding letter grade
try: # try tells python to run the code and if it fails, it will run the except code
    number = int(input("Enter a number from 0 to 100: ")) # ask user to input a number from 0 to 100

    if number >= 90:
        print("Your grade is A")
        print("Congratulations! Great job!")
    elif number >= 80:
        print("Your grade is B")
        print("Keep up the good work!")
    elif number >= 70:
        print("Your grade is C")
        print("You can do better!")
    elif number >= 60:
        print("Your grade is D")
        print("You need to improve!")
    else:
        print("Your grade is F")
        print("You need to try harder!")

except ValueError:
    # Runs if the user types a letter or symbol instead of a number
    print("Invalid input! Please enter a number, not letters.")
    