from collections import Counter
import config

class Plan(object):
    def __init__(self, party_num, freq):
        setattr(self, 'party_num', party_num)
        setattr(self, 'frequency', freq)
        setattr(self, 'income', dict([(i, Counter()) for i in range(party_num + 1)]))
        setattr(self, 'spending', dict([(i, Counter()) for i in range(party_num + 1)]))

    def _update(self, plan, item, amount, party):
        if party is None:
            party = 0
        plan_dict = getattr(self, plan)
        print plan_dict
        plan_dict[party][item] = amount
        setattr(self, plan, plan_dict)

    def update_income(self, item, amount, party=None):
        self._update('income', item, abs(amount), party=None)

    def update_spending(self, item, amount, party):
        self._update('spending', item, -1 * abs(amount), party)


class YearlyPlan(Plan):
    def __init__(self, party_num):
        super(YearlyPlan, self).__init__(party_num, config.yearly_plan_frequency)
        for i in range(party_num):
            self.update_income('Bonus', 0, i+1)
        self.update_spending('Vacation', 0, 0)
        self.update_spending('Gift', 0, 0)

class MonthlyPlan(Plan):
    def __init__(self, party_num):
        super(MonthlyPlan, self).__init__(party_num, config.monthly_plan_frequency)
        for i in range(party_num):
            self.update_income('Pay', 0, i+1)
        self.update_spending('Housing', 0, 0)
        self.update_spending('Property Tax', 0, 0)
        self.update_spending('Property Insurance', 0, 0)
        self.update_spending('Carrier Plan', 0, 0)
        self.update_spending('Cable Plan', 0, 0)
        self.update_spending('Subscription', 0, 0)
        self.update_spending('Pantry Supply', 0, 0)
        self.update_spending('Shopping', 0, 0)
        self.update_spending('Entertainment', 0, 0)

class DailyPlan(Plan):
    def __init__(self, party_num):
        super(DailyPlan, self).__init__(party_num, config.daily_plan_frequency)
        self.update_spending('Grocery', 0, 0)
        self.update_spending('Food Delivery', 0, 0)
        self.update_spending('Eat Out', 0, 0)

class WeekdayPlan(Plan):
    def __init__(self, party_num):
        super(WeekdayPlan, self).__init__(party_num, config.weekday_plan_frequency)
        for i in range(party_num):
            self.update_spending('Work Spending', 0, i+1)
            self.update_spending('Work Transportation', 0, i+1)

class WeekendPlan(Plan):
    def __init__(self, party_num):
        super(WeekendPlan, self).__init__(party_num, config.weekend_plan_frequency)
        self.update_spending('Transportation', 0, 0)
