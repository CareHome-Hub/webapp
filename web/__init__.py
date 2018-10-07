import requests
from .data.models import campaigns, touchpoints, engagement, audience, target, industry
import logzero
from logzero import logger

from flask import Flask, render_template, jsonify, request
logzero.logfile("./rotating-logfile.log", maxBytes=1e6, backupCount=3)

app = Flask(__name__)


# @app.route("/news")
# def index():
#     return news.get_news_articles()

@app.route('/')
def hello_world():
    logger.info("root triggered")
    return jsonify({"status": 418, "error":"I'm a teapot"})


@app.route('/tet/v1/campaigns')
def get_campaign_listing():
    logger.info("CALL /tet/v1/campaigns")
    search = campaigns.get_campaigns()
    logger.info("campaigns.get_campaigns()")
    if 'campaign' in request.args:
        logger.info("campaign - request.args")
        result = []
        req = request.args.get('campaign')
        for camp in search:
            if req == camp['campaign']:
                result.append(camp)
    else:
        result = search

    resp = {}
    resp["status"] = 200
    resp["result"] = result
    return jsonify(resp)


@app.route('/tet/v1/touchpoints')
def get_touchpoint_listing():
    logger.info("/tet/v1/touchpoints")
    search = touchpoints.get_touchpoints()
    if 'touchpoint' in request.args:
        logger.info("touchpoint - request.args")
        result = []
        req = request.args.get('touchpoint')
        for tp in search:
            if req == tp['touchpoint']:
                result.append(tp)
    else:
        result = search

    resp = {}
    resp["status"]=200
    resp["result"]= result
    return jsonify(resp)


@app.route('/tet/v1/engagements')
def get_engagement_listing():
    logger.info("/tet/v1/engagements")
    search = engagement.get_engagements()
    # if 'touchpoint' in request.args:
    #     logger.info("touchpoint - request.args")
    #     result = []
    #     req = request.args.get('touchpoint')
    #     for tp in search:
    #         if req == tp['touchpoint']:
    #             result.append(tp)
    # else:
    result = search

    resp = {}
    resp["status"]=200
    resp["result"]= result
    return jsonify(resp)


@app.route('/tet/v1/industry')
def get_industry_listing():
    logger.info("/tet/v1/industry")
    search = industry.get_industry()
    # if 'touchpoint' in request.args:
    #     logger.info("touchpoint - request.args")
    #     result = []
    #     req = request.args.get('touchpoint')
    #     for tp in search:
    #         if req == tp['touchpoint']:
    #             result.append(tp)
    # else:
    result = search

    resp = {}
    resp["status"]=200
    resp["result"]= result
    return jsonify(resp)


@app.route('/tet/v1/audience')
def get_audience_listing():
    logger.info("/tet/v1/audience")
    search = audience.get_audience()
    # if 'touchpoint' in request.args:
    #     logger.info("touchpoint - request.args")
    #     result = []
    #     req = request.args.get('touchpoint')
    #     for tp in search:
    #         if req == tp['touchpoint']:
    #             result.append(tp)
    # else:
    result = search

    resp = {}
    resp["status"]=200
    resp["result"]= result
    return jsonify(resp)


@app.route('/tet/v1/targets')
def get_target_listing():
    logger.info("/tet/v1/target")
    search = target.get_targets()
    # if 'touchpoint' in request.args:
    #     logger.info("touchpoint - request.args")
    #     result = []
    #     req = request.args.get('touchpoint')
    #     for tp in search:
    #         if req == tp['touchpoint']:
    #             result.append(tp)
    # else:
    result = search

    resp = {}
    resp["status"]=200
    resp["result"]= result
    return jsonify(resp)
















@app.route('/health')
def hello():
    return jsonify({"status":"ok"})


@app.route('/welcome')
def welcome_page():
    return render_template("welcome.html")


@app.route('/campaigns')
def campaign_page():
    entries = campaigns.get_campaigns()
    return render_template('campaign.html', entries=entries)


@app.route('/touchpoints')
def touchpoint_page():
    entries = touchpoints.get_touchpoints()
    return render_template('touchpoint.html', entries=entries)