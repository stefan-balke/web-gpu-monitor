"""
    Render static website based on the load data.
"""
import os
import time
import jinja2
import pandas as pd


if __name__ == '__main__':
    PATH = os.path.dirname(os.path.abspath(__file__))
    PATH_OUTPUT = 'output'
    PATH_DATA = 'load_data.csv'

    if not os.path.exists(PATH_OUTPUT):
        os.makedirs(PATH_OUTPUT)

    load_data = pd.read_csv(PATH_DATA)
    load_data['username'] = load_data['username'].fillna(-1)
    load_data = load_data.groupby(by='hostname')
    modification_time = time.ctime(os.path.getmtime('load_data.csv'))
    context = {'hosts': load_data, 'modification_time': modification_time}

    # get jinja template
    template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(PATH, 'templates')))
    template = template_env.get_template('index.html')

    with open(os.path.join(PATH_OUTPUT, 'index.html'), 'wb') as f:
        html = template.render(context).encode('utf-8')
        f.write(html)
