import requests
from http import HTTPStatus as StatusCodes

links = [
    'https://stage-tody.sptech.team/auth/login',
    'https://stage-tody.sptech.team/demo/list',
    'https://stage-tody.sptech.team/provider/list',
    'https://stage-tody.sptech.team/tag/list',
    'https://stage-tody.sptech.team/language/list'
]


def configure_pages_in_domain():
    for link in links:
        print(link)
        response = requests.get(link, timeout=20)
        if not response.status_code == StatusCodes.OK:
            return print(f"error code: {response.status_code} {link}")
        else:
            print(f'All is OK!:), status code is: {response.status_code}\n')


configure_pages_in_domain()
