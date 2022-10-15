import os
import csv
import platform
import pyfiglet
from time import sleep


platform = platform.system()

if platform == "Linux" :
    def clear() :
        os.system("clear")
else :
    def clear() :
        os.system("cls")

class colors :
    red = "\033[1;91m"
    bold = "\033[1m"
    cyan = "\033[36m"
    white = "\033[1;97m"
    default = "\033[0m"


# Banner
def banner(banner) :
    clear()
    print("\n\n")
    print(pyfiglet.figlet_format(banner))
    print("\n\n")

# Main Menu
def main_menu() :
    banner("E - Commerce")
    print(f"""{colors.white}[ {colors.red}1 {colors.white}]{colors.bold}\tAdd a product
{colors.white}[ {colors.red}2 {colors.white}]\t{colors.bold}Search a product
{colors.white}[ {colors.red}3 {colors.white}]\t{colors.bold}Buy a product
{colors.white}[ {colors.red}4 {colors.white}]\t{colors.bold}Sales by the firm
{colors.white}[ {colors.red}5 {colors.white}]\t{colors.bold}Purchases by the firm
{colors.white}[ {colors.red}6 {colors.white}]\t{colors.bold}Exit\n\n
{colors.white}[ {colors.red}* {colors.white}]\t{colors.bold} {colors.cyan}Please enter your choice{colors.default}""")

    choice = int(input("e-commerce > "))


    if choice == 1 :
        banner("Add a product")
        print(f"{colors.white}[ {colors.red}* {colors.white}]\t{colors.bold}{colors.cyan}Please enter the following information about the product{colors.default}\n\n")
        productName = input(f"{colors.white}[ {colors.red}- {colors.white}]  {colors.bold}Product Name : ")
        with open("./product.csv","r") as csv_file :
            getLine = csv_file.read().splitlines()[0]
            productId = int(getLine.split(",")[0]) + 1
            with open("./product.csv","r") as csv_file :
                if productName not in csv_file.read():
                
                    try :
                        productPrice = int(input(f"{colors.white}[ {colors.red}- {colors.white}]  {colors.bold}Price : "))
                    except :
                        print("Price should be a number ")
                    with open("./product.csv", "a") as csv_file_ :
                        i = csv.writer(csv_file_).writerow([productId,productName,productPrice])
                        print(f"\n\n\n{colors.white}[ {colors.red}+ {colors.white}]\t{colors.bold}Product Successfuly added !")
                        sleep(2)
                        csv_file_.close()
                else :
                    print("does exist")
                    sleep(1)
            csv_file.close()

        
    elif choice == 2 :
        banner("Search")
        print(f"{colors.white}[ {colors.red}* {colors.white}]\t{colors.bold}{colors.cyan}Enter the product name which you want to search{colors.default}\n\n")
        query = input(f"{colors.white}[ {colors.red}- {colors.white}]  {colors.bold}Product Name : ")
        with open("./product.csv","r") as csv_file :
            for line in csv_file.read().splitlines() :
                for word in line.split(",") :
                    if word == query :
                        print(f"""\n\n{colors.bold}
{colors.white}  *  {colors.red}Id {colors.white}: {colors.cyan}{line.split(',')[0]}
{colors.white}  *  {colors.red}ProductName {colors.white}: {colors.cyan}{line.split(',')[1]}
{colors.white}  *  {colors.red}Price {colors.white}: {colors.cyan}{line.split(',')[2]}
{colors.white}  *  {colors.red}StockLeft {colors.white}: {colors.cyan}{line.split(',')[3]}{colors.default}""")
                    
        print(f"\n\n{colors.white}[ {colors.red}! {colors.white}]\t{colors.cyan}Press any key to return back {colors.red}Main Menu{colors.default}")
        input()


    # Buy a product
    elif choice == 3 :
        banner("Buy  a  product")
        print(f"""{colors.white}[ {colors.red}1 {colors.white}]\t{colors.bold}Single orders (all products quanty will be one){colors.default}
{colors.white}[ {colors.red}2 {colors.white}]\t{colors.bold}Bulk orders""")
        choice_ = int(input(f"x : "))
        if choice_ == 1 :
            products = []
            numberOfProducts = int(input("Enter number of products : "))
            for item in range(0,numberOfProducts):
                print("j")
            input()
    elif choice == 4 :
        #jithu -> sales by the firm  bar chart & histogram 





    


while True :
    main_menu()
