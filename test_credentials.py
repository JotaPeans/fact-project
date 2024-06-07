import os
import json
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dotenvpath = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenvpath)

CREDENTIALS_JSON = json.loads(os.environ.get("CREDENTIALS_GOOGLE_API"))