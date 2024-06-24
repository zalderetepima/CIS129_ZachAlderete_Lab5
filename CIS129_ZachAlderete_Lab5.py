# Name: Zach Alderete
# Date: 06/23/2024
# Lab 5 program determines weekely bottle collection and calculates total payout per user input. 

# Declare variables
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
nbr_of_days = 7
keep_going = "y"

# Declare loop
# Loop will continue or end based on user input.
while keep_going.lower() == "y":
    # Set initial total_bottles and counter for the week
    total_bottles = 0
    counter = 1

    # Count-controlled loop to collect bottles for 7 days
    # This while loop will run exactly 7 times, once for each day of the week.
    while counter <= nbr_of_days:
        today_bottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
        total_bottles += today_bottles
        counter += 1

    # Calculate the total payout
    payout_per_bottle = 0.10
    total_payout = total_bottles * payout_per_bottle

    # Display the total number of bottles collected and the total payout for the week.
    print(f"The total number of bottles collected is {total_bottles}")
    print(f"The total paid out is ${total_payout:.2f}")

    # Ask if the user wants to enter another week’s worth of data
    # Prompt the user to input 'y' to run the program again or 'n' to stop.
    keep_going = input("Do you want to enter another week’s worth of data? (Enter 'y' or 'n'): ")

print("End of program.")