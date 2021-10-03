#%%
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileReader
import pandas as pd
from pathlib import Path
import sys
import os
#%%
def read_file(file, first_column=None):
    if Path(file).suffix in ['.xls', '.xlsx', '.xlsm', '.xlsb', '.odf', '.ods', '.odt' ]:
        out = pd.read_excel(file)
    else:
        out = pd.read_csv(file, skipinitialspace=True)

    if first_column is not None:
            out.drop(out.iloc[:,range(out.columns.get_loc(first_column))],axis=1, inplace=True)
    return out

#%%
def extract_pages():
    return True

#%%
def distribute_pages(original_pdf, index_file, ppl_file):

    Path("./out-pdfs").mkdir(exist_ok=True)

    original = PdfFileReader(original_pdf)

    ppl = read_file(ppl_file, 'Person')
    idx = read_file(index_file)
    for p, person in ppl.iterrows():
        pages=[]
        for s,subject in person.iteritems():
            if s == 'Person':
                out_file = subject
            else:
                if subject in ['yes', 'Yes', 'True', '1', True, 1, '+']:
                    idx_subject = idx.loc[idx['Subject'] == s]
                    pages.extend([*range(idx_subject['Start page'].values[0], idx_subject['End page'].values[0]+1)])

        out = PdfFileWriter()
        for page in pages:
            out.addPage(original.getPage(page-1)) #zero index
        with open(f"./out-pdfs/{out_file}.pdf",'wb') as f:
            out.write(f)

# %%
if __name__ == '__main__':
    print(len(sys.argv))
    print(sys.argv)
    if len(sys.argv)==4:
        original_pdf = sys.argv[1]
        index_file = sys.argv[2]
        ppl_file = sys.argv[3]
        print('Using command line files: ')
        print(f"Original pdf: {original_pdf}")
        print(f"Index pdf: {index_file}")
        print(f"People pdf: {ppl_file}")
    else:
        original_pdf = 'original.pdf'
        valid_original = Path(original_pdf).is_file() 

        files = os.listdir('.')
        index_files =[f for f in files if Path(f).stem.lower() in 'index']
        if len(index_files)==1:
            index_file=index_files[0]
            valid_index = Path(index_file).is_file() 
        else: 
            valid_index = False

        ppl_files =[f for f in files if Path(f).stem.lower() in 'people']
        if len(ppl_files)==1:
            ppl_file = ppl_files[0]
            valid_ppl = Path(ppl_file).is_file() 
        else: 
            valid_ppl = False

        if valid_original and valid_index and valid_ppl :
            print('Using default files: ')
            print(f"Original pdf: {original_pdf}")
            print(f"Index file: {index_file}")
            print(f"People file: {ppl_file}")
        else:
            print('Invalid default files')
            original_pdf = input('Enter original pdf: ')
            index_file= input('Enter index file: ')
            ppl_file= input('Enter people pdf: ')

    distribute_pages(original_pdf, index_file, ppl_file)

# %%
