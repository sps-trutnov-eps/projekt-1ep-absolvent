import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import main as masterFunc
from master import convertFuncToStr as novyProgram

# sem piste importy
import pygame
import random
import sys
from itemy import Item
from itemy import textury
from slot import Slot

pygame.font.init()

def main(global_data):
    #itemy = bobek, ohryzek, kebab, noviny, lahev, krabicak, hodinky, tuzemak, energetak, derava_cepice, derave_tricko, derave_kalhoty, pizza, burger

    #barvicky
    cerna = (0, 0, 0)
    transparent_gray = pygame.Color(143, 133, 125, 110)

    #grid properties
    velikost_ctverecku = 93 + 1/3
    gap = 10

    open_slots = [False] * 9
    last_frame_pressed = [False] * 9

    fps_casovac = pygame.time.Clock()
    fps = 60

    #okno
    okraje = 20

    rozliseni_x = 300 + 2*okraje
    rozliseni_y = rozliseni_x

    okno = pygame.display.set_mode((rozliseni_x, rozliseni_y), pygame.SRCALPHA)
    pygame.display.set_caption("Looting koše")
    bg = pygame.image.load("source//textury//Minigame_bg.png")


    pocet_itemu = 9
    pocet_bobku = random.randint(1, 2)

    row_1 = okraje
    row_2 = okraje + velikost_ctverecku + gap
    row_3 = okraje + 2 * velikost_ctverecku + 2 * gap

    col_1 = okraje
    col_2 = okraje + velikost_ctverecku + gap
    col_3 = okraje + 2 * velikost_ctverecku + 2 * gap


    slot_positions = [
        (row_1, col_1),
        (row_2, col_1),
        (row_3, col_1),
        (row_1, col_2),
        (row_2, col_2),
        (row_3, col_2),
        (row_1, col_3),
        (row_2, col_3),
        (row_3, col_3)
    ]

    bobek_open_timer = 90
    font = pygame.font.SysFont("Calibri", 24)

    #item choosing system
    itemy_v_kosi = []
    
    # Get all available item types
    dostupne_itemy = list(textury.keys())
    
    # Determine how many bobeks to include (1-2)
    pocet_bobku = random.randint(1, 2)
    
    # First add the guaranteed bobeks
    bobek_positions = random.sample(range(pocet_itemu), pocet_bobku)
    
    # Track which items we've already added to avoid duplicates
    pouzite_itemy = []
    if "bobek" in dostupne_itemy:
        pouzite_itemy.append("bobek")
    
    # Fill all positions
    for i in range(pocet_itemu):
        if i in bobek_positions:
            # Add a bobek at this position
            item_nazev = "bobek"
        else:
            # For non-bobek positions, choose a random item that hasn't been used yet
            dostupne_neukazane_itemy = [item for item in dostupne_itemy if item not in pouzite_itemy]
            
            # If we've used all items, reset the available items (except bobek)
            if not dostupne_neukazane_itemy:
                pouzite_itemy = ["bobek"] if "bobek" in pouzite_itemy else []
                dostupne_neukazane_itemy = [item for item in dostupne_itemy if item not in pouzite_itemy]
            
            item_nazev = random.choice(dostupne_neukazane_itemy)
            pouzite_itemy.append(item_nazev)
            
        itemy_v_kosi.append(Item(textury[item_nazev], slot_positions[i], item_nazev))


    sloty = []

    for i in range(len(slot_positions)):
        sloty.append(Slot(slot_positions[i][0], slot_positions[i][1], velikost_ctverecku, velikost_ctverecku, transparent_gray))

    # Initialize inventory structure if needed
    if not global_data['inventory']:
        # Create empty columns based on inventory_xy[1]
        for _ in range(global_data['inventory_xy'][1]):
            global_data['inventory'].append([])
    
    # Make sure we have the right number of columns
    while len(global_data['inventory']) < global_data['inventory_xy'][1]:
        global_data['inventory'].append([])

    # Store items temporarily until we know if player found a bobek
    temp_inventory = []
    for _ in range(global_data['inventory_xy'][1]):
        temp_inventory.append([])

    # Flag to track if player found a bobek
    bobek_found = False

    main_loop = True
    while main_loop:
        lmb = False

        udalosti = pygame.event.get()
        for udalost in udalosti:
            if udalost.type == pygame.QUIT:
                main_loop = False

            if udalost.type == pygame.MOUSEBUTTONDOWN and udalost.button == 1:
                lmb = True
            elif udalost.type == pygame.MOUSEBUTTONUP and udalost.button == 1:
                for i in range(len(last_frame_pressed)):
                    last_frame_pressed[i] = False

        fps_casovac.tick(fps)

        mys = pygame.mouse.get_pos()

        okno.fill(cerna)
        okno.blit(bg, (0, 0))

        slot_1_r = pygame.Rect(row_1, col_1, velikost_ctverecku, velikost_ctverecku)
        slot_2_r = pygame.Rect(row_2, col_1, velikost_ctverecku, velikost_ctverecku)
        slot_3_r = pygame.Rect(row_3, col_1, velikost_ctverecku, velikost_ctverecku)

        slot_4_r = pygame.Rect(row_1, col_2, velikost_ctverecku, velikost_ctverecku)
        slot_5_r = pygame.Rect(row_2, col_2, velikost_ctverecku, velikost_ctverecku)
        slot_6_r = pygame.Rect(row_3, col_2, velikost_ctverecku, velikost_ctverecku)
        
        slot_7_r = pygame.Rect(row_1, col_3, velikost_ctverecku, velikost_ctverecku)
        slot_8_r = pygame.Rect(row_2, col_3, velikost_ctverecku, velikost_ctverecku)
        slot_9_r = pygame.Rect(row_3, col_3, velikost_ctverecku, velikost_ctverecku)
      
        slot_rects = [
            slot_1_r, slot_2_r, slot_3_r,
            slot_4_r, slot_5_r, slot_6_r,
            slot_7_r, slot_8_r, slot_9_r
        ]

        for slot in sloty:
            slot.vykresli(okno)

        for i, rect in enumerate(slot_rects):
            if lmb and rect.collidepoint(mys):
                if not last_frame_pressed[i]:
                    open_slots[i] = not open_slots[i]
                    last_frame_pressed[i] = True

                    # Check if this is a bobek
                    if open_slots[i] and itemy_v_kosi[i].nazev == 'bobek':
                        bobek_found = True
                    
                    # Only add item if we're opening the slot and it's not a bobek
                    if open_slots[i] and itemy_v_kosi[i].nazev != 'bobek':
                        # Find the column with the fewest items
                        column_with_space = 0
                        min_items = len(temp_inventory[0])
                        
                        for col_index in range(len(temp_inventory)):
                            if len(temp_inventory[col_index]) < min_items:
                                min_items = len(temp_inventory[col_index])
                                column_with_space = col_index
                                
                        # Only add if the column has space
                        if len(temp_inventory[column_with_space]) < global_data['inventory_xy'][0]:
                            temp_inventory[column_with_space].append(itemy_v_kosi[i].nazev)

        # Draw each item if its slot is open
        for i, is_open in enumerate(open_slots):
            if is_open:
                itemy_v_kosi[i].vykresli(okno)

                if itemy_v_kosi[i].nazev == "bobek":
                    # Show message that player found a bobek
                    bobek_found_text = font.render("Našel jsi bobek a přišel jsi o své věci!", True, (255, 0, 0))
                    text_width = bobek_found_text.get_width()
                    text_x = (rozliseni_x - text_width) / 2
                    okno.blit(bobek_found_text, (text_x, (rozliseni_y / 2)))

                    if bobek_open_timer > 0:
                        bobek_open_timer -= 1

                    if bobek_open_timer <= 0:
                        global_data["nasel_bobek"] = True
                        return 0

        pygame.display.flip()

    # Only save items to inventory if no bobek was found
    if not bobek_found:
        # Transfer items from temp inventory to global inventory
        for col_index in range(len(temp_inventory)):
            for item in temp_inventory[col_index]:
                # Find column with fewest items in global inventory
                min_col = 0
                min_items = len(global_data['inventory'][0])
                for i in range(len(global_data['inventory'])):
                    if len(global_data['inventory'][i]) < min_items:
                        min_items = len(global_data['inventory'][i])
                        min_col = i
                
                # Add item if there's space
                if len(global_data['inventory'][min_col]) < global_data['inventory_xy'][0]:
                    global_data['inventory'][min_col].append(item)
        
        global_data['ulozit'] = True

if __name__ == "__main__":
    masterFunc(novyProgram(main))