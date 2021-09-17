import os
from rich.console import Console
from rich.text import Text
console = Console()

def Display_available_RAM():
    ram = os.popen("vmstat -s").read()
    console.print(Text("Available RAM :",style="bold rgb(175,0,255)"))
    console.print(Text(ram,style="bold blue"))

def Display_Load_avearge():
    data = os.popen("cat /proc/loadavg").read()
    console.print(Text("Load Average :",style="bold rgb(175,0,255)"))
    console.print(Text(data,style="bold blue"))

def Display_Hostname_details():
    data = os.popen("hostnamectl status").read()
    console.print(Text("Hostname Details :",style="bold rgb(175,0,255)"))
    console.print(Text(data,style="bold blue"))


def Display_All_process_count():
    data = os.popen("ps -aux | wc -l").read()
    console.print(Text("Process Count :",style="bold rgb(175,0,255)"))
    console.print(Text(data,style="bold blue"))


def Display_time():
    data = os.popen("uptime -s").read()
    console.print(Text("Present Time :",style="bold rgb(175,0,255)"))
    console.print(Text(data,style="bold blue"))


def main_menu():
	console.print("1.Display available RAM",style="bold blue")
	console.print("2.Display Load avearge",style="bold blue")
	console.print("3.Display Hostname details",style="bold blue")
	console.print("4.Display All process count",style="bold blue")
	console.print("5.Display uptime",style="bold blue")
	console.print("6.Exit",style="bold blue")

operations = {
    "1":Display_available_RAM,
    "2":Display_Load_avearge,
    "3":Display_Hostname_details,
    "4":Display_All_process_count,
    "5":Display_time
}

while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()