"""Hook-first re-orderings of Days 38-60 (2026-11-03), same method as batch_07_hooks.py.
The plain-language FINDING moves to beat 2; year/names follow. No fact removed or added; citations unchanged.
Day 59 keeps its script (its key finding names brain regions, so it is not reordered)."""
import copy
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SOURCES = {}
_base = {}
for _n in ("batch_04", "batch_05", "batch_06"):
    _base.update(_load(_n).DAYS)

EDITS = {
 38: ([0, 2, 1, 3], {2: ["One sociologist defines gaslighting as a type of psychological abuse aimed at making victims seem or feel crazy."],
                     1: ["That's from Paige Sweet's 2019 study, The Sociology of Gaslighting."]}),
 39: ([0, 2, 1, 3], {2: ["In five experiments, the idea that a hard-to-get woman is more desirable failed every time."],
                     1: ["That's from 1973, when Elaine Walster and colleagues tested it."]}),
 40: ([0, 5, 1, 2, 3, 4], {5: ["A very impressive contestant became more attractive after a clumsy blunder."]}),
 41: ([0, 3, 1, 2, 4], {3: ["In a hotel study, a card saying most guests reuse their towels worked better than the standard environmental message."]}),
 42: ([0, 4, 1, 2, 3, 5], {4: ["About half of people agreed to a small request after refusing a large one."]}),
 43: ([0, 4, 1, 2, 3, 5], {4: ["People's snap judgments of faces after 100 milliseconds correlated with judgments made with no time limit."]}),
 44: ([0, 2, 1, 3], {2: ["In a famous classroom study, the students teachers expected to bloom had actually been chosen at random."]}),
 45: ([0, 3, 1, 2, 4], {3: ["In one brain study, teens were more likely to like photos that already had many likes."]}),
 46: ([0, 3, 1, 2, 4, 5], {3: ["In a love quiz, fifty-six percent of respondents chose the secure description."],
                          2: ["They ran the love quiz in a newspaper."]}),
 47: ([0, 2, 1, 3], {2: ["One model says commitment depends on satisfaction, the quality of alternatives and the size of investments."],
                     1: ["That's the investment model Caryl Rusbult proposed in 1980."]}),
 48: ([0, 4, 1, 2, 3, 5], {4: ["In one experiment, people who got a favor bought more raffle tickets than those who did not."]}),
 49: ([0, 5, 1, 2, 3, 4], {5: ["In one study, readers still saw an attitude in an essay writer even when told the position had been assigned."]}),
 50: ([0, 3, 1, 2, 4], {3: ["In one big analysis, perceived similarity predicted attraction more strongly than actual similarity did."]}),
 51: ([0, 2, 1, 3], {2: ["About a third of people noticed their own name in an ear they were ignoring."]}),
 52: ([0, 3, 1, 2, 4], {3: ["Groupthink, one psychologist argued, kept contradictory views from being expressed and evaluated."]}),
 53: ([0, 3, 1, 2, 4], {3: ["One famous simulated-prison study was planned for two weeks but ended after six days."]}),
 54: ([0, 4, 3, 5, 1, 2], {4: ["One study of everyday talk found gossip was mostly neutral, not negative."]}),
 55: ([0, 5, 6, 1, 2, 3, 4], {5: ["In one experiment, about half of the liars thought they had been caught."],
                              3: ["The liars were Cornell students."]}),
 56: ([0, 2, 3, 1, 4], {2: ["One study reported that parental overvaluation predicted narcissism in children."]}),
 57: ([0, 6, 1, 2, 3, 4, 5], {6: ["In two studies, training improved how charismatic and effective leaders were rated."]}),
 58: ([0, 4, 1, 2, 3, 5], {4: ["In a famous line experiment, about three quarters of people conformed to the group at least once."]}),
 60: ([0, 2, 1, 3], {2: ["Trauma bonding theory describes emotional attachments that develop in relationships of intermittent abuse."]}),
}

DAYS = {}
for _d, (_order, _over) in EDITS.items():
    _day = copy.deepcopy(_base[_d])
    _orig = _day["scenes"]
    _new = []
    for _i in _order:
        sec, sents, txt, vis, spec = _orig[_i]
        if _i in _over:
            sents = [(new if new is not None else old[0], old[1]) for new, old in zip(_over[_i], sents)] + list(sents[len(_over[_i]):])
        _new.append((sec, sents, txt, vis, spec))
    _new += [s for k, s in enumerate(_orig) if k not in _order]
    _day["scenes"] = _new
    DAYS[_d] = _day
