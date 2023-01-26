import os
import ftplib

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

ftp_host = os.environ.get("FTP_HOST")
ftp_username = os.environ.get("FTP_USERNAME")
ftp_password = os.environ.get("FTP_PASSWORD")
ftp_path = os.environ.get("FTP_PATH")


def ftp_connect():
    session = ftplib.FTP(ftp_host, ftp_username, ftp_password)
    return session


def ftp_run():
    session = ftp_connect()
    try:
        session.mkd(ftp_path)
    except Exception:
        pass

    for currentpath, folders, files in os.walk('site'):
        host_path = currentpath.replace("site", ftp_path)

        for folder in folders:
            path_folder = os.path.join(host_path, folder)
            print(f"---{path_folder}")
            try:
                session.mkd(path_folder)
            except Exception:
                pass

        for file in files:
            path_file = os.path.join(currentpath, file)
            host_file = os.path.join(host_path, file)
            print(f"   |___{host_file}")
            try:
                file = open(path_file,'rb')
                session.storbinary(f'STOR {host_file}', file)
            except Exception:
                pass


if __name__ == "__main__":
    ftp_run()
