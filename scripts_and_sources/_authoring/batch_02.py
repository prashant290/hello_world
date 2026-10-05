"""Days 11-20 (Month 1)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common_sources import S, SEC, SECOND

SOURCES = {
 "zwicky2005": S("Zwicky, A. M.", 2005, "Just between Dr. Language and I (Language Log post introducing 'frequency illusion')", "Language Log (blog)", "https://languagelog.ldc.upenn.edu/nll/?p=42180", "web search 2026-10-05: term 'frequency illusion' first attested in Zwicky's Language Log post (sources differ on 2005 vs 2006); confirmed via Language Log/OED coverage"),
 "pacificstandard": S("Pacific Standard (magazine)", 2014, "There's a name for that: The Baader-Meinhof phenomenon", "Pacific Standard", "https://psmag.com/?p=38449", "web search 2026-10-05: name traced to a 1994 letter to a newspaper column; magazine article confirmed in results"),
 "simons1999": S("Simons, D. J., & Chabris, C. F.", 1999, "Gorillas in our midst: Sustained inattentional blindness for dynamic events", "Perception, 28(9), 1059-1074", "https://doi.org/10.1068/p281059", SEC + " (design confirmed; exact miss rate varied by condition so only 'many' is claimed)"),
 "danziger2011": S("Danziger, S., Levav, J., & Avnaim-Pesso, L.", 2011, "Extraneous factors in judicial decisions", "Proceedings of the National Academy of Sciences, 108(17), 6889-6892", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3198355", SEC + " (1,000+ decisions, eight judges, ~65% favorable after break)"),
 "weinshall2011": S("Weinshall-Margel, K., & Shapard, J.", 2011, "Overlooked factors in the analysis of parole decisions", "Proceedings of the National Academy of Sciences, 108(42), E833", "https://cris.huji.ac.il/en/publications/overlooked-factors-in-the-analysis-of-parole-decisions/", SEC),
 "hagger2016": S("Hagger, M. S., Chatzisarantis, N. L. D., et al.", 2016, "A multilab preregistered replication of the ego-depletion effect", "Perspectives on Psychological Science, 11(4), 546-573", "https://research.tilburguniversity.edu/en/publications/a-multi-lab-pre-registered-replication-of-the-ego-depletion-effec/", SEC + " (23 labs, N = 2,141, d = 0.04, CI includes zero)"),
 "arkes1985": S("Arkes, H. R., & Blumer, C.", 1985, "The psychology of sunk cost", "Organizational Behavior and Human Decision Processes, 35(1), 124-140", "https://cognition.aau.at/bg/BA/Arkes%20%26%20Blumer%201985.pdf", SEC + " (theater season-ticket field study at $15/$13/$8)"),
 "thorndike1920": S("Thorndike, E. L.", 1920, "A constant error in psychological ratings", "Journal of Applied Psychology, 4(1), 25-29", "https://www.Gwern.net/doc/psychology/personality/1920-thorndike.pdf", SEC + " (officers rating soldiers; term 'halo')"),
 "dion1972": S("Dion, K., Berscheid, E., & Walster, E.", 1972, "What is beautiful is good", "Journal of Personality and Social Psychology, 24(3), 285-290", "https://garfield.library.upenn.edu/classics1990/A1990EH31100001.pdf", SEC),
 "eagly1991": S("Eagly, A. H., Ashmore, R. D., Makhijani, M. G., & Longo, L. C.", 1991, "What is beautiful is good, but...: A meta-analytic review of research on the physical attractiveness stereotype", "Psychological Bulletin, 110(1), 109-128", "https://data.gesis.org/gesiskg/resource/zis-EaglyAshmoreMakhijani1991What", SEC),
 "norton2012": S("Norton, M. I., Mochon, D., & Ariely, D.", 2012, "The IKEA effect: When labor leads to love", "Journal of Consumer Psychology, 22(3), 453-460", "https://dash.harvard.edu/handle/1/12136084", SEC + " (four studies; boundary conditions quoted in abstract summaries)"),
 "wittmann2005": S("Wittmann, M., & Lehnhoff, S.", 2005, "Age effects in perception of time", "Psychological Reports, 97(3), 921-935", "https://publications.igpp.de/index.cgi/bibliography/VMPBGZ3B", SEC + " (499 participants aged 14-94)"),
 "friedman2010": S("Friedman, W. J., & Janssen, S. M. J.", 2010, "Aging and the speed of time", "Acta Psychologica, 134(2), 130-141", "https://pubmed.ncbi.nlm.nih.gov/20163781/", SEC + " (1,865 adults aged 16-80)"),
 "darley1968": S("Darley, J. M., & Latané, B.", 1968, "Bystander intervention in emergencies: Diffusion of responsibility", "Journal of Personality and Social Psychology, 8(4), 377-383", "https://stafforini.com/works/darley-1968-bystander-intervention-emergencies/", SECOND + " (about 85% helped alone vs about 31% with four others)"),
 "fischer2011": S("Fischer, P., Krueger, J. I., Greitemeyer, T., et al.", 2011, "The bystander-effect: A meta-analytic review on bystander intervention in dangerous and non-dangerous emergencies", "Psychological Bulletin, 137(4), 517-537", "https://pred.uni-regensburg.de/id/eprint/20599/", SEC + " (105 effect sizes, 7,700+ participants)"),
 "philpot2020": S("Philpot, R., Liebst, L. S., Levine, M., Bernasco, W., & Lindegaard, M. R.", 2020, "Would I be helped? Cross-national CCTV footage shows that intervention is the norm in public conflicts", "American Psychologist, 75(1), 66-75", "https://academicworks.cuny.edu/jj_pubs/167", SEC + " (219 incidents in Amsterdam, Lancaster, Cape Town; interventions in more than 90%)"),
 "manning2007": S("Manning, R., Levine, M., & Collins, A.", 2007, "The Kitty Genovese murder and the social psychology of helping: The parable of the 38 witnesses", "American Psychologist, 62(6), 555-562", "https://eprints.lancs.ac.uk/id/eprint/3591/", SEC),
 "soroka2019": S("Soroka, S., Fournier, P., & Nir, L.", 2019, "Cross-national evidence of a negativity bias in psychophysiological reactions to news", "Proceedings of the National Academy of Sciences, 116(38), 18888-18892", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6754543", SEC + " (17 countries, 1,156 participants)"),
 "trussler2014": S("Trussler, M., & Soroka, S.", 2014, "Consumer demand for cynical and negative news frames", "International Journal of Press/Politics, 19(3), 360-379", "https://journals.sagepub.com/doi/10.1177/1940161214524832", SEC),
 "huber1982": S("Huber, J., Payne, J. W., & Puto, C.", 1982, "Adding asymmetrically dominated alternatives: Violations of regularity and the similarity hypothesis", "Journal of Consumer Research, 9(1), 90-98", "https://apps.dtic.mil/sti/tr/pdf/ADA111658.pdf", SEC),
 "frederick2014": S("Frederick, S., Lee, L., & Baskin, E.", 2014, "The limits of attraction", "Journal of Marketing Research, 51(4), 487-507", "https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/The-Limits-of-Attraction.pdf", SEC + " (abstract quoted)"),
 "steel2007": S("Steel, P.", 2007, "The nature of procrastination: A meta-analytic and theoretical review of quintessential self-regulatory failure", "Psychological Bulletin, 133(1), 65-94", "https://stafforini.com/works/steel-2007-nature-procrastination-metaanalytic/", SEC + " (691 correlations)"),
 "sirois2013": S("Sirois, F., & Pychyl, T.", 2013, "Procrastination and the priority of short-term mood regulation: Consequences for future self", "Social and Personality Psychology Compass, 7(2), 115-127", "https://eprints.whiterose.ac.uk/id/eprint/91793/", SEC),
}

DAYS = {}

DAYS[11] = dict(
 title="Why You Suddenly See It Everywhere",
 description_core="Ever learn a new word and then see it everywhere? Linguist Arnold Zwicky called it the frequency illusion, and a famous attention study shows we miss much of what we're not focused on.",
 primary=["zwicky2005", "simons1999"],
 hashtags=["#psychology", "#shorts", "#frequencyillusion", "#attention", "#brain", "#psychologyfacts"],
 caveats="INFORMAL TERM. 'Frequency illusion' and 'Baader-Meinhof phenomenon' come from a linguist's blog and a newspaper letter, not from lab experiments. The explanation (attention and noticing) is a widely offered idea, not directly tested in the cited studies; Simons & Chabris demonstrates limits of attention, not the frequency illusion itself. The video hedges with 'one idea'.",
 thumb=(["SEEING IT", "EVERYWHERE?"], 1, 0),
 scenes=[
  ("H", [("Ever learn a new word, then see it everywhere?", "PLAN")], "Seeing it everywhere?", "Stickman surrounded by repeating copies of one word.", "shock/neutral/C; crowd:5@R"),
  ("E", [("Linguist Arnold Zwicky called this the frequency illusion.", "zwicky2005")], "The frequency illusion", "Title card FREQUENCY ILLUSION.", "point/neutral/L; text:FREQUENCY ILLUSION@R"),
  ("E", [("It's also called the Baader-Meinhof phenomenon, a name that came from a 1994 letter to a newspaper column.", "pacificstandard")], "Baader-Meinhof: a 1994 letter", "Newspaper column with a letter.", "stand/neutral/L; text:1994@TR; list:LETTER@R"),
  ("E", [("Both names come from informal sources, not experiments.", "zwicky2005,pacificstandard")], "Informal names, not experiments", "Blog and newspaper icons; lab flask crossed out.", "shrug/neutral/L; cross@R"),
  ("E", [("A related, well-tested finding is that attention is limited.", "simons1999")], "Attention is limited", "Spotlight on a small area.", "think/neutral/L; spotlight@L"),
  ("E", [("In Simons and Chabris's 1999 invisible-gorilla study, viewers counted basketball passes.", "simons1999")], "1999 invisible gorilla study", "Basketballs being passed.", "point/neutral/L; list:PASS,PASS,PASS@R"),
  ("E", [("Many failed to notice a person in a gorilla suit walking through the scene.", "simons1999")], "Many missed the gorilla", "Gorilla silhouette crossing a scene.", "shock/neutral/L; text:GORILLA@R"),
  ("E", [("That shows we can miss things we aren't paying attention to.", "simons1999")], "We miss what we ignore", "Eye with a blind spot.", "stand/neutral/L; qmark@R"),
  ("E", [("One idea is that once something captures your attention, you start noticing what you previously missed.", "zwicky2005,simons1999")], "One idea: you start noticing", "Light bulb switching on a hidden pile of words.", "think/smile/L; lightbulb@R"),
  ("T", [("So if something suddenly seems to be everywhere, ask whether it increased, or whether you simply started noticing.", "zwicky2005")], "Increased, or just noticed?", "Stickman holding a magnifier between two options.", "point/smile/L; text:MORE? OR NOTICED?@R"),
  ("C", [("Tomorrow: do decisions really wear your brain out?", "PLAN")], "Tomorrow: decision fatigue", "Stickman surrounded by choices.", "stand/worry/L; list:A?,B?,C?@R"),
 ])

DAYS[12] = dict(
 title="Is Decision Fatigue Real? The Evidence Says...",
 description_core="Do decisions really wear your brain out? A famous parole study seemed to show it, but critics say case order explains the pattern, and a 23-lab replication of the related ego-depletion effect found it near zero.",
 primary=["danziger2011", "hagger2016"],
 hashtags=["#psychology", "#shorts", "#decisionfatigue", "#egodepletion", "#willpower", "#psychologyfacts"],
 caveats="CONTESTED. Danziger et al. (2011) is a correlational study of Israeli parole boards; Weinshall-Margel & Shapard argue case ordering explains the pattern. Hagger et al. (2016) tested ego depletion, a related but different idea (willpower as a limited resource), not decisions specifically. The video concludes only that decision fatigue is not settled.",
 thumb=(["DECISION", "FATIGUE:", "REAL?"], 2, 0),
 scenes=[
  ("H", [("Do your decisions really wear your brain out?", "PLAN")], "Decisions wear you out?", "Tired stickman surrounded by choices.", "shock/worry/C; list:?,?,?@R"),
  ("E", [("In 2011, researchers studied more than 1,000 parole decisions by eight Israeli judges.", "danziger2011")], "2011: 1,000+ parole decisions", "Eight judges' desks.", "stand/neutral/L; text:8 JUDGES@R"),
  ("E", [("After a food break, about 65 percent of cases were granted parole.", "danziger2011")], "After a break: ~65%", "High bar after a snack.", "point/smile/L; bars:after break=65%,end of session=h6@R"),
  ("E", [("Then the rate fell gradually, sometimes to nearly zero, until the next break.", "danziger2011")], "Then it fell toward zero", "Falling line between breaks.", "stand/worry/L; lines:rate,time,fall@R"),
  ("E", [("The authors argued that irrelevant factors, like breaks, influence rulings.", "danziger2011")], "Breaks influence rulings?", "Cookie and a gavel.", "think/neutral/L; text:BREAKS?@R"),
  ("E", [("But Keren Weinshall-Margel and John Shapard replied that case order isn't random.", "weinshall2011")], "Critics: case order isn't random", "Shuffled case files.", "shrug/neutral/L; list:CASE 1,CASE 2@R"),
  ("E", [("They argued the pattern is likely an artifact of how cases were ordered.", "weinshall2011")], "Likely an ordering artifact", "Case files stacked in order.", "shrug/neutral/L; cross@R"),
  ("E", [("In a 2016 test across 23 labs and 2,141 people, the related ego-depletion effect was close to zero.", "hagger2016")], "2016: ego depletion near zero", "23 lab icons; zero.", "stand/neutral/L; numbers:23 LABS@R; text:~ZERO@TR"),
  ("E", [("So decision fatigue isn't settled science.", "danziger2011,weinshall2011,hagger2016")], "Not settled science", "Scale balanced.", "shrug/smile/L; scale@R"),
  ("T", [("So be careful with claims that your brain simply runs out of decision power.", "hagger2016,weinshall2011")], "Be careful with 'runs out'", "Battery icon with a question mark.", "point/smile/L; qmark@R"),
  ("C", [("Tomorrow: why do you finish a bad movie you're already hating?", "PLAN")], "Tomorrow: sunk costs", "Stickman watching a bad movie.", "stand/worry/L; coin:$12@R"),
 ])

DAYS[13] = dict(
 title="The Sunk Cost Effect: Why Paying Keeps You Going",
 description_core="Why do you keep going with something you've already paid for? A 1985 field study found people who paid full price for theater season tickets attended more plays than discounted buyers.",
 primary=["arkes1985"],
 hashtags=["#psychology", "#shorts", "#sunkcost", "#decisionmaking", "#behavioraleconomics", "#psychologyfacts"],
 caveats="One field study at a university theater; attendance was counted over the first six months of the season. Arkes & Blumer suggest the motive is avoiding the appearance of waste, which is their proposed explanation, not a proven mechanism.",
 thumb=(["THE SUNK", "COST EFFECT"], 1, 0),
 scenes=[
  ("H", [("Why do you finish a movie you're hating?", "PLAN")], "Why finish it?", "Stickman bored in a movie seat.", "think/worry/C; coin:$12@R"),
  ("E", [("In 1985, Hal Arkes and Catherine Blumer studied the sunk cost effect.", "arkes1985")], "The sunk cost effect, 1985", "Title card SUNK COST.", "point/neutral/L; text:SUNK COST@R"),
  ("E", [("It's the tendency to continue something after you've invested money, effort or time.", "arkes1985")], "Keep going after investing", "Coin sinking into water.", "stand/neutral/L; coin:$@R"),
  ("E", [("At an Ohio University theater, they arranged for season tickets to be sold at three prices.", "arkes1985")], "Ohio University theater", "Ticket booth.", "stand/neutral/L; tag:3 PRICES@R"),
  ("E", [("At the beginning of the season, about a third bought at the full $15, a third at $13, and a third at $8.", "arkes1985")], "$15, $13 or $8", "Three tickets with prices.", "point/neutral/L; list:$15,$13,$8@R"),
  ("E", [("Over the next six months, people who paid full price attended more plays than those who paid less.", "arkes1985")], "Full price = more plays", "Bars: $15 high, $8 low.", "stand/smile/L; bars:$8=h35,$15=h70@R"),
  ("E", [("The authors suggest people continue partly to avoid appearing wasteful.", "arkes1985")], "Avoiding looking wasteful", "Stickman hiding an unused ticket.", "think/worry/L; tag:WASTE@R"),
  ("E", [("This was one field study with theater patrons.", "arkes1985")], "One field study", "Single theater icon.", "shrug/neutral/L; text:1 STUDY@R"),
  ("T", [("So when you're deciding whether to continue, ask what you'd choose if you hadn't already paid.", "arkes1985")], "Would you choose it unpaid?", "Stickman with a price tag crossed out.", "point/smile/L; tag:$0?@R"),
  ("C", [("Tomorrow: why do we assume attractive people are better people?", "PLAN")], "Tomorrow: the halo effect", "Halo above a stickman.", "stand/neutral/L; text:HALO@R"),
 ])

DAYS[14] = dict(
 title="The Halo Effect: Why Looks Seem to Count",
 description_core="Do we assume attractive people are better people? The halo effect was named in 1920, and later research found attractive people were rated as more socially competent, though the effect varies a lot between studies.",
 primary=["thorndike1920", "eagly1991"],
 hashtags=["#psychology", "#shorts", "#haloeffect", "#attractiveness", "#bias", "#psychologyfacts"],
 caveats="Eagly et al. (1991) found the 'beauty is good' stereotype was moderately low and variable across studies; the video does not claim attractive people are actually better or more trustworthy. 'Rated as more socially competent' reflects perceptions in lab ratings, mostly of photographs.",
 thumb=(["THE HALO", "EFFECT"], 1, 0),
 scenes=[
  ("H", [("Do you assume attractive people are better people?", "PLAN")], "Better people?", "Stickman with a golden halo.", "think/neutral/C; text:HALO@R"),
  ("E", [("In 1920, psychologist Edward Thorndike asked military officers to rate their soldiers.", "thorndike1920")], "1920: officers rate soldiers", "Officer with a clipboard.", "stand/neutral/L; text:1920@TR; list:RATE@R"),
  ("E", [("The ratings were supposed to be independent: physique, intelligence, leadership and character.", "thorndike1920")], "Four separate ratings", "Four labeled boxes.", "point/neutral/L; list:BODY,MIND,LEAD,CHAR@R"),
  ("E", [("Soldiers rated as physically impressive were also rated as more intelligent, better leaders and finer in character.", "thorndike1920")], "Impressive in one = all", "One checked box pulling the others.", "think/neutral/L; check@R"),
  ("E", [("Thorndike called this a halo.", "thorndike1920")], "He called it a halo", "Halo over a head.", "stand/smile/L; text:HALO@R"),
  ("E", [("In 1972, Karen Dion and colleagues found people assumed attractive strangers had more desirable personalities.", "dion1972")], "1972: attractive = nicer?", "Two photos; one with a halo.", "point/neutral/L; crowd:2@R; text:1972@TR"),
  ("E", [("A 1991 meta-analysis by Alice Eagly's team found that this beauty-is-good effect was moderately low and varied across studies.", "eagly1991")], "1991: modest and variable", "Wobbly small bars.", "shrug/neutral/L; bars:study 1=h22,study 2=h46,study 3=h12@R"),
  ("E", [("Attractive people were rated as more socially competent and better adjusted, on average.", "eagly1991")], "Rated more socially competent", "Smiling faces with checks.", "stand/smile/L; check@R"),
  ("T", [("So when someone seems impressive in one way, ask what you actually know about the rest.", "thorndike1920")], "What do I actually know?", "Stickman peering behind a halo.", "point/smile/L; qmark@R"),
  ("C", [("Tomorrow: why do you love things you built yourself?", "PLAN")], "Tomorrow: things you built", "Stickman proudly holding a wobbly box.", "stand/smile/L; list:DIY@R"),
 ])

DAYS[15] = dict(
 title="Why You Overvalue What You Build Yourself",
 description_core="Why do you love things you built yourself? In four studies, people valued their own creations more, but the effect vanished when they failed to finish or their creation was destroyed.",
 primary=["norton2012"],
 hashtags=["#psychology", "#shorts", "#ikeaeffect", "#behavioraleconomics", "#diy", "#psychologyfacts"],
 caveats="Findings come from lab studies with IKEA boxes, origami and Lego. The 'would you pay 63% more' figure sometimes quoted online was not verified and is not used.",
 thumb=(["THE IKEA", "EFFECT"], 1, 0),
 scenes=[
  ("H", [("Why do you love things you built yourself?", "PLAN")], "Why love your own build?", "Stickman proudly holding a wobbly box.", "stand/smile/C; list:DIY@R"),
  ("E", [("Michael Norton, Daniel Mochon and Dan Ariely call it the IKEA effect.", "norton2012")], "The IKEA effect", "Title card IKEA EFFECT.", "point/neutral/L; text:IKEA EFFECT@R"),
  ("E", [("In four studies, people assembled IKEA boxes, folded origami and built Lego sets.", "norton2012")], "IKEA boxes, origami, Lego", "Three craft icons.", "stand/neutral/L; list:BOX,ORIGAMI,LEGO@R"),
  ("E", [("They valued their own creations more than similar products they hadn't made.", "norton2012")], "Valued their own more", "Two bars: own high, others lower.", "stand/smile/L; bars:others=h40,own=h70@R"),
  ("E", [("Participants also saw their amateur creations as similar in value to experts' creations.", "norton2012")], "Amateur = expert?", "Wobbly crane next to a perfect one.", "think/smile/L; list:MINE,EXPERT@R"),
  ("E", [("And they expected other people to share their opinion.", "norton2012")], "Expected others to agree", "Crowd nodding.", "stand/smile/L; crowd:4@R"),
  ("E", [("In another study, the effect held even for simple boxes that couldn't be customized.", "norton2012")], "Even simple, uncustomizable boxes", "Plain boxes.", "point/neutral/L; list:BOX,BOX@R"),
  ("E", [("But the effect disappeared when people failed to finish building, or when their creation was destroyed.", "norton2012")], "Gone if unfinished or destroyed", "Broken box with a cross.", "shock/worry/L; cross@R"),
  ("T", [("So when you've built something, ask how much of your attachment comes from the effort.", "norton2012")], "How much is the effort?", "Stickman weighing effort vs. object.", "think/smile/L; scale@R"),
  ("C", [("Tomorrow: does time really speed up as you get older?", "PLAN")], "Tomorrow: time and age", "Clock spinning fast.", "stand/neutral/L; clock@R"),
 ])

DAYS[16] = dict(
 title="Does Time Really Speed Up as You Age?",
 description_core="Does time really fly faster as you get older? Surveys found people of all ages say time passes quickly, with age differences mainly for the last ten years, possibly linked to time pressure.",
 primary=["wittmann2005", "friedman2010"],
 hashtags=["#psychology", "#shorts", "#timeperception", "#aging", "#psychologyfacts", "#brain"],
 caveats="These are self-report surveys, so they measure feelings about time, not time perception itself. The time-pressure account is the authors' proposed explanation. The video does not claim to explain why time seems faster; it reports what the surveys found.",
 thumb=(["DOES TIME", "SPEED UP", "WITH AGE?"], 1, 0),
 scenes=[
  ("H", [("Does time really speed up as you get older?", "PLAN")], "Does time speed up?", "Stickman watching clock hands spin.", "shock/neutral/C; clock@R"),
  ("E", [("In 2005, Marc Wittmann and Sandra Lehnhoff surveyed 499 people aged 14 to 94.", "wittmann2005")], "2005: 499 people, ages 14-94", "Group of stickmen of different heights.", "stand/neutral/L; crowd:5@R; text:499 PEOPLE@TR"),
  ("E", [("Everyone, whatever their age, said time passes quickly.", "wittmann2005")], "All ages: time feels fast", "Clock racing.", "stand/smile/L; clock@R"),
  ("E", [("But when asked about the last 10 years, older people said they'd passed faster.", "wittmann2005")], "Last 10 years: older = faster", "Calendar of ten years.", "think/neutral/L; text:10 YEARS@R"),
  ("E", [("For shorter spans, like the last week or month, answers didn't change with age.", "wittmann2005")], "Short spans: no age change", "Flat line.", "shrug/neutral/L; lines:young,old,flat@R"),
  ("E", [("In 2010, William Friedman and Steve Janssen surveyed 1,865 adults.", "friedman2010")], "2010: 1,865 adults", "Larger crowd.", "stand/neutral/L; crowd:5@R; text:1,865@TR"),
  ("E", [("Age differences in the felt speed of time were very small, except for the last ten years.", "friedman2010")], "Age differences very small", "Tiny bars.", "point/neutral/L; bars:young=h40,old=h44@R"),
  ("E", [("They tied the feeling to time pressure: people who felt rushed said time passed quickly.", "friedman2010")], "Linked to time pressure", "Stickman rushing with a checklist.", "walk/worry/L; list:TODO,TODO@R"),
  ("T", [("So if time feels like it's flying, check how rushed you feel, not just how old you are.", "friedman2010")], "How rushed do you feel?", "Stickman checking a stress meter.", "point/smile/L; text:RUSHED?@R"),
  ("C", [("Tomorrow: do crowds really make people less likely to help?", "PLAN")], "Tomorrow: the bystander effect", "Crowd of tiny stickmen.", "stand/worry/L; crowd:5@R"),
 ])

DAYS[17] = dict(
 title="Do Crowds Really Stop People From Helping?",
 description_core="Do more witnesses mean less help? A 1968 experiment found they can, but a 2011 meta-analysis found the effect shrinks in dangerous emergencies, and 2020 CCTV footage of real conflicts showed people stepping in more than 90% of the time.",
 primary=["darley1968", "philpot2020"],
 hashtags=["#psychology", "#shorts", "#bystandereffect", "#socialpsychology", "#helping", "#psychologyfacts"],
 caveats="CONTESTED/OVERSIMPLIFIED. Darley & Latané percentages (about 85% vs about 31%) come from secondary summaries. Philpot et al. studied aggressive public conflicts in three cities; 'intervened' means at least one bystander acted. The '38 witnesses' Genovese story is not supported by court and police records (Manning et al. 2007).",
 thumb=(["DO CROWDS", "STOP HELP?"], 1, 0),
 scenes=[
  ("H", [("Do crowds really make people less likely to help?", "PLAN")], "Do crowds stop help?", "Crowd of tiny stickmen watching.", "think/worry/C; crowd:5@R"),
  ("E", [("In 1968, John Darley and Bibb Latané staged a fake emergency.", "darley1968")], "1968: a staged emergency", "Intercom between rooms.", "stand/neutral/L; text:1968@TR; list:ALARM@R"),
  ("E", [("People who believed they were alone with a person having a seizure helped about 85 percent of the time.", "darley1968")], "Alone: ~85% helped", "Tall bar.", "point/smile/L; bars:alone=85%,with 4 others=31%@R"),
  ("E", [("With four others they believed were listening, only about 31 percent helped.", "darley1968")], "With four others: ~31%", "Short bar.", "stand/worry/L; bars:alone=85%,with 4 others=31%@R"),
  ("E", [("That's the bystander effect: more witnesses, less helping.", "darley1968")], "The bystander effect", "Crowd shrinking helper count.", "stand/neutral/L; crowd:5@R"),
  ("E", [("But a 2011 meta-analysis of over 7,700 participants found the effect shrank in dangerous emergencies.", "fischer2011")], "2011: weaker in danger", "Shrinking bar next to a red warning.", "point/neutral/L; bars:safe=h60,danger=h25@R"),
  ("E", [("And in 2020, researchers studied 219 real conflicts on CCTV in Amsterdam, Lancaster and Cape Town.", "philpot2020")], "2020: 219 real conflicts on CCTV", "Camera icon.", "stand/neutral/L; text:219 CONFLICTS@R"),
  ("E", [("Bystanders intervened in more than 90 percent of them.", "philpot2020")], "Bystanders stepped in: 90%+", "Big 90%+ check.", "stand/smile/L; text:90%+@R; check@TR"),
  ("E", [("Meanwhile, researchers found no evidence that 38 witnesses watched Kitty Genovese's murder.", "manning2007")], "'38 witnesses': no evidence", "Crossed-out '38'.", "shrug/neutral/L; text:38?@R; cross@TR"),
  ("T", [("So 'crowds never help' is too simple: in real public conflicts, help was the norm.", "philpot2020")], "'Crowds never help' is too simple", "Helper stepping forward from a crowd.", "walk/smile/L; crowd:3@R"),
  ("C", [("Tomorrow: why does bad news grab your attention?", "PLAN")], "Tomorrow: bad news", "Newspaper with a siren.", "stand/worry/L; text:BAD NEWS@R"),
 ])

DAYS[18] = dict(
 title="Why Bad News Grabs Your Attention",
 description_core="Why does bad news pull you in? A 17-country lab study found negative news produced stronger physiological reactions on average, and a separate study found people's choices leaned negative.",
 primary=["soroka2019", "trussler2014"],
 hashtags=["#psychology", "#shorts", "#negativitybias", "#news", "#attention", "#psychologyfacts"],
 caveats="Soroka et al. (2019) measured bodily responses in lab settings and found large individual differences. Trussler & Soroka (2014) found politically interested participants were more likely to select negative stories. Neither study shows everyone prefers bad news.",
 thumb=(["WHY BAD NEWS", "GRABS YOU"], 1, 0),
 scenes=[
  ("H", [("Why does bad news grab your attention?", "PLAN")], "Why bad news?", "Stickman staring at a siren headline.", "shock/worry/C; text:BAD NEWS@R"),
  ("E", [("In 2019, Stuart Soroka and colleagues ran lab experiments in 17 countries, on six continents.", "soroka2019")], "2019: 17 countries", "Globe with 17.", "stand/neutral/L; text:17 COUNTRIES@R"),
  ("E", [("They measured the bodily reactions of 1,156 people watching real news videos.", "soroka2019")], "1,156 people, real news", "Sensor on a viewer.", "stand/neutral/L; text:1,156@R"),
  ("E", [("On average, negative stories produced stronger physiological activation than positive ones.", "soroka2019")], "Negative = stronger reaction", "Bars: negative higher.", "point/neutral/L; bars:positive=h35,negative=h65@R"),
  ("E", [("But individuals varied a lot in how strongly they reacted.", "soroka2019")], "People varied a lot", "Scatter of different heights.", "shrug/neutral/L; bars:person A=h30,person B=h75@R"),
  ("E", [("In a separate 2014 study, Marc Trussler and Soroka let people choose which news stories to read.", "trussler2014")], "2014: people choose stories", "Menu of headlines.", "think/neutral/L; list:GOOD,BAD,OTHER@R"),
  ("E", [("People's choices leaned negative, even when that didn't match what they said they wanted.", "trussler2014")], "Choices leaned negative", "Arrow toward BAD.", "stand/worry/L; arrow:right@R; text:BAD@TR"),
  ("E", [("The authors argue that demand, not just editors, helps explain why news is negative.", "trussler2014")], "Demand helps explain it", "Readers as a crowd.", "stand/neutral/L; crowd:4@R"),
  ("T", [("So when a headline pulls you in, it may be tapping a common bias, but not everyone has it equally.", "soroka2019")], "A common bias, not universal", "Stickman noticing the pull.", "point/smile/L; text:NOTICE IT@R"),
  ("C", [("Tomorrow: how can a menu option you never order change what you pick?", "PLAN")], "Tomorrow: the decoy effect", "Menu with three options.", "stand/neutral/L; list:S,M,L@R"),
 ])

DAYS[19] = dict(
 title="Can a Menu Option You Never Order Change Your Pick?",
 description_core="Can a third option you never choose change your pick? In 1982 researchers showed a decoy can shift choices, but a 2014 paper found the effect may be limited to choices shown as numbers.",
 primary=["huber1982", "frederick2014"],
 hashtags=["#psychology", "#shorts", "#decoyeffect", "#marketing", "#decisionmaking", "#psychologyfacts"],
 caveats="CONTESTED IN SCOPE. The widely repeated Economist-subscription example is not used because its data could not be verified. Frederick, Lee & Baskin (2014) say the attraction effect may be restricted to stylized, numeric product descriptions; it does not claim it never happens elsewhere.",
 thumb=(["THE DECOY", "EFFECT"], 1, 0),
 scenes=[
  ("H", [("Can a third option you never choose change your pick?", "PLAN")], "A third option changes picks?", "Menu with three options.", "think/neutral/C; list:A,B,C@R"),
  ("E", [("In 1982, Joel Huber, John Payne and Christopher Puto studied asymmetrically dominated options.", "huber1982")], "1982: dominated options", "Title card DECOY.", "point/neutral/L; text:DECOY@R"),
  ("E", [("A decoy is an option that's clearly worse than one item, but not clearly worse than the other.", "huber1982")], "A decoy: worse than one only", "Three tags: one clearly worse than another.", "stand/neutral/L; list:A,B,DECOY@R"),
  ("E", [("Adding a decoy could increase how often people picked the option that dominated it.", "huber1982")], "Decoy boosts the dominating option", "Bars: option rises.", "point/smile/L; bars:without=h35,with decoy=h65@R"),
  ("E", [("In 2014, Shane Frederick and colleagues tested the limits of this attraction effect.", "frederick2014")], "2014: testing the limits", "Magnifier on a bar.", "stand/neutral/L; text:2014@TR"),
  ("E", [("They found it showed up mainly when every product feature was shown as a number.", "frederick2014")], "Mostly with numbers on paper", "Spec sheet with numbers.", "think/neutral/L; list:7.2,5.5@R"),
  ("E", [("It didn't typically appear when people actually tasted a drink, or saw a picture of a hotel room.", "frederick2014")], "Not with tasting or photos", "Drink and photo with crosses.", "shrug/neutral/L; cross@R"),
  ("E", [("The authors suggest it may be limited to numbers-on-a-page choices.", "frederick2014")], "May be limited to numbers", "Page with numbers.", "stand/neutral/L; text:NUMBERS@R"),
  ("T", [("So when options are listed as numbers, ask if one of them is just there to make another look good.", "huber1982")], "Is one just a decoy?", "Stickman pointing at the odd one out.", "point/smile/L; list:A,B,C?@R"),
  ("C", [("Tomorrow: why do you put off things you care about?", "PLAN")], "Tomorrow: procrastination", "Stickman and a pile of tasks.", "stand/worry/L; list:TODO,TODO@R"),
 ])

DAYS[20] = dict(
 title="Why You Procrastinate on What Matters",
 description_core="Why do you put off things you care about? A large meta-analysis found task aversiveness, low self-efficacy and impulsiveness are strong predictors, and researchers link procrastination to short-term mood repair.",
 primary=["steel2007", "sirois2013"],
 hashtags=["#psychology", "#shorts", "#procrastination", "#productivity", "#motivation", "#psychologyfacts"],
 caveats="Steel (2007) is a review of correlations, not proof of cause. The mood-repair account (Sirois & Pychyl) is a theoretical framework supported by research; it does not explain every case. Not medical or therapeutic advice.",
 thumb=(["WHY YOU", "PROCRASTINATE"], 1, 0),
 scenes=[
  ("H", [("Why do you put off things you care about?", "PLAN")], "Why put it off?", "Stickman with a looming task.", "think/worry/C; list:TODO,TODO@R"),
  ("E", [("In 2007, Piers Steel reviewed 691 correlations in a meta-analysis of procrastination.", "steel2007")], "2007: 691 correlations", "Big number 691.", "point/neutral/L; numbers:691@R"),
  ("E", [("Strong predictors included task aversiveness, task delay, low self-efficacy and impulsiveness.", "steel2007")], "Strong predictors", "List of four predictors.", "stand/neutral/L; list:UNPLEASANT,DELAY,LOW CONFIDENCE,IMPULSE@R"),
  ("E", [("Conscientiousness and its facets, like self-control and organization, were strong predictors too.", "steel2007")], "Self-control and organization", "Check marks.", "stand/smile/L; check@R"),
  ("E", [("Neuroticism and rebelliousness had only weak connections.", "steel2007")], "Weak links: neuroticism", "Thin lines.", "shrug/neutral/L; cross@R"),
  ("E", [("In other words, procrastination is a self-regulation failure more than a time-management problem.", "steel2007")], "Self-regulation, not time management", "Clock crossed out.", "think/neutral/L; clock@R; cross@TR"),
  ("E", [("In 2013, Fuschia Sirois and Timothy Pychyl argued procrastination is partly about short-term mood repair.", "sirois2013")], "2013: short-term mood repair", "Heart bandage.", "stand/neutral/L; text:MOOD REPAIR@R"),
  ("E", [("You avoid the task to escape bad feelings now.", "sirois2013")], "Escape bad feelings now", "Stickman running from a cloud.", "walk/worry/L; waves@R"),
  ("E", [("While the consequences land on your future self.", "sirois2013")], "Consequences hit future you", "Arrow to a later date.", "stand/worry/L; arrow:right@R; text:LATER@TR"),
  ("T", [("So when you stall, ask what feeling you're avoiding, not just whether you're lazy.", "sirois2013")], "What feeling are you avoiding?", "Stickman asking himself.", "point/smile/L; qmark@R"),
  ("C", [("Tomorrow: why do you like what you've seen a lot?", "PLAN")], "Tomorrow: familiarity", "Same shape repeated.", "stand/neutral/L; crowd:4@R"),
 ])
