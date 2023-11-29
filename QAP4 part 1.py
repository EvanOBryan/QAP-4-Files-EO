# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 08:53:48 2023

@author: Evan O'Bryan
"""
import datetime
from datetime import date
NextPolicy=1944
BasicPrem=float(869.00)
DiscountMulti=float(0.25)
ExtraLiability=float(130.00)
GlassCoverage=float(86.00)
LoanerCar=float(58.00)
HSTRate=float(0.15)
ProcessingFee=float(39.99)
def main():
    info()
    Values()
    receipt()
    claims()
    return
def info():
    global FirstName
    FirstName=input("First Name:")
    FirstName=FirstName.title()
    global LastName
    LastName=input("Last Name:")
    LastName=LastName.title()
    global Address
    Address=input("Address:")
    global City
    City=input("City:")
    City=City.title()
    Provinces=["AB","BC","ON","QC","NS","NB","MB","PE","SK","NL","NT","YT","NU"]
    global Province
    Province=input("Province (In 2 letter abbreviation. ex: AB=Alberta):")
    i=0
    while Province!=Provinces[i]:
        i=i+1
        if Provinces[i]==Province:
            break
        if i>=len(Provinces):
            print("Please input correct province.")
            info()
    global PostalCode
    PostalCode=input("Postal Code:")
    global PhoneNum
    PhoneNum=input("Phone Number:")
    global CarsInsured
    CarsInsured=int(input("Num of Cars Insured:"))
    global OptionExtra
    OptionExtra=input("Extra Liability (Up to $1,000,000. Y for yes, N for no):")
    OptionExtra=OptionExtra.upper()
    global OptionLoaner
    OptionLoaner=input("Loaner Car (Y for yes, N for no):")
    OptionLoaner=OptionLoaner.upper()
    global OptionGlass
    OptionGlass=input("Glass Coverage (Y for yes, N for no):")
    OptionGlass=OptionGlass.upper()
    global PaymentOption
    PaymentOption=input("Preferred Payment (DP=Down Payment, F=Full, M=Monthly):")
    PaymentOptions=["DP","F","M"]
    PaymentOption=PaymentOption.upper()
    i=0
    global DownPaymentAmount
    while PaymentOption!=PaymentOptions[i]:
        i=i+1
        if PaymentOptions[i]==PaymentOption:
            break
        if i>=len(PaymentOptions):
            print("Please input correct payment option.")
            info()
    if PaymentOption=="DP":
        DownPaymentAmount=float(input("Down Payment Amount:"))
    else:
        DownPaymentAmount=0
    global today
    today = date.today()
    global Claims
    global ClaimDates
    Claims=[]
    ClaimDates=[]
    Claim=input("Input claim:")
    while Claim!="":
        float(Claim)
        Claims.append(Claim)
        ClaimDate=input("Date of previous Claims (YYYY-MM-DD Format):")
        ClaimDates.append(ClaimDate)
        Claim=input("Input claim (hit enter to end):")
def Values():
    global InsurancePremiums
    InsurancePremiums=BasicPrem+(BasicPrem*DiscountMulti*(CarsInsured-1))
    InsurancePremiums=round(InsurancePremiums,2)
    global TotalExtraCost
    TotalExtraCost=0
    if OptionExtra=="Y":
        TotalExtraCost=TotalExtraCost+(ExtraLiability*CarsInsured)
    if OptionLoaner=="Y":
        TotalExtraCost=TotalExtraCost+(LoanerCar*CarsInsured)
    if OptionGlass=="Y":
        TotalExtraCost=TotalExtraCost+(GlassCoverage*CarsInsured)
    TotalExtraCost=round(TotalExtraCost,2)
    global TotalInsurancePremium
    TotalInsurancePremium=InsurancePremiums+TotalExtraCost
    TotalInsurancePremium=round(TotalInsurancePremium,2)
    global HSTTIP
    HSTTIP=HSTRate*TotalInsurancePremium
    HSTTIP=round(HSTTIP,2)
    global TotalCost
    TotalCost=HSTTIP+TotalInsurancePremium
    TotalCost=round(TotalCost,2)
    global MonthlyPayment
    MonthlyPayment=(TotalCost+ProcessingFee)/8
    MonthlyPayment=round(MonthlyPayment,2)
    global MonthlyPaymentDP
    MonthlyPaymentDP=(TotalCost+ProcessingFee-DownPaymentAmount)/8
    MonthlyPaymentDP=round(MonthlyPaymentDP,2)
    global InvoiceDate
    InvoiceDate=date.today()
    global FirstPaymentDate
    FirstPaymentDate=(InvoiceDate.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
def receipt():
    print("One Stop Insurance Company                   Policy Number:1944")
    print(f'Invoice Date: {today}')
    print(f'Name: {FirstName} {LastName}      Phone Number:{PhoneNum}')
    print(f'Address: {Address}  City: {City}        Province: {Province}')   
    print(f'Postal Code: {PostalCode}')
    print(f'Number of Cars Insured: {CarsInsured}')
    print(" ")
    print(f'Extra Liability: {OptionExtra} Glass Coverage: {OptionGlass} Loaner Car: {OptionLoaner}')
    print(f'Payment Option: {PaymentOption} Down Payment Amount (if applicable): ${DownPaymentAmount}')
    print("")
    print(f'Insurance Premium:                                        ${InsurancePremiums}')
    print(f'Extra Costs (liability, glass coverage, loaner cars):     ${TotalExtraCost}')
    print("                                                          ---------")
    print(f'Total Insurance Premiums:                                 ${TotalInsurancePremium}')
    print(f'HST:                                                      ${HSTTIP}')
    print("                                                          ---------")
    print(f'Total:                                                    ${TotalCost}')
    if PaymentOption=="M":
        print(f'Monthly Payment:                                          ${MonthlyPayment}')
        print(f'First Payment Date:                                        {FirstPaymentDate}')
    if PaymentOption=="DP":
        print(f'Monthly Payment:                                          ${MonthlyPayment}')
        print(f'Monthly Payment (Down Payment):                           ${MonthlyPaymentDP}')
        print(f'First Payment Date:                                        {FirstPaymentDate}')
def claims():
    print("Claim # Claim Date    Amount")
    print("----------------------------")
    for i in range(0,len(Claims)):
        print(f'{i+1}. {ClaimDates[i]}        ${Claims[i]}')
main()