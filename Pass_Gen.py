import random
from colorama import Fore, Style, init
import re
# Initialize colorama
init(autoreset=True)

# Color definitions
COLOR_GREEN = Fore.GREEN
COLOR_RED = Fore.RED
COLOR_YELLOW = Fore.YELLOW
COLOR_BLUE = Fore.BLUE
COLOR_CYAN = Fore.CYAN
COLOR_MAGENTA = Fore.MAGENTA

# Password Generation Functions
def generate_password(length):
    """Generate a strong password with given length"""
    password = ""
    small_az = "qwertyuiopasdfghjklzxcvbnm"
    caps_az = "QWERTYUIOPASDFGHJKLZXCVBNM"
    nums = "1234567890"
    symbols = "!@#$%^&*()_+{<}>?~`,.;'[]\\"
    
    for i in range(int(length)):
        reqs = [small_az, caps_az, nums, symbols]
        password += random.choice(random.choice(reqs))
    return password

def handle_password_generation():
    """Handle the password generation process"""
    print(f"{COLOR_CYAN}OK, I'll assist you in generating your own unique password. ^_^{Style.RESET_ALL}")
    ans1 = input(f"{COLOR_YELLOW}Shall we proceed (y/n): {Style.RESET_ALL}")
    if ans1.lower() == "y":
        while True:
            try:
                pass_len = int(input(f"{COLOR_BLUE}Enter the length of your desired password: {Style.RESET_ALL}"))
                if pass_len < 6:
                    print(f"{COLOR_RED}Password length should be at least 6 characters!{Style.RESET_ALL}")
                else:
                    password = generate_password(pass_len)
                    print(f"{COLOR_GREEN}Your password is ----> {COLOR_MAGENTA}{password}{Style.RESET_ALL}")
                    break
            except ValueError:
                print(f"{COLOR_RED}Please enter a valid number!{Style.RESET_ALL}")

# Password Strength Checking Functions
def check_password_strength(user_pass):
    """Check the strength of a password and return results"""
    strength = 0
    advice = []
    
    if len(user_pass) >= 6:
        strength += 1
    else:
        advice.append("Password should be at least 6 characters long.")
    
    if re.search(r'[A-Z]', user_pass):
        strength += 1
    else:
        advice.append("Add uppercase letters.")
    
    if re.search(r'[a-z]', user_pass):
        strength += 1
    else:
        advice.append("Add Lower case letters.")
    
    if re.search(r'\d', user_pass):
        strength += 1
    else:
        advice.append("Add Some Numbers in your password.")
    
    if re.search(r'[!@#$%^&*()_+{<}>?~`,.;\'\[\]\\]', user_pass):
        strength += 1
    else:
        advice.append("Add some special characters onto your password.")
    
    return strength, advice

def display_strength_results(user_pass, strength, advice):
    """Display the password strength results"""
    print(f"\n{COLOR_CYAN}{'='*50}{Style.RESET_ALL}")
    
    if strength == 5:
        print(f"{COLOR_GREEN}Your password '{COLOR_MAGENTA}{user_pass}{COLOR_GREEN}' is {COLOR_GREEN}Very Strong! ★★★★★{Style.RESET_ALL}")
    elif strength == 4:
        print(f"{COLOR_CYAN}Your password '{COLOR_MAGENTA}{user_pass}{COLOR_CYAN}' is {COLOR_CYAN}Strong! ★★★★☆{Style.RESET_ALL}")
        print(f"{COLOR_YELLOW}Suggestions:{Style.RESET_ALL}")
        for i in range(1, len(advice) + 1):
            print(f"{COLOR_YELLOW}{i}.{Style.RESET_ALL} {advice[i-1]}")
    elif strength == 3:
        print(f"{COLOR_YELLOW}Your password '{COLOR_MAGENTA}{user_pass}{COLOR_YELLOW}' is {COLOR_YELLOW}Medium! ★★★☆☆{Style.RESET_ALL}")
        print(f"{COLOR_YELLOW}Suggestions:{Style.RESET_ALL}")
        for i in range(1, len(advice) + 1):
            print(f"{COLOR_YELLOW}{i}.{Style.RESET_ALL} {advice[i-1]}")
    else:
        print(f"{COLOR_RED}Your password '{COLOR_MAGENTA}{user_pass}{COLOR_RED}' strength is {COLOR_RED}{strength}/5{Style.RESET_ALL} which is considered as {COLOR_RED}WEAK! ★☆☆☆☆{Style.RESET_ALL}")
        print(f"{COLOR_RED}Suggestions:{Style.RESET_ALL}")
        for i in range(1, len(advice) + 1):
            print(f"{COLOR_RED}{i}.{Style.RESET_ALL} {advice[i-1]}")
    
    print(f"{COLOR_CYAN}{'='*50}{Style.RESET_ALL}")

def handle_strength_check():
    """Handle the password strength checking process"""
    print(f"{COLOR_CYAN}OK, Enter your password carefully below.{Style.RESET_ALL}")
    user_pass = input(f"{COLOR_BLUE}Enter your Password: {Style.RESET_ALL}")
    strength, advice = check_password_strength(user_pass)
    display_strength_results(user_pass, strength, advice)

# Main Menu Class
class PasswordManager:
    def show_menu(self):
        """Display the main menu"""
        print(f"\n{COLOR_MAGENTA}{'☆' * 50}{Style.RESET_ALL}")
        print(f"{COLOR_CYAN}Hi! I'm Alex! How can I assist you?{Style.RESET_ALL}")
        print(f"{COLOR_GREEN}1. {COLOR_YELLOW}Generate me a password{Style.RESET_ALL}")
        print(f"{COLOR_GREEN}2. {COLOR_YELLOW}Check the strength of my password{Style.RESET_ALL}")
        print(f"{COLOR_GREEN}3. {COLOR_RED}Quit{Style.RESET_ALL}")
        print(f"{COLOR_MAGENTA}{'☆' * 50}{Style.RESET_ALL}")
    
    def run(self):
        """Run the main program loop"""
        while True:
            self.show_menu()
            ans = input(f"{COLOR_BLUE}Enter your choice (1/2/3): {Style.RESET_ALL}")
            
            if ans == "1":
                handle_password_generation()
            elif ans == "2":
                handle_strength_check()
            elif ans == "3":
                print(f"{COLOR_GREEN}Thank you for using Password Manager! Goodbye! 👋{Style.RESET_ALL}")
                break
            else:
                print(f"{COLOR_RED}Invalid input '{ans}'. Please enter 1, 2, or 3.{Style.RESET_ALL}")
            
            # Continue unless user chose to quit
            if ans != "3":
                continue_choice = input(f"{COLOR_YELLOW}Do you want to continue? (y/n): {Style.RESET_ALL}")
                if continue_choice.lower() != 'y':
                    print(f"{COLOR_GREEN}Thank you for using Password Manager! Goodbye! 👋{Style.RESET_ALL}")
                    break

# Utility Class
class PasswordUtils:
    @staticmethod
    def get_strength_color(strength):
        """Get color based on strength score"""
        if strength == 5:
            return COLOR_GREEN
        elif strength >= 3:
            return COLOR_YELLOW
        else:
            return COLOR_RED

# Run the program
if __name__ == "__main__":
    print(f"{COLOR_CYAN}{'★' * 60}{Style.RESET_ALL}")
    print(f"{COLOR_MAGENTA}        Welcome to Alex's Password Manager!{Style.RESET_ALL}")
    print(f"{COLOR_CYAN}{'★' * 60}{Style.RESET_ALL}")
    
    manager = PasswordManager()
    manager.run()