import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website with the HTML table
url = 'https://ecomodder.com/wiki/Vehicle_Coefficient_of_Drag_List'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the table you want to scrape (you may need to inspect the webpage's HTML structure)
    table = soup.find('table')

    # Create a CSV file for writing
    with open('table_data.csv', 'w', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Find all rows in the table
        rows = table.find_all('tr')

        for row in rows:
            # Extract the data from each cell in the row
            cells = row.find_all(['th', 'td'])
            row_data = [cell.text.strip() for cell in cells]

            # Write the row data to the CSV file
            csv_writer.writerow(row_data)

    print('Data has been scraped and saved to table_data.csv.')
else:
    print('Failed to retrieve the webpage.')




