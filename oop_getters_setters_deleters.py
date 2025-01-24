#Lesson OOP: Getters, Setters, Deleters          22/01/2025

#Exercise n1 Temperature Class

# class Temperature:
#     def __init__(self, celsius:float):
#         self._celsius = celsius
#     @property
#     def celsius(self):
#         return self._celsius
#
#     @celsius.setter
#     def celsius(self, new_temp:float):
#         self._celsius = new_temp
#
#     @property
#     def fahrenheit(self):
#         return (self.celsius * 1.8) + 32
#
# celsius = Temperature(20)
# print(celsius.fahrenheit)

#############################################################################

#Exercise n2 Real Estate Property Value Tracker

# class Property:
#     def __init__(self, address:str, size:int, market_value:float):
#         self._address = address
#         self._size = size
#         self._market_value = market_value
#         self._tax_rate = 0.01
#
#     @property
#     def size_m2(self):
#         return self._size_m2
#
#     @size_m2.setter
#     def size_m2(self, value):
#         self._size_m2 = value
#
#     @property
#     def market_value(self):
#         return self._market_value
#
#     @market_value.setter
#     def market_value(self, value):
#         self._market_value = value
#
#     @property
#     def taxes(self):
#         # The tax calculation could also factor in property size, if relevant
#         return self._market_value * self._tax_rate
#
#     def __str__(self):
#         return (
#             f"Property at {self.address}, Size: {self.size_m2}m², Market Value: $"
#             f"{self.market_value}, Taxes: ${self.taxes:.2f}"
#         )
# home = Property("Washington Street", 139, 350000)
# print(home.taxes)  # Output based on a tax rate
# home.market_value = 480000  # Market value updated
# print(home.taxes)  # Updated tax calculation

#############################################################################

#Exercise n3 Stock Portfolio and Dividend Tracker

# class Stock:
#     def __init__(self, symbol, shares, price):
#         self.symbol = symbol
#         self.shares = shares
#         self.price = price
#         self.dividend_yield = 0.02  # Example static dividend yield
#
#     @property
#     def value(self):
#         return self.shares * self.price
#
#
# class Portfolio:
#     def __init__(self):
#         self.stocks = {}
#
#     def add_stock(self, symbol, shares, price):
#         self.stocks[symbol] = Stock(symbol, shares, price)
#
#     def remove_stock(self, symbol):
#         if symbol in self.stocks:
#             del self.stocks[symbol]
#
#     def update_stock(self, symbol, price):
#         if symbol in self.stocks:
#             self.stocks[symbol].price = price
#
#     def total_value(self):
#         return sum(stock.value for stock in self.stocks.values())
#
#     def dividends(self):
#         return sum(stock.value * stock.dividend_yield for stock in self.stocks.values())
#
# portfolio = Portfolio()
# portfolio.add_stock("AAPL", 50, 150)
# portfolio.add_stock("GOOGL", 30, 2500)
# print(portfolio.total_value())  # Output: total market value of portfolio
# portfolio.update_stock("AAPL", 145)  # Update stock price
# print(portfolio.dividends())  # Output: calculated dividends

#############################################################################

#Exercise n4 Dynamic Sports Team Management System

class Player:
    def __init__(self, name, goals, assists, salary):
        self.name = name
        self.goals = goals
        self.assists = assists
        self._salary = salary

    @property
    def performance_index(self):
        return self.goals * 2 + self.assists

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def update_performance(self, goals, assists):
        self.goals = goals
        self.assists = assists
        # Adjust salary based on new performance index.
        # Example formula:
        self.salary = self.salary + 1000 * self.performance_index

    def __str__(self):
        return (
            f"{self.name}, Goals: {self.goals}, Assists: {self.assists}, Salary: "
            f"${self.salary:.2f}"
        )


class Team:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.players = []

    def add_player(self, name, goals, assists, salary):
        if sum(p.salary for p in self.players) + salary > self.budget:
            print("Cannot add player, salary cap exceeded.")
            return
        self.players.append(Player(name, goals, assists, salary))

    def update_player_performance(self, name, goals, assists):
        player = next((p for p in self.players if p.name == name), None)
        if player:
            player.update_performance(goals, assists)

    def __str__(self):
        return f"Team: {self.name}, Budget: ${self.budget:.2f}, Players:\n" + "\n".join(
            str(player) for player in self.players
        )

team = Team("Sharks", 1000000)  # 1 million budget
team.add_player("John Doe", 10, 5, 50000)  # 50,000 initial salary
team.add_player("Jane Smith", 15, 10, 75000)

print(team)
team.update_player_performance("John Doe", 12, 7)  # Update performance stats
print(team)