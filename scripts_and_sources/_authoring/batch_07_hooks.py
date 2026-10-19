"""Hook-first re-orderings of Days 16-29 (test batch, 2026-10-19).

Why: on the first 15 posted Shorts, the two best performers opened with a plain-language beat right after the
hook ("Scientists call it an earworm... 89 percent"), while most weaker ones opened with "In <year>, <names> ..."
(a name/date dump). Here the plain-language FINDING moves to beat 2 and the attribution (year, names, design)
follows it. No fact is removed or added; sentences keep their citations. Days 1-15 are already posted and
Days 20, 22, 30-60 are untouched (control group)."""
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
for _n in ("batch_02", "batch_03"):
    _base.update(_load(_n).DAYS)

# day: (new scene order by ORIGINAL index, {original index: [new sentence texts]})
EDITS = {
 16: ([0, 2, 1, 3, 4], {2: ["In one survey, people of every age said time passes quickly."],
                        1: ["That was 2005: Marc Wittmann and Sandra Lehnhoff surveyed 499 people aged 14 to 94."]}),
 17: ([0, 2, 1, 3, 4], {2: ["In a fake emergency, people who believed they were alone with a person having a seizure helped about 85 percent of the time."],
                        1: ["That was a 1968 experiment by John Darley and Bibb Latané."]}),
 18: ([0, 3, 1, 2, 4], {3: ["In one big study, negative news videos produced stronger bodily reactions than positive ones, on average."]}),
 19: ([0, 3, 1, 2, 4], {3: ["Adding a clearly worse decoy could make people pick the option that beat it more often."],
                        1: ["In 1982, Huber, Payne and Puto studied these asymmetrically dominated options."]}),
 21: ([0, 2, 1, 3, 4], {2: [None, "The claim: mere repeated exposure, with nothing else added, enhances attitudes."],
                        1: ["In 1968, Robert Zajonc proposed this as the mere exposure effect."]}),
 23: ([0, 2, 1, 3, 4], {2: ["People who expected to have future access to information recalled the information itself less."],
                        1: ["That's from 2011, when Betsy Sparrow, Jenny Liu and Daniel Wegner published four studies in Science."]}),
 24: ([0, 3, 4, 1, 2], {3: ["In one study, students rated their own chances of good events as above average."]}),
 25: ([0, 2, 1, 3, 4], {2: ["Knowing the outcome made people judge it as more likely."],
                        1: ["That's from 1975, when Baruch Fischhoff studied what happens when people learn an outcome."]}),
 26: ([0, 2, 1, 3, 4], {2: ["Switching between tasks costs time, and the cost grows with the complexity of the task rules."],
                        1: ["In 2001, Joshua Rubinstein, David Meyer and Jeffrey Evans found this by studying people switching between tasks."]}),
 27: ([0, 4, 1, 2, 3], {4: ["In one experiment, identical cookies from a nearly empty jar were rated more desirable."]}),
 28: ([0, 3, 1, 2, 4], {3: ["In one experiment, people rated touch they produced themselves as less ticklish, less intense and less pleasant."],
                        4: ["A delay of up to 200 milliseconds between movement and touch made it feel progressively more ticklish."]}),
 29: ([0, 3, 4, 1, 2], {3: ["Students writing their honors theses made a best guess of 33.9 days, on average."],
                        4: ["They actually took 55.5 days on average."]}),
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
