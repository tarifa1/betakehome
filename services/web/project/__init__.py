import os
from json import load
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import create_engine
import pandas as pd


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
engine = create_engine(SQLALCHEMY_DATABASE_URI)


class Equipment(db.Model):
    __tablename__ = "equipment"

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(128), unique=False, nullable=False)
    fleet = db.Column(db.String(128), unique=False, nullable=False)
    equipment_id = db.Column(db.String(128), unique=False, nullable=False)
    equipment_status = db.Column(db.String(1), unique=False, nullable=False)
    date_added = db.Column(db.TIMESTAMP(), nullable=False)
    date_removed = db.Column(db.TIMESTAMP(), nullable=True)

    def __init__(self, id, customer, fleet, equipment_id,
                 equipment_status, date_added, date_removed):
        self.id = id
        self.customer = customer
        self.fleet = fleet
        self.equipment_id = equipment_id
        self.equipment_status = equipment_status
        self.date_added = date_added
        self.date_removed = date_removed


class Events(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.String(128), unique=False, nullable=False)
    sighting_date = db.Column(db.TIMESTAMP(),unique=False,nullable=False)
    sighting_event_code = db.Column(db.Integer,unique=False,nullable=False)
    reporting_railroad_scac = db.Column(db.String(128),unique=False,nullable=False)
    posting_date = db.Column(db.TIMESTAMP(),unique=False,nullable=False)
    from_mark_id = db.Column(db.String(128),unique=False,nullable=False)
    load_empty_status = db.Column(db.String(1), unique=False, nullable=False)
    sighting_claim_code = db.Column(db.String(1), unique=False, nullable=False)
    sighting_event_code_text = db.Column(db.String(128), unique=False, nullable=False)
    train_id = db.Column(db.String(128), unique=False, nullable=True)
    train_alpha_code = db.Column(db.String(128), unique=False, nullable=False)
    location_id = db.Column(db.Integer,unique=False,nullable=False)
    waybill_id = db.Column(db.Integer,unique=False,nullable=False)

    def __init__(self, id, equipment_id, sighting_date, 
                 sighting_event_code, reporting_railroad_scac,
                 posting_date, from_mark_id, load_empty_status,
                 sighting_claim_code, sighting_event_code_text,
                 train_id, train_alpha_code, location_id, waybill_id):
        self.id = id
        self.equipment_id = equipment_id
        self.sighting_date = sighting_date
        self.sighting_event_code = sighting_event_code
        self.reporting_railroad_scac = reporting_railroad_scac
        self.posting_date = posting_date
        self.from_mark_id = from_mark_id
        self.load_empty_status = load_empty_status
        self.sighting_claim_code = sighting_claim_code
        self.sighting_event_code_text = sighting_event_code_text
        self.train_id = train_id
        self.train_alpha_code = train_alpha_code
        self.location_id = location_id
        self.waybill_id = waybill_id


class Locations(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(128), unique=False, nullable=False)
    city_long = db.Column(db.String(128), unique=False, nullable=False)
    station = db.Column(db.String(128), unique=False, nullable=False)
    fsac = db.Column(db.Integer,unique=False,nullable=False)
    scac = db.Column(db.String(128), unique=False, nullable=False)
    spic = db.Column(db.Integer,unique=False,nullable=False)
    state = db.Column(db.String(2), unique=False, nullable=False)
    time_zone = db.Column(db.String(2), unique=False, nullable=False)
    longitude = db.Column(db.Integer,unique=False,nullable=False)
    latitude = db.Column(db.Integer,unique=False,nullable=False)
    country = db.Column(db.String(2), unique=False, nullable=False)

    def __init__(self, id, city, city_long, station, fsac, scac, spic, state,
                 time_zone, longitude, latitude, country):
        self.id = id
        self.city = city
        self.city_long = city_long
        self.station = station
        self.fsac = fsac
        self.scac = scac
        self.spic = spic
        self.state = state
        self.time_zone = time_zone
        self.longitude = longitude
        self.latitude = latitude
        self.country = country


class Waybills(db.Model):
    __tablename__ = "waybills"

    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.String(128),unique=False, nullable=False)
    waybill_date = db.Column(db.TIMESTAMP(),unique=False,nullable=False)
    waybill_number = db.Column(db.Integer,unique=False,nullable=False)
    created_date = db.Column(db.TIMESTAMP(),unique=False,nullable=False)
    billing_road_mark_name = db.Column(db.String(128), unique=False, nullable=False)
    waybill_source_code = db.Column(db.String(128), unique=False, nullable=False)
    load_empty_status = db.Column(db.String(1), unique=False, nullable=False)
    origin_mark_name = db.Column(db.String(128), unique=False, nullable=False)
    destination_mark_name = db.Column(db.String(128), unique=False, nullable=False)
    sending_road_mark = db.Column(db.String(128), unique=False, nullable=False)
    bill_of_lading_number = db.Column(db.String(128), unique=False, nullable=False)
    bill_of_lading_date = db.Column(db.TIMESTAMP(),unique=False,nullable=False)
    equipment_weight = db.Column(db.Integer,unique=False,nullable=False)
    tare_weight = db.Column(db.Integer,unique=False,nullable=False)
    allowable_weight = db.Column(db.Integer,unique=False,nullable=False)
    dunnage_weight = db.Column(db.Integer,unique=False,nullable=False)
    equipment_weight_code = db.Column(db.String(1), unique=False, nullable=True)
    commodity_code = db.Column(db.Integer,unique=False,nullable=False)
    commodity_description = db.Column(db.String(128), unique=False, nullable=False)
    origin_id = db.Column(db.Integer,unique=False,nullable=True)
    destination_id = db.Column(db.Integer,unique=False,nullable=False)
    routes = db.Column(JSONB,unique=False,nullable=False)
    parties = db.Column(JSONB,unique=False,nullable=False)

    def __init__(self, id, equipment_id, waybill_date, waybill_number, created_date,
                 billing_road_mark_name, waybill_source_code, load_empty_status,
                 origin_mark_name, destination_mark_name, sending_road_mark, bill_of_lading_number,
                 bill_of_lading_date, equipment_weight, tare_weight, allowable_weight, dunnage_weight,
                 equipment_weight_code, commodity_code, commodity_description, origin_id, destination_id,
                 routes, parties):
        self.id = id
        self.equipment_id = equipment_id
        self.waybill_date = waybill_date
        self.waybill_number = waybill_number
        self.created_date = created_date
        self.billing_road_mark_name = billing_road_mark_name
        self.waybill_source_code = waybill_source_code
        self.load_empty_status = load_empty_status
        self.origin_mark_name = origin_mark_name
        self.destination_mark_name = destination_mark_name
        self.sending_road_mark = sending_road_mark
        self.bill_of_lading_number = bill_of_lading_number
        self.bill_of_lading_date = bill_of_lading_date
        self.equipment_weight = equipment_weight
        self.tare_weight = tare_weight
        self.allowable_weight = allowable_weight
        self.dunnage_weight = dunnage_weight
        self.equipment_weight_code = equipment_weight_code
        self.commodity_code = commodity_code
        self.commodity_description = commodity_description
        self.origin_id = origin_id
        self.destination_id = destination_id
        self.routes = routes
        self.parties = parties


@app.route("/")
def hello_world():
    return jsonify(app="is_live")


@app.route("/equipment")
def equipment():
    x = pd.read_sql('select * from equipment',con=engine)
    return jsonify(x.to_json(orient='records'))


@app.route("/events")
@app.route("/events/<posting_date>")
def events(posting_date=None):
    if posting_date:
        stmt = f"select * from events where posting_date like '{posting_date}%%'"
        x = pd.read_sql(stmt,con=engine)
    else:
        x = pd.read_sql('select * from events',con=engine)
    return jsonify(x.to_json(orient='records'))


@app.route("/locations")
def locations():
    x = pd.read_sql('select * from locations',con=engine)
    return jsonify(x.to_json(orient='records'))


@app.route("/waybills")
@app.route("/waybills/<waybill_id>")
def waybills(waybill_id=None):
    if waybill_id:
        stmt =f'select * from waybills where id = {waybill_id}'
        x = pd.read_sql(stmt,con=engine)
    else:
        x = pd.read_sql('select * from waybills',con=engine)
    return jsonify(x.to_json(orient='records'))


@app.route("/waybills/<waybill_id>/equipment")
def waybills_equipment(waybill_id):
    stmt =f'select a.* from equipment a join waybills b on a.equipment_id = b.equipment_id where b.id = {waybill_id}'
    x = pd.read_sql(stmt,con=engine)
    return jsonify(x.to_json(orient='records'))


@app.route("/waybills/<waybill_id>/events")
def waybills_events(waybill_id):
    stmt =f'select a.* from events a join waybills b on a.waybill_id = b.id where b.id = {waybill_id}'
    x = pd.read_sql(stmt,con=engine)
    return jsonify(x.to_json(orient='records'))


@app.route("/waybills/<waybill_id>/locations")
def waybills_location(waybill_id):
    stmt =f'select a.* from locations a join waybills b on a.id = b.origin_id where b.id = {waybill_id} union select a.* from locations a join waybills b on a.id = b.destination_id where b.id ={waybill_id};'
    x = pd.read_sql(stmt,con=engine)
    return jsonify(x.to_json(orient='records'))

# foreign keys! SQLAlchemy foreign key constraints were causing issues with dropping tables (not cascading) - have to debug that
# filter events by posting_date: update filtering to be done via body params instead of url params i.e - request.args.get('posting_date'); add filtering by sql comparison operators (<,>,=, <=, >=) 
# read db table data using SQLAlchemy instead of pandas.read_db 
# move SQLAlchemy classes to models.py
# move app routes to routes.py
