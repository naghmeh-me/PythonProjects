countries={'IRAN':'TEHRAN','FRANCE':'PARIS','USA':'WASHIGTON D.C','UNITED KINGDOM':'LONDON','GERMANY':'BERLIN','UAE':'ABU DHABI','TAILAND':'BANGKOK','SPAIN':'MADRID'}

print("welcom enter the name of the country to give you the capital of that or enter exit to break.")

while True:
    country=input("enter:")
    if country=="exit":
        break
    else:
        if country in countries:
            capital=countries[country]
            print(f"capital of {country} is {capital}.")
            continue
        else:
            if country.upper() in countries:
                capital=countries[country.upper()]
                print(f"capital of {country} is {capital}.")
                continue
            else:
                if country.capitalize() in countries:
                    capital=countries[country.capitalize()]
                    print(f"capital of [country] is {capital}.")
                    continue
                else:
                    print("soory this country is not in database.")
                    continue

