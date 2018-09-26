import os
import jinja2


def render_parameterized_notebook(templatefn, outfn, params):
    with open(templatefn) as f:
        templ = jinja2.Template(f.read())

    result = templ.render(**params)
    with open(outfn, 'w') as f:
            f.write(result)


def make_notebook_from_params(paramdct):
    templatefn = paramdct.pop('template')
    if not os.path.exists(templatefn):
        templatefn = templatefn + '.ipynb'

    basename = os.path.splitext(os.path.split(templatefn)[1])[0]
    outnbfn = os.path.join('output_nbs', basename)

    render_parameterized_notebook(templatefn, outnbfn, paramdct)

    return outnbfn


def generate_html_from_notebook(nbfn):
    raise NotImplementedError
