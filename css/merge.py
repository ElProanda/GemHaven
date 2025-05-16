
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())


files_names = [
   "new",
   "grid",
   "table",
   "form",
   "menus",
   "popup",
   "iconmoon",
   "kviktun",
   "custom" ]
data = ""

for file_name in files_names :
   with open(file_name+".css" ,"r") as file_handle :
      temp_data = file_handle.read()
      data = data + temp_data 

with open ('styles.min.css', 'w') as file_handle : 
  file_handle.write(data)
