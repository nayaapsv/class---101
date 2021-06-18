import os
import dropbox
from dropbox.files import WriteMode


class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, source, dest):
        dbx = dropbox.Dropbox(self.access_token)

           
        for path, files in os.walk(source):

            for filename in files:
                    
                localpath = os.path.join(path,filename)

                   
                relativepath = os.path.relpath(localpath, source)
                dropboxpath = os.path.join(dest, relativepath)
                   
                with open(localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxpath, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.Ay-P2D-eXWlCtrEdsRQvyJaUR7GScRsQdKuGISkevzdyReaKtMrbc0Ix-6yVTE1scqo2Mz-LYhBogQlOu0xG3CesbTEGgHIFJ8hXhqAvzWn9wzbi6TS-nOMspHjxZFNWemiJUwo'
    transferData = TransferData(access_token)

    source = input("Enter the source: -")
    dest = "/testFolder/"+source

    transferData.upload_file(source,dest)
    print("file is moved")

main()