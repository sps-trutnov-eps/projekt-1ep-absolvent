import json
import pygame
import multiprocessing
import ctypes


def unfocusWindow():
    ctypes.windll.user32.AllowSetForegroundWindow(-1)


def focusWindow():
    hwnd = pygame.display.get_wm_info()['window']
    ctypes.windll.user32.ShowWindow(hwnd, 5)
    ctypes.windll.user32.BringWindowToTop(hwnd)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    ctypes.windll.user32.SetFocus(hwnd)

######################################################################################################
import Martin_hudba_minihra.main_hra

######################################################################################################

def createWindow(global_data, okno):

    ######################################################################################################
    jmena_funkce = {
       "hudba_minihra": Martin_hudba_minihra.main_hra.main
    }

                                            # Vzdycky vezme jen 1 argument "global data"
    jmena_funkce[okno](global_data)         # Spustena Funkce - Minihra nebo jakykoliv program
    global_data['aktualni_okna'].remove(okno) # Ulozi informaci ze okno je zavreny
    ######################################################################################################








def convertFromManager(obj):
    if isinstance(obj, multiprocessing.managers.ListProxy):
        return [convertFromManager(item) for item in obj]

    elif isinstance(obj, multiprocessing.managers.DictProxy):
        return {key: convertFromManager(value) for key, value in obj.items()}

    elif isinstance(obj, dict):
        return {key: convertFromManager(value) for key, value in obj.items()}

    elif isinstance(obj, list):
        return [convertFromManager(item) for item in obj]

    else:
        return obj


def convertToManager(obj, manager):
    if isinstance(obj, dict):
        proxy_dict = manager.dict()
        for key, value in obj.items():
            proxy_dict[key] = convertToManager(value, manager)
        return proxy_dict
    elif isinstance(obj, list):
        proxy_list = manager.list()
        for item in obj:
            proxy_list.append(convertToManager(item, manager))
        return proxy_list
    else:
        return obj


def cloneManagerList(manager_list, manager):
    regular_list = list(manager_list).copy()
    return manager.list(regular_list)


def readData(global_data, manager):
    try:
        with open("global_data.json", 'r') as file:

            data = convertToManager(json.load(file), manager)
            for key, value in data.items():
                global_data[key] = value

    except:
        reset(global_data)
        readData(global_data, manager)


def ulozit(global_data):
    with open("global_data.json", 'w') as file:
        temp_konec = global_data['konec']

        global_data['konec']  = False
        global_data['reset']  = False
        global_data['ulozit'] = False

        json.dump(convertFromManager(global_data), file, indent=4)

        global_data['konec'] = temp_konec


def reset(global_data):
    global_data = {
        "aktualni_okna": [
            "hudba_minihra"
        ],
        "otevrena_okna": [],
        "konec": False,
        "reset": False,
        "ulozit": False,
        "focus_nastaveni": False,
        "focus_inventory": False,
        "penize": 0,
        "energie": 0,
        "hrac": {
            "x": 960,
            "y": 540
        },
        "nastaveni": {
            "exit": 27,
            "inventory": 9,
            "interakce": 101,
            "nahoru": 119,
            "dolu": 115,
            "doleva": 97,
            "doprava": 100
        },
        "inventory": []
    }

    ulozit(global_data)


if __name__ == "__main__":

    with multiprocessing.Manager() as manager:

        global_data = manager.dict()

        readData(global_data, manager)
        global_data['otevrena_okna'] = cloneManagerList(global_data['aktualni_okna'], manager)
        global_data['aktualni_okna'] = manager.list()

        processes = []
        while True:
            if global_data['reset']:
                reset(global_data)

            if global_data['ulozit']:
                ulozit(global_data)

            if global_data['otevrena_okna'] != []:
                for okno in global_data['otevrena_okna']:
                    process = multiprocessing.Process(target=createWindow, args=(global_data, okno,))
                    processes.append(process)
                    global_data['aktualni_okna'].append(okno)
                    process.start()

                global_data['otevrena_okna'] = manager.list()

            processy_dokonceny = all(not p.is_alive() for p in processes)
            if global_data['konec'] or processy_dokonceny:
                break

        for process in processes:
            process.join()
