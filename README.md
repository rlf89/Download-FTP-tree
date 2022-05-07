# Download-FTP-tree
Recursive FTP directory downloader with python (ftputil)

Usage
-------

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

Credits
-------

Forked from [download_ftp_tree.py](https://gist.github.com/Jwely/ad8eb800bacef9e34dd775f9b3aad987) by Jwely (MIT license).

License
-------

Download-FTP-tree is licensed under the MIT License, see [LICENSE](https://github.com/rlf89/Download-FTP-tree/blob/master/LICENSE) for more information.