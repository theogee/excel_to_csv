import pandas as pd
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed

class Converter:
    def __init__(self, conf, logger):
        self.conf = conf
        self.logger = logger

    def __convert_chunk(self, chunk, output_queue, itr):
        # header = itr == 0
        csv_data = chunk.to_csv(index=False, header=False, sep=self.conf["delimiter"], line_terminator="\n")
        output_queue.put(csv_data)
        return csv_data

    def convert_xlsx_to_csv(self, input_file, output_file, chunk_size=500, num_threads=10):
        self.logger.info(f"converting excel file into csv. input_file: {input_file}. output_file: {output_file}")
        
        output_queue = Queue()

        with pd.ExcelFile(input_file) as xls:
            master = None

            if len(self.conf["columns"]) == 0:
                master = pd.read_excel(xls, sheet_name=self.conf["sheet_number"])
            else:
                master = pd.read_excel(xls, sheet_name=self.conf["sheet_number"], usecols=self.conf["column_idx"])

            num_rows = master.shape[0]
            self.logger.info(f"number of rows: {num_rows}")

            with ThreadPoolExecutor(max_workers=num_threads) as executor:
                futures = []

                for i in range(0, num_rows, chunk_size):
                    chunk = master[i:i+chunk_size]
                    # chunk = pd.read_excel(xls, sheet_name=self.conf["sheet_number"], skiprows=i, nrows=chunk_size, header=0)
                    future = executor.submit(self.__convert_chunk, chunk, output_queue, i)
                    futures.append(future)
                    # self.logger.info(f"registered batch: {i}")

                with open(output_file, "w", encoding="UTF8") as csv_file:
                    csv_headers = map(lambda h: h.strip(), master.columns)
                    csv_file.write(self.conf["delimiter"].join(list(csv_headers)) + "\n")

                    for d in executor.map(lambda f: f.result(), futures):
                        csv_file.write(d)

                    # for future in as_completed(futures):
                    #     csv_data = output_queue.get()
                    #     csv_file.write(csv_data)

        
        self.logger.info("conversion completed")