from .graphdb import gdb
from logzero import logger

test_targets = [
  {
    "name": "Market Share",
    "ref": "tet_trg_0001"
  },
  {
    "name": "Promotion",
    "ref": "tet_trg_0002"
  },

  {
    "name": "Increased Sales",
    "ref": "tet_trg_0003"
  },

  {
    "name": "Brand Awareness",
    "ref": "tet_trg_0004"
  }
]


def get_test_targets():
    return test_targets


def get_targets():
    logger.info("CALL /tet/v1/targets - APPLES")
    graph = gdb.get_db()
    data = graph.data(
      "MATCH(t: TARGET) RETURN t.title as title, t.ref as ref"
    )

    # for elem in data:
    #     print("Element : {}".format(elem))
    return data

