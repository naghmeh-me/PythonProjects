customers={}

print("for exit just enter.")

while True:
    name=input("enter the name:")
    if name=="":
        break
    else:
        
        try:
            account_number=int(input("enter the account number:"))
            first_taraz=int(input("enter the taraz first month:"))
            sum_bougth_products=int(input("enter the number of all bougth products:"))
            credit=int(input("enter customer credit:"))
            allowed_credit_limit=int(input("enter allowed credit limit:"))
        except ValueError:
            print("please enter numeric information.")
            continue
        else:

            customers[name]={
                "account_number":account_number,
                "sum_bougth_products":sum_bougth_products,
                "credit":credit
                }
            new_taraz=first_taraz+sum_bougth_products-credit

            if new_taraz>allowed_credit_limit:
                print(f"name={name}\naccount_number={account_number}\nallowed_credit_limit={allowed_credit_limit}\ntaraz={new_taraz}")
                print("creted limit exceeded.")
            else:
                print(f"name={name}\naccount_number={account_number}\nallowed_credit_limit={allowed_credit_limit}\ntaraz={new_taraz}")
                print("creted limit not exceeded.")
                    

                
                
            
