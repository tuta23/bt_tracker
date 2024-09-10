import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

url = "https://www.buffalotracedistillery.com/product-availability"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the h2 tag with the class "cmp-title__text" that contains the updated time
updated_tag = soup.find('h2', class_='cmp-title__text')

print(updated_tag)

# Extract the text from the tag
if updated_tag:
    updated_text = updated_tag.get_text().strip()

    # Remove the "Updated" part and clean the string
    cleaned_text = updated_text.replace("Updated", "").strip()

    # Convert the cleaned string into a datetime object
    time_updated = datetime.strptime(cleaned_text, '%I:%M %p %m/%d/%Y')

    # Output the datetime object
    print(time_updated)
else:
    print("Update time not found.")
	
# Function to scrape the product availability from the webpage
def scrape_product_availability():

    # Finding the relevant sections for products
    products = soup.find_all('div', class_='container')

    product_dict = {}

    # Exclude specific items
    exclude_items = ["Looking for the Perfect Gift?", "What&#39;s Available At Buffalo Trace Distillery Today?"]

    for product in products:
        # Check if the <h3> tag with class 'cmp-title__text' exists
        product_name_tag = product.find('h3', class_='cmp-title__text')

        # Skip if no valid product name is found
        if product_name_tag is None:
            continue

        product_name = product_name_tag.text.strip()

        # Skip items in the exclude list
        if product_name in exclude_items:
            continue

        # Check if the product is in stock or sold out by looking at the parent container's class
        if 'container--product-availability-available' in product['class']:
            status = 'In Stock'
        elif 'container--product-availability-not-available' in product['class']:
            status = 'Sold Out'
        else:
            status = 'Unknown'

        product_dict[product_name] = status

    return product_dict

def update_csv2(product_dict, time_updated):
    csv_filename = 'BT_availability_log_test2.csv'
    
    # Read the existing CSV file if it exists, otherwise create an empty dataframe
    if os.path.exists(csv_filename):
        df = pd.read_csv(csv_filename)
    else:
        df = pd.DataFrame()

    # Get the current time for the timestamp column
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Check for new products and adjust columns accordingly
    for product in product_dict.keys():
        if product not in df.columns:
            df[product] = 'Not Present on Page'  # Default value for new columns for past timestamps

    # Add "BT_Updated_Time" column if it doesn't exist
    if 'BT_Updated_Time' not in df.columns:
        df['BT_Updated_Time'] = None  # Default to None for past records

    # Create a new row with the current timestamp, BT updated time, and product statuses
    new_row = {'Time': current_time, 'BT_Updated_Time': time_updated.strftime('%Y-%m-%d %H:%M:%S')}
    for product, status in product_dict.items():
        new_row[product] = status

    # Fill in 'Not Present on Page' for any products that are missing from the current scrape
    for product in df.columns:
        if product not in new_row and product != 'Time' and product != 'BT_Updated_Time':
            new_row[product] = 'Not Present on Page'

    # Convert the new_row to a DataFrame and use pd.concat instead of append
    new_row_df = pd.DataFrame([new_row])
    
    df = pd.concat([df, new_row_df], ignore_index=True)

    # Save the dataframe back to the CSV
    df.to_csv(csv_filename, index=False)

# Example of running the scraping and CSV update
product_dict = scrape_product_availability()

update_csv2(product_dict, time_updated)	
