# Be nice to move this to BS
from selenium import webdriver
browser = webdriver.Chrome()

def google():
    links_list = []
    dorks = {
        'workable_security': "remote and security site:workable.com daterange:2458120-2458134",
        'workable_devops': "remote and devops and infrastructure site:workable.com daterange:2458120-2458134",
        'greenhouse': "remote and security site:boards.greenhouse.io daterange:2458120-2458134",
        'greenhouse_devops': "remote and devops and infrastructure site:boards.greenhouse.io daterange:2458120-2458134",
            }
    for i in dorks.keys():
        browser.get('http://www.google.com/search?q=' + dorks[i] + "&t=h_&ia=web")
        links = browser.find_elements_by_xpath("//h3//a[@href]")
        for elem in links:
            link = elem.get_attribute("href")
            links_list.append(link)
        #browser.get('http://www.google.com/search?q=' + dorks[i] + "&t=h_&ia=web&start=10")
        #for elem in links:
        #    link = elem.get_attribute("href")
        #    links_list.append(link)
    browser.quit()
    return links_list
