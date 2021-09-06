import json
import os
from dotenv import load_dotenv
from supabase_py import create_client, Client

load_dotenv()

url: str = os.getenv('SUPABASE_URL')
key: str = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(url, key)

with open("instruments.json") as jsonFile:
    instruments = json.load(jsonFile)
    jsonFile.close()

data = supabase.table("lse_instruments").insert(instruments).execute()
assert len(data.get("data", [])) > 0
print(data.get("data"))