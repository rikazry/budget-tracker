import datetime
import os

class Book(object):
    def __init__(self, book_name='Yearly Budget', party_num=2, data_path=r'budget/data'):
        conf_dict = dict(
                'book_name': book_name,
                'init_date': datetime.date.today(),
                'party': ['party_{}'.format(i) for i in range(party_num)],
                'data_path': data_path,
                )
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        setattr(self, 'configuration', conf_dict)
        #setattr(plan)
        #setattr(record)
        #setattr(forecasted_saving)
        #setattr(realized_saving)

