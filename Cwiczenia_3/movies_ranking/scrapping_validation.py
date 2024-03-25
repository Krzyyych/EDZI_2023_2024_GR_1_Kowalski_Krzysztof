import urllib.robotparser

def is_scrapping_allowed(url, using_url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(f"{url}robots.txt/")
    rp.read()
    return rp.can_fetch("MyBot", using_url)