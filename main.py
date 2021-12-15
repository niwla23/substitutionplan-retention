import os
from dotenv import load_dotenv
from saving import save_snapshot
from prometheus_client import start_http_server
import schedule
import time

load_dotenv()

data_root = os.environ['DATA_PATH']
base_url = os.environ['BASE_URL']
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]
path_this_day = os.environ["PATH_THIS_DAY"]
path_next_day = os.environ["PATH_NEXT_DAY"]
push = os.environ["PUSH"].lower() == "true"
run_at = os.environ["RUN_AT"]

def job(_ctx):
    print("saving plans...")
    save_snapshot(data_root, base_url, username,
                  password, path_this_day, path_next_day, push)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(5424)
    schedule.every().day.at(run_at).do(job, "hi")
    while True:
        schedule.run_pending()
        time.sleep(1)
