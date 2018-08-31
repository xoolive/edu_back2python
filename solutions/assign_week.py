carburant = carburant.assign(week=carburant.date.apply(lambda x: x.week))
carburant.loc[(carburant.week == 53) & (carburant.month == 1), 'week'] = 0
