from py2neo import Graph, authenticate

authenticate("hobby-dpmaagjhhihbgbkedadklpbl.dbs.graphenedb.com:24786", "tet-bolt-user", "b.XTK8iWQGa4Q7.sKGYl271WtWWYeSX")
graph = Graph("bolt://hobby-dpmaagjhhihbgbkedadklpbl.dbs.graphenedb.com:24786",
              user="tet-bolt-user", password="b.XTK8iWQGa4Q7.sKGYl271WtWWYeSX",
              bolt=True, secure = True, http_port = 24789, https_port = 24780)


def get_db():
    return graph


x = get_db()
data = x.data("MATCH (a:CAMPAIGN) RETURN a.campaign")

for elem in data:
    print("Element : {}".format(elem))

