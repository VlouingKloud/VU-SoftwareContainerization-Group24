import urllib3
from bottle import Bottle

app = Bottle()
http = urllib3.PoolManager()

def create_table(table_json):
    table = ""
    for row in table_json:
        table += f"<tr> <th> {str(row)} </th> <td> {table_json[str(row)]} </td> </tr>"
    return "<table style='width: 300px;'" + table + "</table>"

@app.route('/')
def index():
    return 'View the <a href="/view"> dependencies<a> of python390 or compare the <a href="/compare">differences</a> between python370 and python390'
    return 'View the <a href=>dependencies of package python 390<a href="https://34.110.169.110/compare/python/390/370">the differences</a>'


@app.route('/view/<programming_language>/<ver>')
def view(programming_language, ver):
    r = http.request('GET', f'http://34.110.169.110/view/{programming_language}/{ver}')
    a = r.data.decode()
    a = eval(a)
    return '<style>table, th, td {border: 1px solid black;}</style>' + f'{programming_language} {ver} requires ' + create_table(a)


@app.route('/compare/<programming_language>/<ver1>/<ver2>')
def compare(programming_language, ver1, ver2):
    r = http.request('GET', f'http://34.110.169.110/compare/{programming_language}/{ver1}/{ver2}')
    a = r.data.decode()
    a = eval(a)
    return '<style>table, th, td {border: 1px solid black;}</style>' + f'{programming_language} {ver1} requires ' + create_table(a['v1']) + f' <br> while {programming_language} {ver2} requires ' + create_table(a['v2'])


app.run(host='0.0.0.0', port = '10086')
