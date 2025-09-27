import yaml
import os
from dotenv import load_dotenv
from collectors.web_scrapping import *
from collectors.telegram_scrapping import *
from detection.rule_base import *
from alert.email_alert import *

load_dotenv()


def run_pipeline():
    pass

if __name__ == "__main__":
    run_pipeline()
    