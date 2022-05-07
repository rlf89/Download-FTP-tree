#! /usr/bin/python

"""

MIT License

Copyright (c) 2022 rlf89
Copyright (c) 2017 Jwely

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

"""

print('\n*** My server backup script ***\n')

import ftputil, os, shutil
from inspect import getsourcefile

fhelpers = "ftp_helpers.py"

with open(fhelpers, "rb") as source_file:
    hcode = compile(source_file.read(), fhelpers, "exec")

exec(hcode)

localdir = "backup"
mylocation = os.path.dirname(getsourcefile(lambda:0))

my_session_factory = ftputil.session.session_factory(port=21, encoding="UTF-8", debug_level=1)
fhandle = ftputil.FTPHost('mywebsite.com', 'login', 'password', session_factory=my_session_factory)

# use this if you compare file dates
# fhandle.synchronize_times()

# delete old directory from backup directory, ignore 'not exist' error
shutil.rmtree( os.path.join( mylocation, localdir, "somedir" ), True )
# start downloading somedir
download_ftp_tree( fhandle, "/domains/somedir", localdir )

fhandle.close()