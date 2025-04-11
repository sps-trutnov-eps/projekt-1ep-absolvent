import os
import pygame
import multiprocessing

import mesto_1.main

def create_window(global_data, okno):

    ######################################################################################################
    if okno == 'mesto_1':
        mesto_1.main.main(global_data)          # Spustena Funkce - Minihra nebo jakykoliv program

    ######################################################################################################



if __name__ == "__main__":

    ######################################################################################################

    otevrena_okna = ['mesto_1']                 # Ze zacatku otevrena okna

    ######################################################################################################

    with multiprocessing.Manager() as manager:

        global_data = manager.dict()
        global_data['otevrena_okna'] = manager.list(otevrena_okna)
        global_data['konec'] = False

        processes = []
        while True:
            if global_data['otevrena_okna'] != []:
                for okno in global_data['otevrena_okna']:
                    process = multiprocessing.Process(target=create_window, args=(global_data, okno,))
                    processes.append(process)
                    process.start()

                global_data['otevrena_okna'] = manager.list()

            processy_dokonceny = all(not p.is_alive() for p in processes)
            if global_data['konec'] or processy_dokonceny:
                break

        for process in processes:
            process.join()
