from collections import Counter

class Plan(object):
    def __init__(self, party_num, freq):
        setattr(self, 'party_num', party_num)
        setattr(self, 'frequency', freq)
        setattr(self, 'income', dict([(i, Counter()) for i in range(party_num + 1)])
        setattr(self, 'spending', dict([(i, Counter()) for i in range(party_num + 1)])

    def _update(self, plan, item, amount, party):
        if party is None:
            party = 0
        plan_dict = getattr(self, plan)
        plan_dict[party][item] = amount
        setattr(self, plan, plan_dict)

    def update_income(self, item, amount, party=None):
        self._update('income', item, abs(amount), party=None)

    def update_spending(self, item, amount, party):
        self._update('spending', item, -1 * abs(amount), party)


class YearlyPlan(Plan):
    def __init__(self, party_num):
        super(YearlyPlan, self).__init__(party_num, 1)
        for i in range(getattr(self, 'party_num')):
            self.update_income('Bonus', 0, i+1)
        self.update_spending('Vacation', 0, 0)
        self.update_spending('Gift', 0, 0)

class MonthlyPlan(Plan):
    def __init__(self, party_num):
        super(MonthlyPlan, self).__init__(party_num, 12)
        for i in range(getattr(self, 'party_num')):
            self.update_income('Pay', 0, i+1)
