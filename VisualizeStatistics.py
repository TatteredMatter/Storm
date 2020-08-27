import tkinter as tk

storm = 0
mana = 0
creatures = 0
mana_g = 0

root= tk.Tk()

def cast_spell():
    global storm
    global mana
    global creatures
    storm += 1
    lbl_storm.config(text="Storm: " + str(storm))

    if chkbox_creature.get() == 1:
        creatures += 1
        lbl_creatures.config(text="Creatures: " + str(creatures))

def sacrifice():
    global creatures
    creatures -= 1
    lbl_creatures.config(text="Creatures: " + str(creatures))

#Labels
lbl_storm = tk.Label(text = "Storm: " + str(storm))
lbl_storm.grid(row=0,column=0)

lbl_mana = tk.Label(text = "Mana Floating: " + str(mana))
lbl_mana.grid(row=0,column=1)

lbl_creatures = tk.Label(text = "Creatures: " + str(creatures))
lbl_creatures.grid(row=0,column=2)

lbl_mana_generation = tk.Label(text = "Mana Generation: ")
lbl_mana_generation.grid(row=1,column=0)

#Check Buttons
chkbox_creature = tk.IntVar()
tk.Checkbutton(root, text="Creature Spell", variable=chkbox_creature).grid(row=2, column = 2)

#Buttons
btn_cast = tk.Button(text = "Cast Spell", command = cast_spell)
btn_cast.grid(row=4,column = 4)

btn_cast = tk.Button(text = "Sacrifice a Creature", command = sacrifice)
btn_cast.grid(row=5,column = 4)

#Text Entry
entry_mana = tk.Entry()
entry_mana.grid(row = 1, column = 1)



root.mainloop()