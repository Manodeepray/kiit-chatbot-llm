import os




def find_files(path):
    txt_files = []
    csv_files = []
    pdf_files = []
    
    for root, dirs, files in os.walk(path):
            for dir in dirs:
                for file in files:
                    print(file)
                    input_file = os.path.join(root,dir,file)
                    print(input_file)
                    if input_file.endswith(".txt"):
                        
                        txt_files.append(input_file)
                    elif input_file.endswith(".csv"):
                        csv_files.append(input_file)
                    elif input_file.endswith(".pdf"):
                        pdf_files.append(input_file)
                        


    print(txt_files)
    print(csv_files)
    print(pdf_files)         
    return txt_files,csv_files,pdf_files   

find_files(path ="src/data")


    
