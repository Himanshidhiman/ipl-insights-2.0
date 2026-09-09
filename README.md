# ipl-insights-2.0
# IPL Insights 2.0 — Web-Based Cricket Analytics Platform

## Overview
IPL Insights 2.0 is a web-based analytics platform that allows users to explore 
Indian Premier League (IPL) match and delivery-level data interactively. Built with 
Flask and MySQL, the platform enables dynamic querying and real-time retrieval of 
match statistics across 1,000+ IPL matches.

## Features
- **Matches Module** — Explore team-wise and match-wise statistics, results, and history
- **Deliveries Module** — Ball-by-ball delivery data exploration for detailed match analysis
- Dynamic querying against a MySQL database for real-time data retrieval
- Clean, interactive web interface for non-technical users to explore cricket data

## Tech Stack
- **Backend:** Python, Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Data Processing:** Pandas
- **IDE:** Visual Studio Code

## How It Works
The platform ingests IPL match and delivery-level datasets into a MySQL database. 
Flask serves as the backend, handling dynamic queries triggered by user interactions 
on the frontend, and returning real-time results without page reloads.

## Getting Started

### Prerequisites
- Python 3.x
- MySQL Server

### Installation
```bash
git clone https://github.com/Himanshidhiman/ipl-insights-2.0.git
cd ipl-insights-2.0
pip install -r requirements.txt
```

### Setup
1. Create a MySQL database and import the provided dataset
2. Set your database credentials as environment variables:
```bash
   DB_HOST=your_host
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=your_database_name
```
3. Run the app:
```bash
   python app.py
```
4. Visit `http://localhost:5000` in your browser

## Author
**Himanshi**  
[LinkedIn](https://linkedin.com/in/himanshi001) | [GitHub](https://github.com/Himanshidhiman)
