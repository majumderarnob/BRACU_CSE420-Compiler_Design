class dfa:

    def __init__(self, address: str) -> None:
        self.address_list = [i for i in address]
        self.checked = None
        self.state = 1
        self.track = 0
        self.alphabet = 'abcdefghijklmnopqrstuvxyz'
        self.digit = '1234567890'
        self.flag = False

    def run(self) -> str:
        self.length = len(self.address_list)
        while True:

            if self.state == 1:
                if self.address_list[self.track] == 'w':
                    self.state = 5
                elif self.address_list[self.track] in self.alphabet:
                    self.state = 4
                self.track += 1

            elif self.state == 2:
                if self.address_list[self.track] in self.digit or self.address_list[self.track] in self.alphabet or self.address_list[self.track] == 'w':
                    self.state = 2
                if self.address_list[self.track] == '.':
                    self.state = 12
                self.track += 1

            elif self.state == 3:
                if self.track < self.length:
                    if self.address_list[self.track] in self.alphabet or self.address_list[self.track] == 'w':
                        self.state = 3
                else:
                    break
                self.track += 1

            elif self.state == 4:
                if self.address_list[self.track] in self.digit or self.address_list[self.track] in self.alphabet or self.address_list[self.track] == 'w':
                    self.state = 6
                self.track += 1

            elif self.state == 5:
                if self.address_list[self.track] == 'w':
                    self.state = 7
                elif self.address_list[self.track] in self.digit or self.address_list[self.track] in self.alphabet:
                    self.state = 6
                self.track += 1

            elif self.state == 6:
                if self.address_list[self.track] in self.digit or self.address_list[self.track] in self.alphabet or self.address_list[self.track] == 'w':
                    self.state = 6
                elif self.address_list[self.track] == '@':
                    self.flag = True
                    self.state = 8
                self.track += 1

            elif self.state == 7:
                if self.address_list[self.track] == 'w':
                    self.state = 9
                elif self.address_list[self.track] == '@':
                    self.state = 8
                elif self.address_list[self.track] in self.digit or self.address_list[self.track] in self.alphabet:
                    self.state = 6
                self.track += 1

            elif self.state == 8:
                if self.address_list[self.track] in self.alphabet or self.address_list[self.track] == 'w':
                    self.state = 10

            elif self.state == 9:
                if self.address_list[self.track] == '@':
                    self.state = 8
                elif self.address_list[self.track] == '.':
                    self.state = 11
                elif self.address_list[self.track] in self.digit or self.address_list[self.track] in self.alphabet or self.address_list[self.track] == 'w':
                    self.state = 6
                self.track += 1

            elif self.state == 10:
                if self.address_list[self.track] in self.alphabet or self.address_list[self.track] == 'w':
                    self.state = 10
                elif self.address_list[self.track] == '.':
                    self.state = 12
                self.track += 1

            elif self.state == 11:
                if self.address_list[self.track] in self.digit or self.address_list[self.track] in self.alphabet or self.address_list[self.track] == 'w':
                    self.state = 2
                self.track += 1

            elif self.state == 12:
                if self.address_list[self.track] in self.alphabet or self.address_list[self.track] == 'w':
                    self.state = 3
                self.track += 1

        if self.flag:
            return "Email"
        else:
            return "Web"


output = []
n = int(input("How Many Input are there?: "))
for _ in range(n):
    task = dfa(input("Input your Input: "))
    output.append(task.run())

for i in range(len(output)):
    print(f'{output[i]}, {i+1}')
