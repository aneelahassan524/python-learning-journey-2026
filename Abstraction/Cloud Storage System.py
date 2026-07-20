from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def upload_file(self):
        pass

class Google_Drive(Storage):

    def upload_file(self):
        print("Uploading file to Google Drive...")

class Dropbox(Storage):

    def upload_file(self):
        print("Uploading file to Dropbox...")

class OneDrive(Storage):

    def upload_file(self):
        print("Uploading file to OneDrive...")

drive = Google_Drive()
box = Dropbox()
onedrive = OneDrive()
drive.upload_file()   
box.upload_file()
onedrive.upload_file()

