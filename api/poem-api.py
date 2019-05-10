import flask
from flask import request, jsonify
import syllablize_helper
from main import *
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def home():
    return "[]"

@app.route('/api/poem-syllable/', methods=['GET'])
def api_syllable():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    poem_input = ""
    if 'poem' in request.args:
        poem_input = request.args['poem']
    else:
        return "Error: No poem field provided. Please specify an id."

    # Process poem input
    poem_lines = poem_input.split('/')

    results = syllablize_helper.syllablize(poem_lines)
    ret_val = {"data": results}

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(ret_val)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/api/puzzle/', methods=['GET'])
def temp_puzzle_api():
    results = [[0,1,2,10,11], [5,6,7,8,9], [3,4,12,13,14], [15,16,17,18,19], [20,21,22,23,24], [25,26,27,28,29], [30,31,32,33,34], [35,36,37,38,39], [40,41,42,43,44], [45,46,47,48,49], [50,51,52,53,54], [55,56,57,58,59]]
    # number iteration, poem size (syl), number ominoe sizes, sizes (new item for each), unique bools
    # pass list of words, each word is sub-list separated by syllable (2nd param)
    # pass list of syllables (3rd param)

    if 'syllable_poem' in request.args:
        syllable_poem = request.args['syllable_poem']
    else:
        return "Error"

    word_list = syllable_poem.split(",")

    poem_list = []
    syllable_list = []

    for word in word_list:
        word_syls = word.split()
        poem_list.append(word_syls)
        for syllable in word_syls:
            syllable_list.append(syllable)

    if 'num_tilings' in request.args:
        num_tilings = request.args['num_tilings']
    else:
        return "Error"

    if 'poem_size' in request.args:
        poem_size = request.args['poem_size']
    else:
        return "Error"

    if 'num_ominoe_sizes' in request.args:
        num_ominoe_sizes = request.args['num_ominoe_sizes']
    else:
        return "Error"

    if 'ominoe_sizes' in request.args:
        ominoe_sizes = request.args['ominoe_sizes']
    else:
        return "Error"
    ominoe_sizes = ominoe_sizes.split(",")

    if 'unq_ominoes' in request.args:
        unq_ominoes = request.args['unq_ominoes']
    else:
        return "Error"
    unq_ominoes = unq_ominoes.split(",")

    input_list = [int(num_tilings), int(poem_size), int(num_ominoe_sizes)]
    for item in ominoe_sizes:
        input_list.append(int(item))
    for item in unq_ominoes:
        input_list.append(int(item))

    results = main(input_list, poem_list, syllable_list)
    #results = [[0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14], [15,16,17,18,19], [20,21,22,23,24], [25,26,27,28,29], [30,31,32,33,34], [35,36,37,38,39], [40,41,42,43,44], [45,46,47,48,49], [50,51,52,53,54], [55,56,57,58,59]]
    ret_val = {"data": results}
    return jsonify(ret_val)

app.run()
