import json
import pygame
import multiprocessing
import ctypes
from ctypes import wintypes
import importlib

# pip install pywin32
import win32gui
import win32con

def focusWindow():
    # Get the HWND (Window Handle) of the most recent Pygame window
    hwnd = pygame.display.get_wm_info()['window']

    # Apply "always on top" flag using HWND
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    print(f"[+] Window with HWND {hwnd} is now on top.")

def createWindow(global_data, okno):
    ######################################################################################################
                                                # Vzdycky vezme jen 1 argument "global data"
    convertStrToFunc(okno)(global_data)         # Spustena Funkce - Minihra nebo jakykoliv program
    global_data["aktualni_okna"].remove(okno)   # Ulozi informaci ze okno je zavreny
    ######################################################################################################

def setWindowPos(x, y):
    hwnd = pygame.display.get_wm_info()['window']
    width, height = pygame.display.get_surface().get_size()
    ctypes.windll.user32.MoveWindow(hwnd, x, y, width, height, True)

def moveWindow(keybind, event, dragging, mouse_offset):
    """
    pro pouziti se musi pridat tadyto pred main loop

    Inicializace posouvani oken

    win_x, win_y = 100, 100;
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{win_x},{win_y}";
    dragging = False;
    mouse_offset = (0, 0)

    a take se musi pridat do
    "for event in pygame.event.get():"

        "dragging, mouse_offset = moveWindow(global_data['nastaveni']['pohyb_oken'], udalost, dragging, mouse_offset)"
    """



    keys = pygame.key.get_pressed()
    if keys[keybind]:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                dragging = True
                mouse_offset = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False

        elif event.type == pygame.MOUSEMOTION and dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - mouse_offset[0]
            dy = mouse_y - mouse_offset[1]

            # Get current position using ctypes
            hwnd = pygame.display.get_wm_info()['window']
            rect = wintypes.RECT()
            ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
            new_x = rect.left + dx
            new_y = rect.top + dy
            setWindowPos(new_x, new_y)

    return dragging, mouse_offset






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


def convertStrToFunc(string: str):

    if '.' in str(string):
        module_path, func_name = string.rsplit(".", 1)
        module = importlib.import_module(module_path)
        return getattr(module, func_name)

    else:
        return globals()[string]


def convertFuncToStr(func):
    return f"{func.__module__}.{func.__qualname__}"


def reset(global_data):
    global_data = {
        "aktualni_okna": [],
        "otevrena_okna": [],
        "konec": False,
        "reset": False,
        "ulozit": False,
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
            "doprava": 100,
            "pohyb_oken": 1073742050
        },
        "inventory": [],
        "inventory_xy": [6, 3]
    }

    ulozit(global_data)


def main(funkce = None):
    with multiprocessing.Manager() as manager:

        global_data = manager.dict()

        readData(global_data, manager)

        if funkce != None:
            global_data['aktualni_okna'].append(funkce)

        global_data['otevrena_okna'] = cloneManagerList(global_data['aktualni_okna'], manager)
        global_data['aktualni_okna'] = manager.list()


        processes = []
        while True:

            if global_data['reset']:
                reset(global_data)

            if global_data['ulozit']:
                ulozit(global_data)

            if global_data['otevrena_okna'] != []:

                nova_okna = list(set(list(global_data["otevrena_okna"])))
                aktualni_okna = list(set(list(global_data["aktualni_okna"])))

                nova_okna = [item for item in nova_okna if item not in aktualni_okna]

                for okno in nova_okna:
                    global_data['aktualni_okna'].append(okno)
                    process = multiprocessing.Process(target=createWindow, args=(global_data, okno,))
                    processes.append(process)
                    process.start()

                global_data['otevrena_okna'] = manager.list()

            processy_dokonceny = all(not p.is_alive() for p in processes)
            if global_data['konec'] or processy_dokonceny:
                break

        for process in processes:
            process.join()



if __name__ == "__main__":
    from mesta.mapa.main import main as TheProgram #mesta.mapa.main
    main(convertFuncToStr(TheProgram))