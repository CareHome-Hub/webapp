from .graphdb import gdb
from logzero import logger

test_industry = [
  {
    "title": "Alternative dispute resolution",
    "ref": "tet_ind_0003"
  },
  {
    "title": "Automotive",
    "ref": "tet_ind_0009"
  },
  {
    "title": "Aviation",
    "ref": "tet_ind_0010"
  },
  {
    "title": "Chemicals",
    "ref": "tet_ind_0018"
  },
  {
    "title": "Maritime",
    "ref": "tet_ind_0080"
  },
  {
    "title": "Music",
    "ref": "tet_ind_0091"
  },
  {
    "title": "Pharmaceuticals",
    "ref": "tet_ind_0102"
  },
  {
    "title": "Utilities",
    "ref": "tet_ind_0135"
  }
]


def get_test_industry():
    return test_industry


def get_industry():
    logger.info("CALL /tet/v1/industry - APPLES")
    graph = gdb.get_db()
    data = graph.data(
      "MATCH(i: INDUSTRY) RETURN i.title as title, i.ref as ref"
    )

    # for elem in data:
    #     print("Element : {}".format(elem))
    return data

