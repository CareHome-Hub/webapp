from .graphdb import gdb
from logzero import logger

test_engagements = [
  {
    "name": "BA+IM",
    "ref": "eng_lvl_00001"
  },
  {
    "name": "FM",
    "ref": "eng_lvl_00002"
  },

  {
    "name": "Res",
    "ref": "eng_lvl_00003"
  },

  {
    "name": "U+L",
    "ref": "eng_lvl_00004"
  }
]


def get_test_engagements():
    return test_engagements


def get_engagements():
    logger.info("CALL /tet/v1/engagements - APPLES")
    graph = gdb.get_db()
    data = graph.data(
      "MATCH(e: ENGAGEMENT) RETURN e.name as name, e.ref as ref"
    )

    for elem in data:
        print("Element : {}".format(elem))
    return data

