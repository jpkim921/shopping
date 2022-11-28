from flask import Flask, request, render_template
from target_grocery import Target
import pprint
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        search_keyword = request.form['searchtext']
        target = Target()
        # target_results = target.get_search(search_keyword)
        target_results = target.mock_search(search_keyword)

        # pp.pprint(target_results[0]['item'])
        # pp.pprint(target_results[0]['item']['product_description']['title'])

        context = {
            "target": target_results
        }

        # print("context")
        # print(context['target'])
        return render_template('results.html', context=context)
    else:
        return render_template('index.html', context={})