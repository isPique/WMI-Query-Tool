from colorama import Fore, Style, init
import win32com.client
import pywintypes
import json
import os

init(autoreset = True) # Initialize Colorama to enable colored output

def load_queries_from_json(json_file):
    try:
        with open(json_file, 'r') as file: # Attempt to open and load the JSON file
            data = json.load(file)
            return data['queries'] # Return the 'queries' section of the JSON

    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}JSON file '{json_file}' not found.")
        exit(0)

def select_query(queries):
    os.system('cls||clear')
    print(f"Available queries:")
    for i, query in enumerate(queries, start = 1):
        query_number = f"{i:2}"
        print(f"{Fore.LIGHTBLACK_EX}{query_number} - {Fore.YELLOW}{query}")

    while True:
        try:
            choice = int(input(f"\nSelect a query (1 - {len(queries)}): "))
            if 1 <= choice <= len(queries):
                return queries[choice - 1]
            else:
                print(f"{Fore.RED}Invalid choice. Please select a valid query number.")

        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a valid query number.")

def print_results(results): # Function to print the results of a WMI query
    os.system('cls||clear')
    for item in results:
        print(f"{Fore.GREEN}\n--- Result ---")
        for prop in item.Properties_:
            print(f"{Fore.LIGHTRED_EX}{prop.Name}: {Fore.CYAN}{prop.Value}{Style.RESET_ALL}")

if __name__ == "__main__":
    json_file = "queries.json"
    queries = load_queries_from_json(json_file) # Load queries from the JSON file

    while True:
        if queries:
            selected_query = select_query(queries)
            c = win32com.client.GetObject(r"winmgmts:\root\cimv2") # Create a WMI object
            try:
                results = c.ExecQuery(f"SELECT * FROM {selected_query}") # Execute the selected query using WMI and display the results
                print_results(results)

            except pywintypes.com_error as e:
                print(f"{Fore.RED}Error querying {selected_query}: {e}")

        user_choice = input(f"\nChoose an option:\n{Fore.LIGHTBLACK_EX}1. {Fore.YELLOW}Select another query\n{Fore.LIGHTBLACK_EX}2. {Fore.YELLOW}Exit\n\n{Style.RESET_ALL}Enter your choice (1 or 2): ")
        if user_choice == "2":
            break

        elif user_choice != "1":
            print(f"{Fore.RED}Invalid choice. Please select a valid option (1 or 2).")