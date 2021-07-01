import re, requests

url = 'http://www.columbia.edu/~fdc/sample.html'
print(re.findall(r"<h3.+?>(.*)</h3>", requests.get(url).text))
