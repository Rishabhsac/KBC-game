import random

class Kbcgame:

    def __init__(self):

        self.namelist = []
        self.chName = ''
        self.op = ''
        self.que = []
        self.options = []
        self.loptions = []
        self.correct = ()
        self.record = dict()
        self.money = 0


    def instructions(self):

        return """""""""Instructions of game are as follows
        1->There are total 8 questions
        2->You have two lifelines
           a)50-50
           b)Flip the question
        3->One lifeline can be used only once
        4->If you used both lifelines ,winning amount is reduced by Rs.200
        5->In any question only one lifeline can be used
        6->Each question is for Rs.200
        7->Total winning amount is Rs.1600
        8->Wrong answer of any question will QUIT the game
        9->you cannot leave/Quit the game in between\n"""""""""""


    def queoptions(self):

        self.que=["1.Which of these is not a recommended mineral in human diet?",
             "2.Which of these is a term for a place where people gather for shayari and ghazals?",
             "3.Who was the president of india at the turn of the century ,as the 20th century became the 21st century?",
             "4.With which of these states do Chattisgarh,Jharkhand and Andhra Pradesh all share their borders?",
             "5.The first World Championship in what sport held in 2017,through the game has been played since 1877?",
             "6.Which is the largest living species of tortoise in the world,which may weigh about 400 kg?",
             "7.In what sport did India win a bronze in the junior Women's World Cup in Germany in 2013?",
             "8.Which is the coldest place in India?",
             "9.In the human body,what makes the pupil of an eye contract or dilate?",
             "10.who is the author of the poem'Where the mind is without fear?"]


        self.options=[["(A)Strontium","(B)Potassium","(C)Iron","(D)Calcium"],
                      ["(A)Rukhsar","(B)Mushaira","(C)Shikara","(D)Mahabara"],
                      ["(A)K R Narayan","(B)APJ Abdul Kalam","(C)R.Venkatraman","(D)Shankar Dayal Sharma"],
                      ["(A)Madhya Pradesh","(B)Odisha","(C)Bihar","(D)Uttar Pradesh"],
                      ["(A)Test Cricket","(B)Rugby Union","(C)Kabbaddi","(D)Carrom"],
                      ["(A)Sulcata Tortoise","(B)Greneda Tortoise","(C)Golde Greek Tortoise","(D)Galapagos Tortoise"],
                      ["(A)Hockey","(B)Football","(C)Volleyball","(D)Basketball"],
                      ["(A)Yusmarg","(B)Kulgam","(C)Drass","(D)Leh"],
                      ["(A)Hunger","(B)Thirst","(C)Light","(D)Sound"],
                      ["(A)Muhammad Iqbal","(B)Bakim Chandra Chatterjee","(C)RabindraNath Tagore","(D)Sri Aurobindo"]]

        self.correct=("(A)Strontium","(B)Mushaira","(A)K R Narayan","(B)Odisha","(A)Test Cricket","(D)Galapagos Tortoies","(A)Hockey","(C)Drass","(C)Light","(C)RabindraNath Tagore")


    def checkoptions(self,i):

        self.i = i
        choptions = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
        check = 0

        for i in range(len(choptions)):
            if self.op == choptions[i]:
                check += 1
                break

        if check > 0:
            if self.op == self.correct[self.i][1] or self.op == self.correct[self.i][1].lower():
                print("\ncongratulation you got the right answer")
                self.money = self.money + 200
                print("Now your winning amount is {}\n".format(self.money))
            else:
                print("\nSorry your answer is wrong!!")
                print("Thanks for playing!! ")
                print("Your final winning amount is {}\n".format(self.money))
                return ''

        else:
            print("wrong choice")
            return' '


    def complete(self):

        print("\nCongratulations You have completed the game")
        print("Thanks for playing!!")
        print("Your final winning amount is {}\n".format(self.money))


    def lifeline_5050 (self,i):

        self.i = i
        t = 0
        self.loptions = self.options[self.i]
        for j in range (3):
            if self.loptions[j] != self.correct[self.i]:
                self.loptions.remove(self.loptions[j])
                t = t+1
                if t == 2:
                    break
        print("Now options after using 50-50 lifeline are ")
        input("")
        for j in range(2):
            print(self.loptions[j])
        return ''


    def lifeline_flip (self,i):

        self.i = i + 1
        self.queformat(self.i)


    def queformat(self,i):

        self.queoptions()
        self.i = i
        print("Next Question is on your screen now")
        input("")
        print(self.que[self.i])
        input("")
        print("Now your options are")
        input("")
        for j in range(4):
            print(self.options[self.i][j])
        print("\n")


    def playerSelection (self, i):

        self.i = i

        if self.i == 1:
            for i in range(3):

                name = input("Enter player" + str(i+1) +"name: ")
                self.namelist.append(name)
        else:
            self.namelist.remove(self.chName)

        self.chName = random.choice(self.namelist)
        return self.chName


    def testKbcGame (self):

        for i in range(1, 4):

            j = 0
            life = 0
            life50 = 0
            lifeflip = 0
            self.money = 0

            print("WELCOME TO KBC GAME\n")
            print("{} is Selected\n".format(self.playerSelection(i)))
            print(self.instructions())

            while j != -1:

                self.queformat(j)
                print("1->To give the answer")
                print("2->To choose a lifeline")

                try:
                    ch=int(input("Enter your choice "))
                except:
                    print("wrong choice")
                    continue

                if ch == 1:

                    self.op = input("Enter your options(A,B,C or D)")
                    checkopt = self.checkoptions(j)
                    if checkopt == '':
                        break
                    elif checkopt == ' ':
                        continue
                    elif j >= 9:
                        self.complete()
                        break
                    else:
                        j += 1
                        continue

                elif ch == 2:
                    if life < 2:
                        if life == 0:
                            print("Enter 1 for 50-50")
                            print("Enter 2 for Flip the Question")
                            try:
                                self.op = int(input("Choose your lifeline"))
                            except:
                                print ("wrong choice")
                                continue

                            if self.op == 1:
                                self.lifeline_5050(j)

                                life = life + 1
                                life50 = 1

                                self.op = input("Enter your options(A,B,C or D)")

                                checkopt = self.checkoptions(j)
                                if checkopt == '':
                                    break
                                elif checkopt == ' ':
                                    continue
                                elif j >= 9:
                                    self.complete()
                                    break
                                else:
                                    j += 1
                                    continue

                            elif self.op == 2:
                                self.lifeline_flip(j)

                                life += 1
                                lifeflip = 1

                                self.op = input("Enter your options(A,B,C or D)")
                                j = j + 1
                                checkopt = self.checkoptions(j)

                                if checkopt == '':
                                    break
                                elif checkopt == ' ':
                                    continue
                                elif j >= 9:
                                    self.complete()
                                    break
                                else:
                                    j += 1
                                    continue

                            else:
                                print("wrong choice")
                                continue

                        elif life == 1:
                            if life50 == 1:
                                print("Remaining lifeline is Flip the Question")
                                self.lifeline_flip(j)
                                life = life + 1
                                self.money = self.money - 200
                                self.op = input("Enter your options(A,B,C or D)")
                                j = j + 1
                                checkopt = self.checkoptions(j)

                                if checkopt == '':
                                    break
                                elif checkopt == ' ':
                                    continue
                                elif j >= 9:
                                    self.complete()
                                    break
                                else:
                                    j += 1
                                    continue

                                life += 1


                            elif lifeflip == 1:
                                print("Remaining lifeline is 50-50")
                                self.lifeline_5050(j)
                                life = life + 1
                                self.money = self.money - 200
                                self.op = input("Enter your options(A,B,C or D)")
                                checkopt = self.checkoptions(j)

                                if checkopt == '':
                                    break
                                elif checkopt == ' ':
                                    continue
                                elif j >= 9:
                                    self.complete()
                                    break
                                else:
                                    j += 1
                                    continue

                                life += 1

                    else:
                        print("You have used your both lifelines\n")
                        self.op = input("Enter your options(A,B,C or D)")
                        checkopt = self.checkoptions(j)

                        if checkopt == '':
                            break
                        elif checkopt == ' ':
                            continue
                        elif j >= 9:
                            self.complete()
                            break
                        else:
                            j += 1
                            continue

                else:
                    print("wrong choice")
                    continue;


kbc = Kbcgame()
kbc.testKbcGame()
