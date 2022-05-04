import sys

if len(sys.argv) != 2:
    exit(f'Usage: python3 {sys.argv[0]} domain')

domain = sys.argv[1].lower().split('.')[0]

import dns.resolver
import requests

from datetime import datetime
from pathlib import Path

tlds_file = Path.joinpath(Path.home(), '.tlds.txt')

if not Path.exists(tlds_file) or (datetime.now() - datetime.fromtimestamp(Path(tlds_file).stat().st_mtime)).days >= 30:
    r = requests.get('https://github.com/pudsec/otherdomains/raw/main/tlds.txt')
    with open(tlds_file, 'w') as f:
        f.write('\n'.join(r.text.strip().splitlines()))

with open(tlds_file) as f:
    tlds = f.read().strip().splitlines()

for extension in tlds:
    domain_name = f'{domain}.{extension}'
    try:
        a = dns.resolver.resolve(domain_name, 'a')
        print(domain_name, ','.join([_.to_text().strip().rstrip('.') for _ in a]))
    except (KeyboardInterrupt):
        exit('Terminated...')
    except:
        pass
