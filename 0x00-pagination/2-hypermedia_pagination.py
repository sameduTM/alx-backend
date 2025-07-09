#!/usr/bin/env python3
"""paginate the dataset correctly and return the appropriate page of
    the dataset
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Instantiation of dataset to None"""
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing the key-value pairs
            page_size, page, data, next_page, prev_page, total_pages
        """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)
        if not data:
            page_size = 0
        if page == 1:
            prev_page = None
        if page == len(data) or not data:
            next_page = None
        next_page = page + 1
        prev_page = page - 1

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
