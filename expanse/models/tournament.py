class Tournament(object):
    """Tournament model to store tournament data in runtime"""

    def __init__(self, name, organizer, locale):
        self._name = name
        self._organizer = organizer
        self._locale = locale
        self._teams = []
        self._matches = []
        self._my_id = None

    def __str__(self):
        return (self._name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def organizer(self):
        return self._organizer

    @organizer.setter
    def organizer(self, value):
        self._organizer = value

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value

    @property
    def teams(self):
        return self._teams

    @teams.setter
    def teams(self, value):
        self._teams = value

    @property
    def matches(self):
        return self._matches

    @matches.setter
    def matches(self, value):
        self._matches = value

    @property
    def my_id(self):
        return self._my_id

    @my_id.setter
    def my_id(self, value):
        self._my_id = value