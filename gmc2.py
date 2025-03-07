import requests

__ENDPOINT_URL__: str = "https://telmunnshop.squareweb.app/api"

class Pakundo:
    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
    
    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/account_login", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/account_register", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")
    
    def delete(self):
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        requests.post(f"{__ENDPOINT_URL__}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_rank", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def get_key_data(self) -> any:
        params = { "key": self.access_key }
        response = requests.get(f"{__ENDPOINT_URL__}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_money", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_coins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_coins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_name", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_localid(self, id) -> bool:
        payload = { "account_auth": self.auth_token, "id": id }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_id", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def get_player_car(self, car_id) -> any:
        payload = { "account_auth": self.auth_token, "car_id": car_id }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/get_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def delete_player_friends(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/delete_friends", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_w16(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_w16", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_horns(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_horns", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def disable_engine_damage(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/disable_damage", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlimited_fuel", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_wins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_race_wins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_race_loses", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_houses", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_smoke(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_smoke", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_paid_cars(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_paid_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_all_cars(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_all_cars_siren(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_cars_siren", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def account_clone(self, account_email, account_password) -> bool:
        payload = { "account_auth": self.auth_token, "account_email": account_email, "account_password": account_password }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/clone", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_plates(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/set_plates", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_wheels(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_wheels", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_equipments_male(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_equipments_male", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_equipments_female(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_equipments_female", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def hack_car_speed(self, new_hp, new_inner_hp, new_nm, new_torque):
        payload = {
            "account_auth": self.auth_token,
            "car_id": 1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
44,
45,
46,
47,
48,
49,
50,
51,
52,
53,
54,
55,
56,
57,
58,
59,
60,
61,
62,
63,
64,
65,
66,
67,
68,
69,
70,
71,
72,
73,
74,
75,
76,
77,
78,
79,
80,
81,
82,
83,
84,
85,
86,
87,
88,
89,
90,
91,
92,
93,
94,
95,
96,
97,
98,
99,
100,
101,
102,
103,
104,
105,
106,
107,
108,
109,
110,
111,
112,
113,
114,
115,
116,
117,
118,
119,
120,
121,
122,
123,
124,
125,
126,
127,
128,
129,
130,
131,
132,
133,
134,
135,
136,
137,
138,
139,
140,
141,
142,
143,
144,
145,
146,
147,
148,
149,
150,
151,
152,
153,
154,
155,
156,
157,
158,
159,
160,
161,
162,
163,
164,
165,
166,
167,
168,
169,
170,
171,
172,
173,
174,
175,
176,
177,
178,
179,
180,
181,
182,
183,
184,
185,
186,
187,
188,
189,
190,
191,
192,
193,
194,
195,
196,
197,
198,
199,
200,
201,
202,
203,
204,
205,
206,
207,
208,
209,
210,
211,
212,
213,
214,
215,
216,
217,
218,
219,
220,
221,
222,
223,
224,
225,
226,
227,

            "new_hp": new_hp,
            "new_inner_hp": new_inner_hp,
            "new_nm": new_nm,
            "new_torque": new_torque,
        }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/hack_car_speed", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_animations(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_animations", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def max_max1(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/max_max1", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def max_max2(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/max_max2", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
