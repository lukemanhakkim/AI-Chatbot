from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

class nlu_model:
    def train_nlu(self, data, config, model_dir):
        training_data = load_data(data)
        trainer = Trainer(RasaNLUConfig(config))
        trainer.train(training_data)
        model_directory = trainer.persist(model_dir, fixed_model_name='AIchatbotnlu')

    def run_nlu(self):
        interpreter = Interpreter.load('./models/nlu/default/AIchatbotnlu', RasaNLUConfig('config_spacy.json'))
        #print(interpreter.parse("I am planning my holiday to Lithuania. I wonder what is the weather out there."))
        print(interpreter.parse("Whats the latest news?"))

nlu_obj=nlu_model()
"""
def train_nlu(data, config, model_dir):
    training_data = load_data(data)
    trainer = Trainer(RasaNLUConfig(config))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='weathernlu')


def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/weathernlu', RasaNLUConfig('config_spacy.json'))
    print(interpreter.parse("I am planning my holiday to Lithuania. I wonder what is the weather out there."))
"""

if __name__ == '__main__':
   # train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
   #run_nlu()
   nlu_obj.train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
   nlu_obj.run_nlu()