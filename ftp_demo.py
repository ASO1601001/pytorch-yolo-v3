import time
import paramiko
 
HOST = "192.168.0.102" # 接続先サーバーのホスト名
PORT = 22 #使用ポート
USERNAME = "izumin" # サーバーのユーザー名
PASSWORD = "mikuruka3" # サーバーのログインパスワード
upload_src_path = "outputs/test.jpg" # アップロードするファイルパス
upload_dst_path = "/Applications/XAMPP/xamppfiles/htdocs/phone_serch/out_img/test.jpg" # アップロード先のファイルパス
 
def main(local_file, remote_file):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(HOST, port=PORT, username=USERNAME, password=PASSWORD)
        sftp = client.open_sftp()
        sftp.put(local_file, remote_file)
 
    except Exception as e:
        print(e)
 
    finally:
        sftp.close()
        client.close()

interval = 3

while True:
    main(upload_src_path,upload_dst_path)
    time.sleep(interval)