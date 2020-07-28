from collections import defaultdict
from typing import Iterator, Union, Tuple


class FormalContext:
    def __init__(self, context: defaultdict(set)):
        self.context = context
        self.objects = set(context.keys())
        self.context_transposed = defaultdict(set)
        for k, v in context.items():
            self.context_transposed[frozenset()].add(k)
            for attr in v:
                self.context_transposed[attr].add(k)
        self.attributes = sorted(set(self.context_transposed.keys()).difference({frozenset()}))
        self.context[frozenset()] = set(self.attributes)
        self.concept = set(self._concept_generation())

    def add_unused_attributes(self, attrs):
        for attr in attrs:
            self.context_transposed[attr] = set()
            self.context[frozenset()].add(attr)
        self.attributes = sorted(set(self.context_transposed.keys()).difference({frozenset()}))
        self.concept = set(self._concept_generation())

    def _closure(self, some_set: set, obj_type: bool) -> Tuple[frozenset, frozenset]:
        if obj_type:
            set0, set1, dict0, dict1 = set(self.attributes), set(self.objects), self.context, self.context_transposed
        else:
            set0, set1, dict0, dict1 = set(self.objects), set(self.attributes), self.context_transposed, self.context
        for element in some_set.union(frozenset()):
            set0 = set0.intersection(dict0[element])
        for element in set0.union(frozenset()):
            set1 = set1.intersection(dict1[element])
        return frozenset(set0), frozenset(set1)

    def obj_closure(self, objects: set) -> Tuple[frozenset, frozenset]:
        return self._closure(objects, True)

    def attr_closure(self, attributes: set) -> Tuple[frozenset, frozenset]:
        return self._closure(attributes, False)

    def _next_closure(self, A: frozenset) -> Union[Tuple[frozenset, frozenset], None]:
        A = set(A)
        for i in range(len(self.attributes)-1, -1, -1):
            m = self.attributes[i]
            if m in A:
                A.remove(m)
            else:
                C, B = self.attr_closure(A.union({m}))
                if not B.difference(A).intersection(self.attributes[:i]):
                    return C, B
        return None

    def _concept_generation(self) -> Iterator[Tuple[frozenset, frozenset]]:
        # assume the number of objects is larger than the number of attributes
        A = self.attr_closure(set())
        while A is not None:
            yield A
            A = self._next_closure(A[1])


