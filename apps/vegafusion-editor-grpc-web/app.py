from flask import Flask, send_from_directory
from pathlib import Path
import pandas as pd
import vegafusion as vf
import os
import uuid

datasets_dir = Path(__file__).parent / "datasets"


def app_with_setup():
    # Make datasets directory
    datasets_dir.mkdir(parents=True, exist_ok=True)

    # Download flights dataset
    flights_200k_path = datasets_dir / "flights_200k.feather"
    if not flights_200k_path.exists():
        # Load with pandas
        df = pd.read_parquet(
            "https://vegafusion-datasets.s3.amazonaws.com/vega/flights_200k.parquet"
        )

        # To avoid risk of corruption if multiple instances of the app start simultaneously,
        # write to a temporary feather file then rename to final destination
        # (as os.rename is atomic)
        temp_filename = datasets_dir / (str(uuid.uuid4()) + ".feather")
        vf.transformer.to_feather(df, temp_filename)
        os.rename(temp_filename, flights_200k_path)

    return Flask(__name__)


app = app_with_setup()


@app.route("/<path:path>", methods=["GET"])
def static_proxy(path):
    return send_from_directory("./dist", path)


@app.route("/")
def root():
    return send_from_directory("./dist", "index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8087, debug=True)
