import requests

list = {"Geo News": "UC_vt34wimdCzdkrzVejwX9g" , "ARY NEWS": "UCMmpLL2ucRHAXbNHiCPyIyg" ,"DUNYA NEWS": "UCnMBV5Iw4WqKILKue1nP6Hg", "HUM NEWS": "UC0Um3pnZ2WGBEeoA3BX2sKw", "SAMAA NEWS": "UCJekW1Vj5fCVEGdye_mBN6Q"}
api_key = ''

for the_key, the_value in list.items():
  resp = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={the_value}&eventType=live&type=video&key={api_key}')
  data = resp.json()
  for item in data['items']:
    live_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}" 
    channel_name = the_key
    print(the_key + " " + live_url)

