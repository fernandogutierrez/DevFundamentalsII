from flask import Flask
from flask import jsonify
from flask import request

books = [
    {
        'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '1992'
    },
    {
        'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
        'published': '1973'
    },
    {
        'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'
    }
]

app = Flask(__name__)

API_NAME = "/api/v1"


@app.route(f"{API_NAME}/books/<book_id>", methods=["GET"])
def get_book(book_id):
    #return jsonify(books[int(book_id)])
    book_to_return = {}
    for book in books:
        if book.get("id") == int(book_id):
            book_to_return = book
            break
    return jsonify(book_to_return)




@app.route(f"{API_NAME}/books", methods=["GET"])
def list_books():
    return jsonify(books)


@app.route("/", methods=["GET"])
def hello():
    return "hello World!"


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(err=str(e)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000, use_reloader=True)
