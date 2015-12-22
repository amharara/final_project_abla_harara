import os
path = "/Users/PythonPrincess/Desktop/final_project/PDF_FOLDER_2015"
dirs = os.listdir(path)
for file in dirs:
	command = "python pdf2txt.py -o " + "TXT_FOLDER_2015/" + file[:-4] + ".txt " + "PDF_FOLDER_2015/" + file
	os.system(command)