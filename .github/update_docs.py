import os
import ftplib


ftp_host = os.environ.get("FTP_HOST")
ftp_username = os.environ.get("FTP_USERNAME")
ftp_password = os.environ.get("FTP_PASSWORD")


def ftp_connect():
    session = ftplib.FTP(ftp_host, ftp_username, ftp_password)
    return session


def ftp_run():
    session = ftp_connect()
    try:
        session.mkd('site')
    except Exception:
        pass

    for currentpath, folders, files in os.walk('site'):
        # currentpath = currentpath.replace("site", "docs")

        for folder in folders:
            path_folder = os.path.join(currentpath, folder)
            print(f"---{path_folder}")
            try:
                session.mkd(path_folder)
            except Exception:
                pass

        for file in files:
            path_file = os.path.join(currentpath, file)
            print(f"   |___{path_file}")
            try:
                file = open(path_file,'rb')
                session.storbinary(f'STOR {path_file}', file)
            except Exception:
                pass


if __name__ == "__main__":
    ftp_run()
