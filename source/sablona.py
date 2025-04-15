import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import main as masterFunc
from master import convertFuncToStr as novyProgram

# sem piste importy

def main(global_data):
    pass
    # pro otevreni okna "global_data['otevrena_okna'].append(novyProgram(funkce))"
    # sem piste svuj program

if __name__ == "__main__":
    masterFunc(novyProgram(main))
