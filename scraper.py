from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

season_dict = {'season_id' : [], 'season_champion_team' : []}
teams_dict = {'team_id' : [], 'team_name' : [], 'from' : [], 'to' : [], 'years' : [], 'games' : [], 'wins' : [], 'losses' : [], 'W/L_percent' : [] , 'years_league_champion' : []}
season_players_dict = {'season_id' : [], 'player_id' : [], 'team_id' : [], 'points' : []}
trophies_dict = {'trophy_id' : [], 'trophy_name' : []}
player_trophies_dict = {'player_id' : [], 'season_id' : [], 'trophy_id' : []}

def scrape_team(main_url):
    driver.get(main_url + "teams/")
    teams = driver.find_elements(By.XPATH, '//tbody/tr[@class="full_table"]')
    for item in teams:
        team_name_id = item.find_element(By.XPATH, './th/a')
        team_name = team_name_id.text
        team_id = team_name_id.get_attribute('href')[37:-1]
        print(team_name)
        print(team_id)
        first_year = item.find_element(By.XPATH, './td[@data-stat="year_min"]').text
        print(first_year)
        last_year = item.find_element(By.XPATH, './td[@data-stat="year_max"]').text
        print(last_year)
        years = item.find_element(By.XPATH, './td[@data-stat="years"]').text
        print(years)
        games = item.find_element(By.XPATH, './td[@data-stat="g"]').text
        print(games)
        wins = item.find_element(By.XPATH, './td[@data-stat="wins"]').text
        print(wins)
        losses = item.find_element(By.XPATH, './td[@data-stat="losses"]').text
        print(losses)
        win_loss_percent = item.find_element(By.XPATH, './td[@data-stat="win_loss_pct"]').text
        print(win_loss_percent)
        years_league_champion = item.find_element(By.XPATH, './td[@data-stat="years_league_champion"]').text
        print(years_league_champion)
        print('----------------------------------------')
        
def scrape_player(url, next_url):
    driver.get(url + next_url)
    row_num = 0
    for i in range(50):

        print(row_num)
        player_id = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="name_display"]/a').get_attribute('href')[37:-5]
        print(player_id)
        trophies = driver.find_elements(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="awards"]/a')
        for trophy in trophies:
            if(trophy.text != 'AS' and not('NBA' in trophy.text)):
                trophy_str = trophy.text.split('-')
                trophy_rank = trophy_str[1]
                trophy_id = 'awards/' + trophy_str[0]
                print(trophy_id)
                print(trophy_rank)
        player_team = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="team_name_abbr"]/a')
        player_team_id = player_team.get_attribute('href')[37:-10]
        player_points = driver.find_element(By.XPATH, f'//tbody/tr[@data-row="{row_num}"]/td[@data-stat="pts"]').text
        print(player_points)
        print(player_team_id)
        if player_team.text == '2TM':
            row_num += 2
        else:
            row_num += 1
        print('---------------------')

        
def scrape_season(main_url):
    for i in range(2, 13):
        url = main_url + "leagues/"
        driver.get(url) 
        season = driver.find_element(By.CSS_SELECTOR, f'tbody tr[data-row="{i}"] th a')
        season_splitted = season.get_attribute('href').split('/')
        season_id = season_splitted[-1][-9 : -5]
        print(season_id) # both id and end year
        
        season_champion = driver.find_element(By.CSS_SELECTOR, f'tbody tr[data-row="{i}"] td[data-stat="champion"] a').get_attribute('href')
        print(season_champion.replace(season_id, '')[37:-6])
        
        next_url = f"NBA_{season_id}_totals.html"
        scrape_player(url, next_url)
        
def scrape_awards(main_url):
    url = main_url + "awards/"
    driver.get(url)
    nba_awards  = driver.find_elements(By.XPATH, '//div[@class=" forcefull"]/h2[text()="NBA & ABA Season Awards"]/following-sibling::p/a')
    for item in nba_awards:
        award_link = item.get_attribute('href')[37:-5]
        print(award_link)
        award_name = item.text
        print(award_name)        
        

main_url = 'https://www.basketball-reference.com/'

service = Service('C:\chromedriver-win64\chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service, options=options)

scrape_team(main_url)

scrape_season(main_url)

scrape_awards(main_url)

