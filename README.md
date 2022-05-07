# Download-FTP-tree
Recursive FTP directory downloader with python (ftputil)

Example usage:
``` python
import ftputil

fhelpers = "ftp_helpers.py"

with open(fhelpers, "rb") as source_file:
    hcode = compile(source_file.read(), fhelpers, "exec")

exec(hcode)

ftphandle = ftputil.FTPHost("host", "user", "password")

download_ftp_tree(ftphandle, remote_dir, local_dir)

ftphandle.close()
```