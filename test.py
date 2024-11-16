import os
from databricks import sql
from dotenv import load_dotenv

load_dotenv()

try:
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
