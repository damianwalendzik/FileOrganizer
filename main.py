import os, re, shutil

UserInput = input('enter the name of the user who has the target folder in its homedirectory\n')
PathInput = input('provide path to the folder you want to organize\n')
CheckDir = os.listdir(f'/Users/{UserInput}')

if PathInput in CheckDir:
    PATH = f'/Users/{UserInput}/{PathInput}'
    PathList = os.listdir(PATH)
else:
    print('Wrong input, please try again.')
OutputDir = f'/Users/{UserInput}/file-maintenance-scripts-output'
Documents = f'/Users/{UserInput}/file-maintenance-scripts-output/Documents'
Pictures = f'/Users/{UserInput}/file-maintenance-scripts-output/Pictures'
Videos = f'/Users/{UserInput}/file-maintenance-scripts-output/Videos'

if not os.path.exists(OutputDir):
    os.makedirs(OutputDir)
    print(f"Directory '{OutputDir}' created successfully.")
    os.makedirs(Videos)
    print(f"Directory '{Videos}' created successfully.")
    os.makedirs(Pictures)
    print(f"Directory '{Pictures}' created successfully.")
    os.makedirs(Documents)
    print(f"Directory '{Documents}' created successfully.")


if not os.path.exists(Videos):
    os.makedirs(Videos)
    print(f"Directory '{Videos}' created successfully.")


if not os.path.exists(Pictures):
    os.makedirs(Pictures)
    print(f"Directory '{Pictures}' created successfully.")


if not os.path.exists(Documents):
    os.makedirs(Documents)
    print(f"Directory '{Documents}' created successfully.")


def sorting(regex_pattern, file):
    if re.search(regex_pattern, file):
        if regex_pattern == "\.pdf" or regex_pattern == "\.docx":
            SourcePath = f"{PATH}/{file}" 
            DestinationPath = f'{Documents}/{file}'
            print(f'{SourcePath}')
            print(f'{DestinationPath}')
            shutil.move(SourcePath, DestinationPath)
        if regex_pattern == "\.png" or regex_pattern == "\.jpg":
            SourcePath = f"{PATH}/{file}" 
            DestinationPath = f'{Pictures}/{file}'
            print(f'{SourcePath}')
            print(f'{DestinationPath}')
            shutil.move(SourcePath, DestinationPath)
        if regex_pattern == "\.mp4":
            SourcePath = f"{PATH}/{file}" 
            DestinationPath = f'{Videos}/{file}'
            print(f'{SourcePath}')
            print(f'{DestinationPath}')
            shutil.move(SourcePath, DestinationPath)
for file in PathList:
    sorting(r'\.pdf', file)
    sorting(r'\.docx', file)
    sorting(r'\.png', file)
    sorting(r'\.jpg', file)
    sorting(r'\.mp4', file)


    
