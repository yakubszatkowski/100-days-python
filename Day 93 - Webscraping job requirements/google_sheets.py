import gspread, os, datetime
from google.oauth2.service_account import Credentials
import xlsxwriter 

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
main_directory = os.path.dirname(os.path.realpath(__file__))
creds = Credentials.from_service_account_file(f'{main_directory}/.keys/credentials.json', scopes=scopes)
client = gspread.authorize(creds)
sheet_id = os.environ.get('google_sheets_id')
sheet = client.open_by_key(sheet_id)


def update_worksheet(job_title, technologies_count):

    # Today's date and selecting worksheet
    todays_date = datetime.date.today().strftime('%d-%m-%Y')
    no_quotation_job_title = job_title.strip('"').title()
    worksheet = sheet.worksheet(no_quotation_job_title)

    # Formatting technologies list letter case
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
        ordered_count_values = [[technologies_count_dict.get(technology.lower(), 0) for technology in worksheet_technologies]]
        worksheet.update(range_name=f'B{first_empty_row_in_first_col}', values=ordered_count_values)
