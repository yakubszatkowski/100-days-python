import gspread, os, datetime
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(r'Day 93 - Webscraping job requirements\.keys\credentials.json', scopes=scopes)
client = gspread.authorize(creds)
sheet_id = os.environ.get('google_sheets_id')
sheet = client.open_by_key(sheet_id)


# Example
analyzed_job_title = 'Machine Learning'
words_machine_learning = [
    ('python', 22), ('tensorflow', 16), ('pytorch', 16), ('seo', 15), ('numpy', 14), 
    ('pandas', 14), ('matplotlib', 14), ('snowflake', 8), ('google', 8), ('gcp', 6), 
    ('docker', 6), ('kubernetes', 6), ('sql', 5), ('azure', 4), ('terraform', 4), 
    ('excel', 4), ('aws', 2), ('keras', 2), ('linux', 2), ('tableau', 2), ('html', 2), 
]


def update_worksheet(job_title, technologies_count):
    todays_date = datetime.date.today()
    worksheet = sheet.worksheet(analyzed_job_title)

    # Checking if new technology appeared - if yes fill it in first empty cell in first column
    technologies = set([technology[0] for technology in technologies_count])
    worksheet_technologies = set(worksheet.col_values(1)[1:])
    if worksheet_technologies != technologies:
        # print('difference detected')
        odd_values = list(technologies.difference(worksheet_technologies))
        first_empty_row = len(worksheet_technologies) + 2

        odd_value_index = 0
        while worksheet_technologies != technologies:
            worksheet.update_cell(row=first_empty_row, col=1, value=odd_values[odd_value_index])
            first_empty_row += 1
            odd_value_index += 1
            worksheet_technologies = set(worksheet.col_values(1)[1:])



update_worksheet(analyzed_job_title, words_machine_learning)
