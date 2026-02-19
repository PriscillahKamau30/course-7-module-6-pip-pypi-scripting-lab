from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        print("Error: Input must be a list of log entries.")
        return

    # STEP 2: Generate a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation
    print(f"Log successfully written to {filename}")


# Example usage
if __name__ == "__main__":
    # Example log entries
    log_entries = ["User logged in", "User updated profile", "Report exported"]
    
    # Call the function
    generate_log(log_entries)
