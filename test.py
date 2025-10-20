import requests 
from rich.console import Console #type: ignore
console = Console ()
       

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