import requests
from bs4 import BeautifulSoup
import csv
from googletrans import Translator  # Google API to translate
import mysql.connector
from datetime import datetime



global date
def main(page):
    date = input('Please enter date in the following format MM/DD/YYYY: ')
    page = requests.get(f"https://www.yallakora.com/match-center/?date={date}#")
    
    translator = Translator()
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    
    matches_detail = []
    championchimps = soup.find_all("div", {'class': 'matchCard'})
    
    def get_match_info(championchimps):
        championchimp_title = translator.translate(championchimps.contents[1].find('h2').text.strip(), src='ar', dest='en').text
        print(championchimp_title)
        
        all_matches = championchimps.find_all('div', {'class': 'item'})
        n_matches = len(all_matches)
        print(n_matches)

        for i in range(n_matches):
            # Get teams' names
            team_a = translator.translate(all_matches[i].find('div', {'class': 'teamA'}).text.strip(), src='ar', dest='en').text
            team_b = translator.translate(all_matches[i].find('div', {'class': 'teamB'}).text.strip(), src='ar', dest='en').text
            
            # Get score of the match
            match_result = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            print(f"{team_a} {match_result[0].text.strip()} - {match_result[1].text.strip()} {team_b}")
            
            # Get match time
            match_time = all_matches[i].find('span', {'class': 'time'}).text.strip()
            print(f"{match_time}")
            
            # Add match info to matches_detail
            matches_detail.append({
                'tourment': championchimp_title,
                'team A': team_a,
                'score': f"{match_result[0].text.strip()} - {match_result[1].text.strip()}",
                'team B': team_b,
                'match time': match_time,
            })
        
    for league in championchimps:
        get_match_info(league)
    
    print(matches_detail)
    
    keys = matches_detail[0].keys()
    try:
        with open('C:/Users/NIPEAL/OneDrive/Desktop/projectss/py_project_githubs/web_scraping/ws_football_web/matches.csv', 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches_detail)
            print("CSV file created")
    except Exception as e:
        print(f'CSV file creation failed: {e}')
    
    to_database(matches_detail)   

def to_database(match_detail):
    s=date.split('/')
    dates=f"{s[2]}-{s[0]}-{s[1]}"
    
    db_name = input("Enter your database to connect: ")
    conn = mysql.connector.connect(host='localhost', user='root', password='root', database=db_name, use_pure=True)
    cursor = conn.cursor()
    table_name = input("Enter table name: ")
    
    # Create table if it does not exist
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            tourment VARCHAR(255),
            teamA VARCHAR(255),
            score VARCHAR(10),
            teamB VARCHAR(255),
            matchTime TIME,
            match_date DATE
        )
    """)

    for match in match_detail:
        # Use parameterized query to prevent SQL injection and syntax errors
        cursor.execute(f'''
            INSERT INTO {table_name} (tourment, teamA, score, teamB, matchTime, match_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (match['tourment'], match['team A'], match['score'], match['team B'], match['match time'],dates))
    
    conn.commit()
    conn.close()

main(page)

