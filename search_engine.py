from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Day 1: Text Processing ---
def clean_query(user_input):
    return user_input.strip().lower()

# --- Day 2: Master Index Database & Generator ---
mock_database = {
    "file1.txt": "Python is an amazing programming language for backend development",
    "file2.txt": "Google search engines use high performance memory caching tools",
    "file3.txt": "Data structures and algorithms are crucial for coding interviews"
}

def build_index(database):
    inverted_index = {}
    for file_name, file_text in database.items():
        words = file_text.split()
        for word in words:
            clean_word = clean_query(word)
            if clean_word not in inverted_index:
                inverted_index[clean_word] = []
            if file_name not in inverted_index[clean_word]:
                inverted_index[clean_word].append(file_name)
    return inverted_index

# Build global index out of database records
master_index = build_index(mock_database)

# --- Day 3: Speed Cache System ($O(1)$) ---
search_cache = {}

def fast_search(keyword, index_database):
    clean_keyword = clean_query(keyword)
    if clean_keyword in search_cache:
        return {"status": "CACHE HIT", "results": search_cache[clean_keyword]}
    
    results = index_database.get(clean_keyword, [])
    search_cache[clean_keyword] = results
    return {"status": "CACHE MISS", "results": results}
@app.route('/')
def home():
    from flask import render_template
    return render_template('index.html')
# --- Day 4: Web API Routing ---
@app.route('/search', methods=['GET'])
def search_api():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Empty query parameter"}), 400
    
    response_data = fast_search(query, master_index)
    return jsonify(response_data)

if __name__ == "__main__":
    print("🚀 FlashCache API Server running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)