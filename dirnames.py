from pathlib import Path

p = Path(r'C:\Users\Usama Iftikhar\Downloads')

def returnsubdirectories(p) :
    [files for files in p.iterdir() if files.is_dir()]


    lis = list(p.glob('**/'))
    for temp in lis:
        print(temp)


returnsubdirectories(p)
