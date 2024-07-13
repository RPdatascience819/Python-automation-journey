# Step by step
# Step 1 - Login to the system
# Step 2 - Log in
# Step 3 - Import database
# Step 4 - Register the product
# Step 5 - Repeat until the list of products is complete

import pyautogui
import time

# pyautogui.click - click with the mouse
# pyautogui.write - writing a text
# pyautogui.press - press a button
# pytautogui.hotkey - key combination (ctrl + shift)
# pyautogui.scroll - scroll up

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('Ronaldo - Chrome (1)')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)

# click for the loginRonaldo - Chrome (1)
pyautogui.click(x=948, y=409)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('datasciencefull@gmail.com')

# move to the password field
pyautogui.press('tab')
pyautogui.write('mypassword')
pyautogui.click(x=961, y=570)
#pyautogui.click(x=1658, y=368)

time.sleep(3)

# Importing the database

import pandas

table = pandas.read_csv('produtos.csv')
print(table)

# step 4 - Register the product
# for each row in my table

for line in table.index:
    # code
    pyautogui.click(x=886, y=293)

    code = str(table.loc[line, 'code'])
    pyautogui.write(code)

    # brand
    brand = str(table.loc[line, 'brand'])
    pyautogui.press('tab')
    pyautogui.write(brand)

    # type
    type = str(table.loc[line, 'type'])
    pyautogui.press('tab')
    pyautogui.write(type)

    # category
    category = str(table.loc[line, 'category'])
    pyautogui.press('tab')
    pyautogui.write(category)

    # unit price
    unit_price = str(table.loc[line, 'unit_price'])
    pyautogui.press('tab')
    pyautogui.write(unit_price)

    # product cost
    product_cost = str(table.loc[line, 'product_cost'])
    pyautogui.press('tab')
    pyautogui.write(product_cost)

    # OBS
    pyautogui.press('tab')
    obs = str(table.loc[line, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    # click on the send button
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(-1000)
    pyautogui.scroll(+1000)

    # step 5 - repeat for all products - for all table rows









