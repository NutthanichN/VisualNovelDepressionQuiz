class TextReader:
    def __init__(self,start_directory):
        self.directory = start_directory
        self.dialog = list(open(start_directory,'r').read().split('&'))
        self.index = 0
        self.path = []
    def read_text(self,directory):
        self.dialog = list(open(directory,'r').read().split('&'))
        self.index = 0
    def get_next_action(self):
        if self.dialog[self.index][0] == '$':
            return_value = ['D',[self.dialog[self.index][1:]]]
        elif self.dialog[self.index][0] == '@':
            return_value = list(self.dialog[self.index][1:].split('%'))
            question = list(return_value[0].split('+'))
            self.path = list(return_value[1].split('+'))
            return_value = ['Q',question]
        elif self.dialog[self.index][0] == '-':
            return_value = ['S',[self.dialog[self.index][1:]]]
        elif self.dialog[self.index][0] == '=':
            return_value = ['P',[self.dialog[self.index][1:]]]
        self.index += 1
        return return_value
    def change_path(self,question):
        self.read_text(self.path[question-1])

        
        
