# Import datetime so we can create filenames with today's date
from datetime import datetime


def generate_log(data):
    # STEP 1: Validate the input
    # The function should only accept a list
    if not isinstance(data, list):
        raise ValueError("Input must be a list of log entries.")

    # STEP 2: Create the filename using today's date
    # Example: log_20260305.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Open the file and write the log entries
    # "w" means write mode (creates file if it doesn't exist)
    with open(filename, "w") as file:

        # Loop through each entry in the list
        for entry in data:
            # Write the entry and move to the next line
            file.write(entry + "\n")

    # STEP 4: Print a confirmation message
    print(f"Log successfully written to {filename}")

    # STEP 5: IMPORTANT
    # Return the filename so tests can use it
    return filename


# This block only runs when the file is executed directly
# It will NOT run when pytest imports the function
if __name__ == "__main__":
    
    # Example log entries
    logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    # Call the function
    generate_log(logs)