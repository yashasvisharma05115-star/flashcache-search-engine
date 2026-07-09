def clean_query(user_input):
    """
    Takes a raw search input from a user, strips trailing/leading whitespaces,
    and normalizes it to lowercase to prevent database lookup failures.
    """
    cleaned = user_input.strip().lower()
    return cleaned


# --- Day 2: Master Index Generator ---

# Simulating mock files/documents in our system
mock_database = {
    "file1.txt": "Python is an amazing programming language for backend development",
    "file2.txt": "Google search engines use high performance memory caching tools",
    "file3.txt": "Data structures and algorithms are crucial for coding interviews"
}

def build_index(database):
    """
    Reads through all text files, cleans the text, and maps
    each unique word to the files it appears in.
    """
    inverted_index = {}
    
    for file_name, file_text in database.items():
        # Split the text into individual words
        words = file_text.split()
        
        for word in words:
            # Using our Day 1 clean_query function to normalize the word!
            clean_word = clean_query(word)
            
            # If the word isn't in our index card box yet, create an empty list
            if clean_word not in inverted_index:
                inverted_index[clean_word] = []
            
            # Append the file name if it's not already tracked for this word
            if file_name not in inverted_index[clean_word]:
                inverted_index[clean_word].append(file_name)
                
    return inverted_index


# Test both engines together
if __name__ == "__main__":
    print("--- FlashCache: Day 1 Testing ---")
    raw_input = "   PyThOn   "
    processed_input = clean_query(raw_input)
    print(f"Raw Input: '{raw_input}'")
    print(f"Cleaned Input for Engine: '{processed_input}'")
    
    print("\n--- FlashCache: Day 2 Testing ---")
    master_index = build_index(mock_database)
    
    # Test looking up a specific word instantly
    search_keyword = "python"
    matching_files = master_index.get(search_keyword, [])
    print(f"Searching index for keyword: '{search_keyword}'")
    print(f"Found in documents: {matching_files}")