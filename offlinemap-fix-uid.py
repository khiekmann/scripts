import os
import errno
from os.path import expanduser
import shutil
import argparse

home = expanduser("~")
archives = home + "/archives"
offlineimap = home + "/.offlineimap/"
accountId = ''

def parseCommandLineArgument():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('--id', help='Offline email account name', required=True)
    args = parser.parse_args()
    global accountId
    accountId = args.id
    print("Offline account to fix uid " + accountId + ".")    

def createOnlyIfNonExistant(path):
    print("Path " + path + " to be created if non existant.")
    try:
        os.makedirs(path)
        print("Path " + path + " created.")
    except OSError as exception:
        if exception.errno == errno.EEXIST:
            print('Path' + path + ' already exists.')
            print('Remove ' + path + ' and run again.')
            exit()
        else:
            raise

def moveOfflineMetadataToArchives():
    print("Move account info to " + archives + ".")
    shutil.move(offlineimap + "Account-" + accountId, archives)
    print("Move remote repository sync data to " + archives + ".")
    shutil.move(offlineimap + "Repository-" + accountId + "-remote", archives)
    print("Move local repository sync data to " + archives + ".")
    shutil.move(offlineimap + "Repository-" + accountId + "-local", archives)

def printOutro():
    print('Offline metadata moved. You should now run offlineimap again.')
    print('If it runs successfully, remove ' + archives + '.')
    
parseCommandLineArgument()
createOnlyIfNonExistant(archives)
moveOfflineMetadataToArchives()
printOutro()
