'''
This config.py is used when you want to have
dynamic design --> in your project

easy change


'''
'''
class settings:

    def __init__(self):
'''

'''
APP_CURRENCY = "IRR" #To , ...
CURRENCY_SYMBOL = "ریال"
DECIMAL_PLACES = 2


SHOW_BALANCE_FEE = 500  # Fee for checking balance
TRANSFER_FEE = 1000  # Fee for transfers


PIN_LENGTH = 4  # PIN code length
'''



class settings:
    def __init__(self):
        self.APP_CURRENCY = "To" #To , ...
        self.CURRENCY_SYMBOL = "تومان"
        self.DECIMAL_PLACES = 2
        self.SHOW_BALANCE_FEE = 500  # Fee for checking balance
        self.DEPOSIT_FEE = 1000  # Fee for deposits
        self.WITHDRAW_FEE = 1000  # Fee for withdraws
        self.TRANSFER_FEE = 1000  # Fee for transfers

        self.MINIMUM_REMAINING_BALANCE = 100000  # Maximum remaining balance


        self.PIN_LENGTH = 4  # PIN code length

        self.MAX_DEPOSIT_AMOUNT = 10000000  # Max deposit amount
        self.MAX_WITHDRAW_AMOUNT = 200000

        self.MAX_DEPOSIT_AMOUNT_AP = 3000000
        self.MAX_DEPOSIT_AMOUNT_BANK = 10000000
        self.MAX_TRANSFER_AMOUNT = 10000000




