import os
from flask import Flask, request, send_from_directory

# App config.
#form = Flask('formapp', static_url_path='')
DEBUG = True
app = Flask(__name__, static_url_path='')

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/_images/<path:path>")
def uimages(path):
    return send_from_directory('output_html/html/_images', path)

@app.route("/_static/<path:path>")
def ustatic(path):
    return send_from_directory('output_html/html/_static', path)

@app.route("/output_nbs/<path:path>")
def output_nbs(path):
    return send_from_directory('output_nbs', path)

@app.route('/notebook_magic')
def notebook_magic():
    #target = request.args.get('target', default=None, type=str)
    import book_maker

    cleaned_dict = {}
    for k, v in request.args.items():
        cleaned_dict[k] = v

    outnbfn = book_maker.make_notebook_from_params(cleaned_dict)
    outhtmlfn = outnbfn.replace('.ipynb', '.html')

    if os.path.exists(outhtmlfn):
        os.unlink(outhtmlfn)
    genres = book_maker.generate_html_from_notebook()

    if genres != 0:
        return 'nb generation failed!'

    return send_from_directory('output_html/html/', outhtmlfn)



    # nb_html = '<a href="{}">notebook</a>'.format(outnbfn)
    # index_html = '<a href="output_html/html/index.html">html index</a>'


    # return send_from_directory('output_hml', outnbfn)
    #if genres != 0:
    #    return "notebook available at {}, but html generation failed".format(nb_html)
    #else:
    #    return '{}<br>{}'.format(nb_html, index_html)


if __name__ == "__main__":
    app.debug = True
    app.run()
