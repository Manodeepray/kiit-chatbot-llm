import pypdf
import pandas as pd
import os
import glob

class Combiner:
    def pdf_combiner(self, pdf_files,output_pdf):
        
        merger = pypdf.PdfMerger()
        try:
            for pdf in pdf_files:
                merger.append(pdf)
                
            with open(output_pdf, 'wb') as merged_pdf:
                merger.write(merged_pdf)
                
            print(f'Merged PDFs successfully. Output saved to: {output_pdf}')


        except Exception as e:
            print(f"error merging pdfs : {e}")

        return None
    
    def txt_combiner(self, txt_files , output_txt):
        
                
        try:
            read_files = txt_files

            with open(output_txt, "wb") as outfile:
                for f in read_files:
                    with open(f, "rb") as infile:   
                        outfile.write(infile.read())
            print("txt files merged successfully")
            
        except Exception as e:
            print(f"error merging txt files : {e}")
        
        return None
    
    

    
    
    def csv_cbmbiner(self , csv_files , output_csv):
        data_frames = []
        
        try:
            for file in csv_files:
                if file.endswith('.csv'):
                    csv_path = file
                    df = pd.read_csv(csv_path)
                    data_frames.append(df)
                    
            print("dataframes appended")
        except Exception as e:
            print(f"error in appending dfs : {e}")
            
        try:
            combined_df = pd.concat(data_frames, ignore_index=True)
            combined_df = combined_df.dropna()
            combined_df = combined_df.reset_index(drop=True)
            print("csv combined  and saved successfully")
        
            combined_df.to_csv(output_csv)
        except Exception as e:
            print(f"error in combining and saving : {e}")
        return None
        


    
    