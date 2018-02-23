import requests
import config as cfg


# Ninja Jobs login
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
client = requests.Session()


def connect_ninja_jobs(username, password):
    login_information = {
        'username': username,
        'password': password,
    }
    client.post(cfg.ninja_jobs_login, headers=headers, data=login_information)
    ninja_job_listings = client.get(cfg.ninja_jobs, headers=headers)
    print(ninja_job_listings.text)
    return ninja_job_listings.text
