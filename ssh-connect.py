#!/usr/bin/env python
import subprocess
import paramiko
import sys

def copy_file(ssh):
    filename = input("File to copy (include filepath): ")
    local_filename = input("Local filename: ")
    sftp = ssh.open_sftp()
    sftp.get(filename, local_filename)
 
def execute_command(ssh):
    while True:
        ssh_session = ssh.get_transport().open_session()
        command = input("Command: ")
        ssh_session.exec_command(command)
        output = ssh_session.recv(1024)
        print(output.decode())
        if str(command).strip().lower() == "grab":
            copy_file(ssh)
        if str(command).strip().lower() == "exit":
            return

def connect(hostname, username, password):
    try:
        print("Establishing SSH connection.")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, username=username, password=password)
        execute_command(client)
        client.close()
    except paramiko.AuthenticationException:
        print("Authentication failed.")
    except paramiko.SSHException as sshException:
        print("Could not establish SSH connection: {}".format(sshException))
    except Exception as e:
        print("Exception: {}".format(e))
    except KeyboardInterrupt:
        print("\n""Process interrupted by user.")
        sys.exit()

if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")
    hostname = input("Target IP: ")
    connect(hostname, username, password)