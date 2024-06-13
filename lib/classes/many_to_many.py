from typing import List, Optional

class Band:
    all_bands = []
    
    def __init__(self, name: str, hometown: str):
        self.name = name
        self._hometown = hometown  # Make hometown immutable
        self._concerts: List['Concert'] = []  # To keep track of concerts for this band
        Band.all_bands.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise TypeError("Name must be of String type")

    @property
    def hometown(self) -> str:
        return self._hometown

    # Hometown should not have a setter to make it immutable

    def concerts(self) -> List['Concert']:
        return [concert for concert in Concert.all_concerts if concert.band == self]

    def venues(self) -> List['Venue']:
        return list(set([concert.venue for concert in self.concerts()]))

    def play_in_venue(self, venue: 'Venue', date: str) -> 'Concert':
        new_concert = Concert(date, self, venue)
        self._concerts.append(new_concert)
        venue.add_concert(new_concert)
        return new_concert

    def all_introductions(self) -> List[str]:
        return [concert.introduction() for concert in self.concerts()]


class Concert:
    all_concerts = []

    def __init__(self, date: str, band: 'Band', venue: 'Venue'):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all_concerts.append(self)

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise TypeError("Date must be a non-empty string")

    @property
    def venue(self) -> 'Venue':
        return self._venue

    @venue.setter
    def venue(self, value: 'Venue'):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise TypeError("venue should be of class Venue")

    @property
    def band(self) -> 'Band':
        return self._band

    @band.setter
    def band(self, value: 'Band'):
        if isinstance(value, Band):
            self._band = value
        else:
            raise TypeError("Band should be of class Band")

    def hometown_show(self) -> bool:
        return self.band.hometown == self.venue.city

    def introduction(self) -> str:
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all_venues = []

    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city
        self._concerts: List['Concert'] = []  # To keep track of concerts for this venue
        Venue.all_venues.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            print("Input non-empty strings only")

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            print("Input non-empty strings only")

    @classmethod
    def all(cls) -> List['Venue']:
        return cls.all_venues

    def concerts(self) -> List['Concert']:
        return [concert for concert in Concert.all_concerts if concert.venue == self]

    def bands(self) -> List['Band']:
        return list(set([concert.band for concert in self.concerts()]))

    def add_concert(self, concert: 'Concert'):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise TypeError("concert must be an instance of Concert")
