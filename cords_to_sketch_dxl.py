from typing import Tuple
import customtkinter as ctk
import tkinter as tk
import re
import json
import pyperclip
from PIL import Image, ImageTk


ctk.set_appearance_mode("dark") # set app-mode


class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self,
                *args, **kwargs
                ):
        super().__init__(*args, **kwargs)
        self.title(f"Hello There!")
        self.geometry("430x570")
        self.resizable(False, False)

        self.PixelifySans_S30       =ctk.CTkFont(family="Pixelify Sans Bold", size=30)
        self.PixelifySans_S20       =ctk.CTkFont(family="Pixelify Sans Bold", size=20)
        self.PixelifySans_S14       =ctk.CTkFont(family="Pixelify Sans Bold", size=14)
        self.SourceCodeProBold_S20  =ctk.CTkFont(family="Source Code Pro Bold", size=20)
        self.SourceCodeProBold_S14  =ctk.CTkFont(family="Source Code Pro Bold", size=14)

        self.imgSource = Image.open("img/mupscltr.png")
        self.IMGwidth, self.IMGheight = self.imgSource.size

        self.my_image=ctk.CTkImage(light_image          =None,
                                  dark_image            =self.imgSource,
                                  size                  =(self.IMGwidth/15, self.IMGheight/15)
                                  )

        self.image_label=ctk.CTkLabel(master            =self,
                                      image             =self.my_image,
                                      text              ="")

        self.label_1   = ctk.CTkLabel(master            =self, 
                                      text              ="Hello There!",
                                      font              =self.PixelifySans_S30,
                                      )
        
        self.textBox   = ctk.CTkTextbox(master          =self,
                                        width           =430,
                                        height          =350,
                                        fg_color        ="transparent",        
                                        font            =self.SourceCodeProBold_S14,
                                        )
        
        self.label_1.grid(row=0, column=0, padx=(10, 10), pady=(10, 5), sticky="WE", columnspan=2)
        self.textBox.grid(row=1, column=0, padx=(0, 0), pady=(5, 10), sticky="W", columnspan=2)
        self.image_label.grid(row=2, column=0, padx=(0, 0), pady=(0, 0), sticky="W", columnspan=2)

        self.ReadMe = """Code by JohnTitorq
Also visit my github!
https://github.com/JohnTitorq

====================== HELP ======================

* Velocity: 
 Speed at which ALL servos rotate;

* Delay:
 The time between the turns of EACH servo;

* BackUp FileName:
 Name of the file in which your sketch code will
 be saved. If the name matches the name of the
 previous file, it will overwrite;

* Cleat all:
 Clear the fields "Coordinates" and "Sketch";

* Save options:
 Save settings (Velocity, Delay, BackUp FileName).
 The next time you open the program you will not
 need to enter the desired parameters;

* Convert:
 Perform the conversion;

* Copy Coords to clipboard:
 Copy the contents of the "Coordinates" field to
 Clipboard;

* Copy Sketch to clipboard:
 Copy the contents of the "Sketch" field to
 Clipboard;

===================== ПОМОЩЬ =====================

* Velocity:
 скорость с которой будут вращаться ВСЕ
 сервоприводы;

* Delay:
 промежуток времени между поворотами КАЖДОГО
 сервопривода;

* BackUp FileName:
 имя файла, в который сохранится Ваш код для
 скетча. Если название будет соответствовать
 названию предыдущего файла, то он
 перезапишется;

* Cleat all:
 очистить поле "Coordinates" и "Sketch";

* Save options:
 сохранить настройки
 (Valocity, Delay, BackUp FileName).
 При следующем открытии программы вам не нужно
 будет вписывать желаемые параметры;

* Convert:
 выполнить конвертирование;

* Copy Coords to clipboard:
 скопировать содержимое поля "Coordinates"
 в буфер обмена;

* Copy Sketch to clipboard:
 копировать содержимое поля "Sketch"
 в буфер обмена;

==================================================

"""

        self.textBox.insert("0.0", self.ReadMe)
        self.textBox.configure(state="disabled")

class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,
                 all_tbxxs_width, all_tbxxs_height,
                 label_1_text, label_2_text,
                 all_widgets_corner_rad=5, 
                 **kwargs
                 ):
        super().__init__(master, **kwargs)

        self.SourceCodeProBold_S20=ctk.CTkFont(family="Source Code Pro Bold", size=20)
        self.SourceCodeProBold_S14=ctk.CTkFont(family="Source Code Pro Bold", size=14)

        self.all_widgets_corner_rad         = all_widgets_corner_rad
        self.all_tbxxs_width                = all_tbxxs_width
        self.all_tbxxs_height               = all_tbxxs_height

        self.label_1_text                   = label_1_text
        self.label_2_text                   = label_2_text

        self.label_1   = ctk.CTkLabel(master            =self, 
                                      text              =label_1_text,
                                      font              =self.SourceCodeProBold_S14,
                                      )
        self.label_2   = ctk.CTkLabel(master            =self, 
                                      text              =label_2_text,
                                      font              =self.SourceCodeProBold_S14,
                                      )

        self.textbox_1 = ctk.CTkTextbox(master          =self,
                                        corner_radius   =self.all_widgets_corner_rad,
                                        width           =self.all_tbxxs_width,
                                        height          =self.all_tbxxs_height,
                                        )
        self.textbox_2 = ctk.CTkTextbox(master          =self,
                                        corner_radius   =self.all_widgets_corner_rad,
                                        width           =self.all_tbxxs_width,
                                        height          =self.all_tbxxs_height,
                                        )
        
        self.label_1.grid(row=0, column=0, padx=5, pady=(5, 0), sticky="WE")
        self.label_2.grid(row=0, column=1, padx=(5, 5), pady=(5, 0), sticky="WE")
        
        self.textbox_1.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="NWS")
        self.textbox_2.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky="NES")

    def _get_txtb1(self):

        get_info=self.textbox_1.get(1.0, "end-1c")
        return f"{get_info}"
    
    def _get_txtb2(self):

        get_info=self.textbox_2.get(1.0, "end-1c")
        return f"{get_info}"
    
    def insert_txtb2(self, LC, data):

        self.textbox_2.insert(LC, f"{data}\n")

    def del_all(self):

        self.textbox_1.delete("0.0", "end")
        self.textbox_2.delete("0.0", "end")

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, label_text, placeholder_text_1, placeholder_text_2, placeholder_text_3, 
                 bttn_event_1, bttn_event_2, bttn_event_3, bttn_event_4, bttn_event_5, bttn_text_1, bttn_text_2, bttn_text_3, bttn_text_4, bttn_text_5,
                #  ch_bx_1_text, ch_bx_2_text, 
                #  ch_bx_1_command, ch_bx_2_command,
                #  all_ch_bx_width=10, all_ch_bx_height=10, 
                 label_1_text, label_2_text, label_3_text, 
                 all_entry_width=200, all_entry_height=10, all_widgets_corner_rad=0,
                 all_bttn_width=200, all_bttn_height=10, 
                 **kwargs): 
        super().__init__(master, **kwargs)

        self.SourceCodeProBold_S20=ctk.CTkFont(family="Source Code Pro Bold", size=20)
        self.SourceCodeProBold_S14=ctk.CTkFont(family="Source Code Pro Bold", size=14)

        self.label_text                 = label_text
        self.label_1_text               = label_1_text
        self.label_2_text               = label_2_text
        self.label_3_text               = label_3_text
        

        self.placeholder_text_1         = placeholder_text_1
        self.placeholder_text_2         = placeholder_text_2
        self.placeholder_text_3         = placeholder_text_3
        self.all_entry_width            = all_entry_width
        self.all_entry_height           = all_entry_height
        self.all_widgets_corner_rad     = all_widgets_corner_rad
        
        self.all_bttn_width             = all_bttn_width
        self.all_bttn_height            = all_bttn_height
        self.bttn_event_1               = bttn_event_1
        self.bttn_event_2               = bttn_event_2
        self.bttn_event_3               = bttn_event_3
        self.bttn_event_4               = bttn_event_4
        self.bttn_event_5               = bttn_event_5
        self.bttn_text_1                = bttn_text_1
        self.bttn_text_2                = bttn_text_2
        self.bttn_text_3                = bttn_text_3
        self.bttn_text_4                = bttn_text_4
        self.bttn_text_5                = bttn_text_5

        # self.all_ch_bx_width            = all_ch_bx_width
        # self.all_ch_bx_height           = all_ch_bx_height
        # self.ch_bx_1_text               = ch_bx_1_text
        # self.ch_bx_2_text               = ch_bx_2_text
        # self.ch_bx_1_command            = ch_bx_1_command
        # self.ch_bx_2_command            = ch_bx_2_command
        

        self.label = ctk.CTkLabel(master            =self,
                                  text              =self.label_text,
                                  font              =self.SourceCodeProBold_S20,
                                  )
        self.label_1 = ctk.CTkLabel(master          =self,
                                  text              =self.label_1_text,
                                  font              =self.SourceCodeProBold_S14,
                                  )
        self.label_2 = ctk.CTkLabel(master          =self,
                                  text              =self.label_2_text,
                                  font              =self.SourceCodeProBold_S14,
                                  )
        self.label_3 = ctk.CTkLabel(master          =self,
                                  text              =self.label_3_text,
                                  font              =self.SourceCodeProBold_S14,
                                  )
        self.entry_1 = ctk.CTkEntry(master          =self,
                                    placeholder_text=self.placeholder_text_1,
                                    width           =self.all_entry_width,
                                    height          =self.all_entry_height,
                                    corner_radius   =all_widgets_corner_rad,
                                    font            =self.SourceCodeProBold_S14,
                                    )
        self.entry_2 = ctk.CTkEntry(master          =self,
                                    placeholder_text=self.placeholder_text_2,
                                    width           =self.all_entry_width,
                                    height          =self.all_entry_height,
                                    corner_radius   =all_widgets_corner_rad,
                                    font            =self.SourceCodeProBold_S14,
                                    )
        self.entry_3 = ctk.CTkEntry(master          =self,
                                    placeholder_text=self.placeholder_text_3,
                                    width           =self.all_entry_width,
                                    height          =self.all_entry_height,
                                    corner_radius   =all_widgets_corner_rad,
                                    font            =self.SourceCodeProBold_S14,
                                    )
        self.button_1 = ctk.CTkButton(master=       self,
                                    width           =self.all_bttn_width,
                                    height          =self.all_bttn_height,
                                    corner_radius   =self.all_widgets_corner_rad,
                                    text            =self.bttn_text_1,
                                    command         =self.bttn_event_1,

                                    fg_color        ="#1ac200",
                                    text_color      ="#ffffff", 
                                    font            =self.SourceCodeProBold_S14,
                                    )
        self.button_2 = ctk.CTkButton(master=       self,
                                    width           =self.all_bttn_width,
                                    height          =self.all_bttn_height,
                                    corner_radius   =self.all_widgets_corner_rad,
                                    text            =self.bttn_text_2,
                                    command         =self.bttn_event_2,

                                    fg_color        ="#bbc200",
                                    text_color      ="#ffffff", 
                                    font            =self.SourceCodeProBold_S14,
                                    )
        self.button_3 = ctk.CTkButton(master=       self,
                                    width           =self.all_bttn_width,
                                    height          =self.all_bttn_height,
                                    corner_radius   =self.all_widgets_corner_rad,
                                    text            =self.bttn_text_3,
                                    command         =self.bttn_event_3,

                                    fg_color        ="#fa1a0a",
                                    text_color      ="#ffffff", 
                                    font            =self.SourceCodeProBold_S14,
                                    )
        self.button_4 = ctk.CTkButton(master=       self,
                                    width           =self.all_bttn_width,
                                    height          =self.all_bttn_height,
                                    corner_radius   =self.all_widgets_corner_rad,
                                    text            =self.bttn_text_4,
                                    command         =self.bttn_event_4,

                                    # fg_color        ="#fa1a0a",
                                    # text_color      ="#ffffff", 
                                    font            =self.SourceCodeProBold_S14,
                                    )
        self.button_5 = ctk.CTkButton(master=       self,
                                    width           =self.all_bttn_width,
                                    height          =self.all_bttn_height,
                                    corner_radius   =self.all_widgets_corner_rad,
                                    text            =self.bttn_text_5,
                                    command         =self.bttn_event_5,

                                    # fg_color        ="#fa1a0a",
                                    # text_color      ="#ffffff", 
                                    font            =self.SourceCodeProBold_S14,
                                    )
        # self.check_bx_1 = ctk.CTkCheckBox(master    =self,
        #                             text            =self.ch_bx_1_text,
        #                             corner_radius   =self.all_widgets_corner_rad,
        #                             width           =self.all_ch_bx_width,
        #                             height          =self.all_ch_bx_height,
        #                             command         =self.ch_bx_1_command,
        #                             )

        # self.check_bx_2 = ctk.CTkCheckBox(master    =self,
        #                             text            =self.ch_bx_2_text,
        #                             corner_radius   =self.all_widgets_corner_rad,
        #                             width           =self.all_ch_bx_width,
        #                             height          =self.all_ch_bx_height,
        #                             command         =self.ch_bx_2_command,
        #                             )

        self.label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # self.check_bx_1.grid(row=1, column=0, padx=10, pady=5, sticky="W")
        # self.check_bx_2.grid(row=1, column=1, padx=10, pady=5, sticky="E")
        self.label_1.grid(row=2, column=0, padx=10, pady=(2, 0), columnspan=2, sticky="W")
        self.label_2.grid(row=4, column=0, padx=10, pady=(2, 0), columnspan=2, sticky="W")
        self.label_3.grid(row=6, column=0, padx=10, pady=(2, 0), columnspan=2, sticky="W")

        self.entry_1.grid(row=3, column=0, padx=10, pady=(0, 2), columnspan=2)
        self.entry_2.grid(row=5, column=0, padx=10, pady=(0, 2), columnspan=2)
        self.entry_3.grid(row=7, column=0, padx=10, pady=(0, 2), columnspan=2)

        self.button_3.grid(row=8, column=0, padx=10, pady=(5, 2.5), columnspan=2)
        self.button_2.grid(row=9, column=0, padx=10, pady=(2.5, 2.5), columnspan=2)
        self.button_1.grid(row=10, column=0, padx=10, pady=(2.5, 10), columnspan=2)
        self.button_4.grid(row=11, column=0, padx=10, pady=(2.5, 2.5), columnspan=2)
        self.button_5.grid(row=12, column=0, padx=10, pady=(2.5, 2.5), columnspan=2)

        self.entry_1.configure(state="normal")

    def get_vel(self):

        return f"{self.entry_1.get()}"
    
    def get_del(self):

        return f"{self.entry_2.get()}"
    
    def get_name(self):

        return f"{self.entry_3.get()}"
    
    def insert_from_conf(self):

        with open("conf.json", "r") as fh:
            load=json.load(fh)
            self.entry_1.insert(0, load["Vel"])
            self.entry_2.insert(0, load["Del"])
            self.entry_3.insert(0, load["Name"])


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()
        w, h = 780, 450
        self.title(f"DXL COORDINATES GUI BY JOHNTITORQ")
        self.geometry(f"{w}x{h}")
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.frames_height=500

        self.mainframe = MainFrame(master                   =self,
                                   #width                    =600,
                                   #height                   =self.frames_height,
                                   label_text               ="Options",
                                   placeholder_text_1       ="Velocity",
                                   placeholder_text_2       ="Delay",
                                   placeholder_text_3       ="FileName",
                                   all_widgets_corner_rad   =5,
                                   bttn_text_1              ="Convert",
                                   bttn_text_2              ="Save options",
                                   bttn_text_3              ="Clear all",
                                   bttn_text_4              ="Copy Coords to clipboard",
                                   bttn_text_5              ="Copy Sketch to clipboard",
                                   bttn_event_1             =lambda: self.convert_func(ovelocity=self.mainframe.get_vel(), delay=self.mainframe.get_del(), code=self.text_box_frame._get_txtb1(), filename=self.mainframe.get_name()),#print(f"{self.mainframe.get_vel()}\n{self.mainframe.get_del()}\n{self.mainframe.get_name()}\n{self.text_box_frame._get_txtb1()}"),#self.convert_func(ovelocity=self.mainframe.get_vel(), delay=self.mainframe.get_del(), code=self.text_box_frame.  get_txtb1_info()),
                                   bttn_event_2             =lambda: self.dump_args(ovel=self.mainframe.get_vel(), odel=self.mainframe.get_del(), oname=self.mainframe.get_name()),
                                   bttn_event_3             =lambda: self.clear_all(),
                                   bttn_event_4             =lambda: self.CopyString(_string=self.text_box_frame._get_txtb1()),
                                   bttn_event_5             =lambda: self.CopyString(_string=self.text_box_frame._get_txtb2()),
                                #    ch_bx_1_text             ="Use def vel",
                                #    ch_bx_2_text             ="Use def del",
                                #    ch_bx_1_command          ="",#lambda: self.update_window(),
                                #    ch_bx_2_command          ="",#lambda: self.update_window(),
                                   label_1_text             ="Velocity:", 
                                   label_2_text             ="Delay:",
                                   label_3_text             ="BackUp FileName:",
                                   )
        self.text_box_frame = ScrollableFrame(master            =self,
                                              width             =540,
                                              height            =400,
                                              all_tbxxs_width   =250,
                                              all_tbxxs_height  =390,

                                              label_1_text      ="Coordinates:",
                                              label_2_text      ="Sketch:", 
                                              )
        
        self._DEBUG_TEXTBOX = ctk.CTkTextbox(master         =self,
                                            width           =700,
                                            fg_color        ="transparent",        
                                            # font            =self.SourceCodeProBold_S14,
                                            )

        self.mainframe.grid(row=0, column=0, padx=0, pady=5)
        self.text_box_frame.grid(row=0, column=1, padx=0, pady=5)
        self._DEBUG_TEXTBOX.grid(row=1, column=0, padx=0, pady=0, columnspan=2, sticky="EW")
        
        self.mainframe.configure(fg_color="transparent")

        self._DEBUG_TEXTBOX.configure(state="normal")
        self._DEBUG_TEXTBOX.delete("0.0", tk.END)
        self._DEBUG_TEXTBOX.insert("0.0", "Program started.")
        self._DEBUG_TEXTBOX.configure(state="disabled")

        # self.mainframe.check_bx_1.select(0)
        # self.mainframe.check_bx_2.select(0)

        # self.mainframe.check_bx_1.configure(state=tk.DISABLED) 
        # self.mainframe.check_bx_2.configure(state=tk.DISABLED)

        self.mainframe.insert_from_conf()
        
        self.toplevel_window=None
        self.open_toplevel()

    """
    def update_window(self):
        if self.mainframe.check_bx_1.get()==1:  
            self.mainframe.entry_2.configure(state="normal")
            #self.update()
        else:
            self.mainframe.entry_2.configure(state="readonly")
            #self.update() 

        if self.mainframe.check_bx_2.get()==1:  
            self.mainframe.entry_1.configure(state="normal")
            #self.update()
        else:
            self.mainframe.entry_1.configure(state="readonly")
            #self.update()
    """

    def convert_func(self, ovelocity, delay, code, filename):
        
        self.ovelocity  =ovelocity
        self.delay      =delay
        self.code       =code
        self.filename   =filename

        print(self.code)

        f=open("data.txt", "w+")
        f.write(self.code)
        f.close

        fBackUp_filename = f"output/{self.filename}.txt"
        fBackUp=open(fBackUp_filename, "w+")

        m_cords=[]
        with open("data.txt", "w+") as f: 
            for elem in f:
                matches=re.findall(r"\d+", elem)
                id=0
                for x in matches:
                    id+=1
                    match=(f"Dynamixel_Gear({id}, {self.ovelocity}, {x}, {self.delay});")
                    m_cords.append(match)
                    fBackUp.write(f"{match}\n")
                    print(match)
                #m_cords.append(f"\ndelay({delay});")
                m_cords.append(f"\n")
                fBackUp.write(f"\n")
                print(m_cords)

        fBackUp.close

        Zcount=0.0
        for Oelem in m_cords:
            Zcount+=1
            self.text_box_frame.insert_txtb2(LC=Zcount, data=Oelem)
            print(f"{Oelem}")

        self._DEBUG_TEXTBOX.configure(state="normal")
        self._DEBUG_TEXTBOX.delete("0.0", tk.END)
        self._DEBUG_TEXTBOX.insert("0.0", f"Function \"convert_func\" executed successfully. Output saved in -> {fBackUp_filename}")
        self._DEBUG_TEXTBOX.configure(state="disabled")

    def dump_args(self, ovel, odel, oname):

        self.ovel   =ovel
        self.odel   =odel
        self.oname  =oname

        with open("conf.json", "w") as fh:
            conf={
            "Vel": self.ovel, 
            "Del": self.odel, 
            "Name": self.oname,
            }
            json.dump(conf , fh)

        self._DEBUG_TEXTBOX.configure(state="normal")
        self._DEBUG_TEXTBOX.delete("0.0", tk.END)
        self._DEBUG_TEXTBOX.insert("0.0", f"Function \"dump_args\" executed successfully. Args -> {self.ovel} {self.odel} {self.oname}")
        self._DEBUG_TEXTBOX.configure(state="disabled")

    def CopyString(self, _string):

        self._string = _string
        pyperclip.copy(_string)

        self._DEBUG_TEXTBOX.configure(state="normal")
        self._DEBUG_TEXTBOX.delete("0.0", tk.END)
        self._DEBUG_TEXTBOX.insert("0.0", f"Function \"CopyString\" executed successfully.")
        self._DEBUG_TEXTBOX.configure(state="disabled")

    def open_toplevel(self):

        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window=TopLevelWindow(master=self)
        else:
            self.toplevel_window.focus()

    def clear_all(self):

        self.text_box_frame.del_all()

        self._DEBUG_TEXTBOX.configure(state="normal")
        self._DEBUG_TEXTBOX.delete("0.0", tk.END)
        self._DEBUG_TEXTBOX.insert("0.0", f"Function \"clear_all\" executed successfully.")
        self._DEBUG_TEXTBOX.configure(state="disabled")


app = Root()
app.mainloop()    