import os, re, shutil, logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
filehandler = logging.FileHandler('organizer.log')
filehandler.setFormatter(formatter)

streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formatter)

logger.addHandler(streamhandler)
logger.addHandler(filehandler)


UserInput = input('enter the name of the user who has the target folder in its homedirectory\n')
PathInput = input('provide path to the folder you want to organize\n')
CheckDir = os.listdir(f'/Users/{UserInput}')
OutputDir = f'/Users/{UserInput}/file-maintenance-scripts-output'
Documents = f'/Users/{UserInput}/file-maintenance-scripts-output/Documents'
Pictures = f'/Users/{UserInput}/file-maintenance-scripts-output/Pictures'
Videos = f'/Users/{UserInput}/file-maintenance-scripts-output/Videos'
if PathInput in CheckDir:
    PATH = f'/Users/{UserInput}/{PathInput}'
    PathList = os.listdir(PATH)
else:
    logging.warning('Wrong input, please try again.')

if not os.path.exists(OutputDir):
    os.makedirs(OutputDir)
    logging.info(f"Directory '{OutputDir}' created successfully.")
    os.makedirs(Videos)
    logging.info(f"Directory '{Videos}' created successfully.")
    os.makedirs(Pictures)
    logging.info(f"Directory '{Pictures}' created successfully.")
    os.makedirs(Documents)
    logging.info(f"Directory '{Documents}' created successfully.")


if not os.path.exists(Videos):
    os.makedirs(Videos)
    logging.info(f"Directory '{Videos}' created successfully.")


if not os.path.exists(Pictures):
    os.makedirs(Pictures)
    logging.info(f"Directory '{Pictures}' created successfully.")


if not os.path.exists(Documents):
    os.makedirs(Documents)
    logging.info(f"Directory '{Documents}' created successfully.")


def sorting(regex_pattern, file):

    if re.search(regex_pattern, file):

        if regex_pattern == "\.pdf" or regex_pattern == "\.docx":
            SourcePath = f"{PATH}/{file}" 
            DestinationPath = f'{Documents}/{file}'
            shutil.move(SourcePath, DestinationPath)
            logging.debug(f'{SourcePath} has been moved to: {DestinationPath}')

        if regex_pattern == "\.png" or regex_pattern == "\.jpg":
            SourcePath = f"{PATH}/{file}" 
            DestinationPath = f'{Pictures}/{file}'
            shutil.move(SourcePath, DestinationPath)
            logging.debug(f'{SourcePath} has been moved to: {DestinationPath}')

        if regex_pattern == "\.mp4":
            SourcePath = f"{PATH}/{file}" 
            DestinationPath = f'{Videos}/{file}'
            shutil.move(SourcePath, DestinationPath)
            logging.debug(f'{SourcePath} has been moved to: {DestinationPath}')


for file in PathList:
    sorting(r'\.pdf', file)
    sorting(r'\.docx', file)
    sorting(r'\.png', file)
    sorting(r'\.jpg', file)
    sorting(r'\.mp4', file)


    
