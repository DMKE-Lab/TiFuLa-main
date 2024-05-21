import numpy as np


def score1(rule, c=0):
    score = rule["rule_supp"] / (rule["body_supp"] + c)
    return score


def score2(cands_walks, test_query_ts, lmbda):
    max_cands_ts = max(cands_walks["timestamp_0"])
    score = np.exp(
        lmbda * (max_cands_ts - test_query_ts)
    )

    return score

def score_12(rule, cands_walks, test_query_ts, lmbda, a):
    score = (
            a * score1(rule) +
            b * membership_score +
            (1 - a - b) * score2(cands_walks, test_query_ts, lmbda)
    )
    return score
