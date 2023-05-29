"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg


"""


class MathStats():
    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        self._disp = None
        self._sigma_sq = None
      
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)

    @property
    def data(self) -> list:
        return self._data

    @property
    def get_mean(self):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """
        data = self._data
        sums = {'Offline': 0, 'Online': 0}
        for _l in data:
            sums['Offline'] += _l['Offline']
            sums['Online'] += _l['Online']

        self._mean = {'Offline': round(sums['Offline'] / len(data), 2), 'Online': round(sums['Online'] / len(data), 2)}

        return self._mean

    @property
    def max(self):
        data = self._data
        maxs = {'Offline': float('-Inf'), 'Online': float('-Inf')}
        for _l in data:
            if maxs['Offline'] < _l['Offline']:
                maxs['Offline'] = _l['Offline']
            if maxs['Online'] < _l['Online']:
                maxs['Online'] = _l['Online']
        self._max = maxs
      
        return self._max

    @property
    def min(self):
        data = self._data
        mins = {'Offline': float('Inf'), 'Online': float('Inf')}
        for _l in data:
            if mins['Offline'] > _l['Offline']:
                mins['Offline'] = _l['Offline']
            if mins['Online'] > _l['Online']:
                mins['Online'] = _l['Online']
        self._min = mins
      
        return self._min

    @property
    def disp(self):
        data = self._data
        disps = {'Offline': 0, 'Online': 0}
        mean = self._mean
        for _l in data:
            disps['Offline'] += (_l['Offline'] - mean['Offline'])**2
            disps['Online'] += (_l['Online'] - mean['Online'])**2
        self._disp = {'Offline': round(disps['Offline'] / len(data), 2), 'Online': round(disps['Online'] / len(data), 2)}
      
        return self._disp

    @property
    def sigma_sq(self):
        disps = self._disp
        sigmas = {'Offline': round(disps['Offline']**(1/2), 2), 'Online': round(disps['Online']**(1/2), 2)}
        self._sigma_sq = sigmas
      
        return self._sigma_sq
