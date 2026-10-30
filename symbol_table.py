class SymbolTable:
    def __init__(self):
        # Dictionary to store: name -> {'line': int, 'col': int, 'count': int}
        self.table = {}

    def insert(self, name, line, col):
        if name in self.table:
            self.table[name]['count'] += 1
        else:
            self.table[name] = {
                'line': line,
                'col': col,
                'count': 1
            }

    def lookup(self, name):
        return self.table.get(name, None)

    def print_table(self):
        print("\n--- SYMBOL TABLE ---")
        print(f"{'Identifier':<15} | {'Line':<6} | {'Col':<6} | {'Count':<6}")
        print("-" * 45)
        for name, info in self.table.items():
            print(f"{name:<15} | {info['line']:<6} | {info['col']:<6} | {info['count']:<6}")
        print("-" * 45)