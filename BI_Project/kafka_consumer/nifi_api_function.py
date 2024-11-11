import requests

# NiFi API base URL

id="568195d1-0190-1000-e468-ce3f8fb37d78"
def get_process_group_status(group_id,nifi_host):
    url = f'{nifi_host}/flow/process-groups/{group_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None





def is_process_group_running(process_group_status):

    stopped_count = process_group_status['stoppedCount']
    invalid_count = process_group_status['invalidCount']
    if invalid_count >0:
        print("There 's Invalide Processes ")
        statue='-1'
        return statue
    else :
        if stopped_count == 0:
            statue='1' # Group -Process is running
            return statue 
        else :
            statue='0'   # Group -Process not running
            return statue
# Function to start the process group
import json
def start_process_group(nifi_host, process_group_id):
    url = f"{nifi_host}/flow/process-groups/{process_group_id}"
    headers = {'Content-Type': 'application/json'}
    data = {
        'id': process_group_id,
        'state': 'RUNNING'
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_nifi_flow(nifi_host):
    url = f"{nifi_host}/flow/process-groups/root"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(response.raise_for_status())



def Trigger_flow(nifi_host):
    try :
        nifi_flow_json=get_nifi_flow(nifi_host)
        liste_subgroup=nifi_flow_json['processGroupFlow']['flow']['processGroups']
        for subgroup in liste_subgroup:
            if is_process_group_running(subgroup) == '0':
                id=subgroup['id']
                start_process_group(nifi_host,id)

    except Exception as e:
        print('Problem in the Either Connection or group process \n')
        print('Exception :',e.args)
        
        