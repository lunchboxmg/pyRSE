from common import R2D, D2R

UNITS_DEGREES = UNITS_DEG = 'deg'
UNITS_RADIANS = UNITS_RAD = 'rad'

class Coordinate(object):

    def __init__(self, lat, lon, units='deg', alt=0, elevation=0):

        if units.tolower() == 'deg':
            lat * D2R
            lon * D2R

        self._lat = lat
        self._lon = lon
        self._alt = alt
        self._elevation = elevation

    @staticmethod
    def convertFromString(value):

        if ':' in value:
            deg, min_, sec = value.split(':')
            dir_ = sec[-1]
            sec = sec[:-1]
        else:
            dir = value[-1]
            sec = "{:s}.{:s}".format(value[-7:-5], value[-5:-2])
            min_ = value[-9:-7]
            deg = value[:-9]
        
        out = float(deg) + float(min_)/60.0 + float(sec)/3600.0
        if dir_ in 'SsWw': return -out
        return out


    def getLat(self, units='deg'):

        if units == 'deg': return self._lat * R2D
        return self._lat

    def getLon(self, units='deg'):

        if units == 'deg': return self._lon * R2D
        return self._lon

def test():

    slat1 = '12:34:56.78n'
    slon1 = '123:45:67.89w'

    slat2 = ' 123456780N'
    slon2 = '1234567890W'

    print Coordinate.convertFromString(slat1)
    print Coordinate.convertFromString(slon1)

if __name__ == "__main__":

    test()
    