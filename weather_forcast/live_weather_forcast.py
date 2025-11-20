import requests

def weather_forcast(city,api_key,units='metric'):
    #Fetch forecast JSON from OpenWeatherMap (5 day / 3 hour)
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    req = requests.get(url)
    req.raise_for_status()
    return req.json()

def write_table_file(content,city,file_name="data.txt"):

    with open(file_name,'w',encoding="utf-8") as file:
        #adding the Header
        file.write(f'Weather report city:{city} \n')

        file.write('='*120 + '\n')

        #write column name
        file.write(f'{'Sl No':<7}{'Date and time':<20}{'Temperature':<12}{'Humidity':<11}{'Weather':<9}{'Weather Description':<22}{"wind speed":<13}{"wind degree":<14} \n')
        file.write('-'*120+'\n')

        #write file rows
        for i,item in enumerate(content.get('list', []),start=1):

            dt_txt = item.get('dt_txt','')
            temp = item.get('main',{}).get('temp','')
            humidity = item.get('main',{}).get('humidity','')
            weather = item.get('weather', [{}])[0].get('main','')
            weather_desc = item.get('weather', [{}])[0].get('description', '')
            # rain = item.get('rain','')
            wind_speed = item.get('wind',{}).get('speed','')
            wind_degree = item.get('wind',{}).get('deg','')


            file.write(
                f'{i:<5}'
                f'{dt_txt:<22}'
                f'{str(temp):<12}'
                f'{str(humidity):<9}'
                f'{weather:<9}'
                f'{weather_desc:<22}'
                f'{wind_speed:<13}'
                f'{wind_degree:<14} \n'

            )
    return file_name

def main():

    city = "Bangalore"
    api_key = "26631f0f41b95fb9f5ac0df9a8f43c92"
    units = "metric"

    try:
        content = weather_forcast(city,api_key,units=units)
        table_file = write_table_file(content, city, file_name="data.txt")
        print(f"Table saved to :{table_file}")
    except  requests.HTTPError as e:
        print("Http error while fetching weather forcast: ",e)
    except Exception as e:
        print('Error:',e)

if __name__ == "__main__":
    main()


