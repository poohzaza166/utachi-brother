import logging
import yaml
seting = open('config/botsetting.yaml')

try:
    seting = open('config/botsetting.yaml')
    # a = open('botsetting.yaml')
    botconfig = yaml.load(seting, Loader=yaml.FullLoader)
except FileNotFoundError as error:
    # logs.debug(error)
    # logs.info('no config file found genreating new one')
    print('no config file found')
    exit()
except yaml.YAMLError as exc:
    print('config file error ')
    if hasattr(exc, 'problem_mark'):
        mark = exc.problem_mark
        print(f"Error position: (%s:%s)" % (mark.line+1, mark.column+1))
        exit()


if botconfig['bot_setting']['loglevel'] == "debug":
    logging.basicConfig(filename='config/app.log', filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',encoding='utf-8',level=logging.DEBUG)

elif botconfig['bot_setting']['loglevel'] == "info":
    logging.basicConfig(filename='config/app.log', filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',encoding='utf-8',level=logging.INFO)

elif botconfig['bot_setting']['loglevel'] == "error":
    logging.basicConfig(filename='config/app.log', filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',encoding='utf-8',level=logging.ERROR)


logs = logging.getLogger(__name__)





