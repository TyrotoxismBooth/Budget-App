import tkinter as tk
    
class Budget:
    #Main window of the program is defined in __init__
    #Pop-up windows are defined in functions after __init__
    #and logic functions are defined after all the windows are defined.
    def __init__(self):
        main_window = tk.Tk()
        main_window.geometry('300x400')
        main_window.title('Budget App')

        # Frame to display summary totals
        summary_frame = tk.Frame(main_window)
        summary_frame.pack(side='top')
        summary_lbl = tk.Label(summary_frame, text='Budget Summary')
        summary_lbl.grid(row=0, sticky='EW')
        #Labels for totals
        total_lbl = tk.Label(summary_frame, text='Account Total:')
        income_lbl = tk.Label(summary_frame, text='Income:')
        expense_lbl = tk.Label(summary_frame, text='Total Expenses:')
        # IntVars and labels to keep the totals updated
        self.total_var = tk.IntVar(value=0)
        self.income_var = tk.IntVar(value=0)
        self.expense_var = tk.IntVar(value=0)
        total = tk.Label(summary_frame, textvariable=self.total_var)
        income = tk.Label(summary_frame, textvariable=self.income_var)
        expense = tk.Label(summary_frame, textvariable=self.expense_var)
        #Pack summary_frame widgets into a grid
        income_lbl.grid(row=1, column=0)
        income.grid(row=1, column=1)
        expense_lbl.grid(row=2, column=0)
        expense.grid(row=2, column=1)
        total_lbl.grid(row=3, column=0)
        total.grid(row=3, column=1)

        #Frame for entry buttons
        button_frame = tk.Frame(main_window)
        button_frame.pack(side='top', pady='15')

        #Button widgets to open entry dialogue boxes
        income_button = tk.Button(button_frame, text='Add  Income',
                                        command=self.addIncomeWindow)
        expense_button = tk.Button(button_frame, text='Add Expense',
                                        command=self.addExpenseWindow)
        income_button.pack(side='left')
        expense_button.pack(side='left')

        #Frame for the expense totals
        expense_frame = tk.Frame(main_window)
        expense_frame.pack(side='top', pady='15')

        self.expense_title = tk.Label(expense_frame, text='Expenses by Category')
        self.expense_title.grid(row=0, sticky='EW')

        #Initiate Intvars to store expense values
        self.rent_var = tk.IntVar(value=0)
        self.util_var = tk.IntVar(value=0)
        self.grocery_var = tk.IntVar(value=0)
        self.ent_var = tk.IntVar(value=0)
        self.car_var = tk.IntVar(value=0)
        self.gas_var = tk.IntVar(value=0)

        #Widgets to display expense totals
        rent = tk.Label(expense_frame, text='Rent/Mortgage:')
        rent.grid(row=1, column=0)
        rent_lbl = tk.Label(expense_frame, textvariable=self.rent_var)
        rent_lbl.grid(row=1, column=1)
        util = tk.Label(expense_frame, text='Utilities:')
        util.grid(row=2, column=0)
        util_lbl = tk.Label(expense_frame, textvariable=self.util_var)
        util_lbl.grid(row=2, column=1)
        grocery = tk.Label(expense_frame, text='Groceries:')
        grocery.grid(row=3, column=0)
        grocery_lbl = tk.Label(expense_frame, textvariable=self.grocery_var)
        grocery_lbl.grid(row=3, column=1)
        ent = tk.Label(expense_frame, text='Entertainment:')
        ent.grid(row=4, column=0)
        ent_lbl = tk.Label(expense_frame, textvariable=self.ent_var)
        ent_lbl.grid(row=4, column=1)
        car = tk.Label(expense_frame, text='Car Payment:')
        car.grid(row=5, column=0)
        car_lbl = tk.Label(expense_frame, textvariable=self.car_var)
        car_lbl.grid(row=5, column=1)
        gas = tk.Label(expense_frame, text='Gas:')
        gas.grid(row=6, column=0)
        gas_lbl = tk.Label(expense_frame, textvariable=self.gas_var)
        gas_lbl.grid(row=6, column=1)
		
		#Frame for buttons on main_window
		save_frame = tk.Frame(main_window)
		save_frame.pack(side='top')
		
		#Save, load, and quit button widgets
		save_btn = tk.Button(save_frame, text='Save')
		load_btn = tk.Button(save_frame, textl='Load')
		quit_btn = tk.Button(save_frame,text='Quit', command=main_window.destroy)

        tk.mainloop()

    def addIncomeWindow(self):
        income_window = tk.Toplevel()
        income_window.title('Add Income')
        income_window.geometry('300x150')
        #Title frame
        title_frame = tk.Frame(income_window)
        title_frame.pack(side='top')
        title_lbl = tk.Label(title_frame, text='Please enter your income:')
        title_lbl.pack()

        #Radio button frame for pay frequency
        radio_frame = tk.Frame(income_window)
        radio_frame.pack(side='top')
        self.pay_freq = tk.IntVar(value=0)
        message_lbl = tk.Label(radio_frame, text='How often do you get paid?')
        
        weekly_button = tk.Radiobutton(radio_frame, text='Weekly',
                                            variable=self.pay_freq, value=4)
        bi_button = tk.Radiobutton(radio_frame, text='Bi-Weekly',
                                        variable=self.pay_freq, value=2)
        monthly_button = tk.Radiobutton(radio_frame, text='Monthly',
                                            variable=self.pay_freq, value=1)
        message_lbl.pack(side='top')
        weekly_button.pack(side='left')
        bi_button.pack(side='left')
        monthly_button.pack(side='left')

        #Frame for amount entry
        entry_frame = tk.Frame(income_window)
        entry_frame.pack(side='top')
        entry_lbl = tk.Label(entry_frame, text='How much?')
        self.entry = tk.Entry(entry_frame, width='75')
        entry_lbl.pack(side='left')
        self.entry.pack(side='left')

        #Frame for action buttons
        self.action_frame = tk.Frame(income_window)
        self.action_frame.pack(side='top')
        self.add_button = tk.Button(self.action_frame, command=income_window.destroy)
        self.add_button = tk.Button(self.action_frame, text='Add', command=self.addIncomeBtn)
        self.quit_button = tk.Button(self.action_frame, text='Quit', command=income_window.destroy)
        self.add_button.pack(side='left')
        self.quit_button.pack(side='left')

        #A label to prompt user to add another entry or quit
        self.inagain_var = tk.StringVar(value='')
        inagain_lbl = tk.Label(income_window, textvariable=self.inagain_var)
        inagain_lbl.pack(side='top')

    def addExpenseWindow(self):
        expense_window = tk.Toplevel()
        expense_window.title('Add Expense')
        expense_window.geometry('300x200')

        #Frame to hold options for selecting an expense category
        selection_frame = tk.Frame(expense_window)
        selection_frame.pack(side='top')

        #Initialize a StringVar to hold the radio button selection
        self.expense_choice = tk.StringVar(value='')

        #Create widgets for selecting an expense category
        #title widget
        select_lbl = tk.Label(selection_frame, text='Select a category:')
        select_lbl.grid(row=0, sticky='W')

        #Radiobuttons for options
        rent_btn = tk.Radiobutton(selection_frame, text='Rent/Mortgage',
                                        variable=self.expense_choice, value='rent')
        util_btn = tk.Radiobutton(selection_frame, text='Utilities',
                                        variable=self.expense_choice, value='util')
        grocery_btn = tk.Radiobutton(selection_frame, text='Groceries',
                                        variable=self.expense_choice, value='grocery')
        ent_btn = tk.Radiobutton(selection_frame, text='Entertainment',
                                        variable=self.expense_choice, value='ent')
        car_btn = tk.Radiobutton(selection_frame, text='Car',
                                        variable=self.expense_choice, value='car')
        gas_btn = tk.Radiobutton(selection_frame, text='Gas',
                                        variable=self.expense_choice, value='gas')

        #Pack the radiobuttons into the grid
        rent_btn.grid(row=1, column=0)
        util_btn.grid(row=1, column=1)
        grocery_btn.grid(row=1, column=2)
        ent_btn.grid(row=2, column=0)
        car_btn.grid(row=2, column=1)
        gas_btn.grid(row=2,column=2)

        #Frame for the amount entry
        expense_frame = tk.Frame(expense_window)
        expense_frame.pack(side='top')

        #Entry frame widgets
        message = tk.Label(expense_frame, text='Please enter the amount:')
        message.grid(row=0, sticky='W')
        entry_lbl1 = tk.Label(expense_frame, text='Amount:')
        entry_lbl1.grid(row=1, column=0, sticky='W')
        self.entry1 = tk.Entry(expense_frame, width='12')
        self.entry1.grid(row=1, column=1)

        #Frame for buttons
        self.btn_frame = tk.Frame(expense_window)
        self.btn_frame.pack(side='top')

        #Create the button widgets
        add_expense = tk.Button(self.btn_frame, text='Add', command=self.addExpenseBtn)
        add_expense.pack(side='left')
        quit_btn = tk.Button(self.btn_frame, text='Quit', command=expense_window.destroy)
        quit_btn.pack(side='left')

        #A label to prompt user to add another entry or quit
        self.exagain_var = tk.StringVar(value='')
        exagain_lbl = tk.Label(expense_window, textvariable=self.exagain_var)
        exagain_lbl.pack(side='top')
    
    def addIncomeBtn(self):
        amount = int(self.pay_freq.get()) * int(self.entry.get())
        income = self.income_var.get()
        self.income_var.set(income + amount)
        self.calc_total()
        self.inagain_var.set('Your income had been entered.\n Enter another income or press quit.')


    def addExpenseBtn(self):
        amount = int(self.entry1.get())
        self.category = self.expense_choice.get()

        if self.category == 'rent':
            rent = int(self.rent_var.get())
            self.rent_var.set(rent + amount)

        elif self.category == 'util':
            util = int(self.util_var.get())
            self.util_var.set(util + amount)

        elif self.category == 'grocery':
            grocery = int(self.grocery_var.get())
            self.grocery_var.set(grocery + amount)

        elif self.category == 'ent':
            ent = int(self.ent_var.get())
            self.ent_var.set(ent + amount)

        elif self.category == 'car':
            car = int(self.car_var.get())
            self.car_var.set(car + amount)

        elif self.category == 'gas':
            gas = int(self.gas_var.get())
            self.gas_var.set(gas + amount)

        else:
            self.exagain_var.set('Please select an expense category!')
            return

        self.exagain_var.set('Your expense has been entered.\n Enter another expense or press quit')

        self.total_expenses()
        self.calc_total()

    def total_expenses(self):
        rent = self.rent_var.get()
        util = self.util_var.get()
        grocery = self.grocery_var.get()
        ent = self.ent_var.get()
        car = self.car_var.get()
        gas = self.gas_var.get()
        self.expense_var.set(rent + util + grocery + ent + car + gas)

    def calc_total(self):
        income = self.income_var.get()
        expense = self.expense_var.get()
        self.total_var.set(income - expense)
     
app = Budget()
