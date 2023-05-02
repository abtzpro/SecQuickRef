import csv

class SecurityStandards():
    def __init__(self, filename):
        self.filename = filename
        self.standards = []
        self.load_standards()

    def load_standards(self):
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.standards.append(row)

    def search(self, query):
        results = []
        for standard in self.standards:
            if query in standard.values():
                results.append(standard)
        return results

    def display(self, standards):
        for standard in standards:
            for key, value in standard.items():
                print(key + ": " + value)
            print()

if __name__ == '__main__':
    filename = 'cybersecurity_standards.csv'
    standards = SecurityStandards(filename)

    print("Welcome to the Cybersecurity Standards Reference Guide!")
    print("To search for a specific standard, enter the name or acronym below.")
    print("To exit the program, type 'exit'.")

    while True:
        query = input("Enter search query: ")
        if query.lower() == "exit":
            break
        results = standards.search(query)
        if results:
            standards.display(results)
        else:
            print("No results found.")
