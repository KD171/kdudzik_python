import os

directory = r'C:\Users\kdudz\PycharmProjects\kdudzik_python/venv'
# directory = '/dev'
file_list = []
for root, dirs, files in os.walk(directory):
    file_list.extend(files)
print("Number of files in the folder:", len(file_list))
