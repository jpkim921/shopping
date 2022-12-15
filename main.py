from flask import Flask, request, render_template
from target_grocery import Target
from wholefoods import Wholefoods
from cvs_grocery import Cvs

import pprint
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        
        target_results = []
        wf_results = []

        search_keyword = request.form['searchtext']
        target = Target()
        wf = Wholefoods()
        cvs = Cvs()

        # NOTE: need to add in 0 search/wrong search condition
        
        dev_mode = False
        try:
            if dev_mode:
                target_results = target.mock_search(search_keyword)
                wf_results = wf.mock_search(search_keyword)
                cvs_results = cvs.mock_search(search_keyword)
            else:
                target_results = target.get_search(search_keyword)
                wf_results = wf.get_search(search_keyword)
                cvs_results = cvs.get_search(search_keyword)
        except Exception as e:
            print(f"Error: {e}")

        context = {
            "target": target_results,
            "wholefoods": wf_results,
            "cvs": cvs_results
        }

        print(context['cvs'])
        return render_template('results.html', context=context)
    else:
        return render_template('index.html', context={})