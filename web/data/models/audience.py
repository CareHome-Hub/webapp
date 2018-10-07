from .graphdb import gdb
from logzero import logger

test_audience = [
]


def get_test_audience():
    return test_audience


def get_audience():
    logger.info("CALL /tet/v1/audience")
    graph = gdb.get_db()
    data = graph.data(
      "MATCH(a: AUDIENCE) RETURN a.twitter, a.ref, a.gender, a.phone, a.age_group, a.income_lvl,\
       a.postcode_lvl, a.psyc_lvl, a.edu_lvl, a.email, a.behav_lvl"
    )

    # for elem in data:
    #     print("Element : {}".format(elem))
    return data



