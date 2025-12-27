import tkinter as tk 
from tkinter import messagebox, ttk
from core import AdminPanel
import os

#ADMIN_PASSWORD = os.getenv('admin_login_password')
#ADMIN_USERNAME = os.getenv('admin_login_username')

ADMIN_PASSWORD= '1234'
ADMIN_USERNAME= 'admin'




class AdminGUI:
    def __init__(self, bank_system):
        self.bank = bank_system
        
        # Create root window with professional styling
        self.root = tk.Tk()
        self.root.title('Plutus Bank Management System')
        self.root.geometry('1000x700')
        self.root.resizable(False, False)
        
        # Professional color scheme - Swiss Bank inspired
        self.colors = {
            'primary': '#1a237e',      # Deep navy blue
            'secondary': '#283593',    # Medium navy
            'accent': '#ffc107',       # Gold accent
            'accent_dark': '#ff8f00',  # Dark gold
            'background': '#f5f5f5',    # Light gray background
            'surface': '#ffffff',      # White surface
            'text_primary': '#212121', # Dark gray text
            'text_secondary': '#757575',# Medium gray text
            'success': '#4caf50',      # Green
            'error': '#f44336',        # Red
            'border': '#e0e0e0'        # Light border
        }
        
        # Configure root window background
        self.root.configure(bg=self.colors['background'])
        
        # Configure ttk style for professional look
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure button styles
        self.style.configure('Primary.TButton',
                            background=self.colors['primary'],
                            foreground='white',
                            borderwidth=0,
                            focuscolor='none',
                            font=('Helvetica', 11, 'bold'),
                            padding=15)

                            
        self.style.map('Primary.TButton',
                      background=[('active', self.colors['secondary']),
                                 ('pressed', '#1a237e')])
        
        self.style.configure('Accent.TButton',
                            background=self.colors['accent'],
                            foreground=self.colors['text_primary'],
                            borderwidth=0,
                            focuscolor='none',
                            font=('Helvetica', 11, 'bold'),
                            padding=15)
        self.style.map('Accent.TButton',
                      background=[('active', self.colors['accent_dark']),
                                 ('pressed', '#ff8f00')])
        
        self.style.configure('Danger.TButton',
                            background=self.colors['error'],
                            foreground='white',
                            borderwidth=0,
                            focuscolor='none',
                            font=('Helvetica', 11, 'bold'),
                            padding=15)
        self.style.map('Danger.TButton',
                      background=[('active', '#d32f2f'),
                                 ('pressed', '#b71c1c')])
        
        # Configure entry style
        self.style.configure('Professional.TEntry',
                            fieldbackground=self.colors['surface'],
                            borderwidth=2,
                            relief='solid',
                            padding=10,
                            font=('Helvetica', 11))
        
        self.show_login_window()
        self.root.mainloop()

    def clear(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login_window(self):
        """Display professional login window"""
        self.clear()
        
        # Main container frame with padding
        main_frame = tk.Frame(self.root, bg=self.colors['background'])
        main_frame.pack(fill='both', expand=True, padx=50, pady=50)
        
        # Logo/Title section
        title_frame = tk.Frame(main_frame, bg=self.colors['background'])
        title_frame.pack(pady=(0, 40))
        
        # Bank logo/title with elegant styling
        logo_label = tk.Label(
            title_frame,
            text="🏦",
            font=('Helvetica', 48),
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        logo_label.pack()
        
        title_label = tk.Label(
            title_frame,
            text="Plutus Bank",
            font=('Helvetica', 32, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        title_label.pack(pady=(10, 5))
        
        subtitle_label = tk.Label(
            title_frame,
            text="Administrative Portal",
            font=('Helvetica', 14),
            bg=self.colors['background'],
            fg=self.colors['text_secondary']
        )
        subtitle_label.pack()
        
        # Login card - white surface with shadow effect
        login_card = tk.Frame(
            main_frame,
            bg=self.colors['surface'],
            relief='flat',
            bd=0
        )
        login_card.pack(fill='both', expand=True, padx=100)
        
        # Add subtle border effect
        border_frame = tk.Frame(
            login_card,
            bg=self.colors['border'],
            height=2
        )
        border_frame.pack(fill='x', side='top')
        
        # Login form container
        form_frame = tk.Frame(login_card, bg=self.colors['surface'])
        form_frame.pack(fill='both', expand=True, padx=60, pady=50)
        
        # Login title
        login_title = tk.Label(
            form_frame,
            text="Secure Login",
            font=('Helvetica', 24, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary']
        )
        login_title.pack(pady=(0, 30))
        
        # Username section
        username_frame = tk.Frame(form_frame, bg=self.colors['surface'])
        username_frame.pack(fill='x', pady=(0, 20))
        
        username_label = tk.Label(
            username_frame,
            text="Username",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        username_label.pack(fill='x', pady=(0, 8))
        
        self.username_entry = ttk.Entry(
            username_frame,
            style='Professional.TEntry',
            font=('Helvetica', 11),
            width=30
        )
        self.username_entry.pack(fill='x', ipady=12)
        self.username_entry.focus()
        
        # Password section
        password_frame = tk.Frame(form_frame, bg=self.colors['surface'])
        password_frame.pack(fill='x', pady=(0, 30))
        
        password_label = tk.Label(
            password_frame,
            text="Password",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        password_label.pack(fill='x', pady=(0, 8))
        
        self.password_entry = ttk.Entry(
            password_frame,
            style='Professional.TEntry',
            font=('Helvetica', 11),
            show="•",
            width=30
        )
        self.password_entry.pack(fill='x', ipady=12)
        
        # Bind Enter key to login
        self.password_entry.bind('<Return>', lambda e: self.login())
        self.username_entry.bind('<Return>', lambda e: self.password_entry.focus())
        
        # Login button
        login_button = tk.Button(
            form_frame,
            text="Sign In",
            bg=self.colors['primary'],
            fg='white',
            font=('Helvetica', 11, 'bold'),
            command=self.login,
            width=30,
            height=2,
            relief='flat',
            cursor='hand2',
            activebackground=self.colors['secondary'],
            activeforeground='white',
            bd=0,
            padx=20,
            pady=10
        )
        login_button.pack(pady=(0, 15))
        
        # Security notice
        security_label = tk.Label(
            form_frame,
            text="🔒 Your session is encrypted and secure",
            font=('Helvetica', 9),
            bg=self.colors['surface'],
            fg=self.colors['text_secondary']
        )
        security_label.pack()

    def login(self):
        """Handle login authentication"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        # For demo, hardcoded admin credentials
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            self.show_dashboard()
        else:
            messagebox.showerror("Authentication Failed", 
                               "Invalid credentials. Please try again.")

    def show_dashboard(self):
        """Display professional admin dashboard"""
        self.clear()
        
        # Header bar
        header_frame = tk.Frame(
            self.root,
            bg=self.colors['primary'],
            height=80
        )
        header_frame.pack(fill='x', side='top')
        header_frame.pack_propagate(False)
        
        # Header content
        header_content = tk.Frame(header_frame, bg=self.colors['primary'])
        header_content.pack(fill='both', expand=True, padx=40, pady=15)
        
        # Bank logo and title in header
        header_left = tk.Frame(header_content, bg=self.colors['primary'])
        header_left.pack(side='left')
        
        bank_title = tk.Label(
            header_left,
            text="🏦 Plutus Bank | Admin Dashboard",
            font=('Helvetica', 18, 'bold'),
            bg=self.colors['primary'],
            fg='white'
        )
        bank_title.pack(side='left', padx=(0, 20))
        
        # Header right (logout button)
        header_right = tk.Frame(header_content, bg=self.colors['primary'])
        header_right.pack(side='right')
        
        logout_button = tk.Button(
            header_right,
            text="Logout",
            bg=self.colors['error'],
            fg='white',
            font=('Helvetica', 11, 'bold'),
            command=self.show_login_window,
            width=12,
            height=1,
            relief='flat',
            cursor='hand2',
            activebackground='#d32f2f',
            activeforeground='white',
            bd=0,
            padx=10,
            pady=5
        )
        logout_button.pack(side='right')
        
        # Main content area
        main_container = tk.Frame(self.root, bg=self.colors['background'])
        main_container.pack(fill='both', expand=True, padx=40, pady=30)
        
        # Welcome section
        welcome_frame = tk.Frame(main_container, bg=self.colors['background'])
        welcome_frame.pack(fill='x', pady=(0, 30))
        
        welcome_label = tk.Label(
            welcome_frame,
            text="Welcome, Administrator",
            font=('Helvetica', 28, 'bold'),
            bg=self.colors['background'],
            fg=self.colors['text_primary']
        )
        welcome_label.pack(anchor='w')
        
        subtitle_label = tk.Label(
            welcome_frame,
            text="Manage your banking operations",
            font=('Helvetica', 14),
            bg=self.colors['background'],
            fg=self.colors['text_secondary']
        )
        subtitle_label.pack(anchor='w', pady=(5, 0))
        
        # Dashboard cards container
        cards_frame = tk.Frame(main_container, bg=self.colors['background'])
        cards_frame.pack(fill='both', expand=True)
        
        # Create button cards in a grid layout
        buttons_data = [
            ("Create Customer", "👤", self.gui_create_customer, self.colors['primary'], 'white'),
            ("Create Account", "💳", self.gui_create_account, self.colors['primary'], 'white'),
            ("View Accounts", "📊", self.gui_view_accounts, self.colors['accent'], self.colors['text_primary']),
            ("View Transactions", "📋", self.gui_view_transactions, self.colors['accent'], self.colors['text_primary']),
            ("Delete Account", "🗑️", self.gui_delete_account, self.colors['error'], 'white'),
        ]
        
        # Grid layout for buttons (2 columns)
        row = 0
        col = 0
        for text, icon, command, bg_color, fg_color in buttons_data:
            # Card frame
            card = tk.Frame(
                cards_frame,
                bg=self.colors['surface'],
                relief='flat',
                bd=0
            )
            card.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
            
            # Configure grid weights for responsive layout
            cards_frame.grid_columnconfigure(col, weight=1)
            cards_frame.grid_rowconfigure(row, weight=1)
            
            # Card content
            card_content = tk.Frame(card, bg=self.colors['surface'])
            card_content.pack(fill='both', expand=True, padx=30, pady=30)
            
            # Icon
            icon_label = tk.Label(
                card_content,
                text=icon,
                font=('Helvetica', 36),
                bg=self.colors['surface'],
                fg=self.colors['primary']
            )
            icon_label.pack(pady=(0, 15))
            
            # Button - using regular tk.Button for better visibility
            button = tk.Button(
                card_content,
                text=text,
                bg=bg_color,
                fg=fg_color,
                font=('Helvetica', 11, 'bold'),
                command=command,
                width=20,
                height=30,
                relief='flat',
                cursor='hand2',
                activebackground=bg_color,
                activeforeground=fg_color,
                bd=0,
                padx=10,
                pady=8
            )
            button.pack()
            
            # Update grid position
            col += 1
            if col >= 2:
                col = 0
                row += 1
        
        # Footer
        footer_frame = tk.Frame(
            self.root,
            bg=self.colors['background'],
            height=40
        )
        footer_frame.pack(fill='x', side='bottom')
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="© 2024 Plutus Bank. All rights reserved. | Secure Banking System",
            font=('Helvetica', 9),
            bg=self.colors['background'],
            fg=self.colors['text_secondary']
        )
        footer_label.pack(pady=10)

    #-----OPTIONALLLLL-----
    def gui_create_customer(self):
        """Create customer form GUI"""
        self.clear()
        
        # Header bar
        header_frame = tk.Frame(
            self.root,
            bg=self.colors['primary'],
            height=80
        )
        header_frame.pack(fill='x', side='top')
        header_frame.pack_propagate(False)
        
        # Header content
        header_content = tk.Frame(header_frame, bg=self.colors['primary'])
        header_content.pack(fill='both', expand=True, padx=40, pady=15)
        
        # Back button
        back_button = tk.Button(
            header_content,
            text="← Back",
            bg=self.colors['secondary'],
            fg='white',
            font=('Helvetica', 11, 'bold'),
            command=self.show_dashboard,
            relief='flat',
            cursor='hand2',
            activebackground=self.colors['primary'],
            activeforeground='white',
            bd=0,
            padx=15,
            pady=5
        )
        back_button.pack(side='left')
        
        # Title in header
        title_label = tk.Label(
            header_content,
            text="Create New Customer",
            font=('Helvetica', 18, 'bold'),
            bg=self.colors['primary'],
            fg='white'
        )
        title_label.pack(side='left', padx=20, expand=True)
        
        # Submit button in header
        submit_button = tk.Button(
            header_content,
            text="Create Customer",
            bg=self.colors['accent'],
            fg=self.colors['text_primary'],
            font=('Helvetica', 11, 'bold'),
            command=self.submit_create_customer,
            relief='flat',
            cursor='hand2',
            activebackground=self.colors['accent_dark'],
            activeforeground=self.colors['text_primary'],
            bd=0,
            padx=20,
            pady=8
        )
        submit_button.pack(side='right')
        
        # Main content area with scrollable frame
        main_container = tk.Frame(self.root, bg=self.colors['background'])
        main_container.pack(fill='both', expand=True, padx=50, pady=20)
        
        # Form card - simple and visible
        form_card = tk.Frame(
            main_container,
            bg=self.colors['surface'],
            relief='flat',
            bd=0
        )
        form_card.pack(fill='both', expand=True)
        
        # Form title
        form_title = tk.Label(
            form_card,
            text="Customer Information",
            font=('Helvetica', 24, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary']
        )
        form_title.pack(pady=(20, 30))
        
        # Form fields container - simple pack, no expand
        form_fields = tk.Frame(form_card, bg=self.colors['surface'])
        form_fields.pack(padx=80, pady=10)
        
        # Name field
        name_frame = tk.Frame(form_fields, bg=self.colors['surface'])
        name_frame.pack(fill='x', pady=(0, 20))
        
        name_label = tk.Label(
            name_frame,
            text="Full Name *",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        name_label.pack(fill='x', pady=(0, 8))
        
        self.name_entry = tk.Entry(
            name_frame,
            font=('Helvetica', 11),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightbackground=self.colors['border'],
            highlightcolor=self.colors['primary'],
            insertbackground=self.colors['text_primary']
        )
        self.name_entry.pack(fill='x', ipady=10)
        
        # Email field
        email_frame = tk.Frame(form_fields, bg=self.colors['surface'])
        email_frame.pack(fill='x', pady=(0, 20))
        
        email_label = tk.Label(
            email_frame,
            text="Email Address *",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        email_label.pack(fill='x', pady=(0, 8))
        
        self.email_entry = tk.Entry(
            email_frame,
            font=('Helvetica', 11),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightbackground=self.colors['border'],
            highlightcolor=self.colors['primary'],
            insertbackground=self.colors['text_primary']
        )
        self.email_entry.pack(fill='x', ipady=10)
        
        # Age field
        age_frame = tk.Frame(form_fields, bg=self.colors['surface'])
        age_frame.pack(fill='x', pady=(0, 20))
        
        age_label = tk.Label(
            age_frame,
            text="Age *",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        age_label.pack(fill='x', pady=(0, 8))
        
        self.age_entry = tk.Entry(
            age_frame,
            font=('Helvetica', 11),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightbackground=self.colors['border'],
            highlightcolor=self.colors['primary'],
            insertbackground=self.colors['text_primary']
        )
        self.age_entry.pack(fill='x', ipady=10)
        
        # Phone field
        phone_frame = tk.Frame(form_fields, bg=self.colors['surface'])
        phone_frame.pack(fill='x', pady=(0, 20))
        
        phone_label = tk.Label(
            phone_frame,
            text="Phone Number *",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        phone_label.pack(fill='x', pady=(0, 8))
        
        self.phone_entry = tk.Entry(
            phone_frame,
            font=('Helvetica', 11),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightbackground=self.colors['border'],
            highlightcolor=self.colors['primary'],
            insertbackground=self.colors['text_primary']
        )
        self.phone_entry.pack(fill='x', ipady=10)
        
        # Address field
        address_frame = tk.Frame(form_fields, bg=self.colors['surface'])
        address_frame.pack(fill='x', pady=(0, 30))
        
        address_label = tk.Label(
            address_frame,
            text="Address *",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        address_label.pack(fill='x', pady=(0, 8))
        
        self.address_entry = tk.Entry(
            address_frame,
            font=('Helvetica', 11),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightbackground=self.colors['border'],
            highlightcolor=self.colors['primary'],
            insertbackground=self.colors['text_primary']
        )
        self.address_entry.pack(fill='x', ipady=10)
        
        # Focus on first field
        self.name_entry.focus()
        
        # Bind Enter key to submit
        self.address_entry.bind('<Return>', lambda e: self.submit_create_customer())
    
    
    
    
    def submit_create_customer(self):

        #tamame vorodi haro migirim az front

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        age_str = self.age_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()

        #validation
        if not name:
            messagebox.showerror("Validation Error", "Name is required!")
            self.name_entry.focus()
            return
        
        if not email:
            messagebox.showerror("Validation Error", "Email is required!")
            self.email_entry.focus()
            return
        
        if not age_str:
            messagebox.showerror("Validation Error", "Age is required!")
            self.age_entry.focus()
            return
        
        if not phone:
            messagebox.showerror("Validation Error", "Phone is required!")
            self.phone_entry.focus()
            return
        
        if not address:
            messagebox.showerror("Validation Error", "Address is required!")
            self.address_entry.focus()
            return
        
        #call create_customer
        try:

            result = self.bank.create_customer(name, email, age_str, phone, address)
            print('===============================================')
            print('result of create_customer')
            print(result)

            if result is None:
                messagebox.showerror("Error", "Failed to create customer. Please try again.")
                return 

            else :
                messagebox.showinfo("Success", "Customer created successfully!")
                self.name_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.age_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
                self.address_entry.delete(0, tk.END)
                self.name_entry.focus()
                return

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return



    def gui_create_account(self):
        """Create account form GUI"""
        self.clear()
        
        # Header bar
        header_frame = tk.Frame(
            self.root,
            bg=self.colors['primary'],
            height=80
        )
        header_frame.pack(fill='x', side='top')
        header_frame.pack_propagate(False)
        
        # Header content
        header_content = tk.Frame(header_frame, bg=self.colors['primary'])
        header_content.pack(fill='both', expand=True, padx=40, pady=15)
        
        # Back button
        back_button = tk.Button(
            header_content,
            text="← Back",
            bg=self.colors['secondary'],
            fg='white',
            font=('Helvetica', 11, 'bold'),
            command=self.show_dashboard,
            relief='flat',
            cursor='hand2',
            activebackground=self.colors['primary'],
            activeforeground='white',
            bd=0,
            padx=15,
            pady=5
        )
        back_button.pack(side='left')
        
        # Title in header
        title_label = tk.Label(
            header_content,
            text="Create New Account",
            font=('Helvetica', 18, 'bold'),
            bg=self.colors['primary'],
            fg='white'
        )
        title_label.pack(side='left', padx=20, expand=True)
        
        # Submit button in header
        submit_button = tk.Button(
            header_content,
            text="Create Account",
            bg=self.colors['accent'],
            fg=self.colors['text_primary'],
            font=('Helvetica', 11, 'bold'),
            command=self.submit_create_account,
            relief='flat',
            cursor='hand2',
            activebackground=self.colors['accent_dark'],
            activeforeground=self.colors['text_primary'],
            bd=0,
            padx=20,
            pady=8
        )
        submit_button.pack(side='right')
        
        # Main content area
        main_container = tk.Frame(self.root, bg=self.colors['background'])
        main_container.pack(fill='both', expand=True, padx=50, pady=20)
        
        # Form card
        form_card = tk.Frame(
            main_container,
            bg=self.colors['surface'],
            relief='flat',
            bd=0
        )
        form_card.pack(fill='both', expand=True)
        
        # Form title
        form_title = tk.Label(
            form_card,
            text="Account Information",
            font=('Helvetica', 24, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary']
        )
        form_title.pack(pady=(20, 30))
        
        # Form fields container
        form_fields = tk.Frame(form_card, bg=self.colors['surface'])
        form_fields.pack(padx=80, pady=10)
        
        # Customer ID field
        customer_id_frame = tk.Frame(form_fields, bg=self.colors['surface'])
        customer_id_frame.pack(fill='x', pady=(0, 20))
        
        customer_id_label = tk.Label(
            customer_id_frame,
            text="Customer ID *",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        customer_id_label.pack(fill='x', pady=(0, 8))
        
        self.customer_id_entry = tk.Entry(
            customer_id_frame,
            font=('Helvetica', 11),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightbackground=self.colors['border'],
            highlightcolor=self.colors['primary'],
            insertbackground=self.colors['text_primary']
        )
        self.customer_id_entry.pack(fill='x', ipady=10)
        
        # Account Type field
        account_type_frame = tk.Frame(form_fields, bg=self.colors['surface'])
        account_type_frame.pack(fill='x', pady=(0, 20))
        
        account_type_label = tk.Label(
            account_type_frame,
            text="Account Type *",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        account_type_label.pack(fill='x', pady=(0, 8))
        
        # Account type dropdown using Combobox
        self.account_type_var = tk.StringVar(value="standard")
        account_type_combobox = ttk.Combobox(
            account_type_frame,
            textvariable=self.account_type_var,
            values=["standard", "foreign", "crypto"],
            state="readonly",
            font=('Helvetica', 11)
        )
        account_type_combobox.pack(fill='x', ipady=10)
        
        # Balance field
        balance_frame = tk.Frame(form_fields, bg=self.colors['surface'])
        balance_frame.pack(fill='x', pady=(0, 20))
        
        balance_label = tk.Label(
            balance_frame,
            text="Initial Balance *",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        balance_label.pack(fill='x', pady=(0, 8))
        
        self.balance_entry = tk.Entry(
            balance_frame,
            font=('Helvetica', 11),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightbackground=self.colors['border'],
            highlightcolor=self.colors['primary'],
            insertbackground=self.colors['text_primary']
        )
        self.balance_entry.pack(fill='x', ipady=10)
        
        # PIN field
        pin_frame = tk.Frame(form_fields, bg=self.colors['surface'])
        pin_frame.pack(fill='x', pady=(0, 30))
        
        pin_label = tk.Label(
            pin_frame,
            text="PIN Code *",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        pin_label.pack(fill='x', pady=(0, 8))
        
        # PIN entry with show/hide button
        pin_input_frame = tk.Frame(pin_frame, bg=self.colors['surface'])
        pin_input_frame.pack(fill='x')
        
        self.pin_entry = tk.Entry(
            pin_input_frame,
            font=('Helvetica', 11),
            bg=self.colors['surface'],
            fg=self.colors['text_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightbackground=self.colors['border'],
            highlightcolor=self.colors['primary'],
            insertbackground=self.colors['text_primary'],
            show="•"
        )
        self.pin_entry.pack(side='left', fill='x', expand=True, ipady=10)
        
        # Show/Hide PIN button
        self.pin_visible = False
        pin_toggle_button = tk.Button(
            pin_input_frame,
            text="👁️",
            bg=self.colors['background'],
            fg=self.colors['text_primary'],
            font=('Helvetica', 10),
            command=self.toggle_pin_visibility,
            relief='flat',
            cursor='hand2',
            bd=0,
            padx=10,
            pady=5
        )
        pin_toggle_button.pack(side='right', padx=(5, 0))
        
        # Focus on first field
        self.customer_id_entry.focus()
        
        # Bind Enter key to submit
        self.pin_entry.bind('<Return>', lambda e: self.submit_create_account())

    def toggle_pin_visibility(self):
        """Toggle PIN visibility"""
        if self.pin_visible:
            self.pin_entry.config(show="•")
            self.pin_visible = False
        else:
            self.pin_entry.config(show="")
            self.pin_visible = True

    def submit_create_account(self):
        """Submit the create account form - placeholder"""
        pass
    
    def gui_view_accounts(self):
        """Placeholder for view accounts GUI"""
        print("=" * 50)
        print("Button clicked: View Accounts")
        print("Function: gui_view_accounts()")
        print("=" * 50)
        messagebox.showinfo("Info", "View Accounts functionality")
    
    def gui_view_transactions(self):
        """Placeholder for view transactions GUI"""
        print("=" * 50)
        print("Button clicked: View Transactions")
        print("Function: gui_view_transactions()")
        print("=" * 50)
        messagebox.showinfo("Info", "View Transactions functionality")
    
    def gui_delete_account(self):
        """Placeholder for delete account GUI"""
        print("=" * 50)
        print("Button clicked: Delete Account")
        print("Function: gui_delete_account()")
        print("=" * 50)
        messagebox.showinfo("Info", "Delete Account functionality")




if __name__ == "__main__":
    
    from core import AdminPanel
    # Create the bank system instance
    bank_system = AdminPanel()
    
    # Create and run the GUI
    app = AdminGUI(bank_system)
