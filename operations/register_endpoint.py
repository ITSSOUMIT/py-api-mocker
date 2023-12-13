import typer
import json

from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

ALLOWED_HTTP_METHODS = ["GET", "POST"]

def register_endpoint():
  print("\n")
  endpoint = typer.prompt("Endpoint ").rstrip('/')
  questions = [{
    "type": "list",
    "message": "Choose operation :",
    "choices": ALLOWED_HTTP_METHODS,
    "default": "POST",
  }]
  http_method = prompt(questions)[0]
  data = {
    "endpoint": endpoint,
    "http_method": http_method
  }
  try:
    with open("endpoints.json", "r") as file:
      existing_data = json.load(file)
  except FileNotFoundError:
    existing_data = []

  data_exists = any(existing["endpoint"] == endpoint and existing["http_method"] == http_method for existing in existing_data)

  if not data_exists:
    existing_data.append(data)

    with open("endpoints.json", "w") as file:
        json.dump(existing_data, file, indent=2)
    print(f"✅ Endpoint {endpoint} registered successfully")
  else:
    print(f"❌ Endpoint {endpoint} already exists")