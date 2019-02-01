import requests
import pandas as pd

Kellen_Race_id = 1023708
base_url = 'http://cotaaustin.clubspeedtiming.com/api/index.php/'
key = 'key=cs-dev'
backup_key = '&key=83468ce3017376e557b588be7fd0757d982f97e9512a04e57732f3b02f6db6a9'
pd.set_option('display.max_columns', 10)

def findDriversID(driverName):
    request_url = base_url + 'racers/search.json?query=' + driverName.replace(' ', '%20') + '&' + key
    possible_drivers = requests.get(request_url).json()
    for driver in possible_drivers['racers']:
        driver.update(driver.pop('name'))
    df = pd.DataFrame(possible_drivers['racers'])
    df.set_index('id', inplace=True)
    return df

def getDriversRaces(racerID):
    request_url = base_url + 'racers/' + str(racerID) + '/races.json?&' + key
    races_by_driver = requests.get(request_url).json()
    df = pd.DataFrame(races_by_driver['heats'])
    df.set_index('id', inplace=True)
    return df

def getDriversInfo(racerID):
    request_url = base_url + 'racers/' + str(racerID) + '.json?' + key
    driver_info = requests.get(request_url).json()
    driver_info['racer'].update(driver_info['racer'].pop('name'))
    df = pd.DataFrame(driver_info['racer'], index=[0])
    df.set_index('id', inplace=True)
    return df


print(findDriversID2('Kellen Miller'))
#print(getDriversRaces(1023708))
#print(getDriversInfo(1023708))