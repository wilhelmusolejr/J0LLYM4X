# IMPORTS
from cmath import pi
import random
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# CONFIGURATION
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--auto-open-devtools-for-tabs");
chrome_options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
driver_service = Service(executable_path="C:\\Users\\Administrator\\Desktop\\Automation\\Jollymax\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service, options=chrome_options, service_log_path='NUL')
d = driver.command_executor._url

# VARIABLES
timeout = 10

# ACCOUNT
user_email_fb = ''
user_pass = ''
user_phone = ''
user_pin = ''
user_num = ''
user_email = ''


# FOLDER CONFIGURATION
path = "C:/Users/Administrator/Desktop/Automation/Jollymax/transaction"
# os.mkdir(path);

random_fold_num = random.randint(1, 100)
random_fold = False
if os.path.exists(path + "/pin "+user_phone+"(0).txt"):
  fh = open(path + "/pin "+user_phone+"("+ str(random_fold_num) +").txt", "w")
  random_fold = True
else:
  fh = open(path + "/pin "+user_phone+"(0).txt", "w")

fh.write(f"\n - - - - - P I N - - - - - ")
fh.write(f"\n -")
fh.write(f"\n -")
fh.close()

class Denoes:
  def __init__(self, rgDeno, denoClick, target, quantity = 5):
    self.rgDeno = rgDeno
    self.denoClick = denoClick
    self.target = target
    self.quantity = quantity
    self.pin = []

# Number of available voucher
one = 1
twentyThree = 2
thirtySeven = 1
eightyFive = 0
oneTwentyNine = 1

# DATA
deno = {
  '1': Denoes(20, "1", 0, one),
  '23': Denoes(50, "2", 0, twentyThree),
  '37': Denoes(100, "3", 0, thirtySeven),
  '85': Denoes(150, "3", 1, eightyFive),
  '129': Denoes(300, "4", 0, oneTwentyNine)
}

def checkIfLoggedIn():
  print(1)

def footerChecker():
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#layoutMeScroll > div:nth-child(2) > div > div.footer-copyright")))
  
def goToSite(url):
  driver.get(url)
  footerChecker()
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#layoutMeScroll > div:nth-child(2) > div > div.footer-copyright")))

def choosingDeno(target, deno):

  if target == 0: 
      kind = "PH_War_of_Rings_vouchers_"
  elif target == 1: 
      kind = "PH_mu_original_2_vouchers_"

  targetInitial = "#" + kind
  url_target = targetInitial + "4" + " > div:nth-child("+str(deno)+") > div.goods-desc"

  # choosing deno
  #PH_War_of_Rings_vouchers_4 > div:nth-child(2) > div.goods-desc
  driver.find_element(By.CSS_SELECTOR, url_target).click()
  # Inputting email
  form_email_element = "#" + kind + "9 > form > div > div.form-block > div > div:nth-child(3) > div > div > div > div.el-input.el-input--prefix.el-input--suffix > input"
  email = driver.find_element(By.CSS_SELECTOR, form_email_element).get_attribute('value')
  #PH_War_of_Rings_vouchers_9 > form > div > div.form-block > div > div:nth-child(3) > div > div > div > div.el-input.el-input--prefix.el-input--suffix > input
  if not email:
    driver.find_element(By.CSS_SELECTOR, form_email_element).send_keys(user_email)
  # Clicking Buy Now
  driver.find_element(By.CSS_SELECTOR, targetInitial + "10 > div > div.button-main > div > button").click()
  # Buy confirmation
  elem_confirm_but = "#layoutMeScroll > div:nth-child(2) > div > div.shareit-app.shareit-app-detail.page > div.shareit-detail-common-page > div:nth-child(2) > div.el-dialog__wrapper.order-confirm-dlg > div > div.el-dialog__footer > span > button.el-button.button.confirm-button.el-button--primary"
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, elem_confirm_but)))
  time.sleep(2)
  driver.find_element(By.CSS_SELECTOR, "#layoutMeScroll > div:nth-child(2) > div > div.shareit-app.shareit-app-detail.page > div.shareit-detail-common-page > div:nth-child(2) > div.el-dialog__wrapper.order-confirm-dlg > div > div.el-dialog__footer > span > button.el-button.button.confirm-button.el-button--primary").click()
  time.sleep(3)
  driver.close();
  driver.switch_to.window(driver.window_handles[0])

def buyingDeno(isLoggedIn, voucher):
  if not isLoggedIn:
    # ----- page payment
    # --- gcash login
    # ----- wait for page appearance -- waiting for input 
    print("login area")
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div/input")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div/input").send_keys(user_phone)
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[1]/footer/div/button')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/footer/div/button').click()

    # ----- page payment
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div[1]/h2")))
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "ap--current")))

    # print("otp area")
    otp = input("OTP: ")
    for i in otp:
      driver.find_element(By.XPATH, "//input[@type='tel']").send_keys(i)
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[4]/button')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[4]/button').click()

    # print("mpin area")
    # ----- page payment
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/p")))
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//input[@type='tel']")))
    for i in user_pin:
      driver.find_element(By.XPATH, "//input[@type='tel']").send_keys(i)
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/footer/div/button')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/footer/div/button').click()

  # ----- page payment
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/footer/div/button")))
  WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/footer/div/button")))
  driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/footer/div/button").click();

  # ----- page payment
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='success-page']/div[1]/footer/div[2]/button")))
  WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='success-page']/div[1]/footer/div[2]/button")))
  driver.find_element(By.XPATH,"//*[@id='success-page']/div[1]/footer/div[2]/button").click();

  # ----- page payment
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div/div/div/div/div[1]/div[1]/div/div/div[1]/p")))
  print("Payment successful")
  driver.find_element(By.XPATH,"//*[@id='app']/div/div/div/div/div[1]/div[2]/div/p").click();
  time.sleep(2)
  footerChecker()

  # ----- page payment
  element_succ = "#layoutMeScroll > div:nth-child(2) > div > div.shareit-app.cdk.shareit-app-result-xs > div.shareitResult-container > div.cdk-part > div.cdk-value-container > span"
  time.sleep(5)
  pinLocator = driver.find_element(By.CSS_SELECTOR, element_succ).get_attribute('textContent')
  while len(pinLocator) == 0:
    driver.refresh()
    time.sleep(10)
    pinLocator = driver.find_element(By.CSS_SELECTOR, element_succ).get_attribute('textContent')

  # pinLocator = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='layoutMeScroll']/div[2]/div/div[1]/div[1]/div[1]/div/div[2]")))
  pin_game = driver.find_element(By.CSS_SELECTOR, element_succ).get_attribute('textContent')
  print(pin_game)
  # deno[voucher].append(1)
  # pin = pin_game.split(" ")
  pin = pin_game.split(" ")[1]
  addtoNotepad(voucher, pin)
  print(pin)
  return pin



def updateData(data, voucher):
  data[voucher] -= 1;

def updateNotepad(data, pin):
  fh = open( "/pin.txt", "w")
  fh.write(f"\n - - - - - P I N - - - - - ")
  fh.write(f"\n - ")
  fh.close()

def addtoNotepad(voucher, pin):
  if random_fold:
    fh = open(path + "/pin "+user_phone+"("+ str(random_fold_num) +").txt", "a")
  else:
    fh = open(path + "/pin "+user_phone+"(0).txt", "a")

  fh.write(f"\n - " + str(voucher) + " RG PIN")
  # fh.write(f"\n - " + pin)
  fh.close()

def notepad(deno, pin):
  # print(" ----- notepad ")
  # print(deno)
  # print(len(deno.pin))
  # print(deno.quantity)

  if random_fold:
    fh = open(path + "/pin "+user_phone+"("+ str(random_fold_num) +").txt", "a")
  else:
    fh = open(path + "/pin "+user_phone+"(0).txt", "a")

  # fh = open(path + "/pin "+user_phone+".txt", "a")

  if len(deno.pin) == 1:
    fh.write(f"\n ----- " + str(deno.rgDeno) + " * " + str(deno.quantity) + " = " + str(deno.rgDeno * deno.quantity))
  if len(deno.pin) >= 1 and len(deno.pin) <= deno.quantity:
    fh.write(f"\n - PIN " + pin)
  if len(deno.pin) == deno.quantity:
    fh.write(f"\n -")
    fh.write(f"\n -")

  fh.close()
  


# ----- Page Facebook
# print("page Facebook")
driver.get("https://www.facebook.com")
driver.find_element(By.XPATH, "//*[@id='m_login_email']").send_keys(user_email_fb)
driver.find_element(By.XPATH, "//*[@id='m_login_password']").send_keys(user_pass)
driver.find_element(By.XPATH, "//*[@id='login_password_step_element']/button").click();
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div[1]/div/div/h3")))

# print("page Jollymax")
# ----- Page initial
driver.get("https://www.jollymax.com/ph")
time.sleep(4)
# -- wait for page appearance
print("wait for page appearance")
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div/div[1]/div/div[2]/div[2]/div/div[1]")))
# driver.find_element(By.XPATH, "//*[@id='app']/div/div[5]/div/div[2]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div/div[4]/div/div[2]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/div[2]/div/div[1]").click()
# -- Login to jollymax
driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]").click();
time.sleep(5)

# ----- page payment 
urls = ["https://www.jollymax.com/ph/War_of_Rings_vouchers?", "https://www.jollymax.com/ph/mu_original_2_vouchers?"]

initial = True
for attr, value in deno.items():
  tempQuantity = deno[attr].quantity
  print("--------------------------")
  print("--- Buying for " + attr)
  while tempQuantity != 0:
    goToSite(urls[deno[attr].target])
    choosingDeno(deno[attr].target, deno[attr].denoClick)
    if initial:
      deno[attr].pin.append(buyingDeno(False, deno[attr].rgDeno))
      initial = False
    else:
      deno[attr].pin.append(buyingDeno(True, deno[attr].rgDeno))
    notepad(deno[attr], deno[attr].pin[-1])
    tempQuantity -= 1
    time.sleep(3)

print("Transaction done")
exit = int(input("OTP: "));

if exit == 1:
  driver.close()
  
