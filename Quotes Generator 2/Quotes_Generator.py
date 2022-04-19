import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PyPDF2 import PdfFileMerger
import shutil

# get list of pdfs
pdf_folder = "PDF_templates/"
pdf_list = os.listdir(pdf_folder)
print(pdf_list)
quote = "haha"
quote_pdf = "haha2"
PDFtitle = ""


# Grab input from txt box:
def retrieve_input():
    input = self.myText_Box.get("1.0", 'end-1c')


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def save_to_folder(src, dst):
    shutil.copyfile(src, dst)


def UploadAction():
    quote_pdf = filedialog.askopenfilename()
    global upload_quote
    upload_quote["text"] = quote_pdf

    print('Selected:', quote)
    print(pdf_folder + fence_picked.get())
    shutil.copyfile("PDF_templates/" + fence_picked.get(), "folder_to_merge/template.pdf")
    shutil.copyfile(quote_pdf, "folder_to_merge/quote.pdf")

    return quote_pdf


def merge_PDF(event=None):
    print("DIRECTORIES:")
    
    pdfs = ["folder_to_merge/template.pdf", "folder_to_merge/quote.pdf"]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(get_download_path() + "/" + PDFtitle.get("1.0", 'end-1c') + ".pdf")

    # Clean up Data:
    global drop
    global upload_quote
    global fence_picked

    
    PDFtitle.delete("1.0","end")
    upload_quote["text"] = "Upload Quotes PDF"

    merger.close()


root = Tk()
root.title("Merge PDF's")
root.geometry("400x250")
root.configure(bg='black')


# root.iconbitmap(r"edmund_icon.ico")


def callback(*args):
    print(e.get())


# drop Down boxes
# https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter


main_title_lebel = Label(text="TREX FENCING QUOTES & TEMPLATE MERGER :  ", bg="black", fg="white")
main_title_lebel.pack()

main_title_lebel = Label(text="Select Template from Picklist :  ", bg="black", fg="yellow")
main_title_lebel.pack()

fence_picked = StringVar()
fence_picked.set("Pick Available Fence")
drop = OptionMenu(root, fence_picked, *pdf_list)
drop.pack()
# Upload PDF
main_title_lebel = Label(text="Upload the Quotes PDF :  ", bg="black", fg="yellow")
main_title_lebel.pack()

quote_file = StringVar()
fence_picked.set("Pick Available Fence")
upload_quote = tk.Button(root, text='Open Quote PDF', command=UploadAction)
upload_quote.pack()

PDF_name_lebel = Label(text="Add New PDF Name:  ", bg="black", fg="yellow")
PDF_name_lebel.pack()

PDFtitle = tk.Text(root,
                   height=1,
                   width=20,
                   )

PDFtitle.pack()

merge_button_lebel = Label(text="Save merged PDF to Downloads Folder:  ", bg="black", fg="yellow")
merge_button_lebel.pack()

merge_button = tk.Button(root, text='SAVE', command=merge_PDF)
merge_button.pack()

root.mainloop()
