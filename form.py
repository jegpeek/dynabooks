import flask
from flask import Flask, request, send_from_directory

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
    genres = book_maker.generate_html_from_notebook()


    nb_html = '<a href="{}">notebook</a>'.format(outnbfn)
    index_html = '<a href="output_html/html/index.html">html index</a>'

    return send_from_directory('output_hml', outnbfn)
    #if genres != 0:
    #    return "notebook available at {}, but html generation failed".format(nb_html)
    #else:
    #    return '{}<br>{}'.format(nb_html, index_html)


if __name__ == "__main__":
    app.debug = True
    app.run()
