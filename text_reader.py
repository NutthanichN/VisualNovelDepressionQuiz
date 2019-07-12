class TextReader:
    def __init__(self,start_directory,username):
        self.username = username
        self.directory = start_directory
        self.dialog = list(open(start_directory,'r').read().split('&'))
        self.index = 0
        self.path = []
        self.score = 0
        self.failskip = 0
    def read_text(self,directory):
        self.dialog = list(open(directory,'r').read().split('&'))
        self.index = 0
    def get_next_action(self):
        if self.failskip = 0:
            self.failskip = 1
            return
        if self.dialog[self.index][0] == '$':
            return_value = ['D',list(self.dialog[self.index][1:].replace('*',self.username).replace('#','miina').split(':'))]
        elif self.dialog[self.index][0] == '@':
            return_value = list(self.dialog[self.index][1:].split('%'))
            answer = list(return_value[0].split('+'))
            self.answer = answer
            self.question = self.dialog[self.index -1][1:]
            self.path = list(return_value[1].split('+'))
            return_value = ['Q',answer]
        elif self.dialog[self.index][0] == '-':
            return_value = ['S',[self.dialog[self.index][1:]]]
        elif self.dialog[self.index][0] == '=':
            return_value = ['P',[self.dialog[self.index][1:]]]
        else:
            print('this data did not use the correct formatting, the program will skip thi dialog')
        self.index += 1
        return return_value
    def change_path(self,question):
        self.data_entry(question)
        self.read_text(self.path[question-1])
    def data_entry(self,question):
        record = open(f'result/{self.username}.txt','a')
        record.write(f'{self.question[3:]}')
        for answer in self.answer:
            record.write(f'/{answer[:-1]}')
        record.write(f'/{question}\n')
        record.close()
        self.score += int(self.answer[question-1][-1])
    def record_score(self):
        record = open(f'result/{self.username}.txt','a')
        record.write(f'#\n{self.score}\n')
        record.write(f'Patient name : {self.username}\n')
        record.close()
        

        
        
