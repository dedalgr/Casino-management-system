# -*- coding:utf-8 -*-
'''
Created on 20.01.2023 г.

@author: dedal
'''
import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import time

CLIENT_ID = "c8b3b40a-5869-49a6-ae27-4b2a628d9564"
CLIENT_SECRET = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtleS1pZCJ9.eyJzY29wZSI6WyJlcy1hcGktZXh0ZXJuYWw6c3VibWl0LWRlY2xhcmF0aW9uIiwiZXMtYXBpLWV4dGVybmFsOmdhbWJsaW5nIiwiZXMtYXBpLWV4dGVybmFsOmFwaS1leHRlcm5hbCJdLCJleHAiOjE3MzQwNzQxOTEsImp0aSI6IjQ4OWQ4MTJlLWU0NjMtNGRjNS1iNzIyLWI1NjhjNWVjNTYwZCIsImNsaWVudF9pZCI6ImM4YjNiNDBhLTU4NjktNDlhNi1hZTI3LTRiMmE2MjhkOTU2NCJ9.MOT23QkI7PguDEfhAtSXO-hjdZqLznpK_W_QlkHdujj5tZoD3Um5gzpUU0eXxTG0XUs-Q8gcQpqnDV2GgiHr9nh7oX3v_uxWTbXYnK9p2nLwCq-_BmYfElVkByGht836lVTQN2WjhkH-dTFmhTBtoUhfSW_LHKDMa7biwlAkQRJk-7BIpkm9iMYfiSqsS8yVnvs1IIx9AizIOWJINNV7ojKfTBs_5e7svSKB1jj2298nb8U269aX2g8tprskCI5E1NRnfFUntQbxv6Ply7fYVdS_xuSSUyfltGNJDI1L7CZxY5ztZ5PAKAtcFRTr3Cuawu1-ysHQb5nv5mekLx-DCA'


class BadNRArequest(Exception):
    pass


class NRA():

    def __init__(self, client_id, token, debug=False, timeout=8):
        self.client_id = client_id
        self.token = "Bearer " + token
        self.timeout = timeout
        if debug is False:
            self.ACCESS_TOKEN_URL = "https://public-api.nra.bg/gambling/gambling-service/register"
        else:
            self.ACCESS_TOKEN_URL = "https://public-api.nra.bg/gambling/gambling-test-service/register"

    def chk_egn(self, egn):
        self.oauth = OAuth2Session(client=BackendApplicationClient(client_id=self.client_id, access_token=self.token))
        data = {
            "pin": egn,
            "pinType": "IND_EGN"
        }
        try:
            tmp = self.oauth.post(self.ACCESS_TOKEN_URL,
                              headers={"Authorization": self.token, "Content-Type": "application/json; "},
                              json=data, timeout=self.timeout, verify=True)
        except Exception as e:
            print (e)
            time.sleep(0.5)
            return None
            # tmp = self.oauth.post(self.ACCESS_TOKEN_URL,
            #                       headers={"Authorization": self.token, "Content-Type": "application/json; "},
            #                       json=data, timeout=self.timeout)

        try:
            tmp.close()
            self.oauth.close()
        except:
            pass
        if tmp.ok is True:
            if tmp.json()['responseCode'] == 0:
                return False
            else:
                return True
        else:
            raise BadNRArequest(tmp.reason, tmp.json())



if __name__ == '__main__':
    client = NRA(CLIENT_ID, CLIENT_SECRET, debug=False)
    print(client.chk_egn('8703042226'))
    # ACCESS_TOKEN_URL = "https://public-api.nra.bg/gambling/gambling-test-service/register"
    # oauth = OAuth2Session(client=BackendApplicationClient(client_id=CLIENT_ID, access_token=CLIENT_SECRET))
    # data = {
    #     "pin": "8310205560",
    #     "pinType": "IND_EGN"
    # }
    # data = oauth.post(ACCESS_TOKEN_URL, headers={"Authorization": CLIENT_SECRET, "Content-Type": "application/json; "},
    #                   json=data)
    # print(data.json())
