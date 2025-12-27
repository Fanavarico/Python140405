from database import get_session
from utils import hash_password, check_password
from models import Customer, Account , Transaction
from config import settings
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info('AdminPanel class initialized')



'''
logger ->bejaye print() real


logger.info('Info creating customer: {e}') --> print()
logger.error('Error creating customer: {e}') --> error mode
logger.warning('Warning creating customer: {e}') --> warning mode

logger.critical('Critical creating customer: {e}') -->  kheyli jedie ghazi
logger.debug('Debug creating customer: {e}') --> debug mode

'''

class AdminPanel:
    '''
    description of the classs
    this class is used to create a new customer and account
    and show the balance of the account
    and deposit and withdraw and transfer and show the transaction
    and delete the account
    and show the all customers
    and show the all accounts
    and show the all transactions


    Persian Description:
    این کلاس برای ایجاد یک مشتری و حساب و نمایش موجودی حساب و واریز و برداشت و انتقال و نمایش تراکنش ها و حذف حساب و نمایش همه مشتریان و حساب ها و تراکنش ها است.

    '''


    def __init__(self):
        '''
        It doesn't take any parameters
        It creates a session to the database
        '''
        self.session=get_session()
        #fee for shwoing balance
        self.settings = settings()



    def create_customer(self,name:str,email:str,age:int,phone:str,address:str):

        '''
        description : it get information of costumer and create customer class
        Arguments:
            name : string
            email : string
            age : int
            phone : string
            address : string
        
        Returns:
            customer : Customer object

        Raises:
            Exception : if the customer is not created


        '''

        try:
            #create class (it is only class not saving)
            customer= Customer(name=name,email=email,age=age,phone=phone,address=address)
            #after creation of class, we add it to the database
            self.session.add(customer)
            self.session.commit()
            #Don't forget to comment
            #print(f'customer {name} created successfully')
            logger.info(f'customer {name} created successfully')

            return customer

        except Exception as e:
            self.session.rollback()
            logger.error(f'Error creating customer: {e}')

            return None


    def create_account(self,customer_id:int,account_type:str,balance:float, pin:str):
        '''
        description : it get information of account and create account class for that costumer
        Arguments:
            customer_id : int
            account_type : str
            balance : float
            pin : str
        
        Returns:
            account : Account object
        Raises:
            Exception : if the account is not created

        '''
        try:
            customer=self.session.get(Customer,customer_id)
        except Exception as e:
            self.session.rollback()
            logger.error(f'Error creating account: {e}')
            return None

        if not customer:
            logger.error(f'Customer with id {customer_id} not found')
            return None

        try:
            hashed_pin=hash_password(pin)

            if not hashed_pin:
                logger.error(f'Error hashing pin: {pin}')
                return None

            if hashed_pin is None:
                logger.error(f'Error hashing pin: {pin}')
                return None

            

            account= Account(balance=balance,type=account_type,pin=hashed_pin,customer_id=customer_id)
            logger.info(f'Account created successfully')
            self.session.add(account)
            self.session.commit()
            return account

        except Exception as e:
            self.session.rollback()
            logger.error(f'Error creating account: {e}')
            return None



    def show_balance(self,account_id:int):
        '''
        description : it shows the balance of the account
        Arguments:
            account_id : int
        Returns:
            balance : float
        Raises:
            Exception : if the account is not found
        '''
        try:
            account=self.session.get(Account,account_id)
            if not account:
                logger.error(f'Account with id {account_id} not found')
                return None

            balance= account.balance

            if balance < self.settings.SHOW_BALANCE_FEE:
                logger.error(f'Balance is less than show balance fee')
                return None
            

            if balance - self.settings.SHOW_BALANCE_FEE < self.settings.MINIMUM_REMAINING_BALANCE:
                logger.error(f'Balance is less than minimum remaining balance')
                return None

            balance = balance - self.settings.SHOW_BALANCE_FEE
            transaction= Transaction(amount=self.settings.SHOW_BALANCE_FEE,type='show_balance_fee',account_id=account_id)
            self.session.add(transaction)
            
            #save balance to database
            account.balance = balance
            self.session.commit()


            logger.info(f'Balance of account {account_id} is {balance}')
            return balance

        except Exception as e:
            self.session.rollback()
            logger.error(f'Error showing balance: {e}')
            return None

    

    
    def deposit(self,account_id:int,amount:float):
        '''
        description : it deposits the amount to the account
        Arguments:
            account_id : int
            amount : float
        Returns:
            account : Account object
        Raises:
            Exception : if the account is not found 
        '''
        try:
            account=self.session.get(Account,account_id)
            if not account:
                logger.error(f'Account with id {account_id} not found')
                return None

            if amount > self.settings.MAX_DEPOSIT_AMOUNT:
                logger.error(f'Amount is greater than max deposit amount')
                return None

            
            if account.balance < self.settings.DEPOSIT_FEE:
                logger.error(f'Balance is less than deposit fee')
                return None

            if account.balance + amount - self.settings.DEPOSIT_FEE < self.settings.MINIMUM_REMAINING_BALANCE:
                logger.error(f'Balance is less than minimum remaining balance')
                return None

            account.balance=account.balance + amount - self.settings.DEPOSIT_FEE
            transaction= Transaction(amount=amount,type='deposit',account_id=account_id)
            self.session.add(transaction)

            transaction= Transaction(amount=self.settings.DEPOSIT_FEE,type='deposit_fee',account_id=account_id)
            self.session.add(transaction)
            
            self.session.commit()
            return account


        except Exception as e:
            self.session.rollback()
            logger.error(f'Error depositing: {e}')
            return None




    def advanced_deposit(self,account_id:int,amount:float ,software : str):
        '''
        description : it deposits the amount to the account
        Arguments:
            account_id : int
            amount : float
        Returns:
            account : Account object
        Raises:
            Exception : if the account is not found 
        '''
        try:
            account=self.session.get(Account,account_id)
            if not account:
                logger.error(f'Account with id {account_id} not found')
                return None

            if amount > self.settings.MAX_DEPOSIT_AMOUNT:
                logger.error(f'Amount is greater than max deposit amount')
                return None



            if software == 'bank':
                if amount > self.settings.MAX_DEPOSIT_AMOUNT_BANK:
                    logger.error(f'Amount is greater than max deposit amount for bank')
                    return None

            elif software == 'آپ':
                if amount > self.settings.MAX_DEPOSIT_AMOUNT_AP:
                    logger.error(f'Amount is greater than max deposit amount for AP')
                    return None

            

            account.balance=account.balance + amount
            self.session.commit()
            logger.info(f'Deposit of {amount} to account {account_id} successful')
            return account
        except Exception as e:
            self.session.rollback()
            logger.error(f'Error depositing: {e}')
            return None



    def withdraw(self,account_id,amount):
        '''
        description : it withdraws the amount from the account
        Arguments:
            account_id : int
            amount : float
        Returns:
            account : Account object
        Raises:
            Exception : if the account is not found 
        '''

        try:
            account=self.session.get(Account,account_id)

            if not account:
                logger.error(f'Account with id {account_id} not found')
                return None


            

            if amount > self.settings.MAX_WITHDRAW_AMOUNT:
                logger.error(f'Amount is greater than max withdraw amount')
                return None

            if account.balance < self.settings.WITHDRAW_FEE + amount:
                logger.error(f'Balance is less than withdraw fee + amount')
                return None

            if account.balance - amount - self.settings.WITHDRAW_FEE < self.settings.MINIMUM_REMAINING_BALANCE:
                logger.error(f'Balance is less than minimum remaining balance')
                return None


            account.balance=account.balance - amount - self.settings.WITHDRAW_FEE

            transaction= Transaction(amount=amount,type='withdraw',account_id=account_id)
            self.session.add(transaction)

            transaction= Transaction(amount=self.settings.WITHDRAW_FEE,type='withdraw_fee',account_id=account_id)
            self.session.add(transaction)

            self.session.commit()
            logger.info(f'Withdrawal of {amount} from account {account_id} successful')

            return account

        except Exception as e:
            self.session.rollback()
            logger.error(f'Error withdrawing: {e}')
            return None

        


    def transfer(self,account_id , from_account_id,to_account_id,amount):

        if account_id != from_account_id:
            logger.error(f'Account id is not equal to from account id')
            return None

        

        from_account=self.session.get(Account,account_id)
        to_account=self.session.get(Account,to_account_id)

        if not from_account:
            logger.error(f'From account with id {from_account_id} not found')
            return None

        if not to_account:
            logger.error(f'To account with id {to_account_id} not found')
            return None

        if amount > from_account.balance:
            logger.error(f'Amount is greater than from account balance')
            return None

        if amount > self.settings.MAX_TRANSFER_AMOUNT:
            logger.error(f'Amount is greater than max transfer amount')
            return None

        if from_account.balance - amount - self.settings.TRANSFER_FEE < self.settings.MINIMUM_REMAINING_BALANCE:
            logger.error(f'Balance is less than minimum remaining balance')
            return None

        #It is done for initial transfer
        from_account.balance = from_account.balance - amount - self.settings.TRANSFER_FEE

        transaction= Transaction(amount=amount,type='transfer_from',account_id=account_id)
        self.session.add(transaction)

        transaction= Transaction(amount=self.settings.TRANSFER_FEE,type='transfer_fee',account_id=account_id)
        self.session.add(transaction)


        
        #It is done for destijnation
        to_account.balance = to_account.balance + amount
        transaction= Transaction(amount=amount,type='transfer_to',account_id=to_account_id)
        self.session.add(transaction)


        #save to database
        self.session.commit()
        logger.info(f'Transfer of {amount} from account {from_account_id} to account {to_account_id} successful')
        return from_account




    def show_transaction(self,account_id):
        '''
        tarakonesh haro neshoon bede

        ** Models.py --> Class transaction --> id ,amount, type=deposit ya witdhraw, tim,
        dposit() withdraw() --> ye radis tooye clas transaction

        - dddd
        + ddssd
        - dsdssd
        + ddsds
        - dsds
        + ddsds
        - dsds
        + ddsds
        - dsds
        + ddsds
        - dsds
        

        '''
        try:
            transactions=self.session.query(Transaction).filter(Transaction.account_id==account_id).order_by(Transaction.timestamp.desc()).all()
            
            if not transactions:
                logger.error(f'No transactions found for account {account_id}')
                return None
            return transactions


        except Exception as e:
            self.session.rollback()
            logger.error(f'Error showing transactions: {e}')
            return None


    


#class GUI --> 
#gui --> fucntion --> adminpanel.create() adminpanel.() felan felan()\

#a=AdminPanel()
#a.create_customer('ali','email' , 'password', 'sen','shomare carte melisho bege')

'''
Ma dar class omadim va in project to ba Tkinter (python) front zadim
backend python zadim



front --> javascript , html , css --> frontend

backend -->Python



motasel konid?


1--> Django --> in ejaze ro mide behet
2- Fast API --> in ejaze ro mide behet


-->django -->kh kh kh asoon hast , kh feature dar ekhtiaret mizre -->tooye ersale data front o backend konde
handle mikone




fast api --> sorate ersale data khodast --> AI based web app --> fast api --> kh kh sakht --> yeki dota ketab (System design)
fekre hameja bashi , security , authentication , authorization , etc.




#---------------------------------

Future Project --> 

Project 1-->
1- Ba AI (canva , lovely ,....) ---> prompt khob (az gpt ) -->yek tarsimiu
--> html, csv , javascript --> misaze [frontend]

2- in class k sakhtimo admin_gui --> tabe hasho too formate Django misazish





Project 2 -->
hamoone chan class jadid ezafe kon 
ATM --> safe web khode ina bian user pasword , khdoeshon transfer o ....
karmande bank

-->hamine deposit() withdraw() .... --> hardafe password check mishe barashon
class mojaza




project 3 -->
class --> two class (inherent) --> class dollar , clas --> Crypto 
exchange kone 

Djnago




Project 4 -->


1- Ba AI (canva , lovely ,....) ---> prompt khob (az gpt ) -->yek tarsimiu

2- In class ---> miay ba Fast Api anjam midi 




done done README.md --> githubt gharar bede---> 5 ta projecte ghoool
resume khafan mishe



collaborator --> APMaii  [github] 

dar heynehs komaket konm






'''
