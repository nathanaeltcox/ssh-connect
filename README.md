# ssh-connect
Connect to remote ssh host, execute commands, and copy files

Once you have cracked the remote ssh host's password using lockpick-kit.py, use ssh-connect to connect to the remote host,
conduct reconnaissance, input commands, and copy files from the remote host to your machine.

To install: place a copy of this script in your scripts directory.

To use: Script will prompt you for the username, password and ip address of your target system. Once you inpt these, it will
automatically connect. To input commands on the remote machine, simply input the command. To copy a file from the remote 
machine, enter the command "grab". You will be prompted to input the file to copy (including the filepath if you're not in 
the file's directory) and the name you want to call the copy saved on your machine. The file will be saved in the same 
directory as your script, unless a different filepath is specified.
