from typing import List, Set
import math

def apk(actual: Set[str], predicted: List[str], k: int = 10) -> float:
    if k <= 0:
        return 0.0
    predicted = predicted[:k]
    if not actual:
        return 0.0
    score = 0.0
    hits = 0
    for i, p in enumerate(predicted, start=1):
        if p in actual:
            hits += 1
            score += hits / i
    return score / min(len(actual), k)

def mapk(actual_list: List[Set[str]], predicted_list: List[List[str]], k: int = 10) -> float:
    assert len(actual_list) == len(predicted_list)
    if not actual_list:
        return 0.0
    return sum(apk(a, p, k) for a, p in zip(actual_list, predicted_list)) / len(actual_list)

def ndcg_at_k(actual: Set[str], predicted: List[str], k: int = 10) -> float:
    predicted = predicted[:k]
    rels = [1 if p in actual else 0 for p in predicted]
    ideal_rels = sorted(rels, reverse=True)
    def _dcg(xs): return sum((x / math.log2(i+2)) for i, x in enumerate(xs))
    dcg = _dcg(rels)
    idcg = _dcg(ideal_rels)
    return (dcg / idcg) if idcg > 0 else 0.0
