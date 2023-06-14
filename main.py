from Converter import Converter
import time
import os
import json
import logging
import sys

conf = {}
with open(os.path.join(os.getcwd(), "Script/excel_to_csv/conf.json")) as f:
    conf = json.load(f)

logging.basicConfig(
    format="%(asctime)s %(module)s %(lineno)s %(levelname)s %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S", 
    level=logging.INFO,
    handlers=[
        logging.FileHandler("Script/excel_to_csv/main.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger()

def main():
    converter = Converter(conf, logger)

    converter.convert_xlsx_to_csv(conf["input_file_path"], conf["output_file_path"], conf["chunk_size"], conf["num_threads"])

logger.info("PROGRAM STARTED")
s = time.perf_counter()
main()
elapsed = time.perf_counter() - s
logger.info(f"TRACE process completed in {elapsed:0.2f} seconds")
logger.info("PROGRAM FINISHED")
