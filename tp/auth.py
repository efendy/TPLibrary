"""
Authentication

https://docs.theplatform.com/help/wsf-authentication-endpoint

@author efendy.setiawan@theplatform.com
last modified: 20191030
"""

import json
from urllib import request, parse

class Authentication:

    def __init__(self, mpx_user, mpx_pass):
        self.token = ""
        self.mpx_user = mpx_user
        self.mpx_pass = mpx_pass
    
    def sign_in(self):
        endpoint_uri = "https://identity.auth.theplatform.com/idm/web/Authentication/signIn"
        params = {
            "schema": "1.1"
            ,"form": "json"
            ,"username": self.mpx_user
            ,"password": self.mpx_pass
            ,"_duration":"600000"
            # ,"_idleTimeout":""
        }
        token = ""
        response_data = self.request(endpoint_uri, params)
        if not response_data is None:
            sign_in_response = response_data.get("signInResponse")
            if sign_in_response is not None:
                token = sign_in_response.get("token")
            else:
                self.print_data("RESPONSE", response_data)
        return token
    
    def sign_out(self):
        endpoint_uri = "https://identity.auth.theplatform.com/idm/web/Authentication/signOut"
        params = {
            "schema": "1.1"
            ,"form": "json"
            ,"_token": self.token
        }
        rsp = False
        response_data = self.request(endpoint_uri, params)
        if not response_data is None:
            sign_in_response = response_data.get("signOutResponse")
            if sign_in_response is not None:
                rsp = True
            else:
                self.print_data("RESPONSE", response_data)
        return rsp
    
    def request(self, uri, params={}):
        rsp = None
        parameters = ""
        for key in params.keys():
            value = parse.quote(params[key], safe='')
            parameters += key + "=" + value + "&"
        request_url = uri + "?" + parameters
        response_data = request.urlopen(request_url).read()
        if not response_data is None:
            response_json = json.loads(response_data)
            return response_json
        return rsp
    
    def get_token(self):
        if self.token is None or self.token is "":
            self.token = self.sign_in()
        return self.token

    def print_data(self, type, data):
        print(type + " DATA -> START")
        print(data)
        print(type + " DATA <- END")