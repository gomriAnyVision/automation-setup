import os
import requests
import json
import consul


site_ip = "192.168.20.176"
relative_path = os.path.dirname(os.path.abspath(__file__))

def json_loader(json_path):
    with open(json_path,'rb') as f:
        dict_of_json = json.load(f)    
    return dict_of_json

def randomId():
    return 1

# TODO: change function name
def edit_camera_json(camera_template):
    camera_template['message']['title'] = 'test'
    camera_template['message']['_id']   = randomId()
    return camera_template

def http_post(url, payload):
    url         = os.environ(API_URL) or site
    payload     = json.loads(payload)
    print payload
    # response    = requests.post(url,payload)
    # return response

def response_parser(response):
    if response.status_code == 200:
        return True
    else:
        return False

def create_camera(camera_name):
    camera = edit_camera_json(camera_template)
    reponse = http_post(url, camera)
    if reponse_parser(response):
        return 'Created camera successfully for {site}'.format(site=site)
    else: 
        return 'Failed to camera for {site}'.format(site)


if __name__ == "__main__":
    settings =  json_loader(relative_path + '/settings.json')
    camera_template = json_loader(relative_path + '/camera_template.json')

    perpared_camera_json = edit_camera_json(camera_template)
    consul_connection =  consul.Consul(host='127.0.0.1', port=8500, scheme='http')
    print consul_connection.kv.get('webrtc-streamer/', keys=True)