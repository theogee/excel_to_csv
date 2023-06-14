import pandas as pd
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed

class Converter:
    def __init__(self, conf, logger):
        self.conf = conf
        self.logger = logger

    def __convert_chunk(self, chunk, output_queue, itr):
        header = itr == 0
        csv_data = chunk.to_csv(index=False, header=header, sep=";", line_terminator="\n")
        output_queue.put(csv_data)

    def convert_xlsx_to_csv(self, input_file, output_file, chunk_size=500, num_threads=10):
        self.logger.info(f"converting excel file into csv. input_file: {input_file}. output_file: {output_file}")
        
        output_queue = Queue()

        with pd.ExcelFile(input_file) as xls:
            num_rows = pd.read_excel(xls, sheet_name=self.conf["sheet_number"], usecols=[0]).shape[0]

            with ThreadPoolExecutor(max_workers=num_threads) as executor:
                futures = []

                for i in range(0, num_rows, chunk_size):
                    chunk = pd.read_excel(xls, sheet_name=0, skiprows=i, nrows=chunk_size, header=0)
                    future = executor.submit(self.__convert_chunk, chunk, output_queue, i)
                    futures.append(future)

                with open(output_file, "w", encoding="UTF8") as csv_file:
                    for future in as_completed(futures):
                        csv_data = output_queue.get()
                        csv_file.write(csv_data)

        
        self.logger.info("conversion completed")