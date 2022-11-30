from flask import Flask, request, render_template
from target_grocery import Target
from wholefoods import Wholefoods
import pprint
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        search_keyword = request.form['searchtext']
        target = Target()
        wf = Wholefoods()
        # target_results = target.get_search(search_keyword)

        # NOTE: need to add in 0 search/wrong search condition

        target_results = target.mock_search(search_keyword)
        wf_results = wf.mock_search(search_keyword)

        context = {
            "target": target_results,
            "wholefoods": wf_results
        }

        return render_template('results.html', context=context)
    else:
        return render_template('index.html', context={})