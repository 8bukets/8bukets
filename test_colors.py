class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{Colors.HEADER}HEADER: Starting Process...{Colors.ENDC}")
print(f"{Colors.BLUE}BLUE: Info message{Colors.ENDC}")
print(f"{Colors.CYAN}CYAN: Processing...{Colors.ENDC}")
print(f"{Colors.GREEN}GREEN: Success!{Colors.ENDC}")
print(f"{Colors.WARNING}WARNING: Be careful{Colors.ENDC}")
print(f"{Colors.FAIL}FAIL: Error occurred{Colors.ENDC}")
print(f"{Colors.BOLD}BOLD Text{Colors.ENDC}")

print("\n")
print(f"{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
print(f"{Colors.BOLD}║             SUMMARY REPORT             ║{Colors.ENDC}")
print(f"{Colors.BOLD}╠════════════════════════════════════════╣{Colors.ENDC}")
print(f"{Colors.BOLD}║{Colors.ENDC} 📄 Pages Scraped:      {Colors.CYAN}5{Colors.ENDC}             {Colors.BOLD}║{Colors.ENDC}")
print(f"{Colors.BOLD}║{Colors.ENDC} 💾 Posts Saved:        {Colors.GREEN}350{Colors.ENDC}           {Colors.BOLD}║{Colors.ENDC}")
print(f"{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}")
