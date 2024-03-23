# Python 3 script to sort files in dedicated folders according to their type (matching & moving files into subfolders specified in file_ext_dir dictionnary)

from pathlib import Path
import sys

print("Script to sort & organize automatically files according to extension / type in dedicated subfolders (move) :")
print("Audio / Pictures / Vidéos / Documents / Archives / Web / Code / Ebooks / Atari / Executables / Various (default)")

file_ext_dir = { 
        ".mp3" : "Audio",
        ".wav" : "Audio",
        ".ogg" : "Audio",
        ".aac" : "Audio",
        ".flac" : "Audio",
        ".m4a" : "Audio",
        ".mid" : "Audio",
        ".mod" : "Audio",
        ".snd" : "Audio",
        ".wma" : "Audio",
        ".aax" : "Audio",

        ".jpg" : "Pictures",
        ".gif" : "Pictures",        
        ".png" : "Pictures",
        ".jpeg" : "Pictures",                      
        ".webp" : "Pictures",                      
        ".svg" : "Pictures", 
        ".psd" : "Pictures",
        ".eps" : "Pictures",
        ".xcf" : "Pictures",
        ".kra" : "Pictures",  

        ".avi" : "Vidéos",                      
        ".mp4" : "Vidéos",                        
        ".mkv" : "Vidéos",                        
        ".mov" : "Vidéos",
        ".wmv" : "Vidéos",   

        ".doc" : "Documents",
        ".doc" : "Documents",
        ".txt" : "Documents",
        ".pdf" : "Documents",
        ".rtf" : "Documents",
        ".json" : "Documents",
        ".xls" : "Documents",
        ".ppt" : "Documents",
        ".csv" : "Documents",
        ".xml" : "Documents",

        ".epub" : "Ebooks",
        ".fb2" : "Ebooks",
        ".djvu" : "Ebooks",
        ".mobi" : "Ebooks",
        ".cbr" : "Ebooks",
        ".cbz" : "Ebooks",

        ".zip" : "Archives",
        ".rar" : "Archives",
        ".cab" : "Archives",
        ".iso" : "Archives",
        ".bin" : "Archives",
        ".cab" : "Archives",
        ".img" : "Archives",
        ".tar" : "Archives",
        ".lha" : "Archives",
        ".arj" : "Archives",

        ".exe" : "Exec",
        ".bat" : "Exec",
        ".msi" : "Exec",

        ".htm" : "Web",
        ".html" : "Web",
        ".php" : "Web",
        ".css" : "Web",
        ".asp" : "Web",
        ".js" : "Web",

        ".py" : "Code",
        ".bas" : "Code",
        ".c" : "Code",
        ".cpp" : "Code",

        ".pi1" : "Atari",
        ".pc1" : "Atari",
        ".gfa" : "Atari",
        ".lst" : "Atari",
        ".prg" : "Atari",
        ".tos" : "Atari",
        ".ttp" : "Atari",
        ".asm" : "Atari",
        ".inl" : "Atari",
        ".st" : "Atari",
        ".msa" : "Atari",
        ".neo" : "Atari",
        ".gtk" : "Atari",
        ".acc" : "Atari",
        ".app" : "Atari" 
        }

print(file_ext_dir)

# choose the directory you want to sort by sub folders and move file of the matching extensions inside ('Downloads for ex., default, current working directory) 

arguments = sys.argv
# print(arguments)

SORT_DIR = ""

if len(arguments)>1:            # if some arguments were given to launch the script, it should be the path to organize
    if Path(arguments[-1]).is_dir():   # Check if this directory exist
        SORT_DIR = Path(arguments[-1])    # Set as dir to organize
        print(f"Path {arguments[-1]} detected.")

while SORT_DIR == "":  # if no valid arguments was given or no valid entry / path
    print(f"Home directory : {Path.home()}")
    print(f"Current working directory : {Path.cwd()}")
    
    # then we ask user to enter path, choose home, cwd, or quit
    user_choice = input("Enter the path of the directory you want to sort / organize files by file type in dedicated folders : \n OR 'h' for home directory \n OR 'c' for current working directory \n OR 'q' to quit \n : ")  
    
    if Path(user_choice).is_dir():   # Check if this directory exist
        SORT_DIR = Path(user_choice)    # Set as dir to organize
    elif user_choice.lower() == 'q':
        print("Ok. Bye !")
        sys.exit()
    elif user_choice.lower() == 'c':
        SORT_DIR = Path.cwd()
    elif user_choice.lower() == 'h':    
        SORT_DIR = Path.home()
    else:
        print("Not a valid entry / path. Try again. \n")

print(f"Directory to sort & organize : {SORT_DIR}") 

if input("Ready ? (o (continue) /n (quit)) : ").lower() == 'n': 
    print("Ok. Bye !")
    sys.exit()
        
print("Let's sort & organize !")
#SORT_DIR = Path(r'\Users\Public\Downloads') 

files_to_sort = [f for f in SORT_DIR.iterdir() if f.is_file()]  # gen file list for iteration on files only in sort_dir directory

for f in files_to_sort:  # parse each file un folder
    output_dir = SORT_DIR / file_ext_dir.get(f.suffix, "Various")  # set path + name of the file type folder to create and move 
    output_dir.mkdir(exist_ok=True)   # create destination folder (no error if previously created) 
    f.rename(output_dir / f.name)     # move file to new matching folder ( rename at other folder = move )


print(f"{len(files_to_sort)} were sorted & moved in dedicated / matching subfolders.")
print("Done")