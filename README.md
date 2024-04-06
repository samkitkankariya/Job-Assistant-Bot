## Job Assistant Telegram Bot

The Job Assistant Telegram Bot, accessible via `@job_assist_bot` on Telegram, is designed to provide real-time job postings from popular job portals. This bot utilizes web scraping techniques to gather job information, organizes the data into a CSV file, and sends the file directly to users upon request.

### Features
- **Real-Time Job Listings:** The bot scrapes job information from popular job portals, ensuring users get the latest job listings.
- **CSV File Generation:** Job details are organized into a CSV file, making it easy for users to view and analyze the data.
- **Direct File Delivery:** Users can request the job list directly from the bot, and the bot sends the CSV file containing the job listings to the user's Telegram chat.

### How it Works
1. **Web Scraping:** The bot uses web scraping techniques to extract job information from the specified job portal.
2. **CSV File Creation:** The extracted job data is formatted and stored in a CSV file named `Python_Jobs_List.csv`.
3. **Telegram Bot Interaction:** Users interact with the bot using commands (`/start` and `/list`), triggering actions such as initiating the bot and requesting the job list.
4. **File Delivery:** Upon receiving the request, the bot sends the CSV file containing the job listings to the user's chat.

### Usage Instructions
1. **Start the Bot:** Initiate the bot by sending the `/start` command.
2. **Request Job List:** Use the `/list` command to receive the latest job list in CSV format.
3. **File Download:** The bot will send the job list CSV file directly to your Telegram chat.

### Code Overview
The main code performs the following tasks:
- Web scrapes job information from the TimesJobs portal.
- Organizes the job data into a CSV file (`Python_Jobs_List.csv`).
- Implements a Telegram bot using the `python-telegram-bot` library.
- Responds to commands (`/start` and `/list`) to interact with users and provide the job list.

### Files
- `main.py`: Contains the main code for web scraping, CSV file creation, and Telegram bot functionality.
- `keys.py`: Stores the Telegram bot token for authentication.
- `keep_alive.py`: Keeps the server running to ensure continuous bot functionality.

## Dependencies

- `beautifulsoup4`: For parsing HTML and extracting job information.
- `requests`: For sending HTTP requests to fetch job listings.
- `python-telegram-bot`: For interacting with the Telegram API.

## Configuration

Ensure you have Python installed on your system along with the required libraries listed in `requirements.txt`. You also need a valid Telegram bot token obtained from the BotFather on Telegram.

## Example

1. Start the bot by running `python main.py`.
2. Open Telegram and search for your bot.
3. Send the `/list` command to receive the latest job list.

## Additional Information

- The bot sends job listings as a CSV file attachment along with a message containing a link to the job postings.
- The Flask server is kept alive using `keep_alive.py` to ensure the bot runs continuously.
- You can customize the bot's behavior, add more commands, or integrate additional features as per your requirements.

### Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/JobAssistantPlus.git
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Update `keys.py` with your Telegram bot token:
   ```python
   token = 'YOUR_TELEGRAM_BOT_TOKEN'
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

