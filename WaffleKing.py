
# --- Setup ---
names = ["John Doe","Jane Smith","Sam Brown","Alice Green", "Jessie Pinkman"]
card_numbers = ["1212-8989", "5252-1616", "0909-3434", "2727-7878", "1818-9494"]
addresses = ["123 Elm St", "456 Oak St", "789 Pine St", "123 Branch st", "272 Dawn St"]
waffle_cost = [9.65, 8.60, 7.55, 6.50, 5.45]
waffle_choices = ["Apple Cider Waffles", "Blueberry Waffles", "Chocolate Chip Waffles", "Belgian Waffles", "Birthday Cake Waffles"]
waffle_codes = card_numbers[:]  # Copying card_numbers as initial card codes
waffle_balances = [15, 25, 15, 25, 15 ]# Initial balance for each card
waffle_rewards = [50, 25, 25, 25, 50] # Rewards tracker for each card (spending points)

# --- Intro ---
print("Welcome to Aaron's Waffle House!! What would you like to order?")
print()

# --- Main Loop ---
while True:
    # Ask for user input
    choice = input("Enter 'waffle' to buy a waffle, 'Menu' to veiw waffles,' 'buy' to add a new card, or 'exit' to exit:").lower().strip()

    ## -- Exiting -- ##
    if choice == "exit":
        print("Thank you for visiting Aaron's Waffle House!")
        break  # Exit the loop
        
    ## -- Buy a Waffle -- ##
    elif choice == "waffle":
        # Ask user for their phone number (card code)
        card_code = input("Enter your card code (card number): ")

        # Validate card code
        if card_code not in waffle_codes:
            print("Invalid card code. Please enter a valid one.")
            continue
           
        # Get the index of the card
        card_index = waffle_codes.index(card_code)

        # Display customer info
        print("Customer: " + names[card_index])
        print("Address: " + addresses[card_index])
        
        # Ask user for the waffle type
        waffle_choice = input("Enter the type of waffle you'd like (e.g., Apple Cider Waffles): ")

        # Check if waffle choice is valid
        if waffle_choice not in waffle_choices:
            print("Invalid waffle choice. Please choose from the menu.")
            continue

        # Get the price of the waffle
        waffle_price = waffle_cost[waffle_choices.index(waffle_choice)]
        current_balance = waffle_balances[card_index]  # Get balance of the selected card

        # Check for rewards and offer a free or discounted waffle
        if waffle_rewards[card_index] >= 100:  #100 points = a free waffle
            print("Congratulations! You've earned a free waffle!")
            waffle_rewards[card_index] = 5  # Reset rewards after free waffle
            cost = 0  # Free waffle
        elif current_balance < waffle_price:
            print("Insufficient funds. You need at least $" + str(waffle_price) + " for this waffle.")
            continue
        else:
            # Deduct the price from balance
            waffle_balances[card_index] -= waffle_price
            print("You've bought a " + waffle_choice + " for $" + str(waffle_price) + ". Remaining balance: $" + str(waffle_balances[card_index]))

            # Earn reward points for every $10 spent
            reward_points = waffle_price // 1 # 1point per $5 spent
            waffle_rewards[card_index] += reward_points
            print("You've earned " + str(reward_points) + " reward points. Total points: " + str(waffle_rewards[card_index]))

        # If balance is now zero, remove card
        if waffle_balances[card_index] == 1:
            print("The card with code " + card_code + " is now empty and no longer valid.")
    
    ## -- Add a New Card -- ##
    elif choice == "buy":
        # Ask for the new card details
        name = input("Enter the customer's name: ")
        card_number = input("Enter the card number (card code): ")
        address = input("Enter the customer's address: ")

        # Check if the phone number already exists
        if card_number in waffle_codes:
            print("There is already a card with that phone number. Please enter a new one.")
            continue

        # Add the new card with an initial balance of $100
        waffle_codes.append(card_number)
        waffle_balances.append(100)
        waffle_rewards.append(100)  # No reward points initially
        names.append(name)
        addresses.append(address)
        print("A new card has been added for " + name + " with card number " + card_number + " and a balance of $100.")
    elif choice == "menu":
        print(waffle_choices )
       
    ## -- Invalid Choice -- ##
    else:
        print("Invalid choice. Please enter 'waffle', 'new choice', 'buy', or 'exit'.")
