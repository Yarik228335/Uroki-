from bs4 import BeautifulSoup
import requests

response = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%87%D0%B5%D1%80%D0%BA%D0%B0%D1%81%D0%B8")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("p", {"class" : "today-time"})
for elem in soup_list:
    print(elem.text)
    p = elem.text
    summa = 5 * int(p)
