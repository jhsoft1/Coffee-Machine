class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water, self.milk, self.beans, self.cups, self.money = water, milk, beans, cups, money
        self.state = "choosing an action"

    def do_action(self, action):
        if self.state == "choosing an action":
            if action == 'buy':
                self.state = "choosing a type of coffee"
            elif action == 'fill':
                self.water += int(input('\nWrite how many ml of water you want to add:\n'))
                self.milk += int(input('Write how many ml of milk you want to add:\n'))
                self.beans += int(input('Write how many grams of coffee beans you want to add:\n'))
                self.cups += int(input('Write how many disposable coffee cups you want to add:\n'))
            elif action == 'take':
                print(f'I gave you ${self.money}')
                self.money = 0
            elif action == 'exit':
                pass
            elif action == 'remaining':
                print(f'\nThe coffee machine has:\n{self.water} of water\n{self.milk} of milk\n'
                      f'{self.beans} of coffee beans\n{self.cups} of disposable cups\n${self.money} of money\n')
        elif self.state == "choosing a type of coffee":
            self.state = "choosing an action"
            if action == '1':
                if self.water < 250:
                    print('Sorry, not enough water!\n')
                elif self.beans < 16:
                    print('Sorry, not enough coffee beans!\n')
                else:
                    print('I have enough resources, making you a coffee!\n')
                    self.water -= 250
                    self.beans -= 16
                    self.money += 4
                    self.cups -= 1
            elif action == '2':
                if self.water < 350:
                    print('Sorry, not enough water!\n')
                elif self.beans < 20:
                    print('Sorry, not enough coffee beans!\n')
                elif self.milk < 75:
                    print('Sorry, not enough milk!\n')
                else:
                    print('I have enough resources, making you a coffee!\n')
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.money += 7
                    self.cups -= 1
            elif action == '3':
                if self.water < 200:
                    print('Sorry, not enough water!\n')
                elif self.beans < 12:
                    print('Sorry, not enough coffee beans!\n')
                elif self.milk < 100:
                    print('Sorry, not enough milk!\n')
                else:
                    print('I have enough resources, making you a coffee!\n')
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.money += 6
                    self.cups -= 1


machine = CoffeeMachine(400, 540, 120, 9, 550)
to_do = ''
while to_do != 'exit':
    if machine.state == "choosing an action":
        print('Write action (buy, fill, take, remaining, exit):')
    elif machine.state == "choosing a type of coffee":
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    to_do = input()
    machine.do_action(to_do)
