import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.findAll(attrs='css-1dmex2s e1kk1ckf0'):
    name = a.find('h5')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='css-1dmex2s e1kk1ckf0'):

    category = b.find('p')
    if category not in results:
        other_results.append(category.text)
print(results)
print(other_results)
df = pd.DataFrame({'Names': results, 'Categories': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')


