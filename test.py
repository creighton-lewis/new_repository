import requests 
from rich.console import Console #type: ignore
console = Console ()
       
class poc_finder_file : 
        console.print("Enter list of CVE's to search for POC's for")
        input_file = console.input("Input file name (with extension): ")
        with open(input_file, 'r') as file:
                cve_list = file.readlines()
        for cve in cve_list:
                cve = cve.strip()
                year = cve.split('-')[1]
                if "CVE-" not in cve:
                        cve = "CVE-" + cve
                print(f"Searching for {cve}")
                url = (f"https://raw.githubusercontent.com/trickest/cve/refs/heads/main/{year}/{cve}.md")
                response = requests.get(url)
                if response.status_code == 200:
                        console.print(f"[bold green] Trickest url found for {cve}! [/bold green]")
                        text = requests.get(url, timeout=10).text
                        print(text)
                        if text == "*No PoCs":
                                console.print(f"[bold yellow] No POCs available for {cve} [/bold yellow]")
                elif response.status_code == 404:
                        print(f"This CVE POC {cve} is not found in Trickest repo")
                else:
                        console.print(f"[bold red] Error fetching POC for {cve} [/bold red]")
        
def poc_finder() :
        console.print("[bold green] CVE POC Finder [/bold green]")
        cve = console.input("Write cve")
        year = cve.split('-')[1]
        if "CVE-" not in cve:
            cve = "CVE-" + cve
        #return cve, year
        print(f"{cve}")
        url = (f"https://raw.githubusercontent.com/trickest/cve/refs/heads/main/{year}/{cve}.md")
        print (url)
        response = requests.get(url)
        if response.status_code == 200:
                console.print("[bold green] Trickest url found! [/bold green]")
                text = requests.get(url, timeout=10).text
                print(text)
                if text == "*No PoCs":
                        console.print("[bold yellow] No POCs available for this CVE [/bold yellow]")
        elif response.status_code == 404:
                print("This CVE POC is not found in Trickest repo")
        else:
                console.print("[bold red] Error fetching POC [/bold red]")
poc_finder()