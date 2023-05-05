"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaarsik728r887a1b7g-a.oregon-postgres.render.com",
        database="to_do_0cr1",
        user="rehan_kittur",
        password="MMYRTVHlBaPlHx0XwcWwwiCjty0QoRQA")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
