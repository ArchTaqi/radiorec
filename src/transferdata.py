#!/usr/bin/env python3

import dropbox


class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from=None, file_to=None):
        """
        upload a file to Dropbox using API v2
        :param file_from:
        :param file_to:
        :return:
        """
        client = dropbox.Dropbox(self.access_token)
        try:
            with open(file_from, 'rb') as f:
                meta = client.files_upload(f.read(), file_to, mute=True)
            print("Uploaded " + file_to)
        except Exception as e:
            print("Failed to upload " + file_to)
            print(e)

    def get_account_info(self):
        """
        Returns the account information, such as user's display name, quota,
        email address, etc
        :return:
        """
        client = dropbox.Dropbox(self.access_token)
        print(client.users_get_current_account())
