import pywhatkit
import datetime
import time

class TTUL():
    """TTUL: Talk To U Later!"""

    @staticmethod
    def fetch_time(add_secs=0):
        _now  = datetime.datetime.now()
        time  = _now + datetime.timedelta(days=0, seconds=add_secs)
        hours = time.strftime("%H")
        mins  = time.strftime("%M")
        secs  = time.strftime("%S")
        return int(hours), int(mins), int(secs)    
    
    @staticmethod
    def message_generator(module_name, runtime, *args, **kwargs):
        msg ="""\n
        ============================================================
        ============================================================
            
            CODE EXECUTION COMPLETE!
        
            module:     {}
            runtime:    {} seconds
            {}

            Bravo garçon! maintenant de retour au travail!
        
        ============================================================
        ============================================================
        \n""".format(module_name,runtime, '' if 'notes' not in kwargs else 'notes:      ' + kwargs['notes'])
        return msg

    @staticmethod
    def send_message(whatsapp_no, msg):
        h,m,_ = TTUL.fetch_time(60)
        pywhatkit.sendwhatmsg(whatsapp_no,msg,h,m)


class TTUL_timeit(TTUL):
    __whatsapp_no = None
    
    @property
    def whatsapp_no(self):
        return self.__whatsapp_no
    
    @whatsapp_no.setter
    def whatsapp_no(self, no):
        # implement safety logic
        if no is None:
            return
        self.__whatsapp_no = no


    @staticmethod
    def whatsapp_with_timer(func):
        def wrapper(*args, **kwargs):
            start   = time.time()
            rt      = func(*args, **kwargs)
            fin     = time.time()
            runtime = fin-start
            cell_no = TTUL_timeit.__whatsapp_no
            msg     = TTUL_timeit.message_generator(module_name=func.__name__, runtime=runtime, *args, **kwargs)
            TTUL_timeit.send_message(cell_no, msg)
            return rt
        return wrapper



if __name__=='__main__':

    # update number
    ttu             = TTUL_timeit()
    ttu.whatsapp_no = '+27666666666'

    @ttu.whatsapp_with_timer
    def test_function(*args, **kwargs):
        time.sleep(1)

    test_function(notes='The results are stored in S3/temp.')


