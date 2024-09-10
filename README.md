# bt_tracker
# 🥃 Buffalo Trace Product Availability Tracker

Welcome to the **Buffalo Trace Product Availability Tracker**! This Python-based project automates the tracking of product availability from the Buffalo Trace Distillery website. The script checks which products are currently in stock or out of stock, stores the data in a CSV file, and tracks product changes over time.

## 🚀 Project Overview

This script is designed to run twice a day, collecting data on the availability of products sold at Buffalo Trace Distillery. It records the following:

- ✅ **Products In Stock**
- ❌ **Products Out of Stock**
- 📅 **Timestamp**: When the data was collected
- 🔄 **Web Page Update Time**: The last time the Buffalo Trace website was updated by their staff

The script is automated using **cron jobs** to execute at specified times daily. The resulting data is stored in a CSV file for historical analysis.

---

## 📝 Features

- **Automated Product Tracking**: Runs twice daily to capture product availability.
- **Historical Data Collection**: Records stock status of products over time in a CSV file.
- **Web Page Update Tracking**: Logs the last time the Buffalo Trace website was updated.
- **Handling New or Discontinued Products**: Automatically handles the addition of new products or removal of discontinued items from the page.
  - This functionality is untested as BT has not added or removed new products to their availability page since development of this tracker.  🤞
  
---

## ⚙️ How It Works

The script parses the [Buffalo Trace Product Availability](https://www.buffalotracedistillery.com/product-availability) page, identifying all the products listed, and checks whether they are in stock or not.

1. **Scrape Product Data**: 
   - The script uses BeautifulSoup to parse the product list from the web page.
   - The status of each product (In Stock or Sold Out) is determined based on CSS styles.
   
2. **Track Changes Over Time**: 
   - A CSV file is created or updated with the current product availability at each scrape.
   - The file is appended with new data every time the script runs, allowing long-term tracking.
   
3. **Cron Automation** (Done by you on your local machine): 
   - The script is set up to run at specific times every day using cron jobs.
   - For example:
     - **Monday to Saturday**: 9:30 AM and 6:00 PM (Central Time)
     - **Sunday**: 11:30 AM and 6:00 PM (Central Time)

---
## 🛠️ Future Improvements

- Add error handling for page loading failures.
- Implement email notifications for product availability changes.
- Provide data visualization from the CSV output after script has been in place long enough to provide some meaningful data.

---
## 🌟 Contributions
Feel free to contribute to this project! Fork the repository and create a pull request for any new features, fixes, or improvements.


---
## 🥳 Happy Tracking!
