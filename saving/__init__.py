import iservscrapping
import os
import time
from datetime import datetime
from saving.metrics import DOWNLOAD_SIZE, DOWNLOAD_TIME


def save_snapshot(data_root: str, base_url: str, username: str, password: str, path_this_day: str, path_next_day: str, push: bool):
    """Saves both substitution plans

    Saves both substitution plans to the given directory
    in a subfolder named after the current unix timestamp.

    Args:
        data_root (str): The root directory in which all timestamp folders will be created
        base_url (str): the base url of the iserv server without trailing slash
        username (str): iserv username to use
        password (str): iserv password to use
        path_this_day (str): Path to the plan for the current day (no iframe)
        path_next_day (str): Path to the plan for the next day (no iframe)
        push (bool): Whether the git repo should be pushed after making changes.


    """
    # pylint: disable=too-many-arguments

    iserv = iservscrapping.Iserv(base_url, username, password)

    with DOWNLOAD_TIME.labels(operation="login").time():
        iserv.login()

    with DOWNLOAD_TIME.labels(operation="download_this_day").time():
        this_day = iserv.session.get(iserv.url + path_this_day)
    with DOWNLOAD_TIME.labels(operation="download_next_day").time():
        next_day = iserv.session.get(iserv.url + path_next_day)

    this_day_text = this_day.text
    next_day_text = next_day.text
    DOWNLOAD_SIZE.labels(operation="download_this_day").set(
        len(this_day.content))
    DOWNLOAD_SIZE.labels(operation="download_next_day").set(
        len(next_day.content))

    current_path = f"{data_root}/{int(time.time())}"
    os.makedirs(current_path, exist_ok=True)
    with open(f"{current_path}/this_day.html", "w", encoding="utf-8") as file:
        file.write(this_day_text)

    with open(f"{current_path}/next_day.html", "w", encoding="utf-8") as file:
        file.write(next_day_text)

    os.system(f"cd {current_path}; git add this_day.html")
    os.system(f"cd {current_path}; git add next_day.html")
    os.system(
        f"cd {current_path}; git commit -m '📖 add substitution plans from {datetime.now().strftime('%d.%m.%y, %H:%M')}'")
    if push:
        os.system("cd {current_path}; git push")
