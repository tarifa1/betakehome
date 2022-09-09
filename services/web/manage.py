from flask.cli import FlaskGroup

from project import app, db, Equipment, Events, Locations, Waybills
from project.ingest import ingest_csv
import pandas as pd

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    ingest_csv('equipment.csv',Equipment)
    ingest_csv('locations.csv',Locations)
    ingest_csv('events.csv',Events)
    ingest_csv('waybills.csv',Waybills)


if __name__ == "__main__":
    cli()