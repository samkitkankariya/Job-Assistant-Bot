from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
import requests  # Import requests for sending HTTP requests
import csv  # Import CSV for handling CSV files
import datetime  # Import datetime for working with dates and times

from telegram.ext import *  # Import necessary modules from telegram.ext for Telegram bot functionality
import keys  # Import the keys module for accessing the Telegram bot token
import telegram  # Import telegram for Telegram bot functionality
from keep_alive import keep_alive  # Import keep_alive for keeping the server running continuously using UptimeBot

# Define a function to scrape job listings from a specific URL
def find_jobs():
    # Get the HTML code from the desired URL
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=Python&txtLocation=', verify=False).text
    
    # Parse the HTML code using BeautifulSoup with the 'lxml' parser
    soup = BeautifulSoup(html_text, 'lxml')

    # Find all the job listings in the HTML code
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    # Create a CSV file to store the scraped job data with specific headers
    header = ['Date', 'Company Name', 'Required Skills', 'Application Link']
            
    # Write 'w' to create the CSV file and write the header row
    with open('Python_Jobs_List.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

    # Iterate through each job listing
    for index, job in enumerate(jobs):
        # Find the published date of the job listing
        published_date = job.find('span', class_ = 'sim-posted').span.text

        # Check if the job was published 'few days ago'
        if 'few' in published_date:
            # Extract the company name from the job listing
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            # Extract the required skills from the job listing
            required_skills = job.find('span', class_ = 'srp-skills').text.replace(' ','').strip()

            # Extract the application link from the job listing
            application_link = job.header.h2.a['href']
            # Format the application link as a clickable hyperlink
            application_link = f'=HYPERLINK("{application_link}", "Click Here")'

            # Get today's date to add to the job data
            today = datetime.date.today()

            # Create a list with the job data
            data = [today, company_name, required_skills, application_link]     

            # Ensure to open the CSV file in 'a+' mode to append subsequent data rows
            with open('Python_Jobs_List.csv', 'a+', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(data)

    # Print a success message after creating the CSV file
    print("CSV File Created Successfully!")

# Start the bot and define asynchronous functions for handling Telegram commands

print('Starting the bot....')

async def start_command(update, context):
    await update.message.reply_text('Hi! This bot provides real-time job postings available on TimesJobs portal.\nUse /list to get the latest job list.')

# Define a command to send the latest job list as a CSV file to the user
async def list_command(update, context):
    bot = telegram.Bot(token=keys.token)  # Initialize the Telegram bot with the bot token from keys.py
    find_jobs()  # Call the function to scrape job listings and update the CSV file
    file_path = 'Python_Jobs_List.csv'  # Specify the path to the CSV file
    caption = 'Here is your today\'s job list.'  # Optional caption for the file

    try:
        with open(file_path, 'rb') as file:
            await bot.send_document(chat_id=update.effective_chat.id, document=file, caption=caption)  # Send the CSV file with chat ID
        print("File sent successfully!")
        await update.message.reply_text('''Here is your today's Python job list!
Your dream is just a click away...
Go get them!!''')  # Send a response message to the user
        
    except telegram.error.TelegramError as e:
        print(f"Error sending file: {e}")

# Check if the script is executed directly and not imported as a module
if __name__ == '__main__':
    keep_alive()  # Keep the server running to ensure continuous bot functionality
    application = Application.builder().token(keys.token).build()  # Build the Telegram bot application

    # Register command handlers for '/start' and '/list' commands
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('list', list_command))

    # Run the bot with polling
    application.run_polling(1.0)
