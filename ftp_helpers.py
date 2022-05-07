#! /usr/bin/python

def _mirror_ftp_dir( ftp_handle, remotepath ):

	for root, dirs, files in ftp_handle.walk(remotepath):

		# hack to skip a symlink
		# if "private_html" in root:
		#     continue

		for dirname in dirs:
			fullpath = os.path.join( root, dirname )
			try: 
				os.mkdir( os.path.relpath( fullpath, remotepath ) )
			except OSError as error:
				pass # dir exists

		for fname in files:
			fullpath = os.path.join( root, fname )
			ftp_handle.download( fullpath, os.path.relpath( fullpath, remotepath ) )

	print( "Success!!" )


def download_ftp_tree( ftp_handle, remotepath, destination ):

	"""
	Downloads an entire directory tree from an ftp server to the local destination
	:param ftp_handle: an authenticated ftputil.FTPHost instance
	:param remotepath: the folder on the ftp server to download
	:param destination: the local directory to store the copied folder
	"""

	original_directory = os.getcwd()  # remember working directory before function is executed

	os.chdir( destination )

	remotebase = os.path.basename( remotepath )

	os.mkdir( remotebase )

	os.chdir( remotebase ) # change working directory to ftp mirror directory

	_mirror_ftp_dir( ftp_handle, remotepath )

	os.chdir( original_directory )  # reset working directory to what it was before function exec