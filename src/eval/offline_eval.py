import argparse
from .metrics import mapk, ndcg_at_k

def demo_eval():
    actual_list = [set(['t1','t3','t5']), set(['a','b'])]
    predicted_list = [['t1','t2','t3','t4','t5'], ['b','c','a']]
    print('MAP@3 =', mapk(actual_list, predicted_list, k=3))
    print('NDCG@3 (user1) =', ndcg_at_k(actual_list[0], predicted_list[0], k=3))
    print('NDCG@3 (user2) =', ndcg_at_k(actual_list[1], predicted_list[1], k=3))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--demo', action='store_true')
    args = parser.parse_args()
    if args.demo:
        demo_eval()
    else:
        print('Use --demo for a quick test; full offline eval coming next.')
