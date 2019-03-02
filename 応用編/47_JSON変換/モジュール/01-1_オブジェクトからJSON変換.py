
import json

json_data = {'Python':'python-izm.com',
			'SerchEngin':('google.co.jp', 'yahoo.co.jp')}

encode_json_data = json.dumps(json_data, indent=4)

print(encode_json_data)








