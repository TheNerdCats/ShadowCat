from trackbot import TrackBot
from load_config import load_config

config = load_config('config.json')

imei = "442283480893012"
tracker = TrackBot(
    config['host'],
    config['port'],
    config['buffer_size'],
    imei
)

# while True:
#     tracker.ping_tcp_random()

while True:
    print tracker.ping_api_random('123', 'Shaphil')
