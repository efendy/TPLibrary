"""
MPX Web Services

Publish - https://docs.theplatform.com/help/pub-publish-endpoint

@author efendy.setiawan@theplatform.com
last modified: 20191111
"""
from datetime import datetime


class Publish:
    endpoint_uri = "publish.theplatform.com/web/Publish"
    preset_params = {
        "schema": "1.2"
    }

    def __init__(self, in_dict):
        self.source = in_dict

    @staticmethod
    def method(name, media_id, publish_id):
        return {
            name: {
                "mediaId": media_id,
                "profileId": publish_id
            }
        }

    @staticmethod
    def publish(media_id, publish_id):
        return Publish.method("publish", media_id, publish_id)
    
    @staticmethod
    def republish(media_id, publish_id):
        return Publish.method("republish", media_id, publish_id)

    @staticmethod
    def revoke(media_id, publish_id):
        return Publish.method("revoke", media_id, publish_id)
    
    @staticmethod
    def update(media_id, publish_id):
        return Publish.method("update", media_id, publish_id)

    @staticmethod
    def updateMetadata(media_id, publish_id):
        return Publish.method("updateMetadata", media_id, publish_id)