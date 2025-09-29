# Court Case Scraper (MVP) 🏛️

This project was developed as part of the **Python Development Internship** assignment for **Think Act Rise Foundation**.

The **Court Case Scraper (MVP)** is a Minimal Viable Product designed to help users efficiently check the status of their cases in the daily causelists of High Courts and District Courts across India. It provides a simple, interactive interface to search case details, view relevant information, and generate a downloadable PDF report.

-----

## Features

The scraper provides the following core functionalities:

  * **Search Functionality:** Easily search for a case using its **case type**, **number**, and **year**.
  * **Case Details Fetching:** Fetches and clearly displays key case details, including **parties**, **filing date**, current **status**, and **next hearing date**.
  * **Document Download:** Includes a demo flow for downloading judgments/orders.
  * **Local Storage:** Stores all user queries in a local **SQLite database** for history tracking.
  * **Report Generation:** Generates comprehensive **PDF reports** of the case details.
  * **User Interface:** Built with a simple and intuitive **Streamlit-based interface**.

-----

## Project Structure

The repository follows a clear, organized structure:

```
court-mvp/
│
├── app.py                      # Main Streamlit application entry point
├── scrapers/
│   ├── high_court.py           # High Court scraping logic
│   ├── district_court.py       # District Court scraping logic
│   └── utils.py                # Scraper-specific helper functions
├── services/
│   ├── database.py             # Handles SQLite database setup and all queries
│   └── pdf_generator.py        # Module for generating PDF reports
├── data/
│   ├── raw/                    # Stores raw scraper responses (e.g., JSON dumps)
│   └── downloads/              # Stores generated PDFs and other downloaded files
├── court_data.db               # The SQLite database file (created on first run)
├── requirements.txt            # List of all Python dependencies
└── README.md                   # This project documentation
```

-----

## Setup and Running the Application

Follow these steps to set up the project locally and run the Streamlit application.

### 1\. Clone the Repository

```bash
git clone <your-repository-url>
cd court-mvp
```

### 2\. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate

# Activate the virtual environment (Windows - PowerShell)
# .\venv\Scripts\Activate.ps1
```

### 3\. Install Dependencies

Install all necessary Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4\. Run the App

Start the Streamlit application from your terminal:

```bash
streamlit run app.py
```

The app will automatically open in your web browser.

-----

## Future Improvements

The following features are planned for future versions of the project:

  * **Cloud Deployment:** Deploy the application on **Streamlit Cloud** for easy public access.
  * **Automated Notifications:** Implement **daily automated scraping** with push notifications for case updates.
  * **Advanced Filters:** Add more search filters, such as **advocate name** and **bench** composition.
