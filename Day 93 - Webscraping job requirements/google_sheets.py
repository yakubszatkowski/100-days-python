import gspread, os, datetime, time
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(r'Day 93 - Webscraping job requirements\.keys\credentials.json', scopes=scopes)
client = gspread.authorize(creds)
sheet_id = os.environ.get('google_sheets_id')
sheet = client.open_by_key(sheet_id)

# jt = 'Data Engineer'
# tc= [('python', 38), ('sql', 33), ('etl', 32), ('azure', 31), ('aws', 28), ('spark', 24), ('apache', 16), ('agile', 14), ('git', 14), ('docker', 14), ('hadoop', 14), ('sap', 12), ('scala', 8), ('api', 8), ('snowflake', 8), ('java', 8), ('terraform', 7), ('pandas', 6), ('oracle', 6), ('dwh', 6), ('kafka', 6), 
# ('scrum', 5), ('gcp', 5), ('looker', 5), ('kanban', 4), ('mongodb', 4), ('github', 4), ('saas', 4), ('paas', 4), ('kubernetes', 3), ('frontend', 2), ('go', 2), ('llm', 2), ('excel', 2), ('restful', 2), ('jenkins', 2), ('typescript', 2), ('helm', 2), ('gitlab', 2), ('tableau', 2), ('elasticsearch', 1), ('bigquery', 1)]

def update_worksheet(job_title, technologies_count):
    todays_date = datetime.date.today().strftime('%d-%m-%Y')
    no_quotation_job_title = job_title.strip('"').title()
    worksheet = sheet.worksheet(no_quotation_job_title)

    first_row = worksheet.row_values(1)[1:]  # this doesn't include "Date" value in spreadsheet
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
        first_empty_col_in_first_row= len(set_worksheet_technologies) + 2  # "+ 2" so we don't overwrite "Date"

        odd_value_index = 0
        if odd_values:
            while set_worksheet_technologies != set_technologies:
                try:
                    worksheet.update_cell(row=1, col=first_empty_col_in_first_row, value=odd_values[odd_value_index])
                except IndexError:
                    break
                first_empty_col_in_first_row += 1
                odd_value_index += 1
                # set_worksheet_technologies = set(worksheet.row_values(1)[1:])
    time.sleep(25)
    
    # Insert datetime 
    first_column = worksheet.col_values(1)
    if todays_date not in first_column:
        first_empty_row_in_first_col = len(first_column) + 1
        worksheet.update_cell(row=first_empty_row_in_first_col, col=1, value=todays_date)

        # Insert count values based on technologies in the rows
        worksheet_technologies = worksheet.row_values(1)[1:]
        for technology in worksheet_technologies:
            technology_cell = worksheet.find(technology)
            technology_cell_col = technology_cell.col
            for technology_name, count in technologies_count:
                if technology.lower() == technology_name:
                    worksheet.update_cell(first_empty_row_in_first_col, technology_cell_col, count)

# update_worksheet(jt, tc)
