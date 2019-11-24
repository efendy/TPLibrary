"""
MPX Objects

Media - https://docs.theplatform.com/help/media-media-object
Program - https://docs.theplatform.com/help/tvds-program-fields
ProgramAvailability - https://docs.theplatform.com/help/tvds-programavailability-fields

@author efendy.setiawan@theplatform.com
last modified: 20191030
"""
from datetime import datetime


class Media:
    endpoint_uri = "data.media.theplatform.com/media/data/Media"
    preset_params = {
        "schema": "1.10.0",
        "searchSchema": "1.0.0"
    }

    def __init__(self, in_dict):
        self.source = in_dict
        self.id = in_dict.get("id", "")
        self.guid = in_dict.get("guid", "")
        self.title = in_dict.get("title", "")

    def get(self, key, default=None):
        try:
            value = self.source.get(key)
            if value is None:
                return default
            else:
                return value
        except KeyError:
            return default

    def set(self, key, value):
        try:
            value = self.source.get(key)
            if not value is None:
                self.source[key] = value
        except KeyError:
            return False
        return True


class Program:
    endpoint_uri = "data.entertainment.tv.theplatform.com/entertainment/data/Program"
    preset_params = {
        "schema": "2.17.0",
        "searchSchema": "1.3.0"
    }

    def __init__(self, in_dict):
        self.source = in_dict
        self.id = in_dict.get("id", "")
        self.guid = in_dict.get("guid", "")
        self.title = in_dict.get("title", "")

    def get(self, key, default=None):
        try:
            value = self.source.get(key)
            if value is None:
                return default
            else:
                return value
        except KeyError:
            return default
            
    def set(self, key, value):
        try:
            value = self.source.get(key)
            if not value is None:
                self.source[key] = value
        except KeyError:
            return False
        return True


class ProgramAvailability:
    endpoint_uri = "data.entertainment.tv.theplatform.com/entertainment/data/ProgramAvailability"
    preset_params = {
        "schema": "2.17.0",
        "searchSchema": "1.3.0"
    }

    def __init__(self, in_dict):
        self.source = in_dict
        self.id = in_dict.get("id", "")
        self.guid = in_dict.get("guid", "")
        self.series_guid = ""
        if not in_dict.get("seriesId") is None:
            self.series_guid = str(in_dict.get("seriesId").split('/')[-1])
        self.series_title = ""
    
    def get(self, key, default=None):
        try:
            value = self.source.get(key)
            if value is None:
                return default
            else:
                return value
        except KeyError:
            return default
    
    def get_series_title(self):
        return self.series_title

    def set_series_title(self, value):
        self.series_title = value


class PublishProfile:
    endpoint_uri = "data.publish.theplatform.com/publish/data/PublishProfile"
    preset_params = {
        "schema": "1.11.0"
    }

    def __init__(self, in_dict):
        self.source = in_dict
        self.id = in_dict.get("id", "")

    def get(self, key, default=None):
        try:
            value = self.source.get(key)
            if value is None:
                return default
            else:
                return value
        except KeyError:
            return default


class ProfileResult:
    endpoint_uri = "data.workflow.theplatform.com/workflow/data/ProfileResult"
    preset_params = {
        "schema": "1.3.0"
    }

    def __init__(self, in_dict):
        self.source = in_dict
        self.id = in_dict.get("id", "")
        self.mediaId = in_dict.get("mediaId", "")
        self.profileId = in_dict.get("profileId", "")
        self.status = str(in_dict.get("status", "")).lower()
        # id,mediaId,profileId,service,status

    def get(self, key, default=None):
        try:
            value = self.source.get(key)
            if value is None:
                return default
            else:
                return value
        except KeyError:
            return default


class Product:
    endpoint_uri = "data.product.theplatform.com/product/data/Product"
    preset_params = {
        "schema": "2.7.0"
    }

    def __init__(self, in_dict):
        self.source = in_dict
        self.id = in_dict.get("id", "")

    def get(self, key, default=None):
        try:
            value = self.source.get(key)
            if value is None:
                return default
            else:
                return value
        except KeyError:
            return default