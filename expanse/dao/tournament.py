from abc import ABCMeta, abstractmethod

from ..models.database import MongoDatabase
from .generic import GenericDAO


class TournamentDAO(GenericDAO):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_team(self, team, tournament):
        pass

class TournamentDAOMongo(TournamentDAO):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, tournament):
        tournament_to_insert = {
            "name": tournament.name,
            "teams": [],
            "organizer_id": tournament.organizer
        }
        self.db.tournaments.insert(tournament_to_insert)

    def remove(self, tournament):
        print("Not implemented yet")
        pass

    def update(self, querry, update):
        print("update", self.db.tournaments.update(querry, update))

    def add_team(self, team, tournament):
        # add new team to a tournamet
        # need to find the _id of the current tournament
        # insert team_id in the list of teams in db
        print("Not implented yet")
        pass

    def get(self, query):
        tournament = list(self.db.tournaments.find(query))
        return tournament

    def get_one(self, query):
        tournament =  self.db.tournaments.find_one(query)
        return tournament


    def list(self):
        return self.get({})
