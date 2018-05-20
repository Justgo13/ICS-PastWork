#Edited by Ali on 28/12/2016
#Edited by Ali on 29/12/2016
#Edited by Ali on 30/12/2016
#Edited by Jason on 02/01/2017
#Edited by Ali on 04/01/2017
#Edited by Jason on 05/01/2017
#Edited by Jason on 10/01/2017
#Edited by Ali on 12/01/2017
#Edited by Ali on 16/01/2017

'''This program allows the user to cash out different foods/drinks
and then displays the breakdown of costs that they must pay
    -Includes: Cost of Food, Cost of Drinks, Service Charge, Paid Tax,
    Sub Total, and Total Cost'''

from tkinter import*
import random
import time;
import datetime

root= Tk()
root.geometry("1350x750+0+0") #Creates main screen with these dimensions
root.title("LDHSS Cafeteria Service") #Title at top of the screen
root.configure(background='#0072BB') #Background colour to blue

#Frames - Main Left and Right
Tops = Frame(root, width=1350, height=100, bd=14,bg='#FFD034', relief="raise") #Yellow Border
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8,bg='#FFD034', relief="raise") #Yellow Border
f1.pack(side=LEFT)

f2 = Frame(root, width=440, height=650, bd=8,bg='#FFD034', relief="raise") #Yellow Border
f2.pack(side=RIGHT)

#Creates Bottom Two Frames
f1a = Frame(f1, width=900, height=330, bd=6,bg='#FFD034', relief="raise") #Yellow Border 
f1a.pack(side=TOP)

f2a = Frame(f1, width=900, height=320, bd=6,bg='#FF9900', relief="raise") #Orange Border 
f2a.pack(side=BOTTOM)

#Frame - Adding Detailed Boarders - changed bottom right
ft2 = Frame(f2, width=440, height=450, bd=12, bg='#FFD034', relief="raise")#Yellow Border 
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440, height=250, bd=16, bg='#FF9900', relief="raise")#Orange Border 
fb2.pack(side=BOTTOM)

#Frame - Top 2
f1aa = Frame(f1a, width=400, height=330, bd=16, bg='#FFD034', relief="raise") #Yellow Border 
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=330, bd=16,bg='#FFD034', relief="raise") #Yellow Border
f1ab.pack(side=RIGHT)

#Frame - Bottom 2
f2aa = Frame(f2a, width=450, height=330, bd=14, bg='#FF9900', relief="raise") #Orange Border
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=330, bd=14, bg='#FF9900', relief="raise") #Orange Border
f2ab.pack(side=RIGHT)

#Establishing Colours 
Tops.configure(background='#FF4C3B') #Red Border - Top
f1.configure(background='#FF4C3B') #Red Border - Left
f2.configure(background='#FF4C3B') #Red Boarder - Right 

#Main Title - Yellow Background 
labelInfo = Label(Tops, font=('Times',70,'bold'), text = "     LDHSS Cafeteria Service      ", bd=10, bg = '#FFD034')
labelInfo.grid(row=0, column = 0)
#======================================================================Method============================================================================================
def CostofItems():
    Item1=float(E_Fanta.get())
    Item2=float(E_Coke.get())
    Item3=float(E_Sprite.get())
    Item4=float(E_Pepsi.get())
    Item5=float(E_Gingerale.get())
    Item6=float(E_Mountain_Dew.get())
    Item7=float(E_Orange_Crush.get())
    Item8=float(E_Seven_Up.get())
    
    Item9=float(E_Poutine.get())
    Item10=float(E_Cheese_Pizza.get())
    Item11=float(E_Chicken_Sandwhich.get())
    Item12=float(E_Chocolate_Cookie.get())
    Item13=float(E_Chips.get())
    Item14=float(E_Fries.get())
    Item15=float(E_Blueberry_Muffin.get())
    Item16=float(E_Pepperoni_Pizza.get())

    PriceofSoftDrinks = (Item1*1.25)+(Item2*1.25)+(Item3*1.25)+(Item4*1.25)+(Item5*1.25)+(Item6*1.25)+(Item7*1.25)+(Item8*1.25)
    PriceofFood = (Item9*3.25)+(Item10*2.0)+(Item11*3.00)+(Item12*1.00)+(Item13*1.5)+(Item14*3.00)+(Item15*1.50)+(Item16*2.5)

    # Outputting the different end prices
    SoftDrinksPrice = '$', str('%.2f'%(PriceofSoftDrinks))
    FoodPrice = '$', str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofSoftDrinks.set(SoftDrinksPrice)
    Service = '$', str('%.2f'%(0.75))
    ServiceCharge.set(Service)

    SubTotalofItems = '$', str('%.2f'%(PriceofSoftDrinks + PriceofFood + 0.75))
    SubTotal.set(SubTotalofItems)

    #Final Tax Calulations + Final Cost 
    Tax='$',str('%.2f'%((PriceofSoftDrinks + PriceofFood + 0.75)*0.13))
    PaidTax.set(Tax)
    Total_Tax=((PriceofSoftDrinks + PriceofFood + 0.75)*0.13)
    Total='$',str('%.2f'%(PriceofSoftDrinks + PriceofFood + 0.75 + Total_Tax))
    TotalCost.set(Total)
    
#===================================Receipt====================================================================
def Receipt():
    txtReceipt.delete('1.0',END)
    x=random.randint(1001, 5001) #A number ranges from 1001 to 5001
    randomRef = str(x)
    Receipt_Ref.set('BILL #: '+randomRef)

    #create items as text onto the receipt along with quantity bought
    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get()+'\t\t'+DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t\t'+ "Quantity of Items \n\n")
    txtReceipt.insert(END, 'Fanta: \t\t\t\t\t'+ E_Fanta.get()+"\n")
    txtReceipt.insert(END, 'Coke: \t\t\t\t\t'+ E_Coke.get()+"\n")
    txtReceipt.insert(END, 'Sprite: \t\t\t\t\t'+ E_Sprite.get()+"\n")
    txtReceipt.insert(END, 'Pepsi: \t\t\t\t\t'+ E_Pepsi.get()+"\n") 
    txtReceipt.insert(END, 'Gingerale: \t\t\t\t\t'+ E_Gingerale.get()+"\n")
    txtReceipt.insert(END, 'Mountain Dew: \t\t\t\t\t'+ E_Mountain_Dew.get()+"\n")
    txtReceipt.insert(END, 'Orange Crush: \t\t\t\t\t'+ E_Orange_Crush.get()+"\n")
    txtReceipt.insert(END, 'Seven Up: \t\t\t\t\t'+ E_Seven_Up.get()+"\n")
    txtReceipt.insert(END, 'Poutine: \t\t\t\t\t'+ E_Poutine.get()+"\n")
    txtReceipt.insert(END, 'Cheese Pizza: \t\t\t\t\t'+ E_Cheese_Pizza.get()+"\n")
    txtReceipt.insert(END, 'Chicken Sandwhich: \t\t\t\t\t'+ E_Chicken_Sandwhich.get()+"\n")
    txtReceipt.insert(END, 'Chocolate Cookie: \t\t\t\t\t'+ E_Chocolate_Cookie.get()+"\n")
    txtReceipt.insert(END, 'Chips: \t\t\t\t\t'+ E_Chips.get()+"\n") 
    txtReceipt.insert(END, 'Fries: \t\t\t\t\t'+ E_Fries.get()+"\n")   
    txtReceipt.insert(END, 'Blueberry Muffin: \t\t\t\t\t'+ E_Blueberry_Muffin.get()+"\n")
    txtReceipt.insert(END, 'Pepperoni Pizza: \t\t\t\t\t'+ E_Pepperoni_Pizza.get()+"\n\n")
    txtReceipt.insert(END, 'Cost of Drinks:\t\t'+ CostofSoftDrinks.get()+ '\t Tax Paid:\t\t' + PaidTax.get() +"\n")
    txtReceipt.insert(END, 'Cost of Food:\t\t'+ CostofFood.get()+ '\tSubTotal:\t\t' + SubTotal.get() +"\n")
    txtReceipt.insert(END, 'Service Charge:\t\t'+ ServiceCharge.get()+ ' \tTotalCost:\t\t' + TotalCost.get() +"\n")
    
def Exit():
    Exit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if Exit > 0:
        root.destroy() #This stops the program (mainloop)
        return
    
def Reset():    # Resets the program and wipes the screen, hides receipt
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofSoftDrinks.set("")
    CostofFood.set("")
    ServiceCharge.set("")
    SubTotal.set("")
    txtReceipt.delete("1.0",END)

    E_Fanta.set("0")
    E_Coke.set("0")
    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_Gingerale.set("0")
    E_Mountain_Dew.set("0")
    E_Orange_Crush.set("0")
    E_Seven_Up.set("0")

    E_Poutine.set("0")
    E_Cheese_Pizza.set("0")
    E_Chicken_Sandwhich.set("0")
    E_Chocolate_Cookie.set("0")
    E_Chips.set("0")
    E_Fries.set("0")
    E_Blueberry_Muffin.set("0")
    E_Pepperoni_Pizza.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    
    #For entry widget
    txtFanta.configure(state=DISABLED)
    txtCoke.configure(state=DISABLED)
    txtSprite.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtGingerale.configure(state=DISABLED)
    txtMountain_Dew.configure(state=DISABLED)
    txtOrange_Crush.configure(state=DISABLED)
    txtSeven_Up.configure(state=DISABLED)
    txtPoutine.configure(state=DISABLED)
    txtCheese_Pizza.configure(state=DISABLED)
    txtChicken_Sandwhich.configure(state=DISABLED)
    txtChocolate_Cookie.configure(state=DISABLED)
    txtChips.configure(state=DISABLED)
    txtFries.configure(state=DISABLED)
    txtBlueberry_Muffin.configure(state=DISABLED)
    txtPepperoni_Pizza.configure(state=DISABLED)
#===================================CheckButton Calculator============================================================================
def chkbutton_value():
    if (var1.get()==1):
        txtFanta.configure(state=NORMAL) # clicking the check button next to item allows for user to select quantity further on
    elif var1.get()==0:
        txtFanta.configure(state=DISABLED) # not clicking the check button blacks the quantity box out 
        E_Fanta.set("0")                # set quantity box back to 0
    if (var2.get()==1):
        txtCoke.configure(state=NORMAL)
    elif var2.get()==0:
        txtCoke.configure(state=DISABLED)
        E_Coke.set("0")
    if (var3.get()==1):
        txtSprite.configure(state=NORMAL)
    elif var3.get()==0:
        txtSprite.configure(state=DISABLED)
        E_Sprite.set("0")
    if (var4.get()==1):
        txtPepsi.configure(state=NORMAL)
    elif var4.get()==0:
        txtPepsi.configure(state=DISABLED)
        E_Pepsi.set("0")
    if (var5.get()==1):
        txtGingerale.configure(state=NORMAL)
    elif var5.get()==0:
        txtGingerale.configure(state=DISABLED)
        E_Gingerale.set("0")
    if (var6.get()==1):
        txtMountain_Dew.configure(state=NORMAL)
    elif var6.get()==0:
        txtMountain_Dew.configure(state=DISABLED)
        E_Mountain_Dew.set("0")
    if (var7.get()==1):
        txtOrange_Crush.configure(state=NORMAL)
    elif var7.get()==0:
        txtOrange_Crush.configure(state=DISABLED)
        E_Orange_Crush.set("0")
    if (var8.get()==1):
        txtSeven_Up.configure(state=NORMAL)
    elif var8.get()==0:
        txtSeven_Up.configure(state=DISABLED)
        E_Seven_Up.set("0")
    if (var9.get()==1):
        txtPoutine.configure(state=NORMAL)
    elif var9.get()==0:
        txtPoutine.configure(state=DISABLED)
        E_Poutine.set("0")
    if (var10.get()==1):
        txtCheese_Pizza.configure(state=NORMAL)
    elif var10.get()==0:
        txtCheese_Pizza.configure(state=DISABLED)
        E_Cheese_Pizza.set("0")
    if (var11.get()==1):
        txtChicken_Sandwhich.configure(state=NORMAL)
    elif var11.get()==0:
        txtChicken_Sandwhich.configure(state=DISABLED)
        E_Chicken_Sandwhich.set("0")
    if (var12.get()==1):
        txtChocolate_Cookie.configure(state=NORMAL)
    elif var12.get()==0:
        txtChocolate_Cookie.configure(state=DISABLED)
        E_Chocolate_Cookie.set("0")
    if (var13.get()==1):
        txtChips.configure(state=NORMAL)
    elif var13.get()==0:
        txtChips.configure(state=DISABLED)
        E_Chips.set("0")
    if (var14.get()==1):
        txtFries.configure(state=NORMAL)
    elif var14.get()==0:
        txtFries.configure(state=DISABLED)
        E_Fries.set("0")
    if (var15.get()==1):
        txtBlueberry_Muffin.configure(state=NORMAL)
    elif var15.get()==0:
        txtBlueberry_Muffin.configure(state=DISABLED)
        E_Blueberry_Muffin.set("0")
    if (var16.get()==1):
        txtPepperoni_Pizza.configure(state=NORMAL)
    elif var16.get()==0:
        txtPepperoni_Pizza.configure(state=DISABLED)
        E_Pepperoni_Pizza.set("0")
        
#=============================================Variables================================================================================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofSoftDrinks = StringVar()
ServiceCharge = StringVar()

#Drinks Variable
E_Fanta = StringVar()
E_Coke = StringVar()
E_Sprite = StringVar()
E_Pepsi = StringVar()
E_Gingerale = StringVar()
E_Mountain_Dew = StringVar()
E_Orange_Crush = StringVar()
E_Seven_Up = StringVar()

#Food Variable
E_Poutine = StringVar()
E_Cheese_Pizza = StringVar()
E_Chicken_Sandwhich = StringVar()
E_Chocolate_Cookie = StringVar()
E_Chips = StringVar()
E_Fries = StringVar()
E_Blueberry_Muffin = StringVar()
E_Pepperoni_Pizza = StringVar()

#set all variables to 0
E_Fanta.set("0")
E_Coke.set("0")
E_Sprite.set("0")
E_Pepsi.set("0")
E_Gingerale.set("0")
E_Mountain_Dew.set("0")
E_Orange_Crush.set("0")
E_Seven_Up.set("0")

E_Poutine.set("0")
E_Cheese_Pizza.set("0")
E_Chicken_Sandwhich.set("0")
E_Chocolate_Cookie.set("0")
E_Chips.set("0")
E_Fries.set("0")
E_Blueberry_Muffin.set("0")
E_Pepperoni_Pizza.set("0")

DateofOrder.set(time.strftime('%d/%m/%y')) #creates current date onto receipt

#=================================================Soft Drinks (allow user to choose quantity after clicking on checkbox)============================================
Fanta = Checkbutton(f1aa, text="Fanta \t\t\t", variable = var1, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=0, sticky=W)
Coke = Checkbutton(f1aa, text="Coke \t\t", variable = var2, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=1, sticky=W)
Sprite = Checkbutton(f1aa, text="Sprite \t\t", variable = var3, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=2, sticky=W)
Pepsi = Checkbutton(f1aa, text="Pepsi \t\t", variable = var4, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=3, sticky=W)
Gingerale = Checkbutton(f1aa, text="Gingerale \t\t", variable = var5, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=4, sticky=W)
Mountain_Dew = Checkbutton(f1aa, text="Mountain Dew \t\t", variable = var6, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=5, sticky=W)
Orange_Crush = Checkbutton(f1aa, text="Orange Crush \t\t", variable = var7, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=6, sticky=W)
Seven_Up = Checkbutton(f1aa, text="7 Up \t\t", variable = var8, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=7, sticky=W)
#=================================================Foods (allow user to choose quantity after clicking on checkbox)=================================================
Poutine = Checkbutton(f1ab, text="Poutine \t\t\t\t", variable = var9, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=0, sticky=W)
Cheese_Pizza = Checkbutton(f1ab, text="Cheese Pizza \t", variable = var10, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=1, sticky=W)
Chicken_Sandwhich = Checkbutton(f1ab, text="Chicken Sandwhich \t", variable = var11, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=2, sticky=W)
Chocolate_Cookie = Checkbutton(f1ab, text="Chocolate Cookie \t", variable = var12, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=3, sticky=W)
Chips = Checkbutton(f1ab, text="Chips  \t", variable = var13, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=4, sticky=W)
Fries = Checkbutton(f1ab, text="Fries \t", variable = var14, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=5, sticky=W)
Blueberry_Muffin = Checkbutton(f1ab, text="Blueberry Muffin \t", variable = var15, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=6, sticky=W)
Pepperoni_Pizza = Checkbutton(f1ab, text="Pepperoni Pizza \t", variable = var16, onvalue = 1, offvalue=0, 
                            font=('arial',18,'bold'),bg='#FFD034', command=chkbutton_value).grid(row=7, sticky=W)
#=================================================================Enter Widget for Soft Drinks=====================================================================
# User can enter the quantity they want here
txtFanta = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left', textvariable=E_Fanta, state=DISABLED) 
txtFanta.grid(row=0,column=1)
txtCoke = Entry(f1aa,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Coke, state=DISABLED)
txtCoke.grid(row=1,column=1)
txtSprite = Entry(f1aa,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Sprite, state=DISABLED)
txtSprite.grid(row=2,column=1)
txtPepsi = Entry(f1aa,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Pepsi, state=DISABLED)
txtPepsi.grid(row=3,column=1)
txtGingerale = Entry(f1aa,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Gingerale, state=DISABLED)
txtGingerale.grid(row=4,column=1)
txtMountain_Dew = Entry(f1aa,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Mountain_Dew, state=DISABLED)
txtMountain_Dew.grid(row=5,column=1)
txtOrange_Crush  = Entry(f1aa,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Orange_Crush, state=DISABLED)
txtOrange_Crush.grid(row=6,column=1)
txtSeven_Up = Entry(f1aa,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Seven_Up, state=DISABLED)
txtSeven_Up.grid(row=7,column=1)
#==============================================================Enter Widget for Food================================================================================
# User can enter the quantity they want here
txtPoutine = Entry(f1ab,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Poutine, state=DISABLED)
txtPoutine.grid(row=0,column=1)
txtCheese_Pizza = Entry(f1ab,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cheese_Pizza, state=DISABLED)
txtCheese_Pizza.grid(row=1,column=1)
txtChicken_Sandwhich = Entry(f1ab,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Chicken_Sandwhich, state=DISABLED)
txtChicken_Sandwhich.grid(row=2,column=1)
txtChocolate_Cookie = Entry(f1ab,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Chocolate_Cookie, state=DISABLED)
txtChocolate_Cookie.grid(row=3,column=1)
txtChips = Entry(f1ab,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Chips, state=DISABLED)
txtChips.grid(row=4,column=1)
txtFries = Entry(f1ab,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Fries, state=DISABLED)
txtFries.grid(row=5,column=1)
txtBlueberry_Muffin = Entry(f1ab,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Blueberry_Muffin, state=DISABLED)
txtBlueberry_Muffin.grid(row=6,column=1)
txtPepperoni_Pizza = Entry(f1ab,font=('arial', 16,'bold'),bd=8,width=6,justify='left',textvariable=E_Pepperoni_Pizza, state=DISABLED)
txtPepperoni_Pizza.grid(row=7,column=1)
#====================================================================Receipt===================================================================================
labelReceipt = Label(ft2,font=('arial',12,'bold'), text="Receipt:", bd=2, bg = '#FFD034', anchor='w')
labelReceipt.grid(row=0,column=0, sticky=W)
txtReceipt = Text(ft2,width=59,height=22,bg='white',bd=8, font=('arial',11,'bold'))
txtReceipt.grid(row=1,column=0)
#=========================================================Cost of Items Information===============================================================================
labelCostofSoftDrinks=Label(f2aa,font=('arial',14,'bold'), text='Cost of Soft Drinks', bd=8,bg='#FF9900',anchor='w')
labelCostofSoftDrinks.grid(row=2,column=0,sticky=W)
txtCostofSoftDrinks=Entry(f2aa,font=('arial',14,'bold'),bd=8,
                          insertwidth=2, justify='left',textvariable=CostofSoftDrinks)
txtCostofSoftDrinks.grid(row=2,column=1)

labelCostofFood=Label(f2aa,font=('arial',14,'bold'), text='Cost of Food', bg='#FF9900', bd=8, anchor='w')
labelCostofFood.grid(row=3,column=0,sticky=W)
txtCostofFood=Entry(f2aa,font=('arial',14,'bold'),bd=8,
                    insertwidth=2, justify='left', textvariable=CostofFood)
txtCostofFood.grid(row=3,column=1)

labelServiceCharge=Label(f2aa,font=('arial',14,'bold'), text='Service Charge',bg='#FF9900', bd=8, anchor='w')
labelServiceCharge.grid(row=4,column=0,sticky=W)
txtServiceCharge=Entry(f2aa,font=('arial',14,'bold'),bd=8,
                       insertwidth=2, justify='left', textvariable = ServiceCharge)
txtServiceCharge.grid(row=4,column=1)

#==========================================================Payment Information=========================================================================================
labelPaidTax=Label(f2ab,font=('arial',14,'bold'), text='Paid Tax',bg='#FF9900', bd=8)
labelPaidTax.grid(row=2,column=0,sticky=W)
txtPaidTax=Entry(f2ab,font=('arial',14,'bold'),bd=8,
                 insertwidth=2, justify='left', textvariable=PaidTax)
txtPaidTax.grid(row=2,column=1)

labelSubTotal=Label(f2ab,font=('arial',14,'bold'), text='Sub Total',bg='#FF9900', bd=8)
labelSubTotal.grid(row=3,column=0,sticky=W)
txtSubTotal=Entry(f2ab,font=('arial',14,'bold'),bd=8,
                  insertwidth=2, justify='left', textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1)

labelTotalCost=Label(f2ab,font=('arial',14,'bold'), text='Total Cost', bg='#FF9900',bd=8)
labelTotalCost.grid(row=4,column=0,sticky=W)
txtTotalCost=Entry(f2ab,font=('arial',14,'bold'),bd=8,
                   insertwidth=2, justify='left', textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1)

#=============================================================Button====================================================================================================
btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg='black',bg = '#FF9900',font=('arial',16,'bold'),width=5,
                text='Total', command=CostofItems).grid(row=0,column=0)

btnReceipt=Button(fb2,padx=16,pady=1,bd=4,bg ='#FF9900', fg='black',font=('arial',16,'bold'),width=5,
                text='Receipt', command=Receipt).grid(row=0,column=1)

btnReset=Button(fb2,padx=16,pady=1,bd=4,fg='black',bg = '#FF9900', font=('arial',16,'bold'),width=5,
                text='Reset',command=Reset).grid(row=0,column=2)

btnExit=Button(fb2,padx=16,pady=1,bd=4,fg='black',bg = '#FF9900',font=('arial',16,'bold'),width=5,
                text='Exit',command=Exit).grid(row=0,column=3)

root.mainloop()
