from bs4 import BeautifulSoup
import csv
import pandas as pd

def do(i):
    with open('page_'+str(i)+'.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Finding all divs with class "row mb-2"
    rows = soup.find_all('div', class_='row mb-2')

    # List to hold all extracted data
    data = []
    data_finalized = []

    # Iterating through each row to extract information
    for row in rows:
        # Initialize a dictionary to hold the data for this row
        row_data = {}

        # Extract major and school name
        major_school = row.find('h6', class_='mt-3 fw-normal')
        if major_school:
            # Extracting only the direct text of the h6 tag, excluding child tags
            major_school_text = ''.join(major_school.find_all(text=True, recursive=False)).strip()
            row_data['Major_School'] = major_school_text

        # Extract optional description
        description = row.find('span', class_='text-secondary ms-3')
        if description:
            row_data['Description'] = description.get_text(strip=True)


        # Extract date added
        date_added = row.find('p', class_='mb-0 fst-italic')
        if date_added:
            row_data['Date_Added'] = date_added.get_text(strip=True).replace('Added on','')

        # Extract status and date
        status = row.find('span', class_='badge')
        if status:
            row_data['Status_Date'] = status.get_text(strip=True).replace('\n','').replace('\t','')

        row_data['GRE_Stats'] = ''
        row_data['GPA'] = ''
        row_data['Degree'] = ''
        row_data['Citizenship'] = ''

        # Additional attributes
        attribute_index = 1

        additional_badges = row.find_all('span', class_='badge badge-unselected')
        for badge in additional_badges:
            text = badge.get_text(strip=True)
            if "GRE" in text:
                row_data['GRE_Stats'] += text + '; '
            elif "GPA" in text.upper():
                row_data['GPA'] = text
            elif "PhD" in text or "Masters" in text:
                row_data['Degree'] = text
            elif text in ["American", "International"]:
                row_data['Citizenship'] = text
            elif text:  # For other attributes
                row_data[f'Attribute_{attribute_index}'] = text
                attribute_index += 1

        # Remove trailing semicolon and space from GRE_Stats
        if row_data['GRE_Stats']:
            row_data['GRE_Stats'] = row_data['GRE_Stats'].rstrip('; ')

        data_finalized.append(row_data)
    return (pd.DataFrame(data_finalized))
l = []
init = int(input('input start'))
ending = int(input('input end'))
while init<=ending:
    try:
        l.append(do(init))
    except:
        print(init,'... gone away...')
    init+=1
    if init%100==0:
        print('out of',ending-init,',',init,'has been completed!')
pd.concat(l, ignore_index=True).to_csv('out.csv')
print("OK!")