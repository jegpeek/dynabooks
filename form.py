import flask
from flask import Flask, request

# App config.
#form = Flask('formapp', static_url_path='')
DEBUG = True
app = Flask(__name__, static_url_path='')

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route('/notebook_magic')
def notebook_magic():
    #target = request.args.get('target', default=None, type=str)
    import book_maker

    cleaned_dict = {}
    for k, v in request.args.items():
        cleaned_dict[k] = v

    outnbfn = book_maker.make_notebook_from_params(cleaned_dict)
    assert book_maker.generate_html_from_notebook() == 0

    nb_html = '<a href="{}">notebook</a>'.format(outnbfn)
    index_html = '<a href="output_html/html/index.html">html index</a>'

    return nb_html + '<br>' + index_html


if __name__ == "__main__":
    app.debug = True
    app.run()
