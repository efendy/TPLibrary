"""
Client

@author efendy.setiawan@theplatform.com
last modified: 20191112
"""
import json
from urllib import request, parse
from utils.FileManager import FileManager


# DataServiceClient
class DataServiceClient:
    fm = FileManager("", "DataServiceClient", "DataServiceClient")

    def __init__(self, data_object_class, token, account_uri):
        self.data_object_class = data_object_class
        self.base_url = data_object_class.endpoint_uri
        self.data = {
            "totalResults": 0,
            "startIndex": 0,
            "itemsPerPage": 0,
            "entryCount": 0,
            "entries": []
        }
        self.preset_params = data_object_class.preset_params
        self.preset_params["token"] = token
        self.preset_params["account"] = account_uri
        self.preset_params["count"] = "true"
        self.preset_params["form"] = "cjson"
    
    def get_data(self):
        return self.data

    def get_total(self):
        return self.data.get("totalResults", 0)

    def get_entries(self):
        return self.data.get("entries", [])

    def get_size(self):
        return self.data.get("entryCount", 0)
        
    def get_parameters(self):
        return self.parameters
    
    def queries(self, in_dict):
        self.parameters = ""
        for key in self.preset_params.keys():
            value = parse.quote(str(self.preset_params[key]), safe='')
            self.parameters += key + "=" + value + "&"
        for key in in_dict.keys():
            value = parse.quote(str(in_dict[key]), safe='')
            self.parameters += key + "=" + value + "&"

    def request_get(self):
        rsp = False
        if self.parameters is None:
            self.queries({})
        self.data["entries"] = []

        request_url = "http://" + self.base_url + "?" + self.parameters
        self.fm.log_info("REQUEST url={}".format(request_url))

        response_data = request.urlopen(request_url).read()
        self.fm.log_info("RESPONSE data={}".format(response_data))
        if not response_data is None:
            response_json = json.loads(response_data)
            if response_json is not None and response_json.get("entryCount") is not None:
                self.data["totalResults"] = response_json.get("totalResults", 0)
                self.data["startIndex"] = response_json.get("startIndex", 0)
                self.data["itemsPerPage"] = response_json.get("itemsPerPage", 0)
                self.data["entryCount"] = response_json.get("entryCount", 0)
                for entry in response_json.get("entries", []):
                    item = self.data_object_class(entry)
                    self.data["entries"].append(item)
                    rsp = True
            else:
                self.fm.log_error("RESPONSE data={}".format(response_data))
        
        return rsp
    
    def request_post(self, data_arr):
        rsp = False
        if self.parameters is None:
            self.queries({})

        request_url = "http://" + self.base_url + "/feed?" + self.parameters
        self.fm.log_info("REQUEST url={} data={}".format(request_url, data_arr))

        request_data = json.dumps({
            "entries": data_arr
        }).encode()
        req = request.Request(request_url, data=request_data)
        req.add_header('Content-Type', 'application/json')
        response_data = request.urlopen(req).read()
        self.fm.log_info("RESPONSE data={}".format(response_data))
        
        if not response_data is None:
            response_json = json.loads(response_data)
            if response_json is not None and response_json.get("entryCount") is not None:
                rsp = True

        return rsp


# WebClient
class WebClient:
    fm = FileManager("", "WebClient", "WebClient")

    def __init__(self, service_object_class, token, account_uri):
        self.service_object_class = service_object_class
        self.base_url = service_object_class.endpoint_uri
        self.preset_params = service_object_class.preset_params
        self.preset_params["token"] = token
        self.preset_params["account"] = account_uri
        self.preset_params["form"] = "json"
    
    def get_parameters(self):
        try:
            if self.parameters is None:
                self.queries({})
        except:
            self.queries({})
        return self.parameters

    def queries(self, in_dict):
        self.parameters = ""
        for key in self.preset_params.keys():
            value = parse.quote(str(self.preset_params[key]), safe='')
            self.parameters += key + "=" + value + "&"
        for key in in_dict.keys():
            value = parse.quote(str(in_dict[key]), safe='')
            self.parameters += key + "=" + value + "&"

    def request(self, data_arr):
        rsp = False

        request_url = "http://" + self.base_url + "?" + self.get_parameters()
        self.fm.log_info("REQUEST url={} data={}".format(request_url, data_arr))
        # request_data = json.dumps({
        #     "entries": data_arr
        # }).encode()
        request_data = json.dumps(data_arr).encode()
        req = request.Request(request_url, data=request_data)
        req.add_header('Content-Type', 'application/json')
        response_data = request.urlopen(req).read()
        self.fm.log_info("RESPONSE data={}".format(response_data))

        if not response_data is None:
            # TODO need more handling here
            response_json = json.loads(response_data)
            try:
                if not response_json.get("isException"):
                    print("PUBLISH is Success")
                    rsp = True
                else:
                    print("PUBLISH is Exception")
            except:
                rsp = False

        return rsp
