from bottle import Bottle
import psycopg2

"""
the ip addr of the server is https://34.110.169.110/

two endpoints are /compare/<packname>/v1/v2 and /view/<package>/version
"""

app = Bottle()

@app.route('/')
def index():
    return 'DEMO PackMan'

@app.route('/list-all')
def list_all():
    # 
    return 'Not Implemented'

    return packages

@app.route('/view/<package>/<version>')
def view_deps(package, version):
    conn = psycopg2.connect("dbname=deps user=postgres password=b9TsWez5Fq host=my-release-postgresql.default.svc.cluster.local")
    cur = conn.cursor()
    cur.execute("select dep, depver from packdeps where pkg = '{}' and pkgver = {};".format(package, version))
    deps = cur.fetchall()

    res = {}

    for i in deps:
        res[i[0]] = i[1]

    cur.close()
    conn.close()

    return res

@app.route('/compare/<package>/<v1>/<v2>')
def compare(package, v1, v2):
    deps_v1 = {}
    deps_v2 = {}

    conn = psycopg2.connect("dbname=deps user=postgres password=b9TsWez5Fq host=my-release-postgresql.default.svc.cluster.local")
    cur = conn.cursor()
    cur.execute("select dep, depver from packdeps where pkg = '{}' and pkgver = {};".format(package, v1))
    deps = cur.fetchall()

    res = {}

    for i in deps:
        res[i[0]] = i[1]
    deps_v1 = res

    #conn = psycopg2.connect("dbname=deps user=postgres password=b9TsWez5Fq host=my-release-postgresql.default.svc.cluster.local")
    #cur = conn.cursor()
    cur.execute("select dep, depver from packdeps where pkg = '{}' and pkgver = {};".format(package, v2))
    deps = cur.fetchall()

    res = {}

    for i in deps:
        res[i[0]] = i[1]
    cur.close()
    conn.close()

    return {'v1': deps_v1, 'v2': res}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000)
