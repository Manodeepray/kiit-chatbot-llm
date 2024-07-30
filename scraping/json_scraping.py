import pandas as pd
import fitz
import json
import os
def create_json_structure(path):
  """Creates a JSON representation of a directory structure with file content.

  Args:
    path: The root directory path.

  Returns:
    A JSON object representing the directory structure.
  """

  def build_tree(path):
    tree = {}
    for name in os.listdir(path):
      full_path = os.path.join(path, name)
      key = os.path.basename(full_path).replace("/", "_")
        
        
      if os.path.isdir(full_path):
        tree[key] = build_tree(full_path)
      else:
        content = None
        if key.endswith('.txt'):
          with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        elif key.endswith('.csv'):
          try:
            df = pd.read_csv(full_path)
            content = df.to_dict()
          except pd.errors.ParserError as e:
            print(f"Error parsing CSV {full_path}: {e}")
        elif key.endswith('.pdf'):
          try:
            pdf_document = fitz.open(full_path)
            text = ""
            for page_num in range(len(pdf_document)):
              page = pdf_document.load_page(page_num)
              text += page.get_text()
            content = text
          except Exception as e:
            print(f"Error processing PDF {full_path}: {e}")
        tree[key] = {'content': content}  # Include content as a key
        print(key)
    return tree

  root = build_tree(path)
    
  return root

def find_tuple_keys_in_hierarchy(dictionary):
    tuple_keys = []

    def _find_tuple_keys(d):
        for key, value in d.items():
            if isinstance(key, tuple):
                tuple_keys.append(key)
            if isinstance(value, dict):
                _find_tuple_keys(value)

        _find_tuple_keys(dictionary)
  
    return tuple_keys

def save_as_json(input_folder_path ,json_file_path):
    json_structure = create_json_structure(input_folder_path)
    json_data = json.dumps(json_structure, indent=4)
    with open(json_file_path, "w") as outfile:
        outfile.write(json_data)
    
    
    
    
    return json_data


if __name__ == '__main__':
    
    folder_path = "src\data"
    json_path = "src\json\data.json"
    json_data = save_as_json(folder_path , json_path)
    