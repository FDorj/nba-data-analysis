from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import openpyxl
import string


season_dict = {'season_id' : [], 'season_champion_team' : []}
teams_dict = {'team_id' : [], 'team_name' : [], 'from' : [], 'to' : [], 'years' : [], 'games' : [], 'wins' : [], 'losses' : [], 'W/L_percent' : [] , 'years_league_champion' : []}
season_players_dict = {'season_id' : [], 'player_id' : [], 'team_id' : [], 'points' : []}
trophies_dict = {'trophy_id' : [], 'trophy_name' : []}
player_trophies_dict = {'player_id' : [], 'season_id' : [], 'trophy_id' : [], 'trophy_rank' : []}
players_dict = {'player_id' : [], 'player_name' : [], 'player_first_year' : [], 'player_last_year' : [], 'player_pos' : [], 'player_height' : [], 'player_weight' : [], 'player_birth_date' :[]}

def scrape_player_table(main_url, the_dict):
    url = main_url + "players/"
    
    for letter in string.ascii_lowercase:
        driver.get(url + letter + '/')
        
        players_number = int(driver.find_element(By.XPATH, '//div[@id="players_sh"]/h2').text.split(' ')[0])
        row_num = 0
        for i in range(players_number):
            if(driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]').get_attribute('class') == 'thead'):
                row_num += 1
                continue
            
            player_detail = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/th/a | //tbody/tr[@data-row="{row_num}"]/th/strong/a')
            player_name = player_detail.text
            player_id = player_detail.get_attribute('href')[37:-5]
            the_dict['player_id'].append(player_id)
            the_dict['player_name'].append(player_name)
            
            player_first_year = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="year_min"]').text
            the_dict['player_first_year'].append(player_first_year)
            
            player_last_year = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="year_max"]').text
            the_dict['player_last_year'].append(player_last_year)
            
            player_pos = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="pos"]').text
            the_dict['player_pos'].append(player_pos)
            
            player_height = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="height"]').text
            the_dict['player_height'].append(player_height)
            
            player_weight = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="weight"]').text
            the_dict['player_weight'].append(player_weight)

            player_birth_date = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="birth_date"]').get_attribute('csk')
            the_dict['player_birth_date'].append(player_birth_date)

            row_num += 1
            

def scrape_team(main_url, the_dict):
    
    driver.get(main_url + "teams/")
    teams = driver.find_elements(By.XPATH, '//tbody/tr[@class="full_table"]')
    
    for item in teams:
        
        team_name_id = item.find_element(By.XPATH, './th/a')
        team_name = team_name_id.text
        team_id = team_name_id.get_attribute('href')[37:-1]
        the_dict['team_id'].append(team_id)
        the_dict['team_name'].append(team_name)
        
        first_year = item.find_element(By.XPATH, './td[@data-stat="year_min"]').text
        the_dict['from'].append(first_year)
        
        last_year = item.find_element(By.XPATH, './td[@data-stat="year_max"]').text
        the_dict['to'].append(last_year)
        
        years = item.find_element(By.XPATH, './td[@data-stat="years"]').text
        the_dict['years'].append(years)
        
        games = item.find_element(By.XPATH, './td[@data-stat="g"]').text
        the_dict['games'].append(games)
        
        wins = item.find_element(By.XPATH, './td[@data-stat="wins"]').text
        the_dict['wins'].append(wins)
        
        losses = item.find_element(By.XPATH, './td[@data-stat="losses"]').text
        the_dict['losses'].append(losses)
        
        win_loss_percent = item.find_element(By.XPATH, './td[@data-stat="win_loss_pct"]').text
        the_dict['W/L_percent'].append(win_loss_percent)
        
        years_league_champion = item.find_element(By.XPATH, './td[@data-stat="years_league_champion"]').text
        the_dict['years_league_champion'].append(years_league_champion)

        
def scrape_player(url, season_id, season_player_dict, player_trophy_dict):
    next_url = f"NBA_{season_id}_totals.html"
    driver.get(url + next_url)
    row_num = 0
    for i in range(50):
        check_row = driver.find_element(By.XPATH, '//tbody/tr').get_attribute('class')
        if check_row == 'thead':
            row_num += 1
            continue
        
        season_player_dict['season_id'].append(season_id)
        # print(row_num)
        player_id = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="name_display"]/a').get_attribute('href')[37:-5]
        season_player_dict['player_id'].append(player_id)
        

        trophies = driver.find_elements(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="awards"]/a')
        for trophy in trophies:
            if(trophy.text != 'AS' and not('NBA' in trophy.text)):
                trophy_str = trophy.text.split('-')
                trophy_rank = trophy_str[1]
                trophy_id = 'awards/' + trophy_str[0]
                player_trophy_dict['season_id'].append(season_id)
                player_trophy_dict['player_id'].append(player_id)
                player_trophy_dict['trophy_id'].append(trophy_id)
                player_trophy_dict['trophy_rank'].append(trophy_rank)


        player_points = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="pts"]').text
        season_player_dict['points'].append(player_points)
        
        player_team = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="team_name_abbr"]')
        if player_team.text == '2TM':
            row_num += 4
            player_team_id = '2TM'
        else:
            row_num += 1
            player_team_id = player_team.find_element(By.XPATH, './a').get_attribute('href')[37:-10]
        
        season_player_dict['team_id'].append(player_team_id)


        
def scrape_season(main_url, season_dict, season_player_dict, player_trophy_dict):
    for i in range(2, 13):
        url = main_url + "leagues/"
        driver.get(url) 
        season = driver.find_element(By.CSS_SELECTOR, f'tbody tr[data-row="{i}"] th a')
        season_splitted = season.get_attribute('href').split('/')
        season_id = season_splitted[-1][-9 : -5]
        # both id and end year
        season_dict['season_id'].append(season_id)
        
        season_champion = driver.find_element(By.CSS_SELECTOR, f'tbody tr[data-row="{i}"] td[data-stat="champion"] a').get_attribute('href')
        season_dict['season_champion_team'].append(season_champion.replace(season_id, '')[37:-6])
        
        scrape_player(url, season_id, season_player_dict, player_trophy_dict)
        
def scrape_awards(main_url, the_dict):
    url = main_url + "awards/"
    driver.get(url)
    nba_awards  = driver.find_elements(By.XPATH, '//div[@class=" forcefull"]/h2[text()="NBA & ABA Season Awards"]/following-sibling::p/a')
    for item in nba_awards:
        award_link = item.get_attribute('href')[37:-5]
        the_dict['trophy_id'].append(award_link)
        award_name = item.text
        the_dict['trophy_name'].append(award_name)        

main_url = 'https://www.basketball-reference.com/'

service = Service('C:\chromedriver-win64\chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service, options=options)

scrape_team(main_url, teams_dict)

scrape_season(main_url, season_dict, season_players_dict, player_trophies_dict)

scrape_awards(main_url, trophies_dict)

scrape_player_table(main_url, players_dict)

season_df = pd.DataFrame(season_dict)
team_df = pd.DataFrame(teams_dict)
award_df = pd.DataFrame(trophies_dict)
season_players_df = pd.DataFrame(season_players_dict)
player_trophies_df = pd.DataFrame(player_trophies_dict)
player_df = pd.DataFrame(players_dict)


season_df.to_excel('season.xlsx')
team_df.to_excel('team.xlsx')
award_df.to_excel('award.xlsx')
season_players_df.to_excel('season_player.xlsx')
player_trophies_df.to_excel('player_trophy.xlsx')
player_df.to_excel('players.xlsx')

