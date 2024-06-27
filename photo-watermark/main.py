import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

def water1_1(input_img, output_img, text):
   original_img = Image.open(input_img)
   width, height = original_img.size
   watermark = ImageDraw.Draw(original_img)
   font_size = int(width / 11)
   font = ImageFont.truetype("arial.ttf", font_size)
   x, y = int(width / 1.5), int(height / 1.1)
   watermark.text((x, y), text, font=font, fill='#FFF', stroke_width=3, stroke_fill='#222', anchor='ms')
   original_img.save(output_img)

def water2_1(input_img, output_img, logo_img):
   original_img = Image.open(input_img)
   copied_image = original_img.copy()
   width, height = original_img.size
   x, y = int(width / 1.5), int(height / 1.1)
   ii = Image.open(logo_img)
   copied_image.paste(ii,(x,y))
   copied_image.save(output_img)

def img1():
   path = filedialog.askopenfilename()
   entry1.delete(0, tk.END)
   entry1.insert(0, path)

def img2():
   path = filedialog.asksaveasfilename(defaultextension=".png")
   entry2.delete(0, tk.END)
   entry2.insert(0, path)

def img3():
   path = filedialog.askopenfilename()
   entry4.delete(0, tk.END)
   entry4.insert(0, path)

def watermark():
   path1 = entry1.get()
   path2 = entry2.get()
   path3 = entry4.get()
   text = entry3.get()
   if not path1 or not path2 or (not text and not path3):
       messagebox.showerror("Error", "All fields are required!")
       return
   if (text == True):
       water1_1(path1, path2, text)
   else:
       water2_1(path1, path2, path3)
   messagebox.showinfo("Congrats", "Watermarked image saved!")

root = tk.Tk()
root.title("Python Image Watermark")
root.geometry("500x500")

frame1 = tk.Frame(root)
frame1.pack(pady=20)

l1 = tk.Label(frame1, text="Image to Watermark:")
l1.pack(side="left", padx=10)
entry1 = tk.Entry(frame1, width=30)
entry1.pack(side="left")
button1 = tk.Button(frame1, text="Select", width=20, command=img1)
button1.pack(side="right", padx=10)

frame4 = tk.Frame(root)
frame4.pack(pady=20)
l4 = tk.Label(frame4, text="logo to be watermarked:")
l4.pack(side="left", padx=10)
entry4 = tk.Entry(frame4, width=30)
entry4.pack(side="left")
button4 = tk.Button(frame4, text="Select", width=20, command=img3)
button4.pack(side="right", padx=10)

frame2 = tk.Frame(root)
frame2.pack(pady=20)

l2 = tk.Label(frame2, text="Save Watermarked Image")
l2.pack(side="left", padx=10)
entry2 = tk.Entry(frame2, width=30)
entry2.pack(side="left")
button2 = tk.Button(frame2, text="Select", width=20, command=img2)
button2.pack(side="right", padx=10)

frame3 = tk.Frame(root)
frame3.pack(pady=20)

l3 = tk.Label(frame3, text="Enter text")
l3.pack(side="left", padx=10)
entry3 = tk.Entry(frame3, width=30)
entry3.pack(side="left")
button3 = tk.Button(root, width=20, text="Watermark", command=watermark)
button3.pack(expand=True)

root.mainloop()