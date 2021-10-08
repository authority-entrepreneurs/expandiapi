import json

import requests


class GoHighLevel:

    def __init__(self, cred_headers=None):
        self.cred_headers = {
            'Authorization': 'Bearer 198b4460-2877-4e59-a6da-90e426024c82',
            'Content-Type': 'application/json'
        }
    
    def contact_lookup(self, email):

        contact_lookup_url = "https://rest.gohighlevel.com/v1/contacts/lookup"
        params = {"email":email}

        response = requests.request("GET", contact_lookup_url, 
                                    headers=self.cred_headers, 
                                    params=params)
        if response.status_code == 200:
            contact_person_id = response.json().get('contacts')[0].get('id')
            edit_contact_urls = 'https://rest.gohighlevel.com/v1/contacts/{id}'.format(id=contact_person_id)
            payload = params
            response = requests.request("PUT", edit_contact_urls, 
                                    headers=self.cred_headers, 
                                    data=json.dumps(payload))
        else:
            create_contact_urls = 'https://rest.gohighlevel.com/v1/contacts/'
            payload = params

            response = requests.request("POST", create_contact_urls, 
                                    headers=self.cred_headers, 
                                    data=json.dumps(payload))
        print(response.json())
        return response.json()

go_high = GoHighLevel()
