import json
import numpy as np

def replace_values(data):
  if isinstance(data, dict):
    for key, value in data.items():
      if isinstance(value, str):
        data[key] = value.replace('\n', '').replace('\t', '')
      elif isinstance(value, (list, tuple)):
        for i in range(len(value)):
          value[i] = replace_values(value[i])
      elif isinstance(value, dict):
        data[key] = replace_values(value)
      elif isinstance(value, float) and np.isnan(value):
        data[key] = "N/A"
  elif isinstance(data, list):
    for i in range(len(data)):
      data[i] = replace_values(data[i])
  return data

def process_json_file(input_file, output_file):
  with open(input_file, 'r') as f:
    data = json.load(f)

  modified_data = replace_values(data)

  with open(output_file, 'w') as f:
    json.dump(modified_data, f, indent=2)
    
'''def replace_unicode_escapes(data):
    if isinstance(data, str):
        return data.encode('utf-8').decode('unicode_escape')
    elif isinstance(data, dict):
        for key, value in data.items():
            data[key] = replace_unicode_escapes(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = replace_unicode_escapes(data[i])
    return data

def process_json_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    modified_data = replace_unicode_escapes(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(modified_data, f, indent=2, ensure_ascii=False)'''

if __name__ == "__main__":
    input_file = 'src\json\data.json'
    output_file = 'src\json\output.json'
    process_json_file(input_file, output_file)