#!/usr/bin/env python3
import dropbox

class TransferData:
	def __init__(self, access_token):
		self.access_token = access_token

    def upload_file(self, file_from=None, file_to=None):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

    #----------------------------------------------------------------------
    def get_account_info(self):
        """
        Returns the account information, such as user's display name,
        quota, email address, etc
        """
        return self.client.account_info()
