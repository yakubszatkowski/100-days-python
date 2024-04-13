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
    todays_date = datetime.date.today().strftime('%d-%m-%Y')
    worksheet = sheet.worksheet(job_title)

    worksheet_technologies = worksheet.col_values(1)[1:]
    formatted_technologies_list = []
    for technology in technologies_count:
        if len(technology[0]) <= 3:
            formatted_technologies_list.append(technology[0].upper())
        else:
            formatted_technologies_list.append(technology[0].title())

    # Checking if new technology appeared - if yes fill it in first empty cell in first column
    set_technologies = set(formatted_technologies_list)
    set_worksheet_technologies = set(worksheet_technologies)
    if set_worksheet_technologies != set_technologies:
        odd_values = list(set_technologies.difference(set_worksheet_technologies))
        first_empty_row_in_first_column = len(set_worksheet_technologies) + 2

        odd_value_index = 0
        while set_worksheet_technologies != set_technologies:
            worksheet.update_cell(row=first_empty_row_in_first_column, col=1, value=odd_values[odd_value_index])
            first_empty_row_in_first_column += 1
            odd_value_index += 1
            set_worksheet_technologies = set(worksheet.col_values(1)[1:])

    # Insert datetime 
    first_row = worksheet.row_values(1)
    if todays_date not in first_row:
        first_empty_column_in_first_row = len(first_row) + 1
        available_column = first_empty_column_in_first_row
        worksheet.update_cell(row=1, col=first_empty_column_in_first_row, value=todays_date)

        # Insert count values based on technologies in first column
        worksheet_technologies = worksheet.col_values(1)[1:]
        for technology in worksheet_technologies:
            technology_cell = worksheet.find(technology)
            technology_cell_row = technology_cell.row
            # print(f'{technology} - ({technology_cell_row}, {available_column})')
            for technology_name, count in technologies_count:
                if technology.lower() == technology_name:
                    worksheet.update_cell(technology_cell_row, available_column, count)
                    print(count)


update_worksheet(analyzed_job_title, words_machine_learning)
