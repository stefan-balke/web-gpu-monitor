"""
    Render static website based on the load data.
"""
import os
import jinja2
import pandas as pd


if __name__ == '__main__':
    PATH = os.path.dirname(os.path.abspath(__file__))
    PATH_OUTPUT = 'output'

    if not os.path.exists(PATH_OUTPUT):
        os.makedirs(PATH_OUTPUT)

    load_data = pd.read_csv('load_data.csv')
    load_data = load_data.groupby(by='hostname')
    context = {'hosts': load_data}

    # get jinja template
    template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(PATH, 'templates')))
    template = template_env.get_template('index.html')

    with open(os.path.join(PATH_OUTPUT, 'index.html'), 'wb') as f:
        html = template.render(context).encode('utf-8')
        f.write(html)
