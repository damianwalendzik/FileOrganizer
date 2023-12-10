import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
filehandler = logging.FileHandler('organizer.log')
filehandler.setFormatter(formatter)
logging.root.setLevel(logging.DEBUG)

streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formatter)

logger.addHandler(streamhandler)
logger.addHandler(filehandler)

import os
import re
import shutil
import tkinter


def main_function(username, path):
    UserInput = username
    PathInput = path
    CheckDir = os.listdir(f'/Users/{UserInput}')
    OutputDir = f'/Users/{UserInput}/file-maintenance-scripts-output'
    Documents = f'/Users/{UserInput}/file-maintenance-scripts-output/Documents'
    Pictures = f'/Users/{UserInput}/file-maintenance-scripts-output/Pictures'
    Videos = f'/Users/{UserInput}/file-maintenance-scripts-output/Videos'
    Installers = f'/Users/{UserInput}/file-maintenance-scripts-output/Installers'
    Compressed = f'/Users/{UserInput}/file-maintenance-scripts-output/Compressed'
    Frontend = f'/Users/{UserInput}/file-maintenance-scripts-output/Frontend'

    if PathInput in CheckDir:
        PATH = f'/Users/{UserInput}/{PathInput}'
        PathList = os.listdir(PATH)
    else:
        logger.warning('Wrong input, please try again.')

    if not os.path.exists(OutputDir):
        os.makedirs(OutputDir)
        logger.info(f"Directory '{OutputDir}' created successfully.")
        os.makedirs(Videos)
        logger.info(f"Directory '{Videos}' created successfully.")
        os.makedirs(Pictures)
        logger.info(f"Directory '{Pictures}' created successfully.")
        os.makedirs(Documents)
        logger.info(f"Directory '{Documents}' created successfully.")
        os.makedirs(Installers)
        logger.info(f"Directory '{Installers}' created successfully.")
        os.makedirs(Compressed)
        logger.info(f"Directory '{Compressed}' created successfully.")
        os.makedirs(Frontend)
        logger.info(f"Directory '{Frontend}' created successfully.")

    if not os.path.exists(Videos):
        os.makedirs(Videos)
        logger.info(f"Directory '{Videos}' created successfully.")


    if not os.path.exists(Pictures):
        os.makedirs(Pictures)
        logger.info(f"Directory '{Pictures}' created successfully.")


    if not os.path.exists(Documents):
        os.makedirs(Documents)
        logger.info(f"Directory '{Documents}' created successfully.")

    if not os.path.exists(Installers):
        os.makedirs(Installers)
        logger.info(f"Directory '{Installers}' created successfully.")

    if not os.path.exists(Compressed):
        os.makedirs(Compressed)
        logger.info(f"Directory '{Compressed}' created successfully.")

    if not os.path.exists(Frontend):
        os.makedirs(Frontend)
        logger.info(f"Directory '{Frontend}' created successfully.")
    

    def sorting(regex_pattern, file):

        if re.search(regex_pattern, file):

            if regex_pattern == "\.pdf" or regex_pattern == "\.docx":
                SourcePath = f"{PATH}/{file}" 
                DestinationPath = f'{Documents}/{file}'
                shutil.move(SourcePath, DestinationPath)
                logger.debug(f'{SourcePath} has been moved to: {DestinationPath}')

            if regex_pattern == "\.png" or regex_pattern == "\.jpg":
                SourcePath = f"{PATH}/{file}" 
                DestinationPath = f'{Pictures}/{file}'
                shutil.move(SourcePath, DestinationPath)
                logger.debug(f'{SourcePath} has been moved to: {DestinationPath}')

            if regex_pattern == "\.mp4":
                SourcePath = f"{PATH}/{file}" 
                DestinationPath = f'{Videos}/{file}'
                shutil.move(SourcePath, DestinationPath)
                logger.debug(f'{SourcePath} has been moved to: {DestinationPath}')
        
            if regex_pattern == "\.exe" or regex_pattern == "\.dmg" or regex_pattern == "\.iso" or regex_pattern == "\.zip":
                SourcePath = f"{PATH}/{file}" 
                DestinationPath = f'{Installers}/{file}'
                shutil.move(SourcePath, DestinationPath)
                logger.debug(f'{SourcePath} has been moved to: {DestinationPath}')

            if regex_pattern == "\.rar" or regex_pattern == "\.zip":
                SourcePath = f"{PATH}/{file}" 
                DestinationPath = f'{Compressed}/{file}'
                shutil.move(SourcePath, DestinationPath)
                logger.debug(f'{SourcePath} has been moved to: {DestinationPath}')
        
            if regex_pattern == "\.html" or regex_pattern == "\.css":
                SourcePath = f"{PATH}/{file}" 
                DestinationPath = f'{Frontend}/{file}'
                shutil.move(SourcePath, DestinationPath)
                logger.debug(f'{SourcePath} has been moved to: {DestinationPath}')
    for file in PathList:
        sorting(r'\.pdf', file)
        sorting(r'\.docx', file)
        sorting(r'\.png', file)
        sorting(r'\.jpg', file)
        sorting(r'\.mp4', file)
        sorting(r'\.exe', file)
        sorting(r'\.dmg', file)
        sorting(r'\.iso', file)
        sorting(r'\.zip', file)
        sorting(r'\.rar', file)
        sorting(r'\.html', file)

filehandler.close()


