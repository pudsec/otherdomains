import re
import requests

r = requests.get(
    'https://tld-list.com/tlds-from-a-z',
    headers={
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    },
)

with open('tlds.txt', 'w') as f:
    f.write('\n'.join(re.findall(r'href="/tld/([a-z0-9-\.]+)"', r.text, flags=re.I)))
