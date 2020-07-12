class LastRaceStats:
    def __init__(self, dict):
        self.startPos = dict['startPos']
        self.lapsLed = dict['lapsLed']
        self.finishPos = dict['finishPos']
        self.incidents = dict['incidents']
        self.trackName = dict['trackName']\
            .replace('+', ' ')\
            .replace('%5B', '(')\
            .replace('%5D', ')')\
            .replace('%C3%BC', 'u')
        self.sof = dict['sof']
        self.date = dict['date']
        self.seriesID = dict['seriesID']
        self.time = dict['time']
        self.winnerName = dict['winnerName']
        self.winnerID = dict['winnerID']
        self.clubPoints = dict['clubPoints']
        self.champPoints = dict['champPoints']
        self.subsessionID = dict['subsessionID']
        self.seasonID = dict['seasonID']
        self.winnerLL = dict['winnerLL']
