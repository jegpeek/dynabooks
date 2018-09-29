import os
import jinja2
import hashlib


def make_notebook_from_params(paramdct):
    templatefn = os.path.join('templates', paramdct.pop('template'))
    if not os.path.exists(templatefn):
        templatefn = templatefn + '.ipynb'

    with open(templatefn) as f:
        templ = jinja2.Template(f.read())

    result = templ.render(**paramdct)

    # determine the output file name as the sha1 hash of the template name + content of the file
    s = hashlib.sha1(templatefn.encode('utf-8'))
    s.update(result.encode('utf-8'))
    outfn = os.path.join('output_nbs', s.hexdigest() + '.ipynb')

    with open(outfn, 'w') as f:
        f.write(result)

    return outfn


def generate_html_from_notebook():
    return os.system('make html')
