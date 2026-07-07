def clean_query(user_input):
    """
    Takes a raw search input from a user, strips trailing/leading whitespaces,
    and normalizes it to lowercase to prevent database lookup failures.
    """
    # Using the exact string methods from Chapter 2!
    cleaned = user_input.strip().lower()
    return cleaned

# Test our cleaner engine
if __name__ == "__main__":
    print("--- FlashCache: Day 1 Testing ---")
    
    # Simulating a messy user input typing with trailing spaces and mixed casing
    raw_input = "   PyThOn   "
    processed_input = clean_query(raw_input)
    
    # Using an f-string to print the clean results clearly
    print(f"Raw Input: '{raw_input}'")
    print(f"Cleaned Input for Engine: '{processed_input}'")