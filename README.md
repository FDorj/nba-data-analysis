# NBA Data Analysis Project 🏀📊

## Team Members
- **Fatemeh Dorj**
- **Shayan Jafari**

## Project Overview
This project is part of the Data Analysis Bootcamp (Fall 1403) and focuses on analyzing NBA player and team data. The project consists of three main phases:
1. **Data Collection (Web Scraping)**: Extracting data from [Basketball Reference](https://www.basketball-reference.com) using Selenium.
2. **Database Design & Storage**: Storing the extracted data in a relational database using SQLAlchemy.
3. **Data Analysis & Visualization**: Performing statistical analysis and hypothesis testing to answer key questions about player and team performance.

## Technologies Used
- **Python**
- **Selenium** (for web scraping)
- **SQLAlchemy** (for database management)
- **Pandas, NumPy** (for data manipulation)
- **Matplotlib, Seaborn** (for visualization)
- **Jupyter Notebook** (for development and analysis)

## Project Phases
### Phase 1: Data Extraction (Web Scraping)
We used Selenium to extract NBA data and structured it into six tables:
1. **Players**: Contains player details such as name, birth date, nationality, height, weight, position, and career timeline.
2. **Teams**: Includes team name, founding year, championship history, and performance statistics.
3. **Seasons**: Stores season data, including the championship-winning team for each year.
4. **Season Players**: Contains player performance metrics for each season, including points scored and team affiliation.
5. **Awards**: Lists different NBA awards along with their historical winners.
6. **Player Trophy**: Connects players with their respective awards in each season, ranking their achievements.

### Phase 2: Database Design & Storage
We designed a relational database using SQLAlchemy and MySQL. The structure includes:
- **Tables**: Players, Teams, Seasons, Season Players, Awards, and Player Trophy.
- **Relationships**: Foreign keys link players, teams, and awards data efficiently.
- **Normalization**: Ensured minimal redundancy and optimal query performance.

### Phase 3: Data Analysis & Hypothesis Testing
Performed various statistical analyses, including:
- Distribution of player height and experience over seasons.
- Impact of player positions on team success.
- Identifying top players for recruitment based on historical performance.
- Hypothesis testing on agility trends and player development.

---
**Bootcamp Project - Fall 1403**

