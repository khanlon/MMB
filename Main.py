from EvaluatorBasic import EvaluatorBasic
import FanDuelScraper
import allocation
import logging

__author__ = 'Mike'

fan_duel_game_url = "https://www.fanduel.com/e/Game/12666"

fan_duel_players = FanDuelScraper.get_fan_duel_players(fan_duel_game_url)

evaluator = EvaluatorBasic()

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.info('Started logging')

for player in fan_duel_players:
 	score = evaluator.getPlayerValue(player)
 	print 'player: ', player.getName(), ' got a score of: ', score
   	player.setValue(score)

print'\n------ time to see who to use -------\n'
genetic_roster = allocation.genetic_list(fan_duel_players, budget = 35000, epochs=10, 
    num_children = 5, num_survivors = 3, num_remove = 2, rseed=10, logger=logger)
logger.info("Genetic roster: %s", genetic_roster)
logger.info("Genetic roster value: %s " , genetic_roster.get_value())