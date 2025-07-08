import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset
    
    def index_range(self, page: int, page_size: int) -> tuple:
        """return a tuple of size two with start index and end index
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """Simple pagination to get page"""
            assert type(page) == int and type(page_size) == int
            assert page > 0 and page_size > 0 and type(page)
            idx_range = self.index_range(page, page_size)
            dataset = self.dataset()
            if idx_range:
                return dataset[idx_range[0]:idx_range[1]]
            return []
