# json 데이터 다루기
'''
import json
student = {
    'id' : 20200101,
    'name' : 'Hong',
    'histrory' : [
        {'subject':'math','grade':3.0},
        {'subject':'english','grade':4.5},
    ]
}
# dumps
Encoding_json = json.dumps(student)
print(Encoding_json)
print(type(Encoding_json))

# indent : 들여쓰기
Encoding_json = json.dumps(student, indent=4)
print(Encoding_json)
'''

import json
json_data = """{"id":20200101, "name":"Hong",
"history": [{"subject":"math", "grade":3.0}, {"subject":"english","grade":4.5}]}"""

# loads
Decoding_data = json.loads(json_data)
print(Decoding_data)
print(type(Decoding_data))