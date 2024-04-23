import gspread, os, datetime, time
import numpy as np
from google.oauth2.service_account import Credentials
import xlsxwriter 

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(r'Day 93 - Webscraping job requirements\.keys\credentials.json', scopes=scopes)
client = gspread.authorize(creds)
sheet_id = os.environ.get('google_sheets_id')
sheet = client.open_by_key(sheet_id)

jb = 'Machine Learning'
tech = [
    ('python', 27), ('aws', 21), ('tensorflow', 20), ('pytorch', 20), ('numpy', 15), ('pandas', 14), 
    ('azure', 9), ('slack', 8), ('matplotlib', 8), ('git', 7), ('keras', 7), ('jira', 6), ('java', 6), 
    ('hadoop', 6), ('llm', 6), ('php', 4), ('terraform', 4), ('docker', 4), ('mlflow', 4), ('spark', 4), 
    ('kubernetes', 3), ('linux', 3), ('scala', 3), ('sql', 3), ('gcp', 3), ('tableau', 2), ('bash', 2), 
    ('gitlab', 2), ('bert', 2), ('kafka', 2), ('api', 2), ('flask', 2), ('etl', 2)
]

def update_worksheet(job_title, technologies_count):
    todays_date = datetime.date.today().strftime('%d-%m-%Y')
    no_quotation_job_title = job_title.strip('"').title()
    worksheet = sheet.worksheet(no_quotation_job_title)

    first_row = worksheet.row_values(1)[1:]  # This doesn't include "Date" value in spreadsheet
    formatted_technologies_list = []
    for technology in technologies_count:
        if len(technology[0]) <= 3:
            formatted_technologies_list.append(technology[0].upper())
        else:
            formatted_technologies_list.append(technology[0].title())

    # Checking if new technology appeared - if yes fill it in first empty cell in first row
    set_technologies = set(formatted_technologies_list)
    set_worksheet_technologies = set(first_row)
    if set_worksheet_technologies != set_technologies:
        odd_values = list(set_technologies.difference(set_worksheet_technologies))
        ordered_odd_values = [[tech for tech in formatted_technologies_list if tech in odd_values]]
        first_empty_col_in_first_row = len(set_worksheet_technologies) + 1
        column = xlsxwriter.utility.xl_col_to_name(first_empty_col_in_first_row)
        worksheet.update(range_name=f'{column}1', values=ordered_odd_values)

    # Insert datetime 
    first_column = worksheet.col_values(1)
    if todays_date not in first_column:
        first_empty_row_in_first_col = len(first_column) + 1
        worksheet.update_cell(row=first_empty_row_in_first_col, col=1, value=todays_date)

        # Insert count values based on technologies in the first row
        worksheet_technologies = worksheet.row_values(1)[1:]
        technologies_count_dict = {k:v for k, v in technologies_count}
        ordered_count_values = [[technologies_count_dict[technology.lower()] for technology in worksheet_technologies]]
        worksheet.update(range_name=f'B{first_empty_row_in_first_col}', values=ordered_count_values)


update_worksheet(jb, tech)
