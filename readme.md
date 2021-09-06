# Python XLSX extractor & Supabase table seed example
This project is an example of how you can use Python to extract data from an Excel spreadsheet (.xlsx) and then seed a Supabase database table using the extracted data.

The spreadsheet example used in this project is equity instrument data from the [London Stock Exchange](https://www.londonstockexchange.com/reports?tab=instruments).

<br />

# Setup, Install & Use
## Prerequisites
You will need to be able to setup a simple Supabase database and have the `URL` & `KEY` ready.

<br />

## Setup
After you have cloned the repository:
- Install required Python packages: `pip install -r requirements.txt`
- Copy the `.env.example` file contents into a new file called `.env`
- Alter the `SUPABASE_URL` & `SUPABASE_KEY` to your respective Supabase database values

<br />

## Extract data from spreadsheet
Run `python ./main.py` and once it has completed you should now see `headings.txt` and `instruments.json`
- `headings.txt`: A text file containing the column headings relative to the spreadsheet data. You can use these to create the table column names in the database.
- `instruments.json`: Each of the spreadsheet rows formatted into JSON, this will be used to seed the database

<br />

## Supabase Table Setup
- Add a table named `lse_instruments` and create the respective columns from headings.txt
- Note:
    - The `TIDM` column should be set as the `primary key`
    - For simplicity add all of the columns as a `text` datatype and allow each of them to be `nullable`


## Seed Supabase table with extracted spreadsheet data
- Finally to seed the newly created table with the data extracted from the Spreadsheet simply run `python ./seed.py` and wait for it to complete

<br />

Once these steps have been completed you should now be able to browse to your Supabase table on the web ui and see the populated data.