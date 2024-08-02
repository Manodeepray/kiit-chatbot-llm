from scraping_tools import lister


path = 'src\data'


txt_files,csv_files,pdf_files  = lister.find_files(path)

