import os
import logging
from datetime import datetime as dt
from radiorec import record_radio
from transferdata import TransferData


class Radio(object):
    """ An application to record fm radio and upload to dropbox or soundcloud. """

    STREAM_URL = 'http://audio.samaafm.com:8008/1'
    ACCESS_TOKEN = None
    TARGET_DIR = None
    RECORD_NOW = None
    RECORD_NOW_DURATION = None
    logger = None

    def __init__(self):
        logging.basicConfig(filename='error_log.log', level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s')
        self.config()

    def config(self):
        self.ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', None)
        if not self.ACCESS_TOKEN:
            msg = 'You must have "ACCESS_TOKEN" variable'
            logging.error(msg, exc_info=True)
            raise ValueError(msg)

        self.TARGET_DIR = os.environ.get('TARGET_DIR', None)
        if not self.TARGET_DIR:
            msg = 'You must have "TARGET_DIR" variable'
            logging.error(msg)
            raise ValueError('You must have "TARGET_DIR" variable')

        self.RECORD_NOW = int(os.environ.get('RECORD_NOW', None))
        if not self.RECORD_NOW:
            msg = 'You must have "RECORD_NOW" variable'
            logging.error(msg)
            raise ValueError('You must have "RECORD_NOW" variable')

        self.RECORD_NOW_DURATION = float(os.environ.get('RECORD_NOW_DURATION', None))
        if not self.RECORD_NOW_DURATION:
            msg = 'You must have "RECORD_NOW_DURATION" variable'
            logging.error(msg)
            raise ValueError('You must have "RECORD_NOW_DURATION" variable')

    def upload(self, file_name):
        if file_name is not None:
            drop_box_access_token = self.ACCESS_TOKEN
            target_dir = self.TARGET_DIR
            upload_to = target_dir + os.sep + os.path.basename(file_name)
            transfer_data = TransferData(drop_box_access_token, logging)
            transfer_data.get_account_info()
            try:
                transfer_data.upload_file(file_name, upload_to)
                logging.info("Uploaded " + file_name + 'to ' + upload_to)
            except OSError  as e:
                logging.error("Failed to upload " + file_name + 'to ' + upload_to)
                logging.error(e)

    def remove(self, file_name):
        try:
            os.remove(file_name)
            logging.info("Removed: " + file_name)
        except OSError as e:
            logging.error(e)
            pass

    def run(self):
        if self.RECORD_NOW != 0 and self.RECORD_NOW_DURATION > 0:
            print('Record Now')
            radio_record = record_radio(self.STREAM_URL, logging)
            radio_record.start(self.RECORD_NOW_DURATION)
            file_name = radio_record.record_radio()
            logging.info("Recorded File : " + file_name)
            self.upload(file_name)
        else:
            day = str(dt.utcnow().strftime("%A"))
            if day != 'Sunday':
                radio_record = record_radio(self.STREAM_URL, logging)
                file_name = radio_record.record_radio()
                self.upload(file_name)


if __name__ == '__main__':
    radio = Radio()
    radio.run()