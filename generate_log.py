from datetime import datetime

def generate_log(data):
    """
    Generates a log file from a list of entries.
    
    Args:
        data (list): A list of strings representing log entries.
        
    Returns:
        str: The filename of the generated log file.
        
    Raises:
        ValueError: If data is not a list.
    """
    
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # STEP 2: Generate the filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation message
    print(f"Log successfully written to {filename}")

    # STEP 5: Return filename (needed for tests)
    return filename


# Only run this block if the file is executed directly
if __name__ == "__main__":
    logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(logs)