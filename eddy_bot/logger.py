import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(ascitime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)
