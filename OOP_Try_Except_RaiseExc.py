import math
from difflib import get_close_matches


class Helpful:

    def __init__(self, text, pos_int):
        self.text = text
        self.pos_int = pos_int

    def item_count(self):
        if self.pos_int < 0:
            return "Please enter a positive number!"
        else:
            return len(self.text)

    def page_count(self):
        self.p_count = math.ceil(len(self.text) / self.pos_int)
        return self.p_count

    def count_items_on_page(self, page_num):
        self.page_num = page_num

        if self.page_num in range(self.p_count-1):
            return self.pos_int
        elif self.page_num == self.p_count - 1:
            return len(self.text) - self.pos_int * (self.p_count - 1)
        elif self.page_num >= self.p_count:
            raise Exception('Invalid index. Page is missing.')

    def display_page(self, page_number):
        self.page_number = page_number
        self.step = self.pos_int
        self.string_list = [self.text[i:i + self.step] for i in range(0, len(self.text), self.step)]
        return self.string_list[self.page_number]

    def find_page(self, page_sym):
        self.page_sym = page_sym
        self.sym_indx = [indx for indx, item in enumerate(self.text.lower()) if self.page_sym in item]
        text_index = [index for index, value in enumerate(self.text)]
        text_index_list = [text_index[i:i + self.step] for i in range(0, len(text_index), self.step)]

        if self.page_sym not in self.text:
            raise Exception(f"'{self.page_sym}' is missing on the pages")

        self.matches_list = []
        if len(self.page_sym) > 1:
            result = get_close_matches(self.page_sym, self.string_list, cutoff=0.5)
            for item in self.string_list:
                for im in result:
                    if im == item:
                        ind = self.string_list.index(im)
                        self.matches_list.append(ind)

        for s in self.sym_indx:
            for y, x in enumerate(text_index_list):
                if s in x:
                    self.matches_list.append(y)

        return self.matches_list


pages = Helpful('Your beautiful text', 5)
print(pages.page_count())
print(pages.item_count())
print(pages.count_items_on_page(3))
print(pages.display_page(3))
print(pages.find_page('be'))


### FUNCTION Divide

def divide(a):
    a_list = list(a)

    try:
        fir_num = int(a_list[0])
        sec_num = int(a_list[-1])
        return fir_num / sec_num
    except ZeroDivisionError as zd:
        return f"Error code: {zd}"
    except ValueError as ve:
        return f'Error code: {ve}'
    