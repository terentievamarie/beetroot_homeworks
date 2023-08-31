import requests

def get_robots_txt(url):
    if not url.startswith("http"):
        url = "http://" + url
    if not url.endswith("/"):
        url = url + "/"
    
    url =url +"robots.txt"
    response = requests.get(url)

    if response.status_code == 200:
        with open('robots.txt','w') as f:
            f.write(response.text)
            print("It's ok. File saved to 'robots.txt'.")
    else:
        print("Failed.")

get_robots_txt("http://wikipedia.org/")