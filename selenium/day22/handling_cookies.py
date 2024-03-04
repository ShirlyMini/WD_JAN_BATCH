from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
###############3gvet all cookies
# print(driver.get_cookies())
# print(len((driver.get_cookies())))
#
# for i in driver.get_cookies():
#     print("name of cookie", i["name"])
#     print("value of cookie", i["value"])
    #print("expiry of cookie", i["expiry"])

# [
# {'domain': '.rediff.com', 'expiry': 1723297749, 'httpOnly': False, 'name': '__eoi', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ID=a2cdaab27db5263b:T=1707745749:RT=1707745749:S=AA-AfjZKHr6ZbSlMT8AXjCHd9W6h'}, {'domain': '.rediff.com', 'expiry': 1739281750, 'httpOnly': False, 'name': 'connectId', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '{"ttl":86400000,"lastUsed":1707745750010,"lastSynced":1707745750010}'},
# {'domain': '.rediff.com', 'expiry': 1741441749, 'httpOnly': False, 'name': '__gpi', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'UID=00000d0480d962d1:T=1707745749:RT=1707745749:S=ALNI_MZ7uj-qVl3u0H_V7vjGxsePNz9HQw'}, {'domain': '.rediff.com', 'expiry': 1741441750, 'httpOnly': False, 'name': 'cto_bundle', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'zgkbGF92NVlLSXFiZEJOWHhoME5FTjglMkZoVzB1UXZLYkZaUHY3WW9aN0hDcXN0YTZ5bklNT055ekRoZXVXVGVxVWR6WTRNV0pmMUNLSWVlb09YblZvJTJGdDhncnZkU3pqeUVtaENja3lJMmF6MUNYZ1R5S1ZhdUl2Z1RDZ2tyWiUyRnpZVmxQdjRHRVdDS2VNeW4lMkJMSlQ1aVV5NTJjQSUzRCUzRA'},
# {'domain': '.rediff.com', 'expiry': 1741441749, 'httpOnly': False, 'name': '__gads', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ID=606efc23ee9dafca:T=1707745749:RT=1707745749:S=ALNI_MbYfb9XnFZW-xSV-km8853-XvUtxA'}, {'domain': '.rediff.com', 'expiry': 1707832150, 'httpOnly': False, 'name': 'panoramaId_expiry', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1707832149806'}, {'domain': '.rediff.com', 'expiry': 1707745758, 'httpOnly': False, 'name': 'lotame_domain_check', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'rediff.com'}, {'domain': '.rediff.com', 'expiry': 1731073749, 'httpOnly': False, 'name': '_cc_id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '90f68aec766ed23cc82e0ad3c028d1af'}, {'domain': '.rediff.com', 'expiry': 1742305747, 'httpOnly': False, 'name': 'RuW', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'e0ad24cd.6112f8ab49152'}, {'domain': '.money.rediff.com', 'expiry': 1707832146, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.1100358179.1707745746'}, {'domain': 'money.rediff.com', 'httpOnly': False, 'name': 'pbjs_debug', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'null'}, {'domain': '.money.rediff.com', 'expiry': 1742305746, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.802806841.1707745746'}]

#############add cookie

driver.add_cookie({'name': 'mycookie', 'value': "123456789"})
print(driver.get_cookie("mycookie"))

##################delete cookie

driver.delete_cookie('mycookie')
print(driver.get_cookie("mycookie"))#None

#######################delete all cookies
print(len((driver.get_cookies())))
driver.delete_all_cookies()
print(len((driver.get_cookies())))