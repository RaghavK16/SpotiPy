import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
import datetime
from datetime import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "RaghavK16"
TOKEN = "BQC9U1LvuqO34zyKPOZtHq0hoc7FmsdspfWwwJgUQlNFs72RQ4N63PMHdcl1qqx5hLAPusqxwl62bUaz4fFAGCGMQO1UoKCpXMi9Z0J-9wMPh8vHVUmyiz2Xakmk6lm8MHY4S5KVowZ1tFVug89mjH2QuAN14P1xcFoUkbf9"

if __name__ == "__main__":

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        Authorization: "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://developer.spotify.com/console/get-recently-played/?after=(time)".format(time=yesterday_unix_timestamp), headers=headers)

    data = r.json()

    print(data)