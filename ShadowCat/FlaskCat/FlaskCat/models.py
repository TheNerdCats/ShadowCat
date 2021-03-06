from datetime import datetime

from __builtin__ import object
from geojson import Point


class User(object):
    def __init__(self,
                 asset_id,
                 name=None,
                 point=None,
                 device=None,
                 timestamp=datetime.now()):
        self.asset_id = asset_id
        self.name = name
        self.point = Point((
            point["coordinates"][0],
            point["coordinates"][1]
        ))
        self.device = device
        self.timestamp = timestamp


class Device(object):
    def __init__(self, imei, phone_number):
        self.imei = imei
        self.phone_number = phone_number


class AssetPayload(object):
    def __init__(self,
                 asset_id,
                 point,
                 name=None):
        self.AssetId = asset_id
        self.Point = point
        self.Name = name
