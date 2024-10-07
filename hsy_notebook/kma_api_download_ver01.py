from urllib.request import urlopen

domain = "https://~~"
tm = "txx"
stn_id = "dd"
option = "dd"
auth = "xx"

url = domain + tm + stn_id + option + auth
with urlopen(url) as f:
    html = f.read()
    print(html)
