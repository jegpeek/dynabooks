import os
import jinja2
import hashlib


def sha1(filename):
    s = hashlib.sha1()
    s.update(filename.encode('utf-8'))
    return s.hexdigest()


def render_parameterized_notebook(templatefn, outfn, params):
    with open(templatefn) as f:
        templ = jinja2.Template(f.read())

    result = templ.render(**params)
    with open(outfn, 'w') as f:
            f.write(result)


def make_notebook_from_params(paramdct):
    templatefn = os.path.join('templates', paramdct.pop('template'))
    if not os.path.exists(templatefn):
        templatefn = templatefn + '.ipynb'

    basename = os.path.splitext(os.path.split(templatefn)[1])[0]
    basename_sha1 = basename + sha1(str(paramdct))
    outnbfn = os.path.join('output_nbs', basename_sha1) + '.ipynb'

    if os.path.exists(outnbfn):
        os.unlink(outnbfn)
    render_parameterized_notebook(templatefn, outnbfn, paramdct)

    return outnbfn


def generate_html_from_notebook():
    return os.system('make html')
