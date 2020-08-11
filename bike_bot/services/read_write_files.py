import datetime
from pathlib import Path
import json

def loadSavedAds(filename="ads.json") -> dict:
    filepath = Path().absolute().joinpath(filename)
    # Reads given file and creates a dict of ads in file
    # If filepath is None, just skip local file
    if filepath:
        # If the file doesn't exist create it
        if not filepath.exists():
            ads_file = filepath.open(mode='w')
            ads_file.write("{}")
            ads_file.close()
            return

        with filepath.open(mode="r") as ads_file:
            all_ads = json.load(ads_file)
            return all_ads

# Save JSON to outputs folder
def output_json(contents: dict, filename="output"):
    output_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    output_filename = f'{filename}_{output_timestamp}.json'

    filepath = Path().absolute().joinpath("outputs", output_filename)
    with filepath.open(mode="w") as write_file:
        json.dump(contents, write_file)

def load_json(filename="output"):
    filepath = Path().absolute().joinpath("outputs", filename)
    if filepath.exists():
         with filepath.open(mode="r") as input_file:
            newDict = json.load(input_file)
            return newDict
