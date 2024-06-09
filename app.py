from flask import Flask, render_template, request, jsonify
from algorithms.algorithms import bubble_sort, quick_sort, binary_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualize', methods=['POST'])
def visualize():
    algorithm = request.form['algorithm']
    data = request.form['data']
    data_list = list(map(int, data.split(',')))

    if algorithm == 'bubble_sort':
        steps = bubble_sort(data_list)
    elif algorithm == 'quick_sort':
        steps = quick_sort(data_list)
    elif algorithm == 'binary_search':
        target = int(request.form['target'])
        steps = binary_search(data_list, target)
    else:
        steps = []

    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)
