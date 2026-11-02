#DICT REAL WORLD APPLICATIONS
# 1. Use case: Database or API Records - returned records are stored as dictionaries where column names are keys and the row values are the dictionaries
# Representing a single row from a database or API
row = {
    "id": 101,
    "name": "John",
    "country": "Kenya",
    "age": 29,
    "status": "active"
}

# 2. Use case: Mapping to friendly values - Great for converting technical codes into friendly labels
#Mapping translations to friendly values
status_map = {
    "01": "Open",
    "02": "In progress",
    "03": "Done"
}

# 3. Use case: Mapping Abbreviations - Turning short abbreviations into full readable names

country_map = {
    "DE": "Germany",
    "FR": "France",
    "IN": "India"
}

# 4. Use case: Config and Environmental Data - Store system settings like host, port, and usernames in one clean place
#Storing environmental variables and configuration

system_conn = {
    "DB_HOST": "prod-db.company.com",
    "DB_PORT": 5432,
    'DB_USER': "admin_user",
    "DB_NAME": "analytics_warehouse"
}

# 5. Use case: ETL and Pipeline Settings - Great for storing run parameters and controlling how your ETL pipeline loads data
etl_config = {
    "DEBUG_MODE": False,
    "BATCH_SIZE": 500,
    "LOG_LEVEL": "INFO"
}

# 6. Use case: To store metadata - data about your data
table_metadata = {
    "table_name": "customers",
    "columns": {
        "id": {"type": "integer", "nullable": False},
        "name": {"type": "string", "nullable": True}
    },
    "row_count": 105320,
    "file_format": "parquet"
}