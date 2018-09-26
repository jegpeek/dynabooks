import jinja2


def render_parameterized_notebook(templatefn, outfn, params):
    with open(templatefn) as f:
        templ = jinja2.Template(f.read())

    result = templ.render(**params)
    with open(outfn, 'w') as f:
            f.write(result)

eriks_magic = render_parameterized_notebook
