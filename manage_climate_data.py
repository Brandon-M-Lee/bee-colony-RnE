import zipfile
import os
import shutil

path = "C:/Users/csi2/Desktop/bee-colony-RnE/data/climate"

def unzip_file():
    for state in os.listdir(path):
        for year in os.listdir(path+'/'+state):
            if year.endswith('.zip'):
                with zipfile.ZipFile(path+'/'+state+'/'+year, 'r') as zip_ref:
                    try:
                        zip_ref.extractall(path+'/'+state+'/'+year[:-4])
                    except:
                        print(path+'/'+state+'/'+year[:-4])
                os.remove(path+'/'+state+'/'+year)

def classify_file():
    for state in os.listdir(path):
        if not os.path.exists(path+'/'+state+'/all reports'):
            os.makedirs(path+'/'+state+'/all reports')
        if not os.path.exists(path+'/'+state+'/daily summury'):
            os.makedirs(path+'/'+state+'/daily summury')
        for year in os.listdir(path+'/'+state):
            for file in os.listdir(path+'/'+state+'/'+year):
                if file[5] == 'A':
                    os.rename(path+'/'+state+'/'+year+'/'+file, path+'/'+state+'/all reports/'+file)
                elif file[5] == 'D':
                    os.rename(path+'/'+state+'/'+year+'/'+file, path+'/'+state+'/daily summury/'+file)

def clean_directory():
    for state in os.listdir(path):
        for folder in os.listdir(path+'/'+state):
            if folder != 'all reports' and folder != 'daily summury':
                shutil.rmtree(path+'/'+state+'/'+folder)