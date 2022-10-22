import numpy as np

class hire_me:
    def __init__(self, yti:str, mutations_max:int=2, random_pertubation:int=0.042, convergence_break:int=0.8) -> None:
        self.random_pertubation = random_pertubation
        self.convergence_break  = convergence_break
        self.mutations_max      = mutations_max
        self.yti                = yti
        self.ln             = 125
        self.dp             = 21
        self.yhat           = [''.join(np.random.choice(['#',' '], replace=True, size=self.ln))]*self.dp
        self.score          = 0
        self.decrypter()


    def decrypter(self):
        ln_decrypter = [self.ln*i for i in range(self.dp)]
        ln_decrypter
        ytt = []
        for dc in range(1,len(ln_decrypter)):
            a,b = ln_decrypter[dc-1], ln_decrypter[dc]
            ytt.append(self.yti[a:b])
        self.yt = ytt

    def compute_accuracy_score(self, yhat):
        score = []
        [score.append(np.mean([yhi_==yi_ for yhi_,yi_ in zip(yhi,yi)])) for yhi,yi in zip(yhat, self.yt)]
        return score

    def print_result(self, yhat):
        for xx in yhat:
            print(xx)

    def apply_random_mutation(self, yhat):

        def update_yhat(yhat=yhat):
            idx = list(np.random.choice(range(self.ln), replace=False, size=np.random.choice(range(self.mutations_max))))
            idx = sorted(idx)
            y_  = yhat
            for i in idx:
                r   = [' ' if y_[i]=='#' else '#'][0]
                y_  = y_[:i] + r + y_[(i+1):]
            return y_
            
        y_new = []
        for y_ in yhat:
            y_new.append(update_yhat(y_))

        yup = []
        for (sn,sh,yn,yh) in zip(self.compute_accuracy_score(y_new), self.compute_accuracy_score(yhat), y_new, yhat):
            if sn > sh:
                if self.ix < self.convergence_break*self.samples and self.random_pertubation > np.random.uniform():
                    yup.append(yn)
                else:
                    yup.append(yn)
            else:
                yup.append(yh)
        
        return yup, self.compute_accuracy_score(yup)

    def execute(self, samples:int=5000, prints_:bool=True):
        self.ix         = 0
        self.samples    = samples
        while self.ix < samples and np.mean(self.score)<1:

            self.ix += 1
            self.yhat, self.score = self.apply_random_mutation(self.yhat)
            if prints_:
                self.print_result(self.yhat)
                print('')


yti = '###################################################################################################################################################################################################################################################################################      ##       ##  ###  ####       ####       ##  #######       ##  ###  ####################################################  ##  ##  ###  ##   ##  ######  #######  ###  ##  #######  ###  ###  #  #####################################################  ######       ##  #    ######  #######       ##  #######       ####   ######################################################  ##  ##  ###  ##  ##   ######  #######  #######  #######  ###  ####   ######################################################      ##  ###  ##  ###  ####       ####  #######       ##  ###  ####   ###################################################################################################################################################################################  ###  ##       ##       ##  ###  ####  ###  ##       ##  ###  ##      ######################################################  ###  ####  #######  #####  ###  #####  #  ###  ###  ##  ###  ##  ###  #####################################################  # #  ####  #######  #####       ######   ####  ###  ##  ###  ##      ######################################################   #   ####  #######  #####  ###  ######   ####  ###  ##  ###  ##  #  #######################################################  ###  ##       ####  #####  ###  ######   ####       ##       ##  ##   ############################################################################################################################################################################       ##       ##       ##       ##  ###  ##       ##       ################    #######     ################################  ###  ##  ###  ##  ###  ##  ###  ##   ##  ##  ###  #######  ##############   ##     #  ###   ###############################   ######       ##  ###  ##  ###  ##  #    ##   #########   #############   #####  #    ####   ################################   ####   ######  ###  ##  ###  ##  ##   ####   #########################   ##  ####   ##   ###############################       ##   ######       ##       ##  ###  ##       #####  ##################    #######    ########################################################################################################################################################################################################################################################################'



messages = [
    'Hello! :) my name is Zach Wolpe, I\'m a Data Scientist/Machine Learning Engineer & I\'d LOVE to join bending spoons!',
    'I\'ve encrypted a message for you, just for fun.',
    'The message is made up of 2^(125*21) bits (binary encoding), that means there are this many possible combinations:\n',
    2**(125*21),
    'Yikes! That\'s a lot of permutations :(. Luckly I\'ve attached a basic genetic algorithm (GA) that makes quick work of this search space!',
    'press ENTER to run the GA and decrypt the message...'
]

def message_block(idx):
    print(space + messages[idx], end=end)
    print(ENTER, end=end)
    input()

if __name__=='__main__':
    space   = '    '
    end     = '\n'
    ENTER   = end + space + 'Press ENTER to continue.'
    print()
    message_block(0)
    message_block(1)
    print(space + messages[2], end=end)
    print(messages[3])
    print(ENTER, end=end)
    input()
    print(end + space + messages[4], end=end)
    print(end + space + messages[5] + end, end=end)
    input()
    print('fin')
    hire = hire_me(yti=yti)
    hire.execute()







