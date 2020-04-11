# Initial variable to track game play
run = "y"

# Set start and last number
startnumber = 0

# While we are still playing...

while run == "y":
    
    endnumber = int(input ('How many numbers?'))
    for n in range(startnumber, endnumber + startnumber):
        print(n)
    
    startnumber = startnumber + endnumber
    run = input("Would you like to continue? [y/n]")

else:
    print ('All done')





    # Ask the user how many numbers to loop through


    # Loop through the numbers. (Be sure to cast the string into an integer.)


        # Print each number in the range


    # Set the next start number as the last number of the loop


    # Once complete... ask if the user wants to continue
