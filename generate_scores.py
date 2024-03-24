from collections import namedtuple
from ranking_model import Ranking

SC_RANKINGS = {"Rational": 1, "Sacrificing": 3, "Gracious": 2, "Cautious": 5, "Emotional": 4, "Competitive": 6, "Sympathetic": 7, "Uninhibited": 8, "Collaborative": 14, "Dutiful": 9, "Fair": 11, "Tactful": 13, "Tough": 12, "Dynamic": 15, "Steady": 10}

SI_RANKINGS = {"Rational": 1, "Sacrificing": 3, "Gracious": 2, "Cautious": 5, "Emotional": 4, "Competitive": 6, "Sympathetic": 7, "Uninhibited": 8, "Collaborative": 9, "Dutiful": 10, "Fair": 11, "Tactful": 12, "Tough": 13, "Dynamic": 14, "Steady": 15}

OP_RANKINGS = {"Rational": 1, "Sacrificing": 3, "Gracious": 2, "Cautious": 5, "Emotional": 4, "Competitive": 6, "Sympathetic": 7, "Uninhibited": 8, "Collaborative": 9, "Dutiful": 10, "Fair": 11, "Tactful": 12, "Tough": 14, "Dynamic": 13, "Steady": 15}

ADJECTIVES = [ "Rational", "Sacrificing", "Gracious", "Cautious", "Emotional", "Competitive", "Sympathetic", "Uninhibited", "Collaborative", "Dutiful", "Fair", "Tactful", "Tough", "Dynamic",
"Steady" ]

UBP = ["Sacrificing", "Cautious", "Dutiful", "Tactful", "Steady"]

#Ranking = namedtuple('Ranking', ['sc', 'si', 'op'])

def create_rankings(sc_rankings: dict, si_rankings: dict, op_rankings: dict) -> Ranking:
    return Ranking(sc = sc_rankings, si = si_rankings , op = op_rankings)

rankings = create_rankings(SC_RANKINGS, SI_RANKINGS , OP_RANKINGS)
print(rankings)

def universe_sums(rankings: Ranking, universe_adjectives: [str]) -> [int]:
    sc_score, si_score, op_score = 0, 0, 0
    for adjective in universe_adjectives:
        sc_score += rankings.sc[adjective]
        si_score += rankings.si[adjective]
        op_score += rankings.op[adjective]
    return [sc_score, si_score, op_score]

def universe_scores(rankings: Ranking, universe_adjectives: [str]) -> [int]:
    return [65 - val for val in universe_sums(rankings, universe_adjectives)]

def ubp_scores(rankings: Ranking, ubp_adjectives: [str]) -> [int]:
    return universe_scores(rankings, ubp_adjectives)

def global_scores(rankings: Ranking, adjectives: str = ADJECTIVES) -> dict:
    sc_si_score, sc_op_score, si_op_score = 0, 0, 0 
    for adjective in adjectives:
        sc_si_score += abs(rankings.sc[adjective] - rankings.si[adjective])
        sc_op_score += abs(rankings.sc[adjective] - rankings.op[adjective])
        si_op_score += abs(rankings.si[adjective] - rankings.op[adjective])
    return {"sc-si": sc_si_score, "sc-op": sc_op_score, "si-op": si_op_score}
