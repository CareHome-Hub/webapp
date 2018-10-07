from .graphdb import gdb
from logzero import logger

test_touchpoints = [
  {
    "touchpoint": "Touchpoint1",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers_cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint2",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers_cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint3",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers_cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint4",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers_cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint5",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers_cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint6",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers_cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint7",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers_cost": 25.00,
    "sellers_cost_updates": 2.50
  }
]


def get_test_touchpoints():
    return test_touchpoints


def get_touchpoints():
    logger.info("CALL /tet/v1/touchpoints - APPLES")
    graph = gdb.get_db()
    data = graph.data(
      "MATCH(t: TOUCHPOINT) RETURN t.AvgCost as AvgCost, t.AvgReview as AvgReview, t.SCORE as SCORE, t.ref as ref, t.title as title, t.touchpoint as touchpoint, t.type as type"
    )

    for elem in data:
        print("Element : {}".format(elem))
    return data

