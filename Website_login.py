from selenium import webdriver
from selenium.webdriver.common.keys import Keys

sites = {
    "umeabostaden":{"Website": "https://www.bostaden.umea.se/personliga-sidan/logga-i", "UserLink": "ctl00$ContentPlaceHolder_left$InsertFieldWithControls1$LoginUC1$txtUserName", "Login": "insert_login_here", "PassLink": "ctl00$ContentPlaceHolder_left$InsertFieldWithControls1$LoginUC1$txtPassword", "Pass": "insert_password_here"}
}


#sites=[["https://www.bostaden.umea.se/personliga-sidan/logga-in"], ['ctl00$ContentPlaceHolder_left$InsertFieldWithControls1$LoginUC1$txtUserName'], ['ctl00$ContentPlaceHolder_left$InsertFieldWithControls1$LoginUC1$txtPassword'], ['insert_password_here']]

'''
url = sites[""]
driver = webdriver.Chrome('G:/Programming/chromedriver/chromedriver.exe')
driver.get(url)

u = driver.find_element_by_name('ctl00$ContentPlaceHolder_left$InsertFieldWithControls1$LoginUC1$txtUserName')
u.send_keys('insert_login_here')
p = driver.find_element_by_name('ctl00$ContentPlaceHolder_left$InsertFieldWithControls1$LoginUC1$txtPassword')
p.send_keys('insert_password_here')
p.send_keys(Keys.RETURN)

'''


url = "https://www.bostaden.umea.se/personliga-sidan/logga-in"
driver = webdriver.Chrome('G:/Programming/chromedriver/chromedriver.exe')
driver.get(url)

u = driver.find_element_by_name('ctl00$ContentPlaceHolder_left$InsertFieldWithControls1$LoginUC1$txtUserName')
u.send_keys('insert_login_here')
p = driver.find_element_by_name('ctl00$ContentPlaceHolder_left$InsertFieldWithControls1$LoginUC1$txtPassword')
p.send_keys('insert_password_here')
p.send_keys(Keys.RETURN)


url = "https://www.mitthem.se/mina-sidor/logga-in"
driver = webdriver.Chrome('G:/Programming/chromedriver/chromedriver.exe')
driver.get(url)

u = driver.find_element_by_name('ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID')
u.send_keys('insert_login_here')
p = driver.find_element_by_name('ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword')
p.send_keys('insert_password_here')
p.send_keys(Keys.RETURN)


url = "https://www.kalmarhem.se/User/MyPages.aspx?cmguid=d94a414d-b81c-41a7-92e6-eb317d7ced09"
driver = webdriver.Chrome('G:/Programming/chromedriver/chromedriver.exe')
driver.get(url)

u = driver.find_element_by_name('ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID')
u.send_keys('insert_login_here')
p = driver.find_element_by_name('ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword')
p.send_keys('insert_password_here')
p.send_keys(Keys.RETURN)

url = "https://login001.stockholm.se/siteminderagent/forms/amedborgare.jsp?TYPE=33554433&REALMOID=06-3c8c3686-a714-4f36-8fd2-e3767433fd18&GUID=1&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-plxP79%2fxqd6vbILT5FVJyEprfTdnxA5dfC3I3DlWJBdCFOtySw9lhZaOAVqi0ysl&TARGET=-SM-https%3a%2f%2fetjanster%2estockholm%2ese%2fMinaSidor%2finloggad1%2fmina--uppgifter"
driver = webdriver.Chrome('G:/Programming/chromedriver/chromedriver.exe')
driver.get(url)

u = driver.find_element_by_name('user')
u.send_keys('insert_login_here')
p = driver.find_element_by_name('password')
p.send_keys('insert_password_here')
p.send_keys(Keys.RETURN)