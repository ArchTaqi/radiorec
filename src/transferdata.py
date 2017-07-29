#!/usr/bin/env python3
import os
import dropbox


class TransferData:
    access_token = None
    logging = None

    def __init__(self, access_token, logging):
        self.access_token = access_token
        self.logging = logging

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
            self.logging.info("Uploaded " + file_to)
        except Exception as e:
            self.logging.error("Failed to upload " + file_from + "to " + file_to)
            self.logging.error(e)
        finally:
            try:
                os.remove(file_from)
                self.logging.info("Removed: " + file_from)
            except OSError as e:
                self.logging.error(e)
                pass

    def get_account_info(self):
        """
        Returns the account information, such as user's display name, quota,
        email address, etc
        :return:
        """
        client = dropbox.Dropbox(self.access_token)
        print(client.users_get_current_account())
