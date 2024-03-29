class TextReader:
    def __init__(self,start_directory,username):
        self.loop_round = 0
        self.username = username
        self.directory = start_directory
        self.check = 0
            
      
        self.dialog = list(open(start_directory,'r').read().split('&'))
        self.index = 1
        self.path = []
        self.score = 0
        self.loop_stop = False
        
    def read_text(self,directory,num_ans):
        # print(['loop',self.loop_round],num_ans)
        if self.loop_round ==6:
            self.dialog = list(open(directory,'r', encoding='utf-8').read().split('&'))
        elif self.loop_round == 9 and num_ans == 1:
            self.dialog = list(open(directory, 'r', encoding='utf-8').read().split('&'))
        elif self.loop_round == 9 and num_ans == 3:
            self.dialog = list(open(directory, 'r', encoding='utf-8').read().split('&'))
        else:
            self.dialog = list(open(directory,'r').read().split('&'))
        self.index = 1
    def get_next_action(self):
        if self.loop_stop:
            pass
        if self.dialog[self.index][0] == '$':
            return_value = ['D',list(self.dialog[self.index][1:].replace('*',self.username).replace('#','miina').replace('฿','Butler').replace('~',' ').split(':'))]
        elif self.dialog[self.index][0] == '@':
            return_value = list(self.dialog[self.index][1:].split('%'))
            answer = list(return_value[0].split('+'))
            self.answer = answer
            self.ans_no_point = []
            for answer in self.answer:
                self.ans_no_point.append(answer[:-1])
            self.question = self.dialog[self.index -1][1:]
            self.path = list(return_value[1].split('+'))
            return_value = ['Q',self.ans_no_point]
            self.loop_stop = True
        elif self.dialog[self.index][0] == '-':
            return_value = ['S',[self.dialog[self.index][1:]]]
        elif self.dialog[self.index][0] == '=':
            return_value = ['P',[self.dialog[self.index][1:]]]
        elif self.dialog[self.index][0] == '`':
            self.record_score()
        else:
            print('this data did not use the correct formatting, the program will skip thi dialog')
        self.index += 1
        return return_value
    def change_path(self,question):
        self.loop_round +=1
        self.data_entry(question)
        self.read_text(self.path[question-1].replace('\n',''),question -1)
        self.loop_stop = False
        
    def data_entry(self,question):
        record = open(f'result/{self.username}.txt','a')
        self.question = self.question.replace("\n","")
        record.write(f'{self.question[2:]}')
        for answer in self.answer:
            answer = answer.replace("\n","")
            record.write(f'/{answer[:-1]}')
        if self.check ==0:
            self.check =1
            record.write(f'///{question}\n')
        else:
            record.write(f'/{question}\n')
        record.close()
        self.score += int(self.answer[question-1][-1])
    def record_score(self):
        record = open(f'result/{self.username}.txt','a')
        record.write(f'#\n{self.score}\n')
        record.write(f'Patient name : {self.username}\n')
        record.close()
        
