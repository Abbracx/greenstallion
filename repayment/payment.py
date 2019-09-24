from datetime import date, timedelta


# method for loan calculator
def get_halve_income(income=0):
    if income > 0:
        return income / 2
    return income

#loan interest
def get_loan_interest(rate):
    return rate * 0.01

# halve loan interest depending on disbursable date
def get_loan_halve_interest(rate):
    return get_loan_interest(rate) / 2

# amount for loan interest
def get_loan_interest_amount(loan_amount, rate):
    return get_loan_interest(rate) * loan_amount

# amount for halve loan interest
def get_loan_halve_interest_amount(loan_amount, rate):
    return get_loan_halve_interest(rate) * loan_amount

#Eligible loan
def loan_eligible(income , cat):
    if cat is 'copper':
        return get_halve_income(income) * categories['copper']['max_tenure']
    elif cat is 'biz':
        return get_halve_income(income) * categories['biz']['max_tenure']
    elif cat is 'salary_earner':
        return get_halve_income(income) * categories['salary_earner']['max_tenure']
    return None

def processing_fee(loan_amount, fee = 0):
    if fee > 0:
        return loan_amount * (fee * 0.01)

def loan_Disbursement(income,loan_amount,rate,cat):
    
    result = {}
    total_payable = loan_amount + get_loan_interest_amount(loan_amount,rate)
    total_disbursable = loan_amount - processing_fee(loan_amount,3)
    disbursable_date = date.today() + timedelta(days =10)
    
    if cat in categories.keys():
        if disbursable_date.day in range(1,16):
            
            result['eligible'] =  loan_eligible(income, cat)
            result['total_payable'] = total_payable
            result['repayment'] = date(year=disbursable_date.year,month=disbursable_date.month,day=28)
            result['total_disbursable'] = total_disbursable 
            return result
        else:
            
            result['eligible'] =  loan_eligible(income, cat)
            result['total_payable'] = total_payable
            result['repayment'] = date(year=disbursable_date.year,month=disbursable_date.month,day=28) + timedelta(days = 30)
            result['total_disbursable'] = total_disbursable - get_loan_halve_interest_amount(loan_amount,rate)
            return result
        
    result['eligible'] =  None
    result['total_payable'] = None
    result['repayment'] = None
    return result

def loanRepayment():
    LOAN_REPAID = False
    MONTHLY_REPAID = False
    LATENESS = False
    NEXT_PAYMENT_DATE = repayment_date
    USER_LOAN_TENURE = 3
    LOAN_OWED = total_payable
    per_monthly_payment = total_payable/USER_LOAN_TENURE
    MAX_LOAN_TENURE = 6
    LATENESS_DATE = repayment_date + timedelta(days = 1)
    LIST_OF_LATENESS = []
        
    MONTHLY_REPAID, payment = get_monthly_amount(per_monthly_payment)
        
    if LOAN_OWED is not 0:
        
        if not MONTHLY_REPAID and date.today() >= LATENESS_DATE:
            LATENESS = True
            LIST_OF_LATENESS.append(date.today())
            
            while LATENESS:
                for day in LIST_OF_LATENESS:
                    LOAN_OWED = total_payable + latenessInterest(per_monthly_payment,rate)
                LATENESS = False
                    
        if MONTHLY_REPAID and date.today() < LATENESS_DATE:
            LOAN_OWED = total_payable - payment
                
        NEXT_PAYMENT_DATE = NEXT_PAYMENT_DATE + timedelta(days = 30)
    else:
        LOAN_REPAID = True

def get_monthly_amount(per_monthly_amount):
    paid = False
    amount = 0
    if amount_from_gateway == per_monthly_amount:
        paid = True
        amount = amount_from_gateway
        return {'paid': True, 'amount': amount}
    return {'paid':paid, 'amount':amount}
                
        
def latenessInterest(monthly_repayment,rate):
    return monthly_repayment * (rate/100)


if __name__ == '__main__':
    disburse =  loan_Disbursement(2000,4000,categories['copper']['interest'],'copper')
    print('eligible ', disburse['eligible'])
    print('total payable ', disburse['total_payable'])
    print('repayment ', disburse['repayment'])
    print('disbursable ', disburse['total_disbursable'])

