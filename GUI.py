from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as tkFileDialog
import shutil
import os

def getreal(x):

    for idx in range(len(x)):
        if(x[-(idx+1)]=='/'):
            i = len(x) - idx
            param = ''
            while (i<len(x)):
                param += x[i]
                i+=1
            return param

def cleanstr(x):
    
    i = 1
    while(x[-i]==' '):
        i+=1
    f=0
    while(x[f]==' '):
        f+=1
    return(x[f:(len(x)-i+1)])

def ceksama(lisinput,lisplit):
    
    lisbaru = [isi.upper() for isi in lisinput]
    lisbaru2 = [[isidari.upper() for isidari in isi]for isi in lisplit]
    for lis in lisbaru2:
        if (lis==lisbaru):
            return True
    return False

def digit_transformer(x):
    
    def satudigit(digit):
        daftar=["nol","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan"]
        return daftar[int(digit)]

    def duadigit(digit):
        
        if (int(digit[0])==0):
            if (int(digit[1])==0): return ""
            else: return satudigit(digit[1])
        if (int(digit[0])==1):
            if (int(digit[1])==1): return "sebelas"
            elif (int(digit[1])==0): return "sepuluh"
            else: return satudigit(digit[1])+" belas"
        else:
            if (int(digit[1])==0): return (satudigit(digit[0])+" "+"puluh")
            else: return satudigit(digit[0])+" puluh "+satudigit(digit[1])

    def tigadigit(digit):
        
        if (int(digit[0])==0):
            return ""+duadigit(digit[1:3])
        elif (int(digit[0])==1):
            return "seratus "+duadigit(digit[1:3])
        else:
            return satudigit(digit[0])+" ratus "+duadigit(digit[1:3])

    def empatdigit(digit):
        
        if (int(digit[0])==1):
            return "seribu "+tigadigit(digit[1:4])
        else:
            return satudigit(digit[0])+" ribu "+ tigadigit(digit[1:4])

    def limadigit(digit):
        
        return duadigit(digit[0:3])+" ribu "+tigadigit(digit[2:5])

    def enamdigit(digit):
        
        return tigadigit(digit[0:3])+" ribu "+tigadigit(digit[3:6])
  
    nilai=x
    if len(nilai)==2: return(duadigit(nilai))
    elif len(nilai)==1: return(satudigit(nilai))
    elif len(nilai)==3: return(tigadigit(nilai))
    elif len(nilai)==4: return(empatdigit(nilai))
    elif len(nilai)==5: return(limadigit(nilai))
    elif len(nilai)==6: return(enamdigit(nilai))
    
def update_file():
    
    file_menu=open("menu.txt","w")
    for index in range(len(list_minuman)):
        file_menu.write(list_minuman[index])
        file_menu.write(",")
        file_menu.write(list_harga[index])
        file_menu.write(",")
        file_menu.write(str(list_stok[index]))
        file_menu.write("\n")
    file_menu.close()
    
def read_file(list_minumanp,list_hargap,list_stokp):
    
    file_menu=open("menu.txt","r")
    for baris in file_menu:
        data=baris.split(",")
        list_minumanp.append(data[0])
        list_hargap.append(data[1])
        list_stokp.append(int(data[2]))
    file_menu.close()
    
    
def verify_file():
    
    for index in range(len(list_harga)):
        int(list_harga[index])
    for index in range(len(list_stok)):
        int(list_stok[index])

list_minuman=[]
list_harga=[]
list_stok=[]

try:
    
    read_file(list_minuman,list_harga,list_stok)
    verify_file()
        
except IOError:
    
    list_minuman=["Aqua botol","Aqua gelas","Coca-cola","Equil"]
    list_harga=["2500","500","9000","16750"]
    list_stok=[10,7,5,11]
    update_file()

except ValueError:

    list_minuman=["Aqua botol","Aqua gelas","Coca-cola","Equil"]
    list_harga=["2500","500","9000","16750"]
    list_stok=[10,7,5,11]
    update_file()

class mainMenu():
    
    def __init__(self):
        
        self.img = []
        self.window = Tk()
        self.window.title("Vending Machine 2.0")
        self.entripswd = Entry(self.window)
        label = Label(self.window, text= "Silahkan pilih minuman yang diinginkan",justify=CENTER)
        self.radiobtn = []
        self.var = IntVar()
        tmpcnt = 0
        
        for i in range(len(list_minuman)):
            tmpcnt+=1
            
        self.labels = StringVar()
        self.lebel = Label(self.window, textvariable= self.labels,anchor='w',fg='white')
        self.labels.set("")
        self.lebel.grid(row =7, column= 1,columnspan=tmpcnt)
        label.grid(row =2, column= 0, columnspan=tmpcnt)
        self.varharga = []
        self.varstok = []
        
        for i in range(len(list_minuman)):
            self.varharga.append(StringVar())
            self.varharga[i].set("Rp "+list_harga[i])
            self.varstok.append(StringVar())
            self.varstok[i].set("Stok: "+str(list_stok[i]))
            
        for idx in range(len(list_minuman)):
            try:
                self.img.append(PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+list_minuman[idx]+".png"))
                tempbutton = Button(self.window, image=self.img[idx],command = lambda idx = idx : self.ubahtbl(idx))
            except:
                tempbutton = Button(self.window, text=list_minuman[idx],command = lambda idx = idx : self.ubahtbl(idx))
            if (list_stok[idx]==0):
                tempbutton.config(state = DISABLED)
            self.radiobtn.append(tempbutton)
            tempbutton.grid(row=3,column = idx)
            Label(self.window, textvariable=self.varharga[idx]).grid(row=5, column=idx)
            Label(self.window, textvariable=self.varstok[idx]).grid(row=6, column=idx)
            
        #self.Tombol = Button(self.window, text="Buy",command=self.buy)
        #self.Tombol.grid(row =7)
        self.mntncbtn = Button(self.window, text="Pengaturan",command=self.mentenbtn)
        self.mntncbtn.grid(row = 0)
        self.window.mainloop()

    def ubahtbl(self,index):
        list_stok[index] -= 1
        self.labels.set("Anda memesan "+list_minuman[index]+" dengan harga "+digit_transformer(list_harga[index])+" rupiah")
        if (list_stok[index]==0):
            self.radiobtn[index].config(state=DISABLED)
        self.varstok[index].set("Stok: "+str(list_stok[index]))
        update_file()
        
        self.lebel['bg'] = 'blue'

    def mentenbtn(self):
        
        self.entripswd.destroy()
        self.pswdvar = StringVar()
        self.entripswd = Entry(self.window, textvariable = self.pswdvar)
        self.entripswd.grid(row=0, column = 1,sticky='EW')
        self.tumbul = Button(self.window,text="Proceed",command=self.OnClick)
        self.tumbul.grid(row=0,column=2)
        self.entripswd.bind("<Return>", self.OnPressEnter)
        self.pswdvar.set(u"Enter your password here")
        self.window.resizable(True, False)
        self.window.update()
        self.window.geometry(self.window.geometry())
        self.entripswd.focus_set()
        self.entripswd.selection_range(0, END)

    def OnPressEnter(self, event):
        
        if (self.pswdvar.get() == '1606828085'):
            self.window.destroy()
            Maintenance()
            
        else:
            messagebox.showerror("Error","Password Salah")
            self.entripswd.destroy()
            self.tumbul.destroy()
            
    def OnClick(self):
        
        if (self.pswdvar.get() == '1606828085'):
            self.window.destroy()
            Maintenance()
            
        else:
            messagebox.showerror("Error","Password Salah")
            self.entripswd.destroy()
            self.tumbul.destroy()
            

class Maintenance():
    
    def __init__(self):
        
        self.window = Tk()
        self.window.title("Maintenance")
        self.window.protocol("WM_DELETE_WINDOW", self.utama)

        tombolUbahharga = Button (self.window, text = 'Menu ubah Harga', command=self.ubahHarga)
        tombolJenisBarang = Button(self.window, text = 'Menu tambah jenis minuman', command=self.jenisBarang)
        tombolStok = Button(self.window, text = 'Menu tambah Stok', command=self.tambahStok)
        tombolUbahharga.grid(column = 0,row=0)
        tombolJenisBarang.grid(column = 0,row=1)
        tombolStok.grid(row=2,column=0)
        self.varharga = []
        self.varstok = []
        for i in range(len(list_minuman)):
            self.varharga.append(StringVar())
            self.varharga[i].set(list_harga[i])
            self.varstok.append(StringVar())
            self.varstok[i].set("Stok: "+str(list_stok[i]))
        self.window.mainloop()

    def utama(self):
        
        self.window.destroy()
        mainMenu()

    def ubahHarga(self):
        
        for ele in self.window.winfo_children():
            ele.destroy()
        self.img = []
        tombolUbahharga = Button (self.window, text = 'Menu ubah Harga', command=self.ubahHarga)
        tombolJenisBarang = Button(self.window, text = 'Menu tambah jenis minuman', command=self.jenisBarang)
        tombolStok = Button(self.window, text = 'Menu tambah Stok', command=self.tambahStok)
        tombolUbahharga.grid(column = 0,row=0)
        tombolUbahharga.config(state = DISABLED)
        tombolJenisBarang.grid(column = 0,row=1)
        tombolStok.grid(row=2,column=0)
        tombolDismis = Button(self.window,text="Kembali ke vending machine",command=self.dismis).grid(row=3,column=0)
        tombolExit = Button(self.window,text="Keluar dari program",command=self.Exit).grid(row=4,column=0)
        Label(self.window,anchor='w',fg="white",bg="blue").grid(row=0,rowspan=len(list_minuman)+1,column=1,columnspan=2,sticky='NS')
        self.hargabaru = []
        self.Entri=[]
        for idx in range(len(list_minuman)):
            try:
                self.img.append(PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+list_minuman[idx]+".png"))
                Label(self.window,image=self.img[idx]).grid(row = idx, column=3)
            except:
                Label(self.window,text=list_minuman[idx]).grid(row = idx, column=3)
            self.hargabaru.append(StringVar())
            self.hargabaru[idx].set(self.varharga[idx].get())
            self.hargabaru[idx].trace("w", lambda name, index, mode, var=self.hargabaru[idx]: self.callback(var))
            Label(self.window,text = "Rp").grid(row=idx,column=4)
            tmpentri = Entry(self.window, textvariable=self.hargabaru[idx],width=6,validate="key")
            self.Entri.append(tmpentri)
            self.Entri[idx]['validatecommand'] = (self.Entri[idx].register(self.testVal),'%P','%i','%d')
            self.Entri[idx].grid(row=idx, column = 5)
        Button(self.window, text="Ubah harga",command=self.doharga).grid(row=len(list_minuman),column=2,columnspan=4)
            
    def jenisBarang(self):
        
        for ele in self.window.winfo_children():
            ele.destroy()
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('Image Files', '.png')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.png'
        options['parent'] = self.window
        options['title'] = 'Choose the image'
        tombolUbahharga = Button (self.window, text = 'Menu ubah Harga', command=self.ubahHarga)
        tombolJenisBarang = Button(self.window, text = 'Menu tambah jenis minuman', command=self.jenisBarang)
        tombolStok = Button(self.window, text = 'Menu tambah Stok', command=self.tambahStok)
        tombolUbahharga.grid(column = 0,row=0)
        tombolJenisBarang.config(state = DISABLED)
        tombolJenisBarang.grid(column = 0,row=1)
        tombolStok.grid(row=2,column=0)
        tombolDismis = Button(self.window,text="Kembali ke vending machine",command=self.dismis).grid(row=3,column=0)
        tombolExit = Button(self.window,text="Keluar dari program",command=self.Exit).grid(row=4,column=0)
        Label(self.window,anchor='w',fg="white",bg="blue").grid(row=0,rowspan=5,column=1,columnspan=4,sticky='NS')
        Label(self.window,text="Masukkan nama minuman yang baru").grid(row=0,column=6)
        self.newbarang = StringVar()
        struc = Entry(self.window,textvariable=self.newbarang,validate="key")
        struc['validatecommand'] = (struc.register(self.testVal2),'%P','%i','%d')
        struc.grid(row =0, column=7)
        self.newharga = StringVar()
        self.newharga.trace("w", lambda name, index, mode, var=self.newharga: self.callback(var))
        self.newstok = StringVar()
        Label(self.window,text="Masukkan harga minumannya").grid(row=1,column=6)
        entri = Entry(self.window,textvariable=self.newharga,width=6,validate="key")
        entri['validatecommand'] = (entri.register(self.testVal),'%P','%i','%d')
        entri.grid(row =1, column=7)
        Label(self.window,text="Masukkan stok minumannya").grid(row=2,column=6)
        entri2 = Entry(self.window,textvariable=self.newstok,validate="key")
        entri2['validatecommand'] = (entri2.register(self.testVal),'%P','%i','%d')
        entri2.grid(row =2, column=7)
        self.varchk = IntVar()
        self.chkbtn = Checkbutton(self.window,text="Pakai gambar",variable=self.varchk, onvalue=1, offvalue=0,command=self.ubahchk)
        self.chkbtn.grid(row=3,column=6)
        self.btn = Button(self.window,text="Open Image",command=self.askopenfilename)
        self.btn.config(state=DISABLED)
        self.btn.grid(row=3,column=7)
        tomvol = Button(self.window,text="Tambahkan minuman",command=self.addbarang)
        tomvol.grid(row=4,column=6,columnspan=3)
        
    def tambahStok(self):
        
        for ele in self.window.winfo_children():
            ele.destroy()
        self.img = []
        tombolUbahharga = Button (self.window, text = 'Menu ubah Harga', command=self.ubahHarga)
        tombolJenisBarang = Button(self.window, text = 'Menu tambah Jenis barang', command=self.jenisBarang)
        tombolStok = Button(self.window, text = 'Menu tambah Stok', command=self.tambahStok)
        tombolUbahharga.grid(column = 0,row=0)
        tombolStok.config(state = DISABLED)
        tombolJenisBarang.grid(column = 0,row=1)
        tombolStok.grid(row=2,column=0)
        tombolDismis = Button(self.window,text="Kembali ke vending machine",command=self.dismis).grid(row=3,column=0)
        tombolExit = Button(self.window,text="Keluar dari program",command=self.Exit).grid(row=4,column=0)
        Label(self.window,anchor='w',fg="white",bg="blue").grid(row=0,rowspan=len(list_minuman)+1,column=1,columnspan=4,sticky='NS')
        self.nwstk = []
        for idx in range(len(list_minuman)):
            kunci = StringVar()
            self.nwstk.append(StringVar())
            self.nwstk[idx].set('0')
            kunci.set(self.varstok[idx].get()+" +")
            try:
                self.img.append(PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+list_minuman[idx]+".png"))
                Label(self.window,image=self.img[idx]).grid(row = idx, column=5)
            except:
                Label(self.window,text=list_minuman[idx]).grid(row = idx, column=5)
            Label(self.window,textvariable = kunci).grid(row= idx,column=6)
            entri2= Entry(self.window,textvariable=self.nwstk[idx],width=5,validate="key")
            self.nwstk[idx].trace("w", lambda name, index, mode, var=self.nwstk[idx]: self.callback1(var))
            entri2['validatecommand'] = (entri2.register(self.testVal),'%P','%i','%d')
            entri2.grid(row=idx,column=7)
        Button(self.window,text="Tambah Stoknya",command=self.plustok).grid(row=len(list_minuman),column = 5,columnspan=8)

    def plustok(self):
        
        cnt = 0
        for idx in range(len(self.nwstk)):
            value = self.nwstk[idx].get()
            if ((value=='')or(value=='0')):
                cnt+=1
            else:
                list_stok[idx] += int(value)
                messagebox.showinfo("Information","Menu "+list_minuman[idx]+" berhasil ditambahkan stoknya sebanyak "+value)
                self.varstok[idx].set("Stok: "+str(list_stok[idx]))
                update_file()
                
                
        if cnt == len(list_minuman):
            messagebox.showwarning("Peringatan","Tidak ada yang ditambahkan")
        else:
            self.tambahStok()                

    def testVal(self,inStr,i,acttyp):
        
        ind=int(i)
        if acttyp == '1': 
            if not inStr[ind].isdigit():
                return False
        return True

    def testVal2(self,inStr,i,acttyp):
        
        ind=int(i)
        if acttyp == '1': 
            if not inStr[ind].isalpha():
                if inStr[ind] != ' ':
                    return False
        return True

    def callback(self,sv):
        
        c = sv.get()[0:6]
        sv.set(c)

    def callback1(self,sv):
        
        c = sv.get()[0:5]
        sv.set(c)


    def doharga(self):
        
        cnt = 1
        for idx in range(len(self.hargabaru)):
            if (str(self.hargabaru[idx].get())==list_harga[idx])or(self.hargabaru[idx].get()==''):
                cnt+=1
            else:
                list_harga[idx] = self.hargabaru[idx].get()
                messagebox.showinfo("Information","Harga "+list_minuman[idx]+" menjadi "+digit_transformer(list_harga[idx]))
                self.varharga[idx].set(list_harga[idx])
        if (cnt==len(list_harga)+1):
            messagebox.showwarning("Peringatan","Tidak ada pengubahan yang terjadi")
        else:
            update_file()
        self.ubahHarga()

    def askopenfilename(self):
        
        filename = tkFileDialog.askopenfilename(**self.file_opt)
        cleanFilename = ''
        for kata in filename:
            if kata=='/':
                cleanFilename+= '\\'
            else:
                cleanFilename+= kata
        self.cleanFilename = cleanFilename
        self.purename = getreal(filename)
        self.img = PhotoImage(file=cleanFilename)
        lbl = Label(self.window,image=self.img)
        lbl.grid(rowspan = 5,column=9,row=0)
        #shutil.copy(self.cleanFilename,os.path.dirname(os.path.abspath(__file__))+"\\Images")              ini copy filenya

    def ubahchk(self):
        
        if self.varchk.get()==1 :
            self.btn.config(state=NORMAL)
        else:
            self.btn.config(state=DISABLED)

    def addbarang(self):
        
        if ((self.newbarang.get()=='')or(self.newharga.get()=='')or(self.newstok.get()=='')or(self.newbarang.get()==' ')):
            messagebox.showerror("Error","Bagian nama, harga, dan stok tidak boleh dikosongkan")
        else:
            if (self.varchk.get()==1):
                try:
                    str(self.cleanFilename)
                    a = [minuman for minuman in list_minuman]
                    b = [isi.split() for isi in a]
                    tmp = cleanstr(self.newbarang.get())
                    tmpsplit = tmp.split()
                    if (tmp in a):
                        int('a')
                    if (ceksama(tmpsplit,b)):
                        int('a')
                    if os.path.exists(os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+tmp+".png"):
                        os.remove(os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+tmp+".png")
                    shutil.copy(self.cleanFilename,os.path.dirname(os.path.abspath(__file__))+"\\Images")
                    os.rename(os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+self.purename,os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+tmp+".png")
                    img = PhotoImage(os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+tmp+".png",width=120,height=120)
                    list_minuman.append(tmp)
                    #img = PhotoImage(os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+list_minuman[-1]+".png",width=120,height=120)
                    #img.write(filename=os.path.dirname(os.path.abspath(__file__))+"\\Images\\"+list_minuman[-1]+".png",format="png")
                    list_harga.append(self.newharga.get())
                    list_stok.append(int(self.newstok.get()))
                    self.varharga.append(StringVar())
                    self.varharga[-1].set(self.newharga.get())
                    self.varstok.append(StringVar())
                    self.varstok[-1].set(int(self.newstok.get()))
                    messagebox.showinfo("Information","Minuman "+list_minuman[-1]+" dengan harga "+digit_transformer(list_harga[-1])+" dengan stok "+str(list_stok[-1])+" berhasil ditambahkan")
                    update_file()
                    self.jenisBarang()

                except ValueError:
                    messagebox.showerror("Error","Minuman tersebut sudah ada, jangan ditambahkan lagi!")
                    
                except:
                    messagebox.showerror("Error","Harap masukkan file gambarnya!")
            else:
                try:
                    a = [minuman for minuman in list_minuman]
                    b = [isi.split() for isi in a]
                    tmp = cleanstr(self.newbarang.get())
                    tmpsplit = tmp.split()
                    if (tmp in a):
                        int('a')
                    if (ceksama(tmpsplit,b)):
                        int('a')
                    list_minuman.append(tmp)
                    list_harga.append(self.newharga.get())
                    list_stok.append(int(self.newstok.get()))
                    self.varharga.append(StringVar())
                    self.varharga[-1].set(self.newharga.get())
                    self.varstok.append(StringVar())
                    self.varstok[-1].set(int(self.newstok.get()))
                    messagebox.showinfo("Information","Minuman "+list_minuman[-1]+" dengan harga "+digit_transformer(list_harga[-1])+" dengan stok "+str(list_stok[-1])+" berhasil ditambahkan")
                    update_file()
                    self.jenisBarang()
                    
                except ValueError:
                    messagebox.showerror("Error","Minuman tersebut sudah ada, jangan ditambahkan lagi!")

    def Exit(self):
        
        self.window.destroy()

    def dismis(self):
        
        self.window.destroy()
        mainMenu()
        
obj = mainMenu()

