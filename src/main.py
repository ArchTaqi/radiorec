import os
from radiorec import record_radio
from transferdata import TransferData


def main():
    radio_record = record_radio('http://audio.samaafm.com:8008/1')
    file_name = radio_record.record_radio()
    drop_box_access_token = os.environ.get('access_token')
    target_dir = os.environ.get('target_dir')
    upload_to = target_dir + os.sep + file_name
    transfer_data = TransferData(drop_box_access_token)
    transfer_data.get_account_info()
    transfer_data.upload_file(file_name, upload_to)

if __name__ == '__main__':
    main()