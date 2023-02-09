import logging
import os


class Log1:
    @staticmethod
    def log1():
        base_dir = os.path.dirname(os.path.dirname(__file__))
        test = str(base_dir)
        logging.basicConfig(filename=test + "\\Logs\\automation1.log", level=logging.INFO, filemode="a",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p', force=True)
        logg = logging.getLogger()
        logg.setLevel(logging.INFO)
        return logg

