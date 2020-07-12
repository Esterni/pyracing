class YearlyStats:
    def __init__(self, dict):
        self.wins = dict['wins']
        self.winPerc = round(dict['winPerc'], 2)
        self.year = dict['year']
        self.poles = dict['poles']
        self.clubpoints = dict['clubpoints']
        self.avgStart = round(dict['avgStart'], 2)
        self.avgFinish = round(dict['avgFinish'], 2)
        self.top5Perc = round(dict['top5Perc'], 2)
        self.totalLaps = dict['totalLaps']
        self.avgIncPerRace = round(dict['avgIncPerRace'], 2)
        self.avgPtsPerRace = round(dict['avgPtsPerRace'], 2)
        self.lapsLed = dict['lapsLed']
        self.top5 = dict['top5']
        self.lapsLedPerc = round(dict['lapsLedPerc'], 2)
        self.category = dict['category'].replace('+', ' ')
        self.starts = dict['starts']
