vijay = ["Ghilli", "Thuppakki", "Mersal", "Master", "Leo",
         "Bigil", "Kaththi", "Theri", "Sarkar", "Pokkiri"]

ajith = ["Mankatha", "Billa", "Viswasam", "Veeram", "Valimai",
         "Vedalam", "Aarambam", "Citizen", "Dheena", "NKP"]

surya = ["Ghajini", "Ayan", "Singam", "24", "Jai Bhim",
         "Soorarai Pottru", "Kaakha Kaakha", "Vel", "7aum Arivu", "NGK"]

dhanush = ["Asuran", "VIP", "Karnan", "Aadukalam", "Maari",
           "Thiruchitrambalam", "Polladhavan", "Captain Miller", "Raayan", "Raanjhanaa"]

actors = ("Vijay", "Ajith", "Surya", "Dhanush")

actor_set = {"Vijay", "Ajith", "Surya", "Dhanush"}

top_x = int(input("Please enter top x number (1-10): "))
actor = input("Please enter actor name: ")

if actor not in actor_set:
    print("Error: Unknown Actor")

elif top_x < 1 or top_x > 10:
    print("Error: Enter a number between 1 and 10")

else:

    if actor == "Vijay":
        movies = vijay

    elif actor == "Ajith":
        movies = ajith

    elif actor == "Surya":
        movies = surya

    elif actor == "Dhanush":
        movies = dhanush

    print(f"\nHere are the top {top_x} super hit movies of {actor}")

    for i in range(top_x):
        print(f"{i+1}. {movies[i]}")
