import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
import datetime
from datetime import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "RaghavK"
TOKEN = "BQAw-poCgFWWgMWgbQT5Fl_5MHQyzHtdZRlgVxhbrNBtvVg5eE_Q5dm5d1qS2X1Yrq12yW-8ZhsvzMO0WuG0yKJh7teY0gw10e7M4D1JyQbLQ3tq_kVfrm_9Me4kGcwzuGTZd6Fja8rv5MYO6zvpjGbhFLvp1V8WCJX482DF"

if __name__ == "__main__":

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }