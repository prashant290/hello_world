"""Days 21-30 (Month 1)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common_sources import S, SEC, SECOND

SOURCES = {
 "zajonc1968": S("Zajonc, R. B.", 1968, "Attitudinal effects of mere exposure", "Journal of Personality and Social Psychology, 9(2, Pt.2), 1-27", "https://www.psy.lmu.de/allg2/download/audriemmo/ws1011/mere_exposure_effect.pdf", SEC + " (abstract: four types of evidence)"),
 "montoya2017": S("Montoya, R. M., Horton, R. S., Vevea, J. L., Citkowicz, M., & Lauber, E. A.", 2017, "A re-examination of the mere exposure effect: The influence of repeated exposure on recognition, familiarity, and liking", "Psychological Bulletin, 143(5), 459-498", "https://par.nsf.gov/servlets/purl/10198302", SEC + " (268 curve estimates from 81 articles; inverted-U)"),
 "brown2003": S("Brown, A. S.", 2003, "A review of the déjà vu experience", "Psychological Bulletin, 129(3), 394-413", "https://www.ovid.com/journals/plbul/fulltext/00006823-200305000-00004~a-review-of-the-dj-vu-experience", SEC + " (about 60% report it; four explanation categories)"),
 "cleary2012": S("Cleary, A. M., Brown, A. S., Sawyer, B. D., Nomi, J. S., Ajoku, A. C., & Ryals, A. J.", 2012, "Familiarity from the configuration of objects in 3-dimensional space and its relation to déjà vu: A virtual reality investigation", "Consciousness and Cognition, 21(2), 969-975", "https://newsmediarelations.colostate.edu/2012/05/23/spatial-configuration-can-spark-deja-vu-colorado-state-university-psychology-study-reveals/", SEC + " (press release + citation; study design confirmed)"),
 "sparrow2011": S("Sparrow, B., Liu, J., & Wegner, D. M.", 2011, "Google effects on memory: Cognitive consequences of having information at our fingertips", "Science, 333(6043), 776-778", "https://stafforini.com/works/sparrow-2011-google-effects-memory/", SEC + " (four studies; abstract quoted)"),
 "hesselmann2020": S("Hesselmann, G.", 2020, "No conclusive evidence that difficult general knowledge questions cause a 'Google Stroop effect': A replication study", "PeerJ, 8, e10325", "https://peerj.com/articles/10325", SEC + " (also reports two earlier failed replication attempts)"),
 "weinstein1980": S("Weinstein, N. D.", 1980, "Unrealistic optimism about future life events", "Journal of Personality and Social Psychology, 39(5), 806-820", "https://scinapse.io/papers/2145046219", SEC + " (258 students; 42 events)"),
 "anderson2013": S("Anderson, K. B.", 2013, "Consumer fraud in the United States, 2011: The third FTC survey", "U.S. Federal Trade Commission staff report", "https://www.ftc.gov/reports/consumer-fraud-united-states-2011-third-ftc-survey", SEC + " (10.8% of adults; about 25.6 million people)"),
 "fischhoff1975": S("Fischhoff, B.", 1975, "Hindsight is not equal to foresight: The effect of outcome knowledge on judgment under uncertainty", "Journal of Experimental Psychology: Human Perception and Performance, 1(3), 288-299", "https://forrt.org/flora-replication-atlas/doi/10.1037/0096-1523.1.3.288/", SEC + " (abstract quoted)"),
 "roese2012": S("Roese, N. J., & Vohs, K. D.", 2012, "Hindsight bias", "Perspectives on Psychological Science, 7(5), 411-426", "https://www.psychologicalscience.org/news/releases/i-knew-it-all-along-didnt-i-understanding-hindsight-bias.html", SEC + " (three levels of hindsight bias)"),
 "rubinstein2001": S("Rubinstein, J. S., Meyer, D. E., & Evans, J. E.", 2001, "Executive control of cognitive processes in task switching", "Journal of Experimental Psychology: Human Perception and Performance, 27(4), 763-797", "https://www.newswise.com/articles/is-multitasking-more-efficient", SEC + " (abstract-level: switching costs increased with rule complexity)"),
 "ophir2009": S("Ophir, E., Nass, C., & Wagner, A. D.", 2009, "Cognitive control in media multitaskers", "Proceedings of the National Academy of Sciences, 106(37), 15583-15587", "https://pubmed.ncbi.nlm.nih.gov/19706386", SEC),
 "wiradhany2017": S("Wiradhany, W., & Nieuwenstein, M. R.", 2017, "Cognitive control in media multitaskers: Two replication studies and a meta-analysis", "Attention, Perception, & Psychophysics, 79", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5662702", SEC + " (found higher switching costs in heavy media multitaskers; notes later studies did not all show the distractibility link)"),
 "watson2010": S("Watson, J. M., & Strayer, D. L.", 2010, "Supertaskers: Profiles in extraordinary multitasking ability", "Psychonomic Bulletin & Review, 17(4), 479-485", "https://www.sciencedaily.com/releases/2010/03/100329075911.htm", SEC + " (200 students; about 2.5% showed no decline)"),
 "worchel1975": S("Worchel, S., Lee, J., & Adewole, A.", 1975, "Effects of supply and demand on ratings of object value", "Journal of Personality and Social Psychology, 32(5), 906-914", "https://stafforini.com/works/worchel-1975-effects-supply-demand/", SEC + " (200 female undergraduates; cookie jars)"),
 "blakemore1998": S("Blakemore, S.-J., Wolpert, D. M., & Frith, C. D.", 1998, "Central cancellation of self-produced tickle sensation", "Nature Neuroscience, 1(7), 635-640", "https://link.springer.com/article/10.1038/2870", SEC + " (ratings; 0-200 ms delay; cerebellum activity)"),
 "buehler1994": S("Buehler, R., Griffin, D., & Ross, M.", 1994, "Exploring the planning fallacy: Why people underestimate their task completion times", "Journal of Personality and Social Psychology, 67(3), 366-381", "https://bear.warrington.ufl.edu/brenner/mar7588/Papers/buehler-et-al-1994.pdf", SECOND + " (37 students; 33.9 vs 55.5 days; two search results agree)"),
 "kahneman1993": S("Kahneman, D., Fredrickson, B. L., Schreiber, C. A., & Redelmeier, D. A.", 1993, "When more pain is preferred to less: Adding a better end", "Psychological Science, 4(6), 401-405", "https://ius.uzh.ch/dam/jcr:5ae9adc9-61ec-4174-b37c-4b752f36c23b/Kahnemann%20et%20al.%20-%20When%20More%20Pain%20is%20Preferred%20to%20Less%20(1993).pdf", SEC + " (60 s at 14 C vs 60 s plus 30 s at 15 C; about 70% chose to repeat the longer trial)"),
 "redelmeier2003": S("Redelmeier, D. A., Katz, J., & Kahneman, D.", 2003, "Memories of colonoscopy: A randomized trial", "Pain, 104(1-2), 187-194", "https://pubmed.ncbi.nlm.nih.gov/12855328/", SEC + " (n = 682)"),
}

DAYS = {}

DAYS[21] = dict(
 title="Why You Like What You've Seen a Lot",
 description_core="Does seeing something again and again make you like it more? Zajonc proposed the mere exposure effect in 1968, and a 2017 meta-analysis found liking rises with exposure and then levels off and declines.",
 primary=["zajonc1968", "montoya2017"],
 hashtags=["#psychology", "#shorts", "#mereexposure", "#familiarity", "#liking", "#psychologyfacts"],
 caveats="Montoya et al. (2017) is a meta-analysis of 81 articles; shapes vary by stimulus and number of exposures. The video does not claim familiarity makes things objectively better.",
 thumb=(["WHY YOU LIKE", "WHAT'S FAMILIAR"], 1, 0),
 scenes=[
  ("H", [("Why do you like what you've seen a lot?", "PLAN")], "Why like the familiar?", "Same shape repeating around a stickman.", "think/smile/C; crowd:5@R"),
  ("E", [("In 1968, Robert Zajonc proposed the mere exposure effect.", "zajonc1968")], "The mere exposure effect, 1968", "Title card MERE EXPOSURE.", "point/neutral/L; text:MERE EXPOSURE@R"),
  ("E", [("Repeated exposure to something can make you like it more.", "zajonc1968"), ("Zajonc's claim was that mere repeated exposure, with nothing else added, enhances attitudes.", "zajonc1968")], "Repeat exposure = more liking", "Heart growing.", "stand/smile/L; text:SEEN IT AGAIN@R"),
  ("E", [("His 1968 paper described four kinds of evidence, from word frequency to controlled exposure experiments.", "zajonc1968")], "Four kinds of evidence", "Four labeled boxes.", "think/neutral/L; list:WORDS,SYMBOLS,ATTITUDES,TESTS@R"),
  ("E", [("In 2017, Matthew Montoya and colleagues analyzed 268 curve estimates from 81 articles.", "montoya2017")], "2017: 268 curves, 81 articles", "Stack of papers.", "stand/neutral/L; text:81 ARTICLES@R"),
  ("E", [("Liking rose with repeated exposure, then leveled off and declined.", "montoya2017")], "Rise, then decline", "Inverted-U curve.", "point/neutral/L; lines:liking,exposure,hill@R"),
  ("E", [("So more exposure helps up to a point; overexposure can backfire.", "montoya2017")], "Overexposure can backfire", "Curve peaking and falling.", "stand/worry/L; arrow:down@R"),
  ("E", [("Their meta-analysis covered effects on liking, familiarity and recognition.", "montoya2017")], "Liking, familiarity, recognition", "Three labels.", "stand/neutral/L; list:LIKING,FAMILIAR,RECOGNIZE@R"),
  ("T", [("So familiarity can make something feel better, but don't mistake 'I've seen it a lot' for 'it's good'.", "zajonc1968")], "Seen a lot is not good", "Stickman separating two labels.", "point/smile/L; text:SEEN <> GOOD@R"),
  ("C", [("Tomorrow: why do you get déjà vu?", "PLAN")], "Tomorrow: déjà vu", "Repeated scene.", "stand/neutral/L; text:DEJA VU@R"),
 ])

DAYS[22] = dict(
 title="What Actually Causes Déjà Vu?",
 description_core="Why does a new place feel strangely familiar? About 60% of people have had déjà vu, researchers have several competing explanations, and a virtual-reality study supports a scene-layout idea.",
 primary=["brown2003", "cleary2012"],
 hashtags=["#psychology", "#shorts", "#dejavu", "#memory", "#brain", "#psychologyfacts"],
 caveats="UNSETTLED. Brown (2003) organizes explanations into four categories; none is established as the single cause. Cleary et al. (2012) is one lab study in virtual reality supporting one idea (Gestalt familiarity). The video states this as 'may'.",
 thumb=(["WHAT CAUSES", "DEJA VU?"], 1, 0),
 scenes=[
  ("H", [("Why does a new place feel strangely familiar?", "PLAN")], "Why does it feel familiar?", "Stickman in a new room, thought bubble 'I've been here?'.", "think/worry/C; bubble:been here?@TR"),
  ("E", [("Déjà vu is common: about 60 percent of people have experienced it.", "brown2003")], "About 60% have had it", "Big 60%.", "stand/neutral/L; text:~60%@R"),
  ("E", [("In 2003, Alan Brown reviewed the research in Psychological Bulletin.", "brown2003")], "2003 research review", "Stack of papers.", "point/neutral/L; text:2003@TR"),
  ("E", [("He found explanations fall into four groups: dual processing, neurological, memory and attentional.", "brown2003")], "Four groups of explanations", "Four labeled boxes.", "stand/neutral/L; list:DUAL,NEURO,MEMORY,ATTENTION@R"),
  ("E", [("That means researchers still have several competing explanations.", "brown2003")], "Several competing explanations", "Scale with questions.", "shrug/neutral/L; qmark@R"),
  ("E", [("One memory-based idea is that a scene resembles one you've seen before, but you can't recall it.", "cleary2012")], "One idea: forgotten similar scene", "Two similar rooms, one faded.", "think/neutral/L; list:ROOM A,ROOM B@R"),
  ("E", [("In 2012, Anne Cleary's team tested it in virtual reality.", "cleary2012")], "2012: virtual reality test", "VR headset.", "stand/neutral/L; text:VR@R"),
  ("E", [("Scenes with the same layout as an earlier scene felt more familiar when people couldn't recall that earlier scene.", "cleary2012")], "Same layout = more familiar", "Two rooms with the same layout.", "point/smile/L; list:SAME LAYOUT@R"),
  ("E", [("They also reported more déjà vu.", "cleary2012")], "More déjà vu reported", "Rising bar.", "shock/neutral/L; bars:novel=h30,same layout=h65@R"),
  ("T", [("So déjà vu may be a familiarity signal firing without a memory to go with it.", "cleary2012")], "Familiarity without the memory", "Signal bulb with no memory bubble.", "think/smile/L; lightbulb@R"),
  ("C", [("Tomorrow: do search engines change how you remember?", "PLAN")], "Tomorrow: Google and memory", "Search box.", "stand/neutral/L; text:SEARCH@R"),
 ])

DAYS[23] = dict(
 title="Is Google Hurting Your Memory? What Held Up",
 description_core="Does Google make you forget? A 2011 study found people recalled information less when they expected to find it later, but its 'Google Stroop' claim failed replication attempts.",
 primary=["sparrow2011", "hesselmann2020"],
 hashtags=["#psychology", "#shorts", "#googleeffect", "#memory", "#technology", "#psychologyfacts"],
 caveats="MIXED REPLICATION. The replications cited (Hesselmann 2020, plus two earlier attempts he reports) tested the computer-priming ('Google Stroop') claim, not the 'recall where to find it' finding; we do not know from these sources whether the latter replicated. The video avoids claiming search engines harm memory.",
 thumb=(["DOES GOOGLE", "ERASE MEMORY?"], 1, 0),
 scenes=[
  ("H", [("Does Google make you forget things?", "PLAN")], "Does Google make you forget?", "Stickman beside a search box.", "think/worry/C; text:SEARCH@R"),
  ("E", [("In 2011, Betsy Sparrow, Jenny Liu and Daniel Wegner published four studies in Science.", "sparrow2011")], "2011: four studies in Science", "Journal cover.", "stand/neutral/L; text:SCIENCE 2011@R"),
  ("E", [("When people expected to have future access to information, they recalled the information itself less.", "sparrow2011")], "Expect access: recall less", "Bar low.", "stand/neutral/L; bars:no access=h70,expect access=h40@R"),
  ("E", [("They did better at remembering where to find the information.", "sparrow2011")], "Better at 'where to find it'", "Folder icon with a pin.", "point/smile/L; text:WHERE@R"),
  ("E", [("Another claim was that hard trivia questions prime people to think about computers.", "sparrow2011")], "Claim: hard questions prime 'computer'", "Question mark next to a computer.", "think/neutral/L; qmark@R"),
  ("E", [("In 2020, Guido Hesselmann found no conclusive evidence for it in a replication study.", "hesselmann2020")], "2020 replication: no clear evidence", "Cross on a claim card.", "shrug/neutral/L; cross@R"),
  ("E", [("He noted that two earlier replication attempts had failed too.", "hesselmann2020")], "Two earlier attempts failed", "Two crosses.", "stand/neutral/L; list:TRY 1,TRY 2@R; cross@TR"),
  ("E", [("Those replications tested the computer-priming claim, not the memory-for-location one.", "hesselmann2020")], "They tested one claim only", "Two claim cards; one tested.", "point/neutral/L; list:PRIMING,LOCATION@R"),
  ("T", [("So 'we remember where information is' fits the study, but 'Google rots your brain' goes beyond the evidence.", "sparrow2011")], "'Google rots your brain' overreaches", "Stickman pushing back a headline.", "stand/smile/L; text:OVERREACH@R"),
  ("C", [("Tomorrow: why do you think you'd never fall for a scam?", "PLAN")], "Tomorrow: scams", "Warning sign.", "stand/worry/L; text:SCAM?@R"),
 ])

DAYS[24] = dict(
 title="Why You Think You'd Never Fall for a Scam",
 description_core="Why do so many people think they'd never be fooled? Research on unrealistic optimism shows people rate their own odds of bad events as below average, while an FTC survey estimated 10.8% of U.S. adults were fraud victims in 2011.",
 primary=["weinstein1980", "anderson2013"],
 hashtags=["#psychology", "#shorts", "#scams", "#optimismbias", "#fraud", "#psychologyfacts"],
 caveats="Weinstein (1980) studied college students' beliefs about 42 life events, not scams specifically. The FTC survey counts specific frauds it asked about in 2011 and relies on self-report. The video does not claim scam victims are less intelligent or that optimism causes fraud.",
 thumb=(["I'D NEVER", "FALL FOR", "A SCAM"], 2, 0),
 scenes=[
  ("H", [("Why do you think you'd never fall for a scam?", "PLAN")], "'I'd never fall for it'", "Confident stickman next to a scam email.", "stand/smile/C; text:SCAM?@R"),
  ("E", [("In 1980, Neil Weinstein asked 258 college students about 42 life events.", "weinstein1980")], "1980: 258 students, 42 events", "List of events.", "point/neutral/L; text:42 EVENTS@R"),
  ("E", [("They compared their own chances with those of their classmates.", "weinstein1980")], "Own chances vs classmates'", "Two stickmen compared.", "stand/neutral/L; crowd:1@R"),
  ("E", [("Students rated their own chances of good events as above average.", "weinstein1980")], "Good events: above average", "Bar high.", "stand/smile/L; bars:average=h50,mine=h72@R"),
  ("E", [("And their chances of bad events as below average.", "weinstein1980")], "Bad events: below average", "Bar low.", "stand/smile/L; bars:average=h50,mine=h28@R"),
  ("E", [("That's called unrealistic optimism: we can't all be better than average.", "weinstein1980")], "Unrealistic optimism", "Everyone above the line.", "shrug/smile/L; text:ALL ABOVE AVG?@R"),
  ("E", [("A 2013 Federal Trade Commission survey estimated that 10.8 percent of U.S. adults were victims of fraud in 2011.", "anderson2013")], "FTC survey: 10.8% victims", "Big 10.8%.", "stand/worry/L; text:10.8%@R"),
  ("E", [("That's about 25.6 million people.", "anderson2013")], "About 25.6 million people", "Crowd icon with number.", "shock/neutral/L; crowd:5@R; text:25.6M@TR"),
  ("E", [("The survey covered the specific frauds it asked about, not every possible scam.", "anderson2013")], "Only frauds the survey asked about", "Checklist of fraud types.", "think/neutral/L; list:FRAUD 1,FRAUD 2@R"),
  ("T", [("So 'it won't happen to me' feels certain, but the numbers show it happens to many people.", "weinstein1980,anderson2013")], "It happens to many people", "Stickman pausing before clicking.", "point/smile/L; qmark@R"),
  ("C", [("Tomorrow: why do you say 'I knew it all along'?", "PLAN")], "Tomorrow: 'I knew it all along'", "Speech bubble.", "stand/smile/L; bubble:knew it@R"),
 ])

DAYS[25] = dict(
 title="'I Knew It All Along': The Hindsight Trap",
 description_core="Do you really know it all along? Fischhoff's 1975 experiments showed that learning an outcome makes it seem more likely, and people overestimate what they knew beforehand.",
 primary=["fischhoff1975", "roese2012"],
 hashtags=["#psychology", "#shorts", "#hindsightbias", "#cognitivebias", "#memory", "#psychologyfacts"],
 caveats="Fischhoff's 1975 findings are from lab judgment tasks; Roese & Vohs (2012) review the broader literature and propose three levels of hindsight bias. The video's takeaway about checking written predictions is an application of the memory-distortion level, not a tested intervention.",
 thumb=(["I KNEW IT", "ALL ALONG?"], 1, 0),
 scenes=[
  ("H", [("Do you ever say, 'I knew it all along'?", "PLAN")], "'I knew it all along'", "Smug stickman after the fact.", "stand/smile/C; bubble:knew it@R"),
  ("E", [("In 1975, Baruch Fischhoff studied what happens when people learn an outcome.", "fischhoff1975")], "1975: learning the outcome", "Outcome card revealed.", "point/neutral/L; text:1975@TR; text:OUTCOME@R"),
  ("E", [("Knowing the outcome made them judge it as more likely.", "fischhoff1975")], "Outcome seems more likely", "Probability bar rising.", "stand/neutral/L; bars:before=h35,after=h65@R"),
  ("E", [("People were largely unaware of this effect.", "fischhoff1975")], "Largely unaware", "Eye with a blind spot.", "shrug/neutral/L; qmark@R"),
  ("E", [("So they overestimated what they would have known without the outcome.", "fischhoff1975")], "Overestimated what they'd have known", "Bars: actual low, guessed high.", "think/neutral/L; bars:would have known=h35,guessed=h65@R"),
  ("E", [("They also overestimated what others actually knew beforehand.", "fischhoff1975")], "Also overestimated others", "Crowd with thought bubbles.", "stand/neutral/L; crowd:4@R"),
  ("E", [("In 2012, Neal Roese and Kathleen Vohs reviewed the research.", "roese2012")], "2012 review", "Stack of papers.", "stand/neutral/L; text:2012@TR"),
  ("E", [("Roese and Vohs say it is the first overview to draw on research across disciplines.", "roese2012")], "First cross-discipline overview", "Several discipline icons.", "point/neutral/L; list:PSYCH,LAW,MED@R"),
  ("E", [("They proposed three levels of hindsight bias, from memory distortion to higher-level belief.", "roese2012")], "Three levels of hindsight bias", "Three stacked boxes.", "stand/neutral/L; list:MEMORY,INFERENCE,BELIEF@R"),
  ("E", [("The first is misremembering what you predicted.", "roese2012")], "Level 1: misremembering your prediction", "Fading note.", "think/worry/L; bubble:I said...@TR"),
  ("T", [("So when you feel 'I knew it', check whether you wrote down what you actually predicted.", "roese2012")], "Check what you actually wrote", "Stickman checking a note.", "point/smile/L; list:NOTE@R; check@TR"),
  ("C", [("Tomorrow: what does multitasking really cost you?", "PLAN")], "Tomorrow: multitasking", "Stickman juggling.", "stand/worry/L; text:MULTITASK@R"),
 ])

DAYS[26] = dict(
 title="What Multitasking Really Costs Your Brain",
 description_core="Can you really do two things at once? Switching between tasks has measurable costs, and while a small minority of 'supertaskers' show no decline, most people do.",
 primary=["rubinstein2001", "watson2010"],
 hashtags=["#psychology", "#shorts", "#multitasking", "#focus", "#productivity", "#psychologyfacts"],
 caveats="MIXED. Ophir et al. (2009) heavy-media-multitasker findings were not consistently replicated; Wiradhany & Nieuwenstein (2017) did find higher switching costs. The video claims only task-switching costs and the 2.5% supertasker result, which came from 200 students in a driving-simulator study.",
 thumb=(["WHAT MULTITASKING", "REALLY COSTS"], 1, 0),
 scenes=[
  ("H", [("Can you really do two things at once?", "PLAN")], "Two things at once?", "Stickman juggling two tasks.", "shock/worry/C; list:A,B@R"),
  ("E", [("In 2001, Joshua Rubinstein, David Meyer and Jeffrey Evans studied people switching between tasks.", "rubinstein2001")], "2001: task switching", "Arrows swapping A and B.", "stand/neutral/L; text:2001@TR; list:A,B@R"),
  ("E", [("Switching cost time, and the cost grew with the complexity of the task rules.", "rubinstein2001")], "Switching costs time", "Clock with rising bar.", "think/neutral/L; clock@R"),
  ("E", [("In 2009, Eyal Ophir, Clifford Nass and Anthony Wagner reported that heavy media multitaskers were more distracted by irrelevant information.", "ophir2009")], "2009: heavy multitaskers distracted", "Distraction bubbles.", "shock/neutral/L; bubble:ping!@TR"),
  ("E", [("But later studies didn't all find that link.", "wiradhany2017")], "Later studies: mixed", "Mixed check and cross.", "shrug/neutral/L; check@R; cross@TR"),
  ("E", [("A 2017 replication did find higher task-switching costs in heavy media multitaskers.", "wiradhany2017")], "2017: higher switching costs", "Higher bar.", "stand/neutral/L; bars:light=h35,heavy=h65@R"),
  ("E", [("And a 2010 study of 200 students found about 2.5 percent, the 'supertaskers', showed no decline when driving and doing a memory task together.", "watson2010")], "2010: 2.5% 'supertaskers'", "Single gold star among many.", "stand/smile/L; text:2.5%@R"),
  ("E", [("For most other people, performance dropped when they did both.", "watson2010")], "Most others declined", "Falling bar.", "stand/worry/L; arrow:down@R"),
  ("T", [("So most of us pay a cost when we switch tasks, even if a few people don't.", "rubinstein2001,watson2010")], "Switching isn't free", "Price tag on a switch.", "point/smile/L; tag:SWITCH@R"),
  ("C", [("Tomorrow: why does scarcity make things look more valuable?", "PLAN")], "Tomorrow: scarcity", "Nearly empty jar.", "stand/neutral/L; text:2 LEFT@R"),
 ])

DAYS[27] = dict(
 title="Does Scarcity Make Things Look Better?",
 description_core="Does scarcity make things look better? In a 1975 experiment, identical cookies from a nearly empty jar were rated as more desirable.",
 primary=["worchel1975"],
 hashtags=["#psychology", "#shorts", "#scarcity", "#marketing", "#persuasion", "#psychologyfacts"],
 caveats="One classic lab experiment with 200 female undergraduates and one product (cookies); real shopping may differ. The study did not test 'only 2 left' messages in stores.",
 thumb=(["DOES SCARCITY", "WORK?"], 1, 0),
 scenes=[
  ("H", [("Does 'almost gone' make things look better?", "PLAN")], "'Almost gone' = better?", "Stickman eyeing a nearly empty jar.", "think/neutral/C; text:2 LEFT@R"),
  ("E", [("In 1975, Stephen Worchel, Jerry Lee and Akanbi Adewole tested how supply affects value.", "worchel1975")], "1975: supply and value", "Jar icons.", "point/neutral/L; text:1975@TR; text:SUPPLY@R"),
  ("E", [("A total of 200 female undergraduates rated cookies.", "worchel1975")], "200 undergraduates rated cookies", "Cookie.", "stand/neutral/L; text:200@R"),
  ("E", [("One glass jar held ten cookies, another held just two.", "worchel1975")], "Ten cookies vs two", "Two jars.", "point/neutral/L; list:10,2@R"),
  ("E", [("The cookies were identical, but the ones from the nearly empty jar were rated more desirable.", "worchel1975")], "Scarce cookies rated higher", "Bars: ten low, two high.", "stand/smile/L; bars:ten cookies=h40,two cookies=h72@R"),
  ("E", [("Cookies were also rated more valuable when their supply changed from abundant to scarce.", "worchel1975")], "Abundant to scarce = even more", "Jar emptying.", "think/neutral/L; arrow:down@R"),
  ("E", [("And cookies that were scarce because of high demand were rated higher than cookies scarce because of an accident.", "worchel1975")], "Scarce from demand rated higher", "Crowd taking cookies vs spilled jar.", "stand/neutral/L; crowd:3@R"),
  ("E", [("It tested one product with one group, so shoppers in real stores may behave differently.", "worchel1975")], "One product, one group", "Single cookie.", "shrug/neutral/L; text:1 PRODUCT@R"),
  ("T", [("So when you see 'only two left', ask whether you want the item or just the scarcity.", "worchel1975")], "The item, or the scarcity?", "Stickman holding two options.", "point/smile/L; qmark@R"),
  ("C", [("Tomorrow: why can't you tickle yourself?", "PLAN")], "Tomorrow: tickling", "Feather.", "stand/smile/L; text:TICKLE@R"),
 ])

DAYS[28] = dict(
 title="Why You Can't Tickle Yourself",
 description_core="Why can't you tickle yourself? A 1998 experiment found self-produced touch felt less ticklish than the same touch from a robot, and the brain appears to predict the sensory result of your own movements.",
 primary=["blakemore1998"],
 hashtags=["#psychology", "#shorts", "#neuroscience", "#brain", "#tickle", "#psychologyfacts"],
 caveats="Blakemore et al. (1998) used a robot-controlled touch task with small samples in a lab; 'the cerebellum is involved in predicting' is the authors' interpretation. The video describes tendencies from this study only.",
 thumb=(["WHY CAN'T YOU", "TICKLE YOURSELF?"], 1, 0),
 scenes=[
  ("H", [("Why can't you tickle yourself?", "PLAN")], "Can't tickle yourself?", "Stickman with a feather, unimpressed.", "shrug/neutral/C; text:TICKLE@R"),
  ("E", [("In 1998, Sarah-Jayne Blakemore, Daniel Wolpert and Chris Frith studied exactly that.", "blakemore1998")], "1998: Blakemore, Wolpert, Frith", "Title card TICKLE STUDY.", "point/neutral/L; text:1998@TR; text:TICKLE STUDY@R"),
  ("E", [("A robot touched people's palm, or they moved a robot arm to produce the touch themselves.", "blakemore1998")], "Robot touch vs self-produced", "Two robot arms.", "stand/neutral/L; list:ROBOT,SELF@R"),
  ("E", [("People rated self-produced touch as less ticklish, less intense and less pleasant.", "blakemore1998")], "Self-touch: less ticklish", "Bars: self low, robot high.", "stand/smile/L; bars:self=h30,robot=h70@R"),
  ("E", [("When the researchers added a delay of up to 200 milliseconds between your movement and the touch, it felt progressively more ticklish.", "blakemore1998")], "200 ms delay: more ticklish", "Clock with delay.", "think/neutral/L; clock@R; text:200 MS@TR"),
  ("E", [("They proposed that your brain predicts the sensory results of your own movements.", "blakemore1998")], "Brain predicts your movements' effects", "Brain with an arrow.", "think/smile/L; brain:@R; arrow:right@TR"),
  ("E", [("That prediction helps cancel the sensation when you cause it yourself.", "blakemore1998")], "Prediction cancels the sensation", "Plus and minus cancelling.", "stand/smile/L; text:CANCEL@R"),
  ("E", [("Brain scans showed less cerebellum activity for a movement that produced the touch than for one that didn't.", "blakemore1998")], "Less cerebellum activity", "Brain with a quiet region.", "point/neutral/L; brain:cerebellum@R"),
  ("T", [("So your brain treats touches you cause differently from touches caused by someone else.", "blakemore1998")], "Self-caused vs other-caused", "Two hands.", "stand/smile/L; list:ME,YOU@R"),
  ("C", [("Tomorrow: why does everything take longer than you planned?", "PLAN")], "Tomorrow: planning", "Clock and calendar.", "stand/worry/L; clock@R"),
 ])

DAYS[29] = dict(
 title="Why Everything Takes Longer Than Planned",
 description_core="Why do projects run late? In a classic study, students' best guesses for finishing their thesis averaged 33.9 days, but they took 55.5 days, and only about 30% finished by their predicted date.",
 primary=["buehler1994"],
 hashtags=["#psychology", "#shorts", "#planningfallacy", "#productivity", "#timemanagement", "#psychologyfacts"],
 caveats="The figures (37 students; 33.9 vs 55.5 days; about 30% on time; 48.6-day worst case) come from secondary summaries that agree with each other; the primary PDF could not be opened here. The study also included other tasks with similar results.",
 thumb=(["WHY IT TAKES", "LONGER"], 1, 0),
 scenes=[
  ("H", [("Why does everything take longer than you planned?", "PLAN")], "Why does it run late?", "Stickman looking at a clock.", "shock/worry/C; clock@R"),
  ("E", [("In 1994, Roger Buehler, Dale Griffin and Michael Ross studied the planning fallacy.", "buehler1994")], "1994: the planning fallacy", "Title card PLANNING FALLACY.", "point/neutral/L; text:PLANNING FALLACY@R"),
  ("E", [("They followed 37 psychology students writing their honors theses.", "buehler1994")], "37 students, honors theses", "Stack of theses.", "stand/neutral/L; text:37 STUDENTS@R"),
  ("E", [("On average, students' best guess was 33.9 days.", "buehler1994")], "Best guess: 33.9 days", "Bar at 33.9.", "stand/smile/L; bars:guess=33.9d,actual=55.5d@R"),
  ("E", [("They actually took 55.5 days on average.", "buehler1994")], "Actual: 55.5 days", "Taller bar at 55.5.", "shock/worry/L; bars:guess=33.9d,actual=55.5d@R"),
  ("E", [("That means the average was about 22 days later than their best guess.", "buehler1994")], "About 22 days later", "Arrow showing a gap.", "stand/worry/L; arrow:right@R; text:+22 DAYS@TR"),
  ("E", [("Only about 30 percent finished by the date they had predicted.", "buehler1994")], "Only ~30% on time", "30% check.", "stand/neutral/L; text:~30%@R"),
  ("E", [("Even the average worst-case forecast, 48.6 days, fell short.", "buehler1994")], "Even worst case fell short", "Worst-case bar below the actual.", "shrug/neutral/L; text:48.6 DAYS@R"),
  ("E", [("Forecasts for other people were generally less biased than forecasts for themselves.", "buehler1994"), ("The same broad pattern appeared across several experiments involving academic and everyday tasks.", "buehler1994")], "Others' forecasts less biased", "Two stickmen estimating.", "think/neutral/L; crowd:1@R"),
  ("T", [("So try estimating the task the way you'd estimate it for someone else.", "buehler1994")], "Estimate like it's someone else's", "Stickman viewing himself from outside.", "point/smile/L; text:SOMEONE ELSE@R"),
  ("C", [("Tomorrow: how do you actually remember an experience?", "PLAN")], "Tomorrow: how you remember", "Memory bubble.", "stand/neutral/L; bubble:memory@R"),
 ])

DAYS[30] = dict(
 title="Peak-End: How Endings Shape Memory",
 description_core="Do you remember experiences by their total length? Experiments suggest the peak and the ending matter more: people preferred a longer cold-water trial that ended slightly warmer, and colonoscopy patients with a milder ending rated the procedure less unpleasant.",
 primary=["kahneman1993", "redelmeier2003"],
 hashtags=["#psychology", "#shorts", "#peakendrule", "#memory", "#kahneman", "#psychologyfacts"],
 caveats="The 1993 study used mild cold-water pain with volunteers (about 70% chose the longer trial); the colonoscopy trial (n=682) is one clinical setting. 'Peak-end rule' is a proposed account that fits these results, not an exact law.",
 thumb=(["HOW ENDINGS", "SHAPE MEMORY"], 1, 0),
 scenes=[
  ("H", [("How do you actually remember an experience?", "PLAN")], "How do you remember it?", "Stickman with a memory bubble.", "think/neutral/C; bubble:memory@R"),
  ("E", [("In 1993, Daniel Kahneman and colleagues had people put a hand in painfully cold water.", "kahneman1993")], "1993: cold-water hand", "Hand in cold water.", "stand/worry/L; text:14C@R; text:1993@TR"),
  ("E", [("One trial lasted 60 seconds.", "kahneman1993")], "Trial 1: 60 seconds", "Clock at 60.", "stand/neutral/L; clock@R; text:60 S@TR"),
  ("E", [("The other lasted 90 seconds, with the last 30 seconds slightly warmer.", "kahneman1993")], "90 s, slightly warmer end", "Clock at 90.", "point/neutral/L; clock@R; text:90 S@TR"),
  ("E", [("Afterwards, people could choose which trial to repeat.", "kahneman1993")], "They chose which to repeat", "Two options.", "think/neutral/L; list:60 S,90 S@R"),
  ("E", [("Nearly 70 percent chose the longer one.", "kahneman1993")], "Nearly 70% chose the longer", "Bar ~70%.", "shock/neutral/L; text:~70%@R"),
  ("E", [("They chose more total discomfort because it ended a bit better.", "kahneman1993")], "More total pain, better ending", "Line ending upward.", "stand/smile/L; lines:pain,time,endup@R"),
  ("E", [("In 2003, Donald Redelmeier, Joel Katz and Kahneman tested it on 682 colonoscopy patients.", "redelmeier2003")], "2003: 682 colonoscopy patients", "Clipboard.", "stand/neutral/L; text:682@R; text:2003@TR"),
  ("E", [("Half had a short, milder period added to the end of the procedure.", "redelmeier2003")], "Half got a milder ending", "Two groups.", "point/neutral/L; list:NORMAL,MILDER END@R"),
  ("E", [("Those patients rated the experience as less unpleasant and were more likely to return for a follow-up.", "redelmeier2003")], "Less unpleasant; more likely to return", "Smile bar.", "stand/smile/L; bars:standard=h70,milder end=h45@R"),
  ("T", [("So how an experience ends can shape how you remember it, so plan a good ending.", "kahneman1993,redelmeier2003")], "Plan a good ending", "Stickman finishing with a flourish.", "walk/smile/L; check@R"),
  ("C", [("Tomorrow: does copying someone's body language build trust?", "PLAN")], "Tomorrow: mirroring", "Two stickmen mirroring.", "stand/neutral/L; crowd:1@R"),
 ])
