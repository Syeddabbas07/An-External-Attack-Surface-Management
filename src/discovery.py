import subprocess  
from rich.console import Console  

console = Console()  

def enumerate_subdomains(domain):  
    console.print(f"[blue]Starting passive enumeration for {domain}...[/bluegi]")
    try:  
        result = subprocess.run( 
            ["subfinder", "-d", domain, "-silent"],  
            capture_output=True, text=True, check=True 
        )
        subdomains = result.stdout.strip().split("\n") 
        console.print(f"[green]Found {len(subdomains)} subdomains![/green]") 
        return [s for s in subdomains if s] 
    except Exception as e: 
        console.print(f"[red]Error: {e}[/red]")  
        return []  #


if __name__ == "__main__":  
    test_domain = "example.com" 
    subs = enumerate_subdomains(test_domain)  
    console.print(subs[:10])