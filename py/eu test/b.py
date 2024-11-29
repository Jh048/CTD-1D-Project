import sys
import os

# Add the parent folder (CTD 1D CODE) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from timer import timer  # Import your custom timer module


def start_or_archive():
    start_or_archive_choice = input('Do you want to start a timer? (Y/N) ').upper()
    
    if start_or_archive_choice == 'Y':
        title = input("YES was entered. What are we doing today? ")
        print(f"Starting the timer for: {title}")
        timer()  # Start the timer after getting the title
    
    elif start_or_archive_choice == 'N':
        archive_choice = input('Do you want to look at your history? (Y/N) ').upper()
        if archive_choice == 'Y':
            print('Loading History..........')
            # History function to be implemented
        else:
            print('Bye! Have a great day!')
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        start_or_archive()  # Restart the function to prompt the user again

# Call the function
# Main entry point
if __name__ == "__main__":
    start_or_archive()
