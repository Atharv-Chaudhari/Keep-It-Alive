from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
# import time
import requests
from bs4 import BeautifulSoup
from pytz import timezone
from flask import Flask
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler = APScheduler()

def scheduleTask():
  try:
    print("\nRobot Task Execution Started....\n")
    print(datetime.datetime.now(timezone("Asia/Kolkata")).strftime("%A, %d. %B %Y %I:%M:%S%p"))
    url=[ r"url_of_website"]
    for i in url:
      response = requests.get(i)
      html_page = response.text

      soup = BeautifulSoup(html_page, 'html.parser')
    print("\nRobot Task Execution Ended....\n")
    print(datetime.datetime.now(timezone("Asia/Kolkata")).strftime("%A, %d. %B %Y %I:%M:%S%p"))
  except Exception as e:
    print(e)

@app.route('/')
def hello_world():
  return 'Status :- Robot Running....'

if __name__ == '__main__':
    scheduler.add_job(id = 'Scheduled Task', func=scheduleTask, trigger="interval", seconds=600)
    scheduler.start()
    app.run(host="0.0.0.0",debug=True)
