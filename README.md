# OSMIMPORT-PYTHON

This application parses OSM data in PBF (Protocol Buffer Format) and imports it into an existing RethinkDB database.

This application was heavily inspired by [ederoyd46](https://github.com/ederoyd46)'s [osmimport-go](https://github.com/ederoyd46/osmimport-go) application.

# Requirements

The application's requirements are described in the requirements.txt file.

Use pip to install these automatically either global or inside a virtualenv.

```bash
pip install -r requirements.txt
```

# Usage

```bash
python main.py dbhost dbport dbname pbf

dbhost = RethinkDB host
dbport = RethinkDB port
dbname = RethinkDB database name
pbf = Full path to PBF file to parse
```