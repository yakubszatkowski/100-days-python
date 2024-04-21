# NOT TO BE USED IN MAIN CODE
import gspread, os
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(r'Day 93 - Webscraping job requirements\.keys\credentials.json', scopes=scopes)
client = gspread.authorize(creds)
sheet_id = os.environ.get('google_sheets_id')
sheet = client.open_by_key(sheet_id)

analyzed_job_titles = [
    '"machine learning"', '"data science"', '"data engineer"', '"data analyst"', 
    '"software engineer"', '"web developer"', '"game developer"', '"devops engineer"', 
    '"mobile app developer"', '"automation engineer"'
]

# Creating worksheets
for job in analyzed_job_titles:
    job_title_no_quotation = job.strip('"').title()
    sheet.add_worksheet(title=job_title_no_quotation, rows=1000, cols=100)
    # sheet.add_worksheet(title=f'{job_title_no_quotation} graph', rows=50, cols=50)
