from selenium import webdriver
from getpass import getpass
import os.path as path

driver = webdriver.Firefox()
driver.get("https://fiwifi.fi.upm.es:8003/index.php?zone=fiwifi&redirurl=http%3A%2F%2Fgoogle.com%2F")

username = driver.find_element_by_name("auth_user")
password = driver.find_element_by_name("auth_pass")

if not path.isfile("./.secret"):
    user = input("Matricula: ")
    with open("./.secret", "w") as secret_file:
        secret_file.write(user)
        secret_file.close()
    username.send_keys(user.strip())
else:
    with open("./.secret", "r") as secret_file:
        user = secret_file.readline().strip()
        username.send_keys(user)

user_pass = getpass("Password: ")
password.send_keys(user_pass)

driver.find_element_by_name("accept").click()
driver.close()
