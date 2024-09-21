import time
import random
import webbrowser
import os

# Set the percent chance (you can modify this value)
percentchance = 80  # Example: 50% chance

# Wait for 5 minutes (300 seconds)
time.sleep(300)

# Generate a random number between 0 and 100
random_number = random.randint(0, 100)

# Compare the random number with percentchance
if random_number <= percentchance:
    # Get the script directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Path to the randomquestions.txt file
    file_path = os.path.join(script_dir, 'randomquestions.txt')

    # Read the file and get non-empty lines
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]

        # Check if there are any lines to select from
        if lines:
            # Choose a random line
            selected_url = random.choice(lines)

            # Open the URL in the default web browser
            webbrowser.open(selected_url)
        else:
            print("No valid lines in the randomquestions.txt file.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
else:
    print("Random number is greater than percentchance. Script will now end.")
