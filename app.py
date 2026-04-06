import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s",
    force=True   
)

def add(a, b):
    logging.info("Addition operation performed")
    return a + b