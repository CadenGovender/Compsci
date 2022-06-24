#07/06/2022
#This Program is for Julie to keep track of which items are being used and by who
#Created by Caden Govender

#Import tkinter so we can make a GUI
from tkinter import *

#Create the buttons and labels
def setup_buttons():
    
    #These are the global variables that are used
    global receipt_details, entry_customerfn, entry_receiptnum, entry_hireditems, entry_numberitems, total_entries, delete_item

    #All the labels, buttons and entry boxes
    Label(main_window, text="Customer Full Name") .grid(column=0, row=0)
    entry_customerfn = Entry(main_window)
    entry_customerfn.grid(column=1, row=0)

    Label(main_window, text="Receipt Number") .grid(column=0, row=1)
    entry_receiptnum = Entry(main_window)
    entry_receiptnum.grid(column=1, row=1)

    Label(main_window, text="Items Hired") .grid(column=0, row=2)
    entry_hireditems = Entry(main_window)
    entry_hireditems.grid(column=1, row=2)

    Label(main_window, text="Number of Items Hired") .grid(column=0, row=3)
    entry_numberitems = Entry(main_window)
    entry_numberitems.grid(column=1, row=3)

    Label(main_window, text="Row #") .grid(column=0, row=5, pady=20)
    delete_item = Entry(main_window)
    delete_item .grid(column=1, row=5, pady=20)
    
    Label(main_window, text="               ") .grid(column=2, row=0)

    Button(main_window, text="Delete Row", command=delete_row, width=10) .grid(column=0, row=6, sticky=N)
    Button(main_window, text="Quit", command=quit, width=10) .grid(column=4, row=0, sticky=E)
    Button(main_window, text="Append Details", command=check_inputs) .grid(column=3, row=6)
    Button(main_window, text="Print Details", command=print_receipt_details, width=10) .grid(column=4, row=6, sticky=E)

#Print all the receipt details
def print_receipt_details():

    #The global variables that are used
    global total_entries, name_count
    name_count = 0

    #Create the column headings
    Label(main_window, font=("Helvetica 13 "), text="Row").grid(column=0, row=7) 
    Label(main_window, font=("Helvetica 13 "), text="Customer Full Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 13 "), text="Receipt Number").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 13 "), text="Item(s) Hired").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 13 "), text="Number of Items Hired").grid(column=4, row=7)

#Add each item in the list into its own row
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(receipt_details[name_count][0])).grid(column=1, row=name_count+8)
        Label(main_window, text=(receipt_details[name_count][1])).grid(column=2, row=name_count+8)
        Label(main_window, text=(receipt_details[name_count][2])).grid(column=3, row=name_count+8)
        Label(main_window, text=(receipt_details[name_count][3])).grid(column=4, row=name_count+8)
        name_count += 1

#Check the inputs are all valid and not blank
def check_inputs():
    
    #The global variables that are used
    global receipt_details, entry_customerfn, entry_receiptnum, entry_hireditems, entry_numberitems, total_entries
    input_check = 0
    Label(main_window, text="               ") .grid(column=2, row=0)
    Label(main_window, text="               ") .grid(column=2, row=1)
    Label(main_window, text="               ") .grid(column=2, row=2)
    Label(main_window, text="               ") .grid(column=2, row=3)

    #Check that the customer full name is not blank, set error text if blank
    if len(entry_customerfn.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=0)
        input_check = 1

    #Check that the receipt number is not blank and is in integer, set error text if blank or is not an integer
    if (entry_receiptnum.get().isdigit()):
        if int(entry_receiptnum.get()) < 1 or int(entry_receiptnum.get()) > 500:
            Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
            input_check = 1
    else:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
        input_check = 1

    # check the number of items hired if blank or is not between 1 - 500, set error text
    if (entry_numberitems.get().isdigit()):
        if int(entry_numberitems.get()) < 1 or int(entry_numberitems.get()) > 500:
            Label(main_window, fg="red", text="1-500") .grid(column=2, row=3)
            input_check = 1
    else:
        Label(main_window, fg="red", text="1-500") .grid(column=2, row=3)
        input_check = 1

    #Check that the item hired entry box is not blank, set error text if blank
    if len(entry_hireditems.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=2)
        input_check = 1
    if input_check == 0:
        append_name()

#Add the next receipt details to the list
def append_name():

    #The global variables that are used
    global receipt_details, entry_customerfn, entry_receiptnum, entry_hireditems, entry_numberitems, total_entries

    #Append each item to its own area of the list
    receipt_details.append([entry_customerfn.get(), entry_receiptnum.get(), entry_hireditems.get(), entry_numberitems.get()])

    #Clear the boxes
    entry_customerfn.delete(0, 'end')
    entry_receiptnum.delete(0, 'end')
    entry_hireditems.delete(0, 'end')
    entry_numberitems.delete(0, 'end')
    total_entries += 1

#Quits the program when button quit is pressed
def quit():
    main_window.destroy()

#Delete a row from the list
def delete_row():

    #The global variables that are used
    global receipt_details, delete_item, total_entries, name_count

    #Finds which row needs to be deleted and deletes it 
    del receipt_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')

    #Removes the information when delete row is pressed
    Label(main_window, text="          ").grid(column=0, row=name_count+7)
    Label(main_window, text="          ").grid(column=1, row=name_count+7)
    Label(main_window, text="          ").grid(column=2, row=name_count+7)
    Label(main_window, text="          ").grid(column=3, row=name_count+7)
    Label(main_window, text="          ").grid(column=4, row=name_count+7)
    
#Start the program 
def main():

    #The global variables that are used
    global main_window
    global receipt_details, total_entries

    #Create empty list for receipt details and empty variable for entries in the list
    receipt_details = []
    total_entries = 0

    #Create the gui and start it
    main_window = Tk()
    
    #Title for the main window
    main_window.title("Julie's Party Hire")
    setup_buttons()
    main_window.mainloop()


main()