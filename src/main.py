import os
from datetime import datetime as dt
from radiorec import record_radio
from transferdata import TransferData


def upload(file_name):
    if file_name is not None:
        drop_box_access_token = os.environ.get('access_token')
        target_dir = os.environ.get('target_dir')
        upload_to = target_dir + os.sep + file_name
        transfer_data = TransferData(drop_box_access_token)
        transfer_data.get_account_info()
        transfer_data.upload_file(file_name, upload_to)


def main():
    record_now = os.environ.get('record_now')
    record_now_duration = os.environ.get('record_now_duration')
    if record_now is not None and record_now_duration > 0:
        print('Record Now')
        radio_record = record_radio('http://audio.samaafm.com:8008/1')
        radio_record.start(record_now_duration)
        file_name = radio_record.record_radio()
        upload(file_name)
    else:
        day = int(dt.utcnow().strftime("%A"))
        if day != 'Sunday':
            radio_record = record_radio('http://audio.samaafm.com:8008/1')
            file_name = radio_record.record_radio()
            upload(file_name)

if __name__ == '__main__':
    main()
