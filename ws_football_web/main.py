import requests
from bs4 import BeautifulSoup
import csv
from googletrans import Translator #google API to translate 
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine



date=input('please enter date in the following format MM/DD/YYYY : ')
page=requests.get(f"https://www.yallakora.com/match-center/?date={date}#")


def main(page):
    translator = Translator()
    src=page.content
    soup=BeautifulSoup(src,'lxml')
    
    matches_detail = []
    championchimps = soup.find_all("div",{'class':'matchCard'})
    
    
    def get_match_info(championchimps):
        
        championchimp_title=translator.translate(championchimps.contents[1].find('h2').text.strip(), src='ar', dest='en').text
        print(championchimp_title)
        
        all_matches=championchimps.find_all('div',{'class':'item'})
        # print(all_matches)
        
        n_matches=len(all_matches)
        print(n_matches)

        
        for i in range(n_matches):
            #get teams names
            team_a=translator.translate(all_matches[i].find('div',{'class':'teamA'}).text.strip(),src='ar',dest='en').text
            team_b=translator.translate(all_matches[i].find('div',{'class':'teamB'}).text.strip(),src='ar',dest='en').text
            
            #get score of the match
            match_result=all_matches[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            
            print(f"{team_a} {match_result[0].text.strip()}-{match_result[1].text.strip()} {team_b}")
            
            #get match time
            match_time=all_matches[i].find('span',{'class':'time'}).text.strip()
            print(f"{match_time}")
            
            #add match info to matches_details
            matches_detail.append({'tourment':championchimp_title,
                                   'team A':team_a,
                                   'score':f"{ match_result[0].text.strip()} - {match_result[1].text.strip()}",
                                   'team B':team_b,
                                   'match time':match_time,
                                   })
        
    for league in championchimps:
        get_match_info(league)
    
    print(matches_detail)
    
    keys=matches_detail[0].keys()
    try :
        
        with open('C:/Users/NIPEAL/OneDrive/Desktop/projectss/py_project_githubs/web_scraping/ws_football_web/matches.csv','w',newline='',encoding='utf-8') as f:
            dict_writer=csv.DictWriter(f,keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches_detail)
            print("csv file created")
            
            
    except :
        print('csv and database not been created, something happen.')
    
    def to_database(match_detail):
        db_name=input("enter your database to connect: ")
        conn=mysql.connector.connect(host='localhost', user ='root',
                                     password='root',database=db_name,
                                     use_pure=True)
        cursor=conn.cursor()
        table_name=input("enter table name: ")
        # cursor.execute(f"""CREATE TABLE IF NOT EXIST {table_name}({''.join(match_detail[0].keys())})""")
        for match in match_detail:
            cursor.execute(f'''
                          INSERT INTO {table_name}(tourment,taemA,score,teamB,matchTime)
                          VALUES ({match['tourment']}, {match['team A']}, {match['score']}, {match['team B']}, {match['match time']} )
                          ''')
        conn.commit()
        conn.close()
    to_database(match_detail=matches_detail)   
    
    
    
main(page)




