"""Days 31-40 (Month 2: People, persuasion & relationships)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common_sources import S, SEC, SECOND

SOURCES = {
 "chartrand1999": S("Chartrand, T. L., & Bargh, J. A.", 1999, "The chameleon effect: The perception-behavior link and social interaction", "Journal of Personality and Social Psychology, 76(6), 893-910", "https://www.semanticscholar.org/paper/The-chameleon-effect:-the-perception-behavior-link-Chartrand-Bargh/6d067a072b9cf8f226eabca90d7bb1d93867a8f6", SECOND + " (nonconscious mimicry of postures/mannerisms; mimicry increases liking)"),
 "maddux2008": S("Maddux, W. W., Mullen, E., & Galinsky, A. D.", 2008, "Chameleons bake bigger pies and take bigger pieces: Strategic behavioral mimicry facilitates negotiation outcomes", "Journal of Experimental Social Psychology, 44(2), 461-468", "https://willmaddux.web.unc.edu/wp-content/uploads/sites/15846/2018/04/JESP-Mimicking-and-Negotiations.pdf", SECOND + " (67% vs 12.5% of dyads reached agreement; mimicry correlated with joint gain)"),
 "jecker1969": S("Jecker, J., & Landy, D.", 1969, "Liking a person as a function of doing him a favour", "Human Relations, 22(4), 371-378", "https://en.wikipedia.org/wiki/Ben_Franklin_effect", SECOND + " (design and main result from several summaries that agree)"),
 "bond2006": S("Bond, C. F., Jr., & DePaulo, B. M.", 2006, "Accuracy of deception judgments", "Personality and Social Psychology Review, 10(3), 214-234", "https://journals.sagepub.com/doi/10.1207/s15327957pspr1003_2", SEC + " (206 documents, 24,483 judges; 54%; 47% of lies, 61% of truths)"),
 "gdrt2006": S("Global Deception Research Team", 2006, "A world of lies", "Journal of Cross-Cultural Psychology, 37(1), 60-74", "https://pubmed.ncbi.nlm.nih.gov/20976033/", SEC + " (58-country survey; gaze aversion the dominant belief)"),
 "depaulo2003": S("DePaulo, B. M., Lindsay, J. J., Malone, B. E., Muhlenbruck, L., Charlton, K., & Cooper, H.", 2003, "Cues to deception", "Psychological Bulletin, 129(1), 74-118", "https://scholars.duke.edu/publication/660134", SEC + " (158 cues, 1,338 estimates; cues faint and unreliable)"),
 "milgram1963": S("Milgram, S.", 1963, "Behavioral study of obedience", "Journal of Abnormal and Social Psychology, 67(4), 371-378", "https://www.psy.miami.edu/_assets/pdf/rpo-articles/milgram-1963.pdf", SEC + " (26 of 40 continued to 450 V)"),
 "perry2013": S("Perry, G.", 2013, "Behind the shock machine: The untold story of the notorious Milgram psychology experiments", "The New Press (book)", "https://www.researchgate.net/publication/333618191_Behind_the_Shock_Machine_the_untold_story_of_the_notorious_Milgram_psychology_experiments", SECOND + " (archive findings: improvised prompts; 24 variations; majority disobeyed in more than half)"),
 "haslam2014": S("Haslam, S. A., Reicher, S. D., & Birney, M. E.", 2014, "Nothing by mere authority: Evidence that in an experimental analogue of the Milgram paradigm participants are motivated not by orders but by appeals to science", "Journal of Social Issues, 70(3), 473-488", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10946829/", SEC + " (title/abstract quoted in search results; link is a related engaged-followership paper)"),
 "freedman1966": S("Freedman, J. L., & Fraser, S. C.", 1966, "Compliance without pressure: The foot-in-the-door technique", "Journal of Personality and Social Psychology, 4(2), 195-202", "https://www.semanticscholar.org/paper/Compliance-without-pressure:-the-foot-in-the-door-Freedman-Fraser/00964495e374c0f26ba753b94c13efcb33129dfd", SECOND + " (Palo Alto homeowners; 53% vs 22% in the product-survey experiment)"),
 "dillard1984": S("Dillard, J. P., Hunter, J. E., & Burgoon, M.", 1984, "Sequential-request persuasive strategies: Meta-analysis of foot-in-the-door and door-in-the-face", "Human Communication Research, 10(4), 461-488", "https://www.simplypsychology.org/compliance.html", SECOND + " (effects small: r = .17 and .15; moderated by prosocial requests)"),
 "stivers2009": S("Stivers, T., Enfield, N. J., Brown, P., et al.", 2009, "Universals and cultural variation in turn-taking in conversation", "Proceedings of the National Academy of Sciences, 106(26), 10587-10592", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2705608/", SEC + " (ten languages; response peak within 200 ms; means within a quarter second)"),
 "koudenburg2011": S("Koudenburg, N., Postmes, T., & Gordijn, E. H.", 2011, "Disrupting the flow: How brief silences in group conversations affect social needs", "Journal of Experimental Social Psychology, 47(2), 512-515", "https://research.rug.nl/en/publications/disrupting-the-flow-how-brief-silences-in-group-conversations-aff/", SEC),
 "strutzenberg2017": S("Strutzenberg, C. C., Wiersma-Mosley, J. D., Jozkowski, K. N., & Becnel, J. N.", 2017, "Love-bombing: A narcissistic approach to relationship formation", "Discovery, The Student Journal of Dale Bumpers College, 18(1) (University of Arkansas)", "https://scholarworks.uark.edu/discoverymag/vol18/iss1/14/", SEC + " (484 college students; correlational)"),
 "sweet2019": S("Sweet, P. L.", 2019, "The sociology of gaslighting", "American Sociological Review, 84(5), 851-875", "https://www.researchgate.net/publication/335953689_The_Sociology_of_Gaslighting", SEC + " (definition, interview-based findings)"),
 "walster1973": S("Walster, E., Walster, G. W., Piliavin, J., & Schmidt, L.", 1973, "'Playing hard to get': Understanding an elusive phenomenon", "Journal of Personality and Social Psychology, 26(1), 113-121", "https://stafforini.com/works/walster-1973-playing-hard-get/", SEC + " (71 college students; five experiments; selective woman preferred)"),
 "aronson1966": S("Aronson, E., Willerman, B., & Floyd, J.", 1966, "The effect of a pratfall on increasing interpersonal attractiveness", "Psychonomic Science, 4(6), 227-228", "https://link.springer.com/article/10.3758/BF03342263", SEC + " (92% vs 30% contestants; coffee spill)"),
}

DAYS = {}

DAYS[31] = dict(
 title="Does Copying Body Language Build Trust?",
 description_core="Does mirroring someone's body language make them like you? Classic studies link natural mimicry with liking, and one negotiation experiment found pairs reached agreement far more often when the buyer mimicked the seller.",
 primary=["chartrand1999", "maddux2008"],
 hashtags=["#psychology", "#shorts", "#bodylanguage", "#mimicry", "#persuasion", "#psychologyfacts"],
 caveats="The negotiation figures (67% vs 12.5% of pairs) come from secondary summaries of Maddux et al. (2008); the PDF could not be opened here. Both studies are controlled experiments, not everyday conversations. The video claims 'liking' and 'better deals', not that copying someone on purpose reliably builds trust.",
 thumb=(["DOES MIRRORING", "BUILD TRUST?"], 1, 0),
 scenes=[
  ("H", [("Does copying someone's body language make them trust you?", "PLAN")], "Does mirroring work?", "Two stickmen mirroring each other's posture.", "stand/neutral/C; crowd:1@R"),
  ("E", [("In 1999, Tanya Chartrand and John Bargh described the chameleon effect: people nonconsciously mimic the postures and mannerisms of those they interact with.", "chartrand1999")], "The chameleon effect, 1999", "Stickman unconsciously copying another's pose.", "point/neutral/L; crowd:1@R; text:CHAMELEON EFFECT@TR"),
  ("E", [("They reported that mimicry increases liking.", "chartrand1999")], "Mimicry and liking", "Heart growing between two stickmen.", "stand/smile/L; text:LIKING@R"),
  ("E", [("In 2008, William Maddux, Elizabeth Mullen and Adam Galinsky tested mimicry in a negotiation.", "maddux2008")], "2008: a negotiation test", "Two stickmen across a table.", "think/neutral/L; crowd:1@R; text:2008@TR"),
  ("E", [("When buyers were told to mimic the seller's body language, 67 percent of pairs reached an agreement.", "maddux2008")], "Mimic: 67% reached a deal", "Tall bar labeled 67%.", "stand/smile/L; bars:mimic=67%,no mimic=12.5%@R"),
  ("E", [("Without mimicry instructions, only 12.5 percent did.", "maddux2008")], "No mimicry: 12.5%", "Short bar labeled 12.5%.", "shrug/neutral/L; bars:mimic=67%,no mimic=12.5%@R"),
  ("E", [("The more mimicking that actually happened, the greater the joint gain.", "maddux2008")], "More mimicry, more joint gain", "Rising line.", "point/smile/L; lines:mimicry,joint gain,up@R"),
  ("E", [("Both were controlled experiments, not studies of everyday conversations.", "chartrand1999,maddux2008")], "Lab experiments, not daily life", "Lab flask icon.", "shrug/neutral/L; text:LAB STUDIES@R"),
  ("T", [("So mirroring goes along with liking, and in one negotiation experiment deliberate mimicry went along with better deals.", "chartrand1999,maddux2008")], "Liking and better deals", "Stickman nodding with a handshake.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: does asking someone for a favor make them like you more?", "PLAN")], "Tomorrow: asking for favors", "Stickman holding out a hand.", "stand/neutral/L; text:FAVOR?@R"),
 ])

DAYS[32] = dict(
 title="Does Asking for a Favor Make People Like You?",
 description_core="Does asking someone for a favor make them like you more? In a 1969 experiment, students the researcher personally asked for money back reported liking him more than students asked by a secretary.",
 primary=["jecker1969"],
 hashtags=["#psychology", "#shorts", "#benfranklineffect", "#persuasion", "#socialpsychology", "#psychologyfacts"],
 caveats="One classic 1969 experiment, known to us through several consistent summaries rather than the original paper. Cognitive dissonance is the classic explanation, not a proven mechanism. The 'small favor may help' takeaway is an application of the finding, not a tested tip.",
 thumb=(["DO FAVORS", "MAKE FRIENDS?"], 1, 0),
 scenes=[
  ("H", [("Does asking someone for a favor make them like you?", "PLAN")], "Favors = liking?", "Stickman asking a friend for a favor.", "think/neutral/C; crowd:1@R"),
  ("E", [("In 1969, researchers Jecker and Landy invited students to a quiz competition where they could win money.", "jecker1969")], "1969: a quiz for money", "Coins and a quiz card.", "stand/neutral/L; coin:$@R; text:1969@TR"),
  ("E", [("Afterward, one group was asked by the researcher to return the money, because he'd used his own funds.", "jecker1969")], "Group 1: the researcher asks", "Researcher stickman holding a hand out.", "point/neutral/L; crowd:1@R"),
  ("E", [("Another group was asked by a secretary, citing department funds.", "jecker1969")], "Group 2: a secretary asks", "Secretary stickman with a clipboard.", "stand/neutral/L; list:DEPT FUNDS@R"),
  ("E", [("A third group was not asked at all.", "jecker1969")], "Group 3: not asked", "Empty chair.", "shrug/neutral/L; text:NOT ASKED@R"),
  ("E", [("Students the researcher himself had asked reported liking him more than students asked by the secretary.", "jecker1969")], "Asked by him: liked him more", "Heart above the researcher.", "stand/smile/L; bars:secretary=h35,researcher=h70@R"),
  ("E", [("The classic explanation is cognitive dissonance: if you helped someone, you may conclude you must like them.", "jecker1969")], "'I helped, so I like them'", "Thought bubble linking help and liking.", "think/neutral/L; bubble:I helped him@TR"),
  ("E", [("It's one 1969 experiment, so treat the result as a suggestion, not a rule.", "jecker1969")], "One experiment, not a rule", "Single test tube.", "shrug/neutral/L; text:1 STUDY@R"),
  ("T", [("So if you want to build rapport, asking for a small favor may help, but it's not guaranteed.", "jecker1969")], "A small favor may help", "Stickman politely asking.", "point/smile/L; qmark@R"),
  ("C", [("Tomorrow: can you spot a liar from their body language?", "PLAN")], "Tomorrow: spotting lies", "Magnifier over a face.", "stand/neutral/L; qmark@R"),
 ])

DAYS[33] = dict(
 title="Can You Really Spot a Liar? What Research Says",
 description_core="Can you tell when someone is lying? A large meta-analysis found people are right about 54% of the time, and another found the behavioral cues people rely on are faint and unreliable.",
 primary=["bond2006", "depaulo2003"],
 hashtags=["#psychology", "#shorts", "#lying", "#bodylanguage", "#deception", "#psychologyfacts"],
 caveats="Bond & DePaulo (2006) average is for real-time judgments with no training or aids; accuracy varies by situation. The gaze-aversion belief figure comes from the Global Deception Research Team (58-country survey; majority in 51 countries). The video does not say lie detection is impossible, only that these cues are unreliable.",
 thumb=(["CAN YOU SPOT", "A LIAR?"], 1, 0),
 scenes=[
  ("H", [("Can you tell when someone is lying?", "PLAN")], "Can you spot a liar?", "Stickman squinting at another stickman.", "think/neutral/C; qmark@R"),
  ("E", [("In 2006, Charles Bond and Bella DePaulo combined results from 206 documents and 24,483 judges.", "bond2006")], "2006: 206 documents, 24,483 judges", "Stack of papers.", "point/neutral/L; text:206 STUDIES@R"),
  ("E", [("When people judged lies and truths in real time, with no special training, they were right about 54 percent of the time.", "bond2006")], "Right about 54% of the time", "54% bar next to a 50% line.", "stand/neutral/L; bars:chance=h50:50%,people=h54:54%@R"),
  ("E", [("That's barely better than a coin flip.", "bond2006")], "Barely better than a coin flip", "Coin.", "shrug/smile/L; coin:HEADS@R"),
  ("E", [("They correctly spotted 47 percent of lies and 61 percent of truths.", "bond2006")], "47% of lies, 61% of truths", "Two bars.", "stand/neutral/L; bars:lies=h47:47%,truths=h61:61%@R"),
  ("E", [("People also tended to regard their conversation partners as honest.", "bond2006")], "We tend to assume honesty", "Smiley partner.", "stand/smile/L; crowd:1@R"),
  ("E", [("In a survey of 58 countries, most people in 51 of them said liars avert their gaze.", "gdrt2006")], "51 of 58: 'liars look away'", "Globe with eyes.", "point/neutral/L; text:51 OF 58@R"),
  ("E", [("But a 2003 meta-analysis of 158 possible cues found that cues to deception are faint and unreliable.", "depaulo2003")], "2003: cues are faint and unreliable", "Faint dotted line.", "shrug/neutral/L; lines:cue,truth,flat@R"),
  ("T", [("So instead of trusting a hunch about eye contact, be cautious about judging honesty from behavior alone.", "depaulo2003,bond2006")], "Be careful judging honesty", "Stickman hesitating before judging.", "point/smile/L; qmark@R"),
  ("C", [("Tomorrow: why did so many people obey in the Milgram experiment?", "PLAN")], "Tomorrow: Milgram", "Shock-machine dial (no people).", "stand/neutral/L; text:MILGRAM@R"),
 ])

DAYS[34] = dict(
 title="Milgram: Do People Really Obey Blindly?",
 description_core="In Milgram's 1963 study, 26 of 40 men continued to the highest shock level, but archive research and a 2014 study suggest 'blind obedience' is too simple an explanation.",
 primary=["milgram1963", "perry2013"],
 hashtags=["#psychology", "#shorts", "#milgram", "#obedience", "#socialpsychology", "#psychologyfacts"],
 caveats="CONTESTED. The 65% figure is from one 1963 condition (Yale, 40 men). Perry (2013) draws on Milgram's archive: 24 variations, most with majority disobedience, improvised prompts, and some participants doubting the shocks were real. Haslam, Reicher & Birney (2014) propose 'engaged followership' based on an experimental analogue. The shocks were not real (the learner was an actor); described in neutral terms.",
 thumb=(["DO WE OBEY", "BLINDLY?"], 1, 0),
 scenes=[
  ("H", [("Do people really obey authority blindly?", "PLAN")], "Blind obedience?", "Stickman facing an instruction card.", "think/worry/C; list:CONTINUE@R"),
  ("E", [("In Stanley Milgram's 1963 study, 40 men were told to give increasingly severe electric shocks to another person, who was actually an actor.", "milgram1963")], "1963: 40 men, a staged learner", "Dial with rising numbers.", "stand/neutral/L; text:40 MEN@R; text:1963@TR"),
  ("E", [("Twenty-six of the 40 continued to the final 450-volt switch.", "milgram1963")], "26 of 40: full 450 volts", "26 of 40 counter.", "shock/neutral/L; text:26 OF 40@R"),
  ("E", [("That's the famous 65 percent.", "milgram1963")], "The famous 65%", "Big 65%.", "stand/neutral/L; text:65%@R"),
  ("E", [("But Gina Perry's research in Milgram's archives found the experimenter improvised and coaxed participants.", "perry2013")], "Archives: the experimenter improvised", "Archive box.", "think/neutral/L; list:ARCHIVE@R"),
  ("E", [("She also found Milgram ran 24 variations, and in more than half of them most people did not obey.", "perry2013")], "24 variations; often most refused", "24 with a cross.", "shrug/neutral/L; text:24 VARIATIONS@R; cross@TR"),
  ("E", [("In 2014, Haslam, Reicher and Birney reported that participants in an experimental analogue responded more to appeals to science than to blunt orders.", "haslam2014")], "2014: science appeals beat orders", "Beaker vs. megaphone.", "stand/neutral/L; list:SCIENCE,ORDERS@R"),
  ("E", [("They describe this as engaged followership, not blind obedience.", "haslam2014")], "Engaged followership", "Stickman following willingly.", "walk/neutral/L; text:ENGAGED FOLLOWERSHIP@R"),
  ("T", [("So 'people just follow orders' is too simple an explanation for Milgram's results.", "haslam2014,perry2013")], "'Just following orders' is too simple", "Scale with a question mark.", "point/smile/L; scale@R"),
  ("C", [("Tomorrow: how does a tiny request lead to a bigger yes?", "PLAN")], "Tomorrow: small requests", "Small box then big box.", "stand/neutral/L; list:SMALL,BIG@R"),
 ])

DAYS[35] = dict(
 title="The Foot-in-the-Door Technique: Does It Work?",
 description_core="Does agreeing to a small request make you say yes to a bigger one? In a 1966 field experiment it did, but a 1984 meta-analysis found the effect small.",
 primary=["freedman1966", "dillard1984"],
 hashtags=["#psychology", "#shorts", "#footinthedoor", "#persuasion", "#compliance", "#psychologyfacts"],
 caveats="The 53% vs 22% figures come from secondary summaries of Freedman & Fraser (1966). Dillard et al. (1984) found a small average effect (r about .17) that depended on request type (stronger when prosocial). The video states both the original effect and its modest size.",
 thumb=(["SMALL YES,", "BIGGER YES?"], 1, 0),
 scenes=[
  ("H", [("Can a tiny request make you say yes to a bigger one?", "PLAN")], "Tiny ask, bigger yes?", "Small box then large box.", "think/neutral/C; list:SMALL,BIG@R"),
  ("E", [("Researchers Freedman and Fraser tested what they called the foot-in-the-door technique in 1966.", "freedman1966")], "1966: foot-in-the-door", "A foot in a doorway.", "point/neutral/L; door@R; text:1966@TR"),
  ("E", [("They asked homeowners in Palo Alto, California, to agree to a small request first.", "freedman1966")], "Small request first", "Houses with a clipboard.", "stand/neutral/L; list:QUESTIONNAIRE@R"),
  ("E", [("In one experiment, 53 percent agreed to a two-hour home visit by investigators after a small earlier request.", "freedman1966")], "After small request: 53% agreed", "Tall bar 53%.", "stand/smile/L; bars:after small=53%,no small=22%@R"),
  ("E", [("Without that first small request, only 22 percent agreed.", "freedman1966")], "Without it: 22%", "Short bar 22%.", "shrug/neutral/L; bars:after small=53%,no small=22%@R"),
  ("E", [("The authors suggested agreeing changes how you see yourself: as the kind of person who helps.", "freedman1966")], "'I'm someone who helps'", "Thought bubble.", "think/smile/L; bubble:I help@TR"),
  ("E", [("But in a 1984 meta-analysis, Dillard, Hunter and Burgoon found the effect was small, with a correlation of about 0.17.", "dillard1984")], "1984 meta-analysis: effect small", "Tiny bar.", "shrug/neutral/L; bars:effect=h17:r=.17@R"),
  ("E", [("It worked mainly when the request was prosocial, such as helping a cause.", "dillard1984")], "Works mostly for prosocial requests", "Heart on a request card.", "stand/smile/L; list:HELP A CAUSE@R"),
  ("T", [("So a small yes can nudge a bigger one, but the effect is modest.", "freedman1966,dillard1984")], "A nudge, not a trick", "Gentle nudge arrow.", "point/smile/L; arrow:right@R"),
  ("C", [("Tomorrow: why does a short silence feel so awkward?", "PLAN")], "Tomorrow: awkward silence", "A blank speech bubble.", "stand/neutral/L; bubble:...@R"),
 ])

DAYS[36] = dict(
 title="The 200-Millisecond Rule Behind Awkward Silence",
 description_core="Why does a short silence feel awkward? Across ten languages, most replies come within about 200 milliseconds, and a 2011 study found a brief silence in a group conversation led to more negative emotion and feelings of rejection.",
 primary=["stivers2009", "koudenburg2011"],
 hashtags=["#psychology", "#shorts", "#conversation", "#silence", "#communication", "#psychologyfacts"],
 caveats="Stivers et al. (2009) measured question-answer timing in ten languages; Koudenburg et al. (2011) tested brief silences in group conversations in the lab. Neither shows silence 'makes people talk' (the original topic idea, dropped as unsupported). The takeaway links the two findings loosely and is hedged.",
 thumb=(["WHY SILENCE", "FEELS AWKWARD"], 1, 0),
 scenes=[
  ("H", [("Why does a short silence in conversation feel awkward?", "PLAN")], "Why does silence feel awkward?", "Two stickmen with empty speech bubbles.", "shock/worry/C; bubble:...@R"),
  ("E", [("In 2009, Tanya Stivers and colleagues studied conversations in ten languages around the world.", "stivers2009")], "2009: ten languages", "Globe with ten dots.", "point/neutral/L; text:10 LANGUAGES@R; text:2009@TR"),
  ("E", [("All ten languages avoided overlapping talk and minimized silence between turns.", "stivers2009")], "Little overlap, little silence", "Two bubbles not overlapping.", "stand/neutral/L; bubble:Q@TR; bubble:A@R"),
  ("E", [("Most replies came within about 200 milliseconds of the end of a question.", "stivers2009")], "Replies: about 200 ms", "Stopwatch at 0.2.", "shock/neutral/L; clock@R; text:200 MS@TR"),
  ("E", [("Differences between languages in the average gap were within about a quarter of a second.", "stivers2009")], "Languages differ by under 0.25 s", "Close bars.", "stand/neutral/L; bars:lang A=h40,lang B=h46@R"),
  ("E", [("The authors suggest a shared human basis for this timing.", "stivers2009")], "A shared human basis?", "Globe with a link.", "think/neutral/L; qmark@R"),
  ("E", [("In 2011, Namkje Koudenburg and colleagues studied what a brief silence does in a group conversation.", "koudenburg2011")], "2011: silence in groups", "Group of stickmen.", "stand/neutral/L; crowd:4@R; text:2011@TR"),
  ("E", [("When a silence disrupted the flow, people felt more negative emotions and more rejected.", "koudenburg2011")], "Silence: more negative feelings", "Frowny face.", "stand/worry/L; text:REJECTED@R"),
  ("T", [("So when a silence feels awkward, the feeling has a basis in how tightly conversations are timed.", "stivers2009,koudenburg2011")], "Awkward has a basis", "Clock beside a speech bubble.", "point/smile/L; clock@R"),
  ("C", [("Tomorrow: what does research actually say about love bombing?", "PLAN")], "Tomorrow: love bombing", "A heart with a question mark.", "stand/neutral/L; qmark@R"),
 ])

DAYS[37] = dict(
 title="Love Bombing: What Research Actually Says",
 description_core="What does research say about love bombing? A 2017 survey of 484 college students linked it with narcissistic tendencies, insecure attachment and lower self-esteem, but it is early, correlational research.",
 primary=["strutzenberg2017"],
 hashtags=["#psychology", "#shorts", "#lovebombing", "#relationships", "#dating", "#psychologyfacts"],
 caveats="SENSITIVE / EARLY RESEARCH. One survey study (Strutzenberg et al. 2017; college students; correlational). The video does not diagnose anyone or claim causes, and does not call love bombing a clinical diagnosis. Educational, not therapy or medical advice.",
 thumb=(["LOVE BOMBING:", "THE RESEARCH"], 1, 0),
 scenes=[
  ("H", [("What does research actually say about love bombing?", "PLAN")], "What does research say?", "Heart with a magnifying glass.", "think/neutral/C; qmark@R"),
  ("E", [("In 2017, Strutzenberg and colleagues published what they described as the first study to empirically examine love-bombing.", "strutzenberg2017")], "2017: first empirical study", "Journal cover.", "point/neutral/L; text:2017@TR; text:FIRST STUDY@R"),
  ("E", [("They defined it as excessive communication early in a romantic relationship, used to gain power and control.", "strutzenberg2017")], "Defined: early excessive messaging", "Phone with many message bubbles.", "stand/neutral/L; bubble:msg@TR; bubble:msg@R"),
  ("E", [("They surveyed 484 college students at a large southern university.", "strutzenberg2017")], "484 college students", "Survey sheet.", "stand/neutral/L; text:484@R"),
  ("E", [("Love-bombing was linked to narcissistic tendencies and insecure attachment.", "strutzenberg2017")], "Linked: narcissism, insecure attachment", "Two linked boxes.", "think/neutral/L; list:NARCISSISM,ATTACHMENT@R"),
  ("E", [("It was also linked to lower self-esteem.", "strutzenberg2017")], "Also linked to lower self-esteem", "Falling bar.", "stand/neutral/L; arrow:down@R"),
  ("E", [("And it was associated with more text and media use in relationships.", "strutzenberg2017")], "More texting and media use", "Phone icon.", "stand/neutral/L; list:TEXTS@R"),
  ("E", [("The study was a survey of college students, so it can't show cause and effect.", "strutzenberg2017")], "A survey can't show cause", "Scale with a question.", "shrug/neutral/L; qmark@R"),
  ("E", [("That makes it early research, not a settled diagnosis.", "strutzenberg2017")], "Early research, not a diagnosis", "Sapling.", "stand/neutral/L; text:EARLY RESEARCH@R"),
  ("T", [("So treat 'love bombing' as a description of a pattern in one study, and not as a test for who someone is.", "strutzenberg2017")], "A pattern, not a test", "Stickman setting a label down.", "point/smile/L; cross@R"),
  ("C", [("Tomorrow: where does the word gaslighting come from?", "PLAN")], "Tomorrow: gaslighting", "A lamp with a question mark.", "stand/neutral/L; lightbulb@R"),
 ])

DAYS[38] = dict(
 title="Gaslighting: What the Research Says",
 description_core="What does gaslighting actually mean? Sociologist Paige Sweet's 2019 study defines it as a type of psychological abuse aimed at making victims feel 'crazy', and finds it rooted in social inequalities.",
 primary=["sweet2019"],
 hashtags=["#psychology", "#shorts", "#gaslighting", "#relationships", "#sociology", "#psychologyfacts"],
 caveats="SENSITIVE. Based on one sociological study (Sweet 2019) using interviews about abusive relationships. The video describes the study's argument; it does not diagnose anyone. The word's origin in the 1938 play 'Gas Light' is not claimed (not verified here). Educational, not therapy or medical advice.",
 thumb=(["GASLIGHTING:", "WHAT IT MEANS"], 1, 0),
 scenes=[
  ("H", [("What does gaslighting actually mean?", "PLAN")], "What does it mean?", "A lamp flickering.", "think/neutral/C; lightbulb@R"),
  ("E", [("In 2019, sociologist Paige Sweet published a study called The Sociology of Gaslighting.", "sweet2019")], "2019: The Sociology of Gaslighting", "Journal cover.", "point/neutral/L; text:2019@TR; text:SOCIOLOGY@R"),
  ("E", [("She defines gaslighting as a type of psychological abuse aimed at making victims seem or feel crazy.", "sweet2019")], "A type of psychological abuse", "Stickman with swirling thoughts.", "stand/worry/L; waves@R"),
  ("E", [("The aim, she writes, is to create a surreal interpersonal environment.", "sweet2019")], "A 'surreal' environment", "Warped room.", "think/neutral/L; text:SURREAL@R"),
  ("E", [("Sweet argues gaslighting is more than a psychological problem between two people.", "sweet2019")], "More than a personal problem", "Two stickmen inside a bigger circle.", "stand/neutral/L; crowd:2@R"),
  ("E", [("She argues it is rooted in social inequalities, including gender.", "sweet2019")], "Rooted in social inequality", "Unequal scale.", "point/neutral/L; scale@R"),
  ("E", [("It happens in power-laden intimate relationships.", "sweet2019")], "In power-laden relationships", "Two stickmen of unequal size.", "stand/neutral/L; crowd:1@R"),
  ("E", [("Her study was based on life-course interviews.", "sweet2019")], "Based on interviews", "Microphone.", "stand/neutral/L; text:INTERVIEWS@R"),
  ("E", [("She found abusers used gender stereotypes, racial stereotypes and victims' institutional settings to manipulate their sense of reality.", "sweet2019")], "Stereotypes and institutions used", "List of three tools.", "think/neutral/L; list:GENDER,RACE,INSTITUTION@R"),
  ("E", [("Women of different racial and social backgrounds experienced gaslighting in different forms.", "sweet2019")], "It took different forms", "Three different shapes.", "stand/neutral/L; crowd:3@R"),
  ("T", [("So in this research, gaslighting describes a pattern within abusive power dynamics, not an ordinary disagreement.", "sweet2019")], "Abuse pattern, not disagreement", "Stickman separating two cards.", "point/smile/L; text:PATTERN@R"),
  ("C", [("Tomorrow: does playing hard to get actually work?", "PLAN")], "Tomorrow: playing hard to get", "A door with a lock.", "stand/neutral/L; door@R"),
 ])

DAYS[39] = dict(
 title="Does Playing Hard to Get Actually Work?",
 description_core="Does playing hard to get make you more attractive? In five experiments in 1973 it failed, and what worked was being selective: easy for the participant to get, but hard for others.",
 primary=["walster1973"],
 hashtags=["#psychology", "#shorts", "#dating", "#attraction", "#relationships", "#psychologyfacts"],
 caveats="The headline study (Walster et al. 1973) used male college participants rating women's profiles; the video says so. One older study cannot show how everyone reacts today. The takeaway describes what these experiments supported, not dating advice for everyone.",
 thumb=(["DOES PLAYING", "HARD TO GET", "WORK?"], 2, 0),
 scenes=[
  ("H", [("Does playing hard to get actually work?", "PLAN")], "Does it work?", "Stickman behind a locked door.", "think/neutral/C; door@R"),
  ("E", [("In 1973, Elaine Walster and colleagues tested this in five experiments.", "walster1973")], "1973: five experiments", "Five test tubes.", "point/neutral/L; text:5 EXPERIMENTS@R; text:1973@TR"),
  ("E", [("They found the idea that a hard-to-get woman is more desirable failed in all five.", "walster1973")], "'Hard to get' failed ×5", "Five crosses.", "shock/neutral/L; cross@R"),
  ("E", [("In one study, 71 college men learned that a woman had seen their profile and four others.", "walster1973")], "71 college men, 5 profiles", "Five profile cards.", "stand/neutral/L; text:5 PROFILES@R"),
  ("E", [("She was either easy to get, hard to get, or selective.", "walster1973")], "Easy, hard or selective", "Three door labels.", "think/neutral/L; list:EASY,HARD,SELECTIVE@R"),
  ("E", [("The selective woman was willing to date the participant, but not the other men.", "walster1973")], "Selective: yes to him only", "Check beside one profile.", "stand/neutral/L; check@R"),
  ("E", [("Participants largely preferred the selective woman.", "walster1973")], "She was preferred", "Heart on the selective option.", "stand/smile/L; text:SELECTIVE@R"),
  ("E", [("She was seen as having the strengths of both the easy and hard-to-get women, and none of the weaknesses.", "walster1973")], "Both strengths, no weaknesses", "Checklist of strengths.", "point/smile/L; list:PLUS,PLUS@R"),
  ("E", [("That study used only male participants, so it can't tell us how everyone reacts.", "walster1973")], "Male participants only", "Single male icon.", "shrug/neutral/L; text:MEN ONLY@R"),
  ("T", [("So what the experiments support is not playing hard to get, but showing someone they are your selective choice.", "walster1973")], "Selective, not hard to get", "Stickman choosing one card.", "point/smile/L; check@R"),
  ("C", [("Tomorrow: can making a mistake make you more likable?", "PLAN")], "Tomorrow: a spilled coffee", "A coffee cup tipping.", "stand/neutral/L; text:OOPS@R"),
 ])

DAYS[40] = dict(
 title="The Pratfall Effect: When Mistakes Make You Likable",
 description_core="Can a blunder make you more likable? In a 1966 experiment, a very competent contestant who spilled coffee became more attractive, while a mediocre one became less attractive.",
 primary=["aronson1966"],
 hashtags=["#psychology", "#shorts", "#pratfalleffect", "#likability", "#socialpsychology", "#psychologyfacts"],
 caveats="One early study with male University of Minnesota students listening to recordings. The effect is described as depending on perceived competence; the video does not claim it generalizes to all settings. 'May humanize you' is hedged.",
 thumb=(["WHEN MISTAKES", "MAKE YOU", "LIKABLE"], 1, 0),
 scenes=[
  ("H", [("Can making a mistake make you more likable?", "PLAN")], "Can a mistake help?", "Stickman spilling coffee.", "shock/neutral/C; text:OOPS@R"),
  ("E", [("In 1966, Elliot Aronson and colleagues played male college students tape recordings of a quiz show interview.", "aronson1966")], "1966: a quiz-show recording", "Tape recorder.", "stand/neutral/L; text:1966@TR; text:TAPE@R"),
  ("E", [("One contestant answered about 92 percent of the hard questions correctly.", "aronson1966")], "A: ~92% correct", "Tall bar.", "stand/smile/L; bars:A=92%,B=30%@R"),
  ("E", [("Another answered only about 30 percent correctly.", "aronson1966")], "B: ~30% correct", "Short bar.", "shrug/neutral/L; bars:A=92%,B=30%@R"),
  ("E", [("At the end, in some versions, the contestant clumsily spilled coffee on himself.", "aronson1966")], "Some versions: a spilled coffee", "Cup tipping over.", "shock/neutral/L; text:SPILL@R"),
  ("E", [("The very impressive contestant became more attractive after the blunder.", "aronson1966")], "Impressive + blunder: more attractive", "Rising bar.", "stand/smile/L; bars:before=h45,after=h70@R"),
  ("E", [("The mediocre contestant became less attractive after the same blunder.", "aronson1966")], "Mediocre + blunder: less attractive", "Falling bar.", "stand/worry/L; bars:before=h45,after=h25@R"),
  ("E", [("The authors speculated that a blunder makes a superior person seem more human.", "aronson1966")], "A blunder seems 'human'", "Thought bubble.", "think/smile/L; bubble:human@TR"),
  ("E", [("So the pratfall effect depends on how competent someone already seems.", "aronson1966")], "Depends on perceived competence", "Scale with two sides.", "point/neutral/L; scale@R"),
  ("E", [("This was one early study, using recordings and male students.", "aronson1966")], "One early study", "Single card.", "shrug/neutral/L; text:1 STUDY@R"),
  ("T", [("So a small slip may humanize you if people already see you as capable, but it may not help otherwise.", "aronson1966")], "May humanize you, if capable", "Stickman shrugging with a smile.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: does knowing what others do change what you do?", "PLAN")], "Tomorrow: following the crowd", "Crowd of tiny stickmen.", "stand/neutral/L; crowd:5@R"),
 ])
