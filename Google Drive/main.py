
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1UOHQUi7s-SNa12y5usxcGAnproZFNN3m'

file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'hello.txt'})
file1.SetContentString('Hello world!')
file1.Upload()

file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
for index, file in enumerate(file_list):
  file.GetContentFile(file['title']) 
  print(index+1, 'file downloaded: ', file['title'])