import gspread, os
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(r'Day 93 - Webscraping job requirements\.keys\credentials.json', scopes=scopes)
client = gspread.authorize(creds)
sheet_id = os.environ.get('google_sheets_id')
sheet = client.open_by_key(sheet_id)

analyzed_job_titles = [
    # data related
    '"machine learning"', '"data science"', '"data engineer"', '"data analyst"',
    # web development related
    '"back end developer"', '"front end developer"', '"web developer"', '"full stack developer"', 
    # software related
    '"software engineer"', '"software developer"',
    # mobile app related
    '"android developer"', '"ios developer"', '"mobile app developer"', 
    # other
    '"game developer"', '"blockchain"', '"rpa"', '"cloud engineer"', '"devops"'
    # '"_______"', 
]

# Creating worksheets
for job in analyzed_job_titles:
    job_title_no_quotation = job.strip('"').title()
    sheet.add_worksheet(title=job_title_no_quotation, rows=50, cols=2000)
    sheet.add_worksheet(title=f'{job_title_no_quotation} graph', rows=20, cols=40)
