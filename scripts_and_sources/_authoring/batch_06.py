"""Days 51-60 (Month 2: People, persuasion & relationships)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common_sources import S, SEC, SECOND

SOURCES = {
 "moray1959": S("Moray, N.", 1959, "Attention in dichotic listening: Affective cues and the influence of instructions", "Quarterly Journal of Experimental Psychology, 11(1), 56-60", "https://doi.org/10.1080/17470215908416289", SECOND + " (about a third heard their own name in the ignored channel)"),
 "wood1995": S("Wood, N., & Cowan, N.", 1995, "The cocktail party phenomenon revisited: How frequent are attention shifts to one's name in an irrelevant auditory channel?", "Journal of Experimental Psychology: Learning, Memory, and Cognition, 21(1), 255-260", "https://doi.org/10.1037/0278-7393.21.1.255", SEC + " (about a third noticed their name; replication of Moray)"),
 "howard1995": S("Howard, D. J., Gengler, C., & Jain, A.", 1995, "What's in a name? A complimentary means of persuasion", "Journal of Consumer Research, 22(2), 200-211", "https://doi.org/10.1086/209445", SEC + " (three experiments; remembering a name increased compliance with a purchase request)"),
 "janis1972": S("Janis, I. L.", 1972, "Victims of groupthink: A psychological study of foreign-policy decisions and fiascoes", "Houghton Mifflin (book)", "https://www.britannica.com/topic/Victims-of-Groupthink-A-Psychological-Study-of-Foreign-Policy-Decisions-and-Fiascoes", SEC + " (Bay of Pigs, Pearl Harbor and Vietnam as case studies; contradictory views not expressed or evaluated)"),
 "esser1998": S("Esser, J. K.", 1998, "Alive and well after 25 years: A review of groupthink research", "Organizational Behavior and Human Decision Processes, 73(2-3), 116-141", "https://www.sciencedirect.com/science/article/abs/pii/S0749597898927583", SEC + " ('too early to pass judgment'; case studies confirm the model, experimental validation lacking)"),
 "haney1973": S("Haney, C., Banks, C., & Zimbardo, P.", 1973, "Interpersonal dynamics in a simulated prison", "International Journal of Criminology and Penology, 1, 69-97", "https://en.wikipedia.org/wiki/Stanford_prison_experiment", SECOND + " (24 selected; 10 prisoners/11 guards; planned two weeks, ended after six days)"),
 "letexier2019": S("Le Texier, T.", 2019, "Debunking the Stanford Prison Experiment", "American Psychologist, 74(7), 823-839", "https://doi.org/10.1037/amp0000401", SEC + " (archival analysis; guards coached; told which behavior was wanted)"),
 "reicher2006": S("Reicher, S., & Haslam, S. A.", 2006, "Rethinking the psychology of tyranny: The BBC prison study", "British Journal of Social Psychology, 45(1), 1-40", "https://doi.org/10.1348/014466605X48998", SECOND + " (guards did not identify with their role)"),
 "dunbar1997": S("Dunbar, R. I. M., Marriott, A., & Duncan, N. D. C.", 1997, "Human conversational behavior", "Human Nature, 8(3), 231-246", "https://doi.org/10.1007/BF02912493", SEC + " (45 conversations; about two-thirds social topics)"),
 "robbins2020": S("Robbins, M. L., & Karan, A.", 2020, "Who gossips and how in everyday life?", "Social Psychological and Personality Science, 11(2), 185-195", "https://doi.org/10.1177/1948550619837000", SEC + " (467 participants; EAR sampling; mostly neutral; about 52 minutes per awake day)"),
 "feinberg2012": S("Feinberg, M., Willer, R., Stellar, J., & Keltner, D.", 2012, "The virtues of gossip: Reputational information sharing as prosocial behavior", "Journal of Personality and Social Psychology, 102(5), 1015-1030", "https://doi.org/10.1037/a0026650", SEC),
 "feinberg2014": S("Feinberg, M., Willer, R., & Schultz, M.", 2014, "Gossip and ostracism promote cooperation in groups", "Psychological Science, 25(3), 656-664", "https://doi.org/10.1177/0956797613510184", SEC),
 "gilovich1998": S("Gilovich, T., Savitsky, K., & Medvec, V. H.", 1998, "The illusion of transparency: Biased assessments of others' ability to read one's emotional states", "Journal of Personality and Social Psychology, 75(2), 332-346", "https://doi.org/10.1037/0022-3514.75.2.332", SECOND + " (Cornell students; about half of liars thought they were caught, about a quarter were)"),
 "brummelman2015": S("Brummelman, E., Thomaes, S., Nelemans, S. A., de Castro, B. O., Overbeek, G., & Bushman, B. J.", 2015, "Origins of narcissism in children", "Proceedings of the National Academy of Sciences, 112(12), 3659-3662", "https://doi.org/10.1073/pnas.1420870112", SEC + " (overvaluation predicted narcissism; warmth predicted self-esteem; first prospective longitudinal test)"),
 "kealy2015": S("Kealy, D., et al.", 2015, "On overvaluing parental overvaluation as the origins of narcissism", "Proceedings of the National Academy of Sciences, 112(21) (commentary on Brummelman et al.)", "https://www.pnas.org/doi/10.1073/pnas.1507035112", "web search 2026-10-05: title and existence confirmed; author attribution taken from the published reply 'Reply to Kealy et al.' (a search summary named different authors, so no author is named in the script)"),
 "antonakis2011": S("Antonakis, J., Fenley, M., & Liechti, S.", 2011, "Can charisma be taught? Tests of two interventions", "Academy of Management Learning & Education, 10(3), 374-396", "https://doi.org/10.5465/amle.2010.0012", SEC + " (12 charismatic leadership tactics; Study 1 34 managers randomized; Study 2 41 MBA participants)"),
 "asch1956": S("Asch, S. E.", 1956, "Studies of independence and conformity: I. A minority of one against a unanimous majority", "Psychological Monographs, 70(9), 1-70", "https://doi.org/10.1037/h0093718", SECOND + " (123 participants; about three-quarters conformed at least once; about a third of critical trials)"),
 "bond1996": S("Bond, R., & Smith, P. B.", 1996, "Culture and conformity: A meta-analysis of studies using Asch's line judgment task", "Psychological Bulletin, 119(1), 111-137", "https://doi.org/10.1037/0033-2909.119.1.111", SEC + " (133 studies, 17 countries, 24,617 participants; higher in collectivist cultures)"),
 "kross2011": S("Kross, E., Berman, M. G., Mischel, W., Smith, E. E., & Wager, T. D.", 2011, "Social rejection shares somatosensory representations with physical pain", "Proceedings of the National Academy of Sciences, 108(15), 6270-6275", "https://doi.org/10.1073/pnas.1102693108", SEC + " (recent unwanted breakup; ex photo; overlap in secondary somatosensory cortex and dorsal posterior insula)"),
 "woo2014": S("Woo, C.-W., Koban, L., Kross, E., et al.", 2014, "Separate neural representations for physical pain and social rejection", "Nature Communications, 5, 5380", "https://doi.org/10.1038/ncomms6380", SEC + " (60 participants; separate patterns)"),
 "dutton1981": S("Dutton, D. G., & Painter, S. L.", 1981, "Traumatic bonding: The development of emotional attachments in battered women and other relationships of intermittent abuse", "Victimology, 6(1-4), 139-155", "https://scholar.google.com/scholar?q=Dutton+Painter+1981+Traumatic+bonding+Victimology+6+139-155", SECOND + " (citation and the two conditions: power imbalance and intermittent abuse)"),
 "dutton1993": S("Dutton, D. G., & Painter, S.", 1993, "Emotional attachments in abusive relationships: A test of traumatic bonding theory", "Violence and Victims, 8(2), 105-120", "https://pubmed.ncbi.nlm.nih.gov/8193056/", SEC + " (75 women; abuse, intermittency and power differentials accounted for 55% of variance in attachment at six-month follow-up)"),
}

DAYS = {}

DAYS[51] = dict(
 title="Does Hearing Your Own Name Grab Attention?",
 description_core="Does your own name cut through noise? About a third of people noticed their own name in an audio channel they were told to ignore, and one set of experiments found that a salesperson remembering a name increased compliance with a purchase request.",
 primary=["moray1959", "wood1995", "howard1995"],
 hashtags=["#psychology", "#shorts", "#cocktailparty", "#attention", "#persuasion", "#psychologyfacts"],
 caveats="The 'about a third' figure is from Moray (1959) and the 1995 replication; it implies most people did not notice. The persuasion finding is from three experiments in consumer settings and is not a guarantee.",
 thumb=(["YOUR NAME", "GRABS ATTENTION?"], 1, 0),
 scenes=[
  ("H", [("Does hearing your own name really grab your attention?", "PLAN")], "Does your name grab you?", "Stickman turning toward a sound.", "think/neutral/C; text:NAME@R"),
  ("E", [("In 1959, Neville Moray ran a listening experiment where people focused on one ear and ignored the other.", "moray1959")], "1959: ignore one ear", "Headphones.", "stand/neutral/L; text:1959@TR; text:ONE EAR@R"),
  ("E", [("About a third of them noticed their own name in the ear they were ignoring.", "moray1959")], "~1/3 heard their own name", "Bar at about a third.", "stand/smile/L; bars:noticed=33%,did not=67%@R"),
  ("E", [("In 1995, Nicole Wood and Nelson Cowan repeated the experiment.", "wood1995")], "1995: a replication", "Repeat arrows.", "point/neutral/L; text:1995@TR; loop@R"),
  ("E", [("Again, only about a third noticed their name.", "wood1995")], "Again, only ~1/3 noticed", "Bar at about a third.", "stand/neutral/L; bars:noticed=33%,did not=67%@R"),
  ("E", [("That means about two thirds did not notice it.", "wood1995")], "~2/3 did not notice", "Taller bar.", "shrug/neutral/L; bars:noticed=33%,did not=67%@R"),
  ("E", [("In 1995, Daniel Howard and colleagues ran three experiments on names and persuasion.", "howard1995")], "1995: names and persuasion", "Name tag.", "stand/neutral/L; tag:NAME@R; text:3 STUDIES@TR"),
  ("E", [("In them, a salesperson remembering the customer's name increased compliance with a purchase request.", "howard1995")], "Remembered name: more compliance", "Handshake.", "stand/smile/L; check@R"),
  ("T", [("So your name can catch the attention of some people, and remembering a name may help persuade.", "moray1959,wood1995,howard1995")], "Names catch some, may persuade", "Stickman nodding.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: how can a team of smart people make a terrible decision together?", "PLAN")], "Tomorrow: smart teams, bad calls", "Team around a table.", "stand/neutral/L; crowd:5@R"),
 ])

DAYS[52] = dict(
 title="Groupthink: Can Smart Teams Make Dumb Decisions?",
 description_core="Janis described groupthink in 1972 using foreign-policy fiascoes like the Bay of Pigs. A 1998 review found case studies supported the model but experimental validation was lacking, and concluded it was too early to judge the theory.",
 primary=["janis1972", "esser1998"],
 hashtags=["#psychology", "#shorts", "#groupthink", "#decisionmaking", "#socialpsychology", "#psychologyfacts"],
 caveats="Groupthink is influential but contested; the video presents it as an unproven theory. The term appeared before Janis, so the video says he described it in his book rather than that he coined it.",
 thumb=(["GROUPTHINK:", "SMART TEAMS,", "DUMB CALLS?"], 2, 0),
 scenes=[
  ("H", [("Can a team of smart people make a terrible decision together?", "PLAN")], "Can smart teams fail?", "Team around a table.", "think/neutral/C; crowd:5@R"),
  ("E", [("In 1972, psychologist Irving Janis described groupthink in his book, Victims of Groupthink.", "janis1972")], "1972: Janis describes groupthink", "Book.", "point/neutral/L; text:1972@TR; text:GROUPTHINK@R"),
  ("E", [("He studied foreign-policy fiascoes such as the Bay of Pigs invasion and Pearl Harbor.", "janis1972")], "Bay of Pigs, Pearl Harbor", "Stack of files.", "stand/neutral/L; list:BAY OF PIGS,PEARL HARBOR@R"),
  ("E", [("He argued groupthink kept contradictory views from being expressed and evaluated.", "janis1972")], "Contradictory views kept quiet", "Mouth covered.", "shock/worry/L; text:SILENCED@R"),
  ("E", [("In 1998, James Esser reviewed twenty-five years of groupthink research.", "esser1998")], "1998: a 25-year review", "Calendar.", "stand/neutral/L; text:1998@TR; numbers:25 YRS@R"),
  ("E", [("He noted that case studies had confirmed the model.", "esser1998")], "Case studies fit the model", "Check.", "stand/smile/L; check@R"),
  ("E", [("But reviews noted a lack of experimental validation.", "esser1998")], "But experiments lacked", "Empty lab flask.", "shrug/worry/L; cross@R"),
  ("E", [("Esser concluded it was too early to pass judgment on groupthink theory.", "esser1998")], "Too early to judge", "Scale.", "shrug/neutral/L; scale@R"),
  ("E", [("He said more research was needed to decide whether to keep, modify or discard it.", "esser1998")], "Keep, modify or discard?", "Three options.", "think/neutral/L; list:KEEP,MODIFY,DISCARD@R"),
  ("T", [("So groupthink is a vivid and influential idea that still lacks firm experimental proof.", "janis1972,esser1998")], "Influential, still unproven", "Stickman with a question mark.", "stand/neutral/L; qmark@R"),
  ("C", [("Tomorrow: what really happened in the Stanford prison experiment?", "PLAN")], "Tomorrow: Stanford prison study", "Prison bars.", "stand/neutral/L; text:STANFORD?@R"),
 ])

DAYS[53] = dict(
 title="The Stanford Prison Experiment and Why It's Disputed",
 description_core="The Stanford prison study ran for six days with 24 students. A 2019 archival analysis argued the guards had been coached, and a BBC replication reported guards did not identify strongly with their role.",
 primary=["haney1973", "letexier2019", "reicher2006"],
 hashtags=["#psychology", "#shorts", "#stanfordprisonexperiment", "#zimbardo", "#socialpsychology", "#psychologyfacts"],
 caveats="The video presents the criticisms as reported by the authors (Le Texier 2019; Reicher & Haslam 2006), not as settled fact. Zimbardo and colleagues defended the study. Haney et al. figures come from secondary summaries.",
 thumb=(["STANFORD PRISON", "STUDY: DISPUTED"], 1, 0),
 scenes=[
  ("H", [("Did ordinary students really turn into cruel guards in a mock prison?", "PLAN")], "Did students turn cruel?", "Prison bars.", "think/worry/C; text:PRISON@R"),
  ("E", [("In 1971, Philip Zimbardo's team at Stanford ran a simulated prison study with 24 selected male students.", "haney1973")], "1971: 24 students, a mock prison", "Prison bars.", "stand/neutral/L; text:1971@TR; numbers:24@R"),
  ("E", [("Ten became prisoners and eleven became guards.", "haney1973")], "10 prisoners, 11 guards", "Two groups.", "point/neutral/L; list:10 PRISONERS,11 GUARDS@R"),
  ("E", [("It was planned for two weeks but ended after six days.", "haney1973")], "Planned 14 days, ended day 6", "Calendar.", "shock/neutral/L; bars:planned=14d,actual=6d@R"),
  ("E", [("In 2019, Thibault Le Texier analyzed archival records and argued the guards had been coached.", "letexier2019")], "2019: archives suggest coaching", "Archive box.", "point/neutral/L; text:2019@TR; text:ARCHIVES@R"),
  ("E", [("He reported they were told which behavior was wanted.", "letexier2019")], "Told which behavior was wanted", "Instruction card.", "stand/worry/L; list:BE TOUGH@R"),
  ("E", [("In a BBC replication reported in 2006, Stephen Reicher and Alexander Haslam found the guards did not identify with their role.", "reicher2006")], "BBC replication: guards didn't identify", "TV screen.", "stand/neutral/L; text:BBC STUDY@R"),
  ("E", [("These are the authors' reported findings, and the original team defended its study.", "letexier2019,reicher2006")], "Authors' claims; team disagrees", "Scale.", "shrug/neutral/L; scale@R"),
  ("T", [("So this famous experiment is now seriously disputed, and does not simply show that situations make people cruel.", "haney1973,letexier2019,reicher2006")], "Famous, but seriously disputed", "Stickman with a question mark.", "stand/neutral/L; qmark@R"),
  ("C", [("Tomorrow: why do people gossip so much?", "PLAN")], "Tomorrow: why people gossip", "Two stickmen whispering.", "stand/neutral/L; crowd:2@R"),
 ])

DAYS[54] = dict(
 title="Why Do People Gossip? What Research Shows",
 description_core="Is gossip mostly cruel? In everyday recordings of 467 people, gossip was mostly neutral, and experiments suggest sharing reputational information can be prosocial and can help groups cooperate.",
 primary=["dunbar1997", "robbins2020", "feinberg2012", "feinberg2014"],
 hashtags=["#psychology", "#shorts", "#gossip", "#socialpsychology", "#relationships", "#psychologyfacts"],
 caveats="Findings come from specific samples and tasks (observed conversations, recorded daily speech, lab group games), so they do not describe all gossip. The video does not say gossip is always harmless.",
 thumb=(["WHY DO PEOPLE", "GOSSIP?"], 1, 0),
 scenes=[
  ("H", [("Why do people gossip so much?", "PLAN")], "Why do people gossip?", "Two stickmen whispering.", "think/neutral/C; crowd:2@R"),
  ("E", [("In 1997, Robin Dunbar and colleagues analyzed 45 natural conversations.", "dunbar1997")], "1997: 45 natural conversations", "Speech bubbles.", "stand/neutral/L; text:1997@TR; numbers:45@R"),
  ("E", [("About two thirds of the conversation time went to social topics.", "dunbar1997")], "~2/3 about social topics", "Bar at two thirds.", "stand/smile/L; bars:social=67%,other=33%@R"),
  ("E", [("In 2020, Megan Robbins and Alexander Karan sampled everyday conversations of 467 people.", "robbins2020")], "2020: 467 people sampled", "Counter.", "stand/neutral/L; text:2020@TR; numbers:467@R"),
  ("E", [("They found gossip was mostly neutral, not negative.", "robbins2020")], "Mostly neutral, not negative", "Neutral face icon.", "point/neutral/L; text:NEUTRAL@R"),
  ("E", [("On average, it took up about 52 minutes of an awake day.", "robbins2020")], "~52 minutes a day awake", "Clock.", "shock/neutral/L; clock@R"),
  ("E", [("In 2012, Matthew Feinberg and colleagues described sharing reputational information as a form of prosocial behavior.", "feinberg2012")], "2012: gossip can be prosocial", "Heart.", "stand/smile/L; text:2012@TR; text:PROSOCIAL@R"),
  ("E", [("And in 2014, his team reported that gossip and ostracism promote cooperation in groups.", "feinberg2014")], "2014: gossip helps cooperation", "Group working together.", "stand/smile/L; text:2014@TR; crowd:5@R"),
  ("E", [("These findings come from specific samples and tasks, so they don't describe all gossip.", "dunbar1997,robbins2020,feinberg2012,feinberg2014")], "Specific samples, not all gossip", "Scale.", "shrug/neutral/L; scale@R"),
  ("T", [("So gossip is common, often neutral, and sometimes helps groups cooperate.", "dunbar1997,robbins2020,feinberg2014")], "Common, often neutral", "Stickman with a check.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: can other people really read how you feel?", "PLAN")], "Tomorrow: can others read you?", "Face with question mark.", "stand/neutral/L; qmark@R"),
 ])

DAYS[55] = dict(
 title="The Illusion of Transparency: Can People Read You?",
 description_core="Do others see your nervousness? In a classic study, about half of liars thought they had been caught, but only about a quarter actually were. Psychologists call this the illusion of transparency.",
 primary=["gilovich1998"],
 hashtags=["#psychology", "#shorts", "#illusionoftransparency", "#anxiety", "#socialpsychology", "#psychologyfacts"],
 caveats="The liar figures (about half vs about a quarter) come from secondary summaries of one experiment in Gilovich, Savitsky & Medvec (1998). The sample was Cornell students; results may differ elsewhere.",
 thumb=(["CAN PEOPLE", "READ YOU?"], 1, 0),
 scenes=[
  ("H", [("Can other people really read how you feel?", "PLAN")], "Can others read you?", "Stickman with a see-through chest.", "think/worry/C; text:NERVOUS?@R"),
  ("E", [("In 1998, Thomas Gilovich, Kenneth Savitsky and Victoria Medvec published research on the illusion of transparency.", "gilovich1998")], "1998: the illusion of transparency", "Glass pane.", "point/neutral/L; text:1998@TR; text:TRANSPARENCY@R"),
  ("E", [("It's the tendency to overestimate how well others can read your emotional states.", "gilovich1998")], "We overestimate how readable we are", "Eye icon.", "stand/neutral/L; text:OVERESTIMATE@R"),
  ("E", [("In one experiment, Cornell students told lies.", "gilovich1998")], "Cornell students told lies", "Speech bubble.", "stand/neutral/L; bubble:a lie@TR"),
  ("E", [("Observers then watched each student and judged whether that student was lying.", "gilovich1998")], "Observers judged who was lying", "Magnifier.", "point/neutral/L; qmark@R"),
  ("E", [("About half of the liars thought they had been caught.", "gilovich1998")], "Liars: ~50% thought they were caught", "Bar at 50%.", "shock/worry/L; bars:thought caught=50%,actually caught=25%@R"),
  ("E", [("But only about a quarter actually were.", "gilovich1998")], "Actually caught: ~25%", "Bar at 25%.", "shrug/neutral/L; bars:thought caught=50%,actually caught=25%@R"),
  ("E", [("So the liars overestimated how transparent they were.", "gilovich1998")], "They overestimated their transparency", "Gap between bars.", "think/neutral/L; bars:thought caught=50%,actually caught=25%@R"),
  ("E", [("This was a laboratory study with students, not every real-world situation, so treat it as one data point.", "gilovich1998")], "Lab study, students", "Lab flask.", "shrug/neutral/L; text:LAB@R"),
  ("T", [("So in this research, people were less readable than they feared.", "gilovich1998")], "Less readable than they feared", "Stickman relaxing.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: is there a real research difference between narcissism and confidence?", "PLAN")], "Tomorrow: narcissism vs confidence", "Mirror.", "stand/neutral/L; qmark@R"),
 ])

DAYS[56] = dict(
 title="Narcissism vs. Confidence: What Research Suggests",
 description_core="Are narcissism and healthy self-esteem the same? A 2015 longitudinal study reported that parental overvaluation predicted narcissism while parental warmth predicted self-esteem, and a published commentary questioned how far the findings go.",
 primary=["brummelman2015", "kealy2015"],
 hashtags=["#psychology", "#shorts", "#narcissism", "#selfesteem", "#parenting", "#psychologyfacts"],
 caveats="One study with a published commentary challenging it; the video says the origins of narcissism are debated. Narcissism in children is a trait measure, not a diagnosis. No person is labelled.",
 thumb=(["NARCISSISM VS", "CONFIDENCE"], 1, 0),
 scenes=[
  ("H", [("Is there a real research difference between narcissism and confidence?", "PLAN")], "Narcissism vs confidence", "Mirror.", "think/neutral/C; text:VS@R"),
  ("E", [("In 2015, Eddie Brummelman and colleagues followed children over time to study where narcissism comes from.", "brummelman2015")], "2015: children followed over time", "Calendar.", "stand/neutral/L; text:2015@TR; text:LONGITUDINAL@R"),
  ("E", [("They reported that parental overvaluation predicted narcissism.", "brummelman2015")], "Overvaluation predicted narcissism", "Rising line.", "point/neutral/L; lines:overvaluation,narcissism,up@R"),
  ("E", [("Parental warmth predicted self-esteem instead.", "brummelman2015")], "Warmth predicted self-esteem", "Heart.", "stand/smile/L; text:WARMTH@R"),
  ("E", [("They described it as the first prospective longitudinal test of this question.", "brummelman2015")], "First prospective longitudinal test", "Timeline.", "stand/neutral/L; arrow@R"),
  ("E", [("The results suggest narcissism and self-esteem have different origins.", "brummelman2015")], "Different origins", "Two arrows.", "think/neutral/L; list:NARCISSISM,SELF-ESTEEM@R"),
  ("E", [("A published commentary argued that parental overvaluation may be overvalued as an explanation.", "kealy2015")], "A commentary pushed back", "Speech bubble.", "shrug/worry/L; bubble:overvalued?@TR"),
  ("E", [("So the origins of narcissism are still debated.", "brummelman2015,kealy2015")], "Origins still debated", "Scale.", "shrug/neutral/L; scale@R"),
  ("E", [("These are measures of traits in children, not diagnoses of anyone, and no real person is being labelled here.", "brummelman2015")], "Traits, not diagnoses", "Cross.", "stand/neutral/L; cross@R"),
  ("T", [("So confidence and narcissism appear to differ, and their origins may too, but the picture is still debated.", "brummelman2015,kealy2015")], "They differ; origins debated", "Stickman with a question mark.", "stand/neutral/L; qmark@R"),
  ("C", [("Tomorrow: what do charismatic leaders actually do?", "PLAN")], "Tomorrow: what charisma is", "Spotlight.", "stand/neutral/L; spotlight@R"),
 ])

DAYS[57] = dict(
 title="Can Charisma Be Taught? What Research Found",
 description_core="Is charisma a gift or a skill? In 2011, researchers identified twelve charismatic leadership tactics and found that training in them improved leaders' ratings in two studies.",
 primary=["antonakis2011"],
 hashtags=["#psychology", "#shorts", "#charisma", "#leadership", "#communication", "#psychologyfacts"],
 caveats="Two studies (34 managers; 41 MBA participants), with charisma measured by others' ratings. The video does not claim charismatic leaders make good decisions.",
 thumb=(["CAN CHARISMA", "BE TAUGHT?"], 1, 0),
 scenes=[
  ("H", [("Is charisma a gift, or a set of learnable tactics?", "PLAN")], "Gift or learnable?", "Spotlight on a speaker.", "think/neutral/C; spotlight@R"),
  ("E", [("In 2011, John Antonakis and colleagues tested whether charisma can be taught.", "antonakis2011")], "2011: can charisma be taught?", "Teacher board.", "point/neutral/L; text:2011@TR; text:TAUGHT?@R"),
  ("E", [("They identified twelve charismatic leadership tactics.", "antonakis2011")], "Twelve charismatic tactics", "Counter.", "stand/neutral/L; numbers:12@R"),
  ("E", [("These included things like using metaphors and rhetorical questions.", "antonakis2011")], "Metaphors, rhetorical questions", "Two speech bubbles.", "stand/neutral/L; list:METAPHORS,QUESTIONS@R"),
  ("E", [("In the first study, 34 managers were randomized into training or not.", "antonakis2011")], "Study 1: 34 managers randomized", "Counter.", "stand/neutral/L; numbers:34@R; text:STUDY 1@TR"),
  ("E", [("In the second study, 41 MBA participants took part.", "antonakis2011")], "Study 2: 41 MBA participants", "Counter.", "stand/neutral/L; numbers:41@R; text:STUDY 2@TR"),
  ("E", [("Training improved how charismatic and effective the leaders were rated.", "antonakis2011")], "Training improved the ratings", "Rising bar.", "stand/smile/L; bars:before=h35,after=h70@R"),
  ("E", [("The studies tested specific behaviors, as judged by others, not personality overall.", "antonakis2011")], "Specific behaviors, rated by others", "Rating card.", "point/neutral/L; text:RATINGS@R"),
  ("E", [("Ratings of charisma alone don't tell us whether a leader's decisions are good.", "antonakis2011")], "Charisma isn't good judgment", "Scale.", "shrug/neutral/L; scale@R"),
  ("T", [("So in these studies, charisma looked more like a learnable set of behaviors than a fixed gift.", "antonakis2011")], "Looked learnable, not fixed", "Stickman with a smile.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: would you give a wrong answer just because everyone else did?", "PLAN")], "Tomorrow: the Asch experiment", "Crowd with one stickman.", "stand/neutral/L; crowd:5@R"),
 ])

DAYS[58] = dict(
 title="The Asch Conformity Experiment, Explained",
 description_core="Would you give a wrong answer to match the group? In Asch's line studies, about three-quarters of participants conformed at least once, and a 133-study meta-analysis found higher conformity in collectivist cultures.",
 primary=["asch1956", "bond1996"],
 hashtags=["#psychology", "#shorts", "#asch", "#conformity", "#socialpsychology", "#psychologyfacts"],
 caveats="Asch figures are from secondary summaries of the 1956 monograph. They describe a lab task with an obvious answer, not everyday opinions. The meta-analysis result is a group average, not a statement about any individual or country.",
 thumb=(["WOULD YOU", "CONFORM?"], 1, 0),
 scenes=[
  ("H", [("Would you give a wrong answer just because everyone else did?", "PLAN")], "Would you go along?", "Crowd with one stickman.", "think/neutral/C; crowd:5@R"),
  ("E", [("In the 1950s, Solomon Asch asked people to match line lengths in a group.", "asch1956")], "1950s: matching line lengths", "Lines on a card.", "stand/neutral/L; text:1950s@TR; text:LINES@R"),
  ("E", [("The others were working with him, and on some trials they gave obviously wrong answers.", "asch1956")], "Others gave wrong answers on purpose", "Crowd pointing.", "point/neutral/L; crowd:5@R"),
  ("E", [("In his 1956 report, 123 participants took part.", "asch1956")], "1956 report: 123 participants", "Counter.", "stand/neutral/L; text:1956@TR; numbers:123@R"),
  ("E", [("About three quarters conformed at least once.", "asch1956")], "~3/4 conformed at least once", "Bar at 75%.", "shock/neutral/L; bars:conformed once=75%@R"),
  ("E", [("About a third of the critical answers matched the wrong majority.", "asch1956")], "~1/3 of critical answers", "Bar at 33%.", "stand/neutral/L; bars:critical answers=33%@R"),
  ("E", [("In 1996, Rod Bond and Peter Smith analyzed 133 studies from 17 countries.", "bond1996")], "1996: 133 studies, 17 countries", "Globe.", "stand/neutral/L; text:1996@TR; numbers:133@R"),
  ("E", [("Those included 24,617 participants.", "bond1996")], "24,617 participants", "Counter.", "stand/neutral/L; numbers:24,617@R"),
  ("E", [("They found conformity was higher in collectivist cultures.", "bond1996")], "Higher in collectivist cultures", "Taller bar.", "point/neutral/L; bars:individualist=h40,collectivist=h65@R"),
  ("E", [("These were lab tasks with obvious answers, not everyday opinions.", "asch1956")], "Lab tasks, obvious answers", "Lines card.", "shrug/neutral/L; text:LAB@R"),
  ("T", [("So group pressure can sway answers, and how much seems to vary across cultures.", "asch1956,bond1996")], "Group pull varies by culture", "Stickman with a small arrow.", "stand/neutral/L; check@R"),
  ("C", [("Tomorrow: do breakups really hurt like physical pain?", "PLAN")], "Tomorrow: breakups and pain", "Broken heart.", "stand/neutral/L; qmark@R"),
 ])

DAYS[59] = dict(
 title="Do Breakups Hurt Like Physical Pain? It's Contested",
 description_core="Does heartbreak overlap with physical pain in the brain? A 2011 study found overlapping activity in pain-related regions after a recent breakup, while a 2014 study with 60 participants found separate patterns for physical pain and social rejection.",
 primary=["kross2011", "woo2014"],
 hashtags=["#psychology", "#shorts", "#breakup", "#heartbreak", "#neuroscience", "#psychologyfacts"],
 caveats="Contested: the two studies reach different conclusions about overlap vs separate patterns. Both measure brain activity, not injury. The 'heat pain' detail in Kross et al. is from the study design as commonly summarized.",
 thumb=(["DO BREAKUPS HURT", "LIKE PAIN?"], 1, 0),
 scenes=[
  ("H", [("Do breakups really hurt like physical pain?", "PLAN")], "Do breakups hurt like pain?", "Broken heart.", "think/worry/C; text:HEARTBREAK@R"),
  ("E", [("In 2011, Ethan Kross and colleagues studied people who had recently had an unwanted breakup.", "kross2011")], "2011: a recent unwanted breakup", "Broken heart.", "stand/worry/L; text:2011@TR; text:BREAKUP@R"),
  ("E", [("Participants viewed a photo of their ex.", "kross2011")], "Viewing a photo of an ex", "Photo frame.", "stand/neutral/L; text:PHOTO@R"),
  ("E", [("They also felt physical heat pain in the scanner.", "kross2011")], "Also: physical heat pain", "Thermometer.", "shock/neutral/L; text:HEAT@R"),
  ("E", [("Kross's team reported that activity overlapped in the secondary somatosensory cortex and the dorsal posterior insula during both experiences.", "kross2011")], "Overlap in two brain regions", "Brain with glowing areas.", "point/neutral/L; brain@R"),
  ("E", [("In 2014, Choong-Wan Woo and colleagues tested this question again with 60 participants.", "woo2014")], "2014: tested with 60 people", "Counter.", "stand/neutral/L; text:2014@TR; numbers:60@R"),
  ("E", [("They found separate brain patterns for physical pain and social rejection.", "woo2014")], "Separate patterns", "Two brains.", "point/neutral/L; list:PAIN,REJECTION@R"),
  ("E", [("So the two studies point in different directions.", "kross2011,woo2014")], "Studies point different ways", "Two arrows.", "shrug/neutral/L; list:OVERLAP,SEPARATE@R"),
  ("E", [("Both studies measured brain activity, not injury or damage, so neither shows a breakup physically harms the body.", "kross2011,woo2014")], "Brain activity, not injury", "Cross over a bandage.", "shrug/neutral/L; cross@R"),
  ("T", [("So breakups do activate pain-related areas, but whether that is the same as physical pain is still contested.", "kross2011,woo2014")], "Pain-related areas, same as pain? Contested", "Stickman with a question mark.", "shrug/neutral/L; qmark@R"),
  ("C", [("Tomorrow: what is trauma bonding?", "PLAN")], "Tomorrow: what is trauma bonding?", "Two linked hearts.", "stand/neutral/L; qmark@R"),
 ])

DAYS[60] = dict(
 title="Trauma Bonding: What the Theory Says",
 description_core="What is trauma bonding? A 1981 theory describes emotional attachments in relationships with a power imbalance and intermittent abuse, and a 1993 study of 75 women found these factors accounted for 55% of the variance in attachment six months later. This is educational, not a diagnosis. If you or someone you know is unsafe, contact local support services.",
 primary=["dutton1981", "dutton1993"],
 hashtags=["#psychology", "#shorts", "#traumabonding", "#relationships", "#mentalhealth", "#psychologyfacts"],
 caveats="Sensitive topic. Presented as a research-based theory tested in one sample, not a diagnosis, and without blame or advice. The description adds a support note. The 1993 figures are from the abstract as quoted in search results.",
 thumb=(["TRAUMA BONDING:", "THE THEORY"], 1, 0),
 scenes=[
  ("H", [("What is trauma bonding?", "PLAN")], "What is trauma bonding?", "Two linked hearts.", "think/neutral/C; qmark@R"),
  ("E", [("In 1981, Donald Dutton and Susan Painter proposed traumatic bonding theory.", "dutton1981")], "1981: traumatic bonding theory", "Book.", "point/neutral/L; text:1981@TR; text:THEORY@R"),
  ("E", [("It describes emotional attachments that develop in relationships of intermittent abuse.", "dutton1981")], "Attachment in intermittent abuse", "Linked hearts.", "stand/neutral/L; text:INTERMITTENT@R"),
  ("E", [("The theory names two conditions: a power imbalance and intermittent abuse.", "dutton1981")], "Two conditions", "Two-item list.", "stand/neutral/L; list:POWER IMBALANCE,INTERMITTENT ABUSE@R"),
  ("E", [("In 1993, Dutton and Painter tested the theory with 75 women.", "dutton1993")], "1993: tested with 75 women", "Counter.", "stand/neutral/L; text:1993@TR; numbers:75@R"),
  ("E", [("Abuse, its intermittency and power differences together accounted for 55 percent of the variance in attachment six months later.", "dutton1993")], "55% of variance in attachment", "Bar at 55%.", "point/neutral/L; bars:explained=55%@R"),
  ("E", [("That is a result from one sample, not a diagnosis of anyone, and it does not apply to every relationship.", "dutton1993")], "One sample, not a diagnosis", "Cross.", "shrug/neutral/L; cross@R"),
  ("E", [("These studies describe patterns, not blame for anyone in such a relationship.", "dutton1981,dutton1993")], "Patterns, not blame", "Open hands.", "stand/neutral/L; text:NO BLAME@R"),
  ("T", [("So trauma bonding is a research-based theory about power imbalance and intermittent abuse, not a diagnosis.", "dutton1981,dutton1993")], "A theory, not a diagnosis", "Stickman with a small check.", "stand/neutral/L; check@R"),
  ("C", [("Tomorrow: is Blue Monday actually real?", "PLAN")], "Tomorrow: is Blue Monday real?", "Calendar.", "stand/neutral/L; text:BLUE MONDAY?@R"),
 ])
