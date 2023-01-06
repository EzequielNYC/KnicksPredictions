from selenium import webdriver
from selenium.webdriver.common.by import By
import time




# accessing chrome page 
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# javascript load up
driver.implicitly_wait(5)

# accessing website 
driver.get("https://www.teamrankings.com/nba/team/new-york-knicks")

# getting basic table from page 
table = driver.find_element(by='id', value='DataTables_Table_0')

# creating txt file with data 
with open("updated1_test.txt","w") as f:
    f.write(table.text)

#switches pages to betting table  
link = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[3]/main/div[3]/a[2]")

print("---------------------------")

# gets betting view 
link.click()
time.sleep(1)
table = driver.find_element(by='id', value='DataTables_Table_0')


# appending second page data 
with open("updated1_test.txt","a") as f:
    f.write(table.text)

driver.close()


