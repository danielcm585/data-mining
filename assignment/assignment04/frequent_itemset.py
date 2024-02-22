"""
Nama : Daniel Christian Mandolang
NPM  : 2106630006
"""

from typing import Set


def get_support(
    itemset: frozenset[str], 
    transactions: Set[frozenset[str]]
) -> float:

    support = 0
    for transaction in transactions:
        if itemset.issubset(transaction):
            support += 1
    support /= len(transactions)
    return support


def generate_frequent_itemset(
    transactions: Set[frozenset[str]], 
    min_support: float
) -> Set[frozenset[str]]:

    F = set()
    for transaction in transactions:
        for item in transaction:
            itemset = frozenset({item})
            support = get_support(itemset, transactions)
            if support >= min_support:
                F.add(itemset)

    result = F
    for k in range(2, len(F)+1):
        C = set()
        for itemset_1 in F:
            for itemset_2 in F:
                if itemset_1 == itemset_2: 
                    continue
                new_itemset = frozenset(itemset_1.union(itemset_2))
                support = get_support(new_itemset, transactions)
                if support >= min_support: 
                    C.add(new_itemset)
        F = C
        result = result.union(F)
    
    return set(sorted(result, key=len))


initial_itemsets = {
    frozenset({'laptop', 'mouse', 'keyboard', 'headphone'}), 
    frozenset({'laptop', 'mouse', 'keyboard'}), 
    frozenset({'mouse', 'keyboard', 'headphone'}), 
    frozenset({'laptop', 'keyboard', 'headphone'}),
    frozenset({'laptop', 'mouse', 'keyboard', 'webcam'}), 
}
print(generate_frequent_itemset(initial_itemsets, 0.6))
