import ftplib
import time

def ftp_upload(hostname, username, password, upload_src_path, upload_dst_path):
    # FTP接続・アップロード
    ftp = ftplib.FTP(hostname)
    ftp.set_pasv("true")
    ftp.login(username, password)
    fp = open(upload_src_path, 'rb')
    ftp.storbinary(upload_dst_path ,fp)

    # 終了処理
    ftp.close()
    fp.close()


hostname = "127.0.0.1" # 接続先サーバーのホスト名
upload_src_path = "test.jpg" # アップロードするファイルパス
upload_dst_path = "STOR phone_serch/out_img/test.jpg" # アップロード先のファイルパス
username = "root" # サーバーのユーザー名
password = "root" # サーバーのログインパスワード
interval = 3

while True:
    ftp_upload(hostname, username, password, upload_src_path, upload_dst_path)
    time.sleep(interval)