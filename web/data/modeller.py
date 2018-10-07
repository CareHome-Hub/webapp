from logzero import logger

campaigns = [
  {
    "campaign": "Campaign1",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign_Totals": {
      "Actual_Goal": "785",
      "Conversion_Rate": 55.55,
      "Starting_Budget": 500.50,
      "Cost": 275.45,
      "Improvements_Cost": 150,
      "Success_Fee": 75.50,
      "Budget_Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign2",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint3",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign_Totals": {
      "Actual_Goal": "785",
      "Conversion_Rate": 55.55,
      "Starting_Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success_Fee": 75.50,
      "Budget_Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign3",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign_Totals": {
      "Actual_Goal": "785",
      "Conversion_Rate": 55.55,
      "Starting_Budget": 500.50,
      "Cost": 275.45,
      "Improvements_Cost": 150,
      "Success_Fee": 75.50,
      "Budget_Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign4",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign_Totals": {
      "Actual_Goal": "785",
      "Conversion_Rate": 55.55,
      "Starting_Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success_Fee": 75.50,
      "Budget_Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign5",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign_Totals": {
      "Actual_Goal": "785",
      "Conversion_Rate": 55.55,
      "Starting_Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success_Fee": 75.50,
      "Budget_Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign6",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign_Totals": {
      "Actual_Goal": "785",
      "Conversion_Rate": 55.55,
      "Starting_Budget": 500.50,
      "Cost": 275.45,
      "Improvements_Cost": 150,
      "Success_Fee": 75.50,
      "Budget_Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign7",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign_Totals": {
      "Actual_Goal": "785",
      "Conversion_Rate": 55.55,
      "Starting_Budget": 500.50,
      "Cost": 275.45,
      "Improvements_Cost": 150,
      "Success_Fee": 75.50,
      "Budget_Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign8",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign_Totals": {
      "Actual_Goal": "785",
      "Conversion_Rate": 55.55,
      "Starting_Budget": 500.50,
      "Cost": 275.45,
      "Improvements_Cost": 150,
      "Success_Fee": 75.50,
      "Budget_Rollover": 2.50
    }
  }
]


def get_camps():
    logger.info("Getting Camps")
    return campaigns


