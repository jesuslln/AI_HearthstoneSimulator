from abc import ABC, abstractmethod

## This class is an interface to guide bot implementations
class bot_agent(ABC):
    @abstractmethod
    def play_next_turn(self,game,player):
        pass