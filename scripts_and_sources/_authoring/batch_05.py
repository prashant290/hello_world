"""Days 41-50 (Month 2: People, persuasion & relationships)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common_sources import S, SEC, SECOND

SOURCES = {
 "goldstein2008": S("Goldstein, N. J., Cialdini, R. B., & Griskevicius, V.", 2008, "A room with a viewpoint: Using social norms to motivate environmental conservation in hotels", "Journal of Consumer Research, 35(3), 472-482", "https://doi.org/10.1086/586910", SEC + " (descriptive-norm message beat the standard message; room-specific message did better still)"),
 "bohner2014": S("Bohner, G., & Schluter, L. E.", 2014, "A room with a viewpoint revisited: Descriptive norms and hotel guests' towel reuse behavior", "PLOS ONE, 9(8), e104086", "https://doi.org/10.1371/journal.pone.0104086", SEC + " (German hotels; both messages beat no message; norm message not more effective than the standard message)"),
 "cialdini1975": S("Cialdini, R. B., Vincent, J. E., Lewis, S. K., Catalan, J., Wheeler, D., & Darby, B. L.", 1975, "Reciprocal concessions procedure for inducing compliance: The door-in-the-face technique", "Journal of Personality and Social Psychology, 31(2), 206-215", "https://doi.org/10.1037/h0076284", SECOND + " (three experiments, 202 passersby; 50% vs 17% small-request-only and 25% in another control)"),
 "dillard1984": S("Dillard, J. P., Hunter, J. E., & Burgoon, M.", 1984, "Sequential-request persuasive strategies: Meta-analysis of foot-in-the-door and door-in-the-face", "Human Communication Research, 10(4), 461-488", "https://www.simplypsychology.org/compliance.html", SECOND + " (effects small: r = .17 and .15; moderated by prosocial requests)"),
 "willis2006": S("Willis, J., & Todorov, A.", 2006, "First impressions: Making up your mind after a 100-ms exposure to a face", "Psychological Science, 17(7), 592-598", "https://doi.org/10.1111/j.1467-9280.2006.01750.x", SEC + " (100-ms judgments correlated with unlimited-time judgments; more time raised confidence, not correlations significantly)"),
 "rosenthal1968": S("Rosenthal, R., & Jacobson, L.", 1968, "Pygmalion in the classroom: Teacher expectation and pupils' intellectual development", "Holt, Rinehart & Winston (book)", "https://en.wikipedia.org/wiki/Pygmalion_effect", SECOND + " (teachers told randomly chosen pupils would bloom; early critiques of the IQ test for first and second graders)"),
 "jussim2005": S("Jussim, L., & Harber, K. D.", 2005, "Teacher expectations and self-fulfilling prophecies: Knowns and unknowns, resolved and unresolved controversies", "Personality and Social Psychology Review, 9(2), 131-155", "https://doi.org/10.1207/s15327957pspr0902_3", SEC + " (self-fulfilling prophecies occur but effects are small and do not accumulate)"),
 "sherman2016": S("Sherman, L. E., Payton, A. A., Hernandez, L. M., Greenfield, P. M., & Dapretto, M.", 2016, "The power of the like in adolescence: Effects of peer influence on neural and behavioral responses to social media", "Psychological Science, 27(7), 1027-1035", "https://doi.org/10.1177/0956797616645673", SEC + " (more likes -> more liking; reward, social cognition, imitation, attention regions; risky photos -> reduced cognitive-control activity)"),
 "hazan1987": S("Hazan, C., & Shaver, P.", 1987, "Romantic love conceptualized as an attachment process", "Journal of Personality and Social Psychology, 52(3), 511-524", "https://doi.org/10.1037/0022-3514.52.3.511", SEC + " (newspaper love quiz; 56/25/19%; relationship length averages)"),
 "fraley2002": S("Fraley, R. C.", 2002, "Attachment stability from infancy to adulthood: Meta-analysis and dynamic modeling of developmental mechanisms", "Personality and Social Psychology Review, 6(2), 123-151", "https://doi.org/10.1207/S15327957PSPR0602_03", SEC + " (27 effect sizes from 23 papers; r about .39)"),
 "rusbult1980": S("Rusbult, C. E.", 1980, "Commitment and satisfaction in romantic associations: A test of the investment model", "Journal of Experimental Social Psychology, 16(2), 172-186", "https://doi.org/10.1016/0022-1031(80)90007-4", SEC + " (investment model: satisfaction, alternatives, investments)"),
 "rusbult1995": S("Rusbult, C. E., & Martz, J. M.", 1995, "Remaining in an abusive relationship: An investment model analysis of nonvoluntary dependence", "Personality and Social Psychology Bulletin, 21(6), 558-571", "https://doi.org/10.1177/0146167295216002", SEC + " (100 women in shelters; commitment higher with poorer alternatives, higher investments, less reported abuse)"),
 "regan1971": S("Regan, D. T.", 1971, "Effects of a favor and liking on compliance", "Journal of Experimental Social Psychology, 7(6), 627-639", "https://doi.org/10.1016/0022-1031(71)90025-4", SEC + " (Coke favor; more raffle tickets even when the giver was not liked)"),
 "jones1967": S("Jones, E. E., & Harris, V. A.", 1967, "The attribution of attitudes", "Journal of Experimental Social Psychology, 3(1), 1-24", "https://doi.org/10.1016/0022-1031(67)90034-0", SECOND + " (Castro essays; attitudes inferred even when position was assigned)"),
 "ross1977": S("Ross, L.", 1977, "The intuitive psychologist and his shortcomings: Distortions in the attribution process", "Advances in Experimental Social Psychology, 10, 173-220", "https://doi.org/10.1016/S0065-2601(08)60357-3", SEC + " (coined 'fundamental attribution error')"),
 "montoya2008": S("Montoya, R. M., Horton, R. S., & Kirchner, J.", 2008, "Is actual similarity necessary for attraction? A meta-analysis of actual and perceived similarity", "Journal of Social and Personal Relationships, 25(6), 889-922", "https://doi.org/10.1177/0265407508096700", SEC + " (313 studies; perceived > actual similarity; actual effect depended on interaction)"),
 "moray1959": S("Moray, N.", 1959, "Attention in dichotic listening: Affective cues and the influence of instructions", "Quarterly Journal of Experimental Psychology, 11(1), 56-60", "https://doi.org/10.1080/17470215908416289", SECOND + " (about a third heard their own name in the ignored channel)"),
 "wood1995": S("Wood, N., & Cowan, N.", 1995, "The cocktail party phenomenon revisited: How frequent are attention shifts to one's name in an irrelevant auditory channel?", "Journal of Experimental Psychology: Learning, Memory, and Cognition, 21(1), 255-260", "https://doi.org/10.1037/0278-7393.21.1.255", SEC + " (about a third noticed their name; replication of Moray)"),
 "howard1995": S("Howard, D. J., Gengler, C., & Jain, A.", 1995, "What's in a name? A complimentary means of persuasion", "Journal of Consumer Research, 22(2), 200-211", "https://doi.org/10.1086/209445", SEC + " (three experiments; remembering a name increased compliance with a purchase request)"),
}

DAYS = {}

DAYS[41] = dict(
 title="Social Proof: Does the Crowd Really Sway You?",
 description_core="Do we copy what others do? A famous hotel-towel study found a 'most guests reuse towels' card beat the standard message, but a 2014 study in German hotels found the norm message was not more effective than the standard one.",
 primary=["goldstein2008", "bohner2014"],
 hashtags=["#psychology", "#shorts", "#socialproof", "#persuasion", "#cialdini", "#psychologyfacts"],
 caveats="Goldstein et al. (2008) is a classic result, but Bohner & Schluter (2014) found the norm message was not more effective than the standard one in German hotels. The video presents both and does not claim social proof is guaranteed. No percentages are quoted.",
 thumb=(["DOES THE CROWD", "SWAY YOU?"], 1, 0),
 scenes=[
  ("H", [("Do we really copy the crowd, even over hotel towels?", "PLAN")], "Do we copy the crowd?", "Stickman beside a towel.", "think/neutral/C; crowd:5@R"),
  ("E", [("In 2008, Noah Goldstein, Robert Cialdini and Vladas Griskevicius ran field experiments in a hotel.", "goldstein2008")], "2008: hotel field experiments", "Hotel building.", "stand/neutral/L; text:2008@TR; text:HOTEL@R"),
  ("E", [("Guests saw a card asking them to reuse their towels.", "goldstein2008")], "A card: reuse your towels", "Towel and card.", "point/neutral/L; list:REUSE TOWELS@R"),
  ("E", [("A card saying most guests reuse their towels worked better than the standard environmental message.", "goldstein2008")], "'Most guests' beat the standard card", "Taller bar for the norm card.", "stand/smile/L; bars:standard=h40,most guests=h65@R"),
  ("E", [("A message about guests who stayed in that very room did better still.", "goldstein2008")], "This room's guests: better still", "Tallest bar.", "point/smile/L; bars:standard=h40,most guests=h65,this room=h85@R"),
  ("E", [("The researchers took this as a sign that people follow what similar others do.", "goldstein2008")], "People follow similar others", "Crowd of similar stickmen.", "think/neutral/L; crowd:5@R"),
  ("E", [("But in 2014, Gerd Bohner and Lisa Schluter tried the idea in German hotels.", "bohner2014")], "2014: tested again, in Germany", "Map pin.", "stand/neutral/L; text:2014@TR; text:GERMANY@R"),
  ("E", [("Both messages beat no message at all.", "bohner2014")], "Both messages beat no message", "Two bars above a short one.", "stand/smile/L; bars:none=h20,standard=h60,norm=h60@R"),
  ("E", [("But the norm message was not more effective than the standard one.", "bohner2014")], "Norm message: no extra gain", "Two equal bars.", "shrug/neutral/L; bars:standard=h60,norm=h60@R"),
  ("T", [("So social proof may nudge people, but this famous towel result is not guaranteed to hold.", "goldstein2008,bohner2014")], "A nudge, not a guarantee", "Stickman shrugging.", "stand/neutral/L; qmark@R"),
  ("C", [("Tomorrow: does asking for too much first make people agree to less?", "PLAN")], "Tomorrow: ask big, then small", "Big and small boxes.", "stand/neutral/L; text:BIG, THEN SMALL?@R"),
 ])

DAYS[42] = dict(
 title="The Door-in-the-Face Technique: Does It Work?",
 description_core="Does a big request first make people agree to a smaller one? In 1975 experiments with 202 passersby, about half agreed to the small request after refusing a large one, versus 17% when asked the small request alone.",
 primary=["cialdini1975", "dillard1984"],
 hashtags=["#psychology", "#shorts", "#doorintheface", "#persuasion", "#cialdini", "#psychologyfacts"],
 caveats="Percentages come from secondary summaries of Cialdini et al. (1975). The average effect in the 1984 meta-analysis is small, and results depend on factors such as whether the request is prosocial. The video does not claim the technique works reliably.",
 thumb=(["ASK BIG,", "THEN SMALL?"], 1, 0),
 scenes=[
  ("H", [("Does asking for too much first make people agree to less?", "PLAN")], "Ask big, then small?", "Big box then small box.", "think/neutral/C; text:BIG > SMALL@R"),
  ("E", [("In 1975, Robert Cialdini and colleagues tested what they called the door-in-the-face technique.", "cialdini1975")], "1975: door-in-the-face", "Door with a face-shaped shape.", "point/neutral/L; door@R; text:1975@TR"),
  ("E", [("The idea: make a large request first, then a smaller one.", "cialdini1975")], "Large request, then smaller", "Two boxes, large and small.", "stand/neutral/L; list:BIG,SMALL@R"),
  ("E", [("Across their experiments, they approached 202 passersby.", "cialdini1975")], "202 passersby", "Counter.", "stand/neutral/L; numbers:202@R"),
  ("E", [("About half agreed to the small request after refusing the large one.", "cialdini1975")], "~50% agreed after a big ask", "Bar at 50%.", "stand/smile/L; bars:big first=50%,small only=17%@R"),
  ("E", [("Only 17 percent agreed when asked the small request alone.", "cialdini1975")], "Small ask alone: 17%", "Short bar at 17%.", "shrug/neutral/L; bars:big first=50%,small only=17%@R"),
  ("E", [("Their explanation was reciprocal concessions: you backed down, so I'll meet you halfway.", "cialdini1975")], "Reciprocal concessions", "Two figures stepping toward each other.", "think/neutral/L; arrow@R"),
  ("E", [("In 1984, Dillard and colleagues combined many studies in a meta-analysis.", "dillard1984")], "1984: a meta-analysis", "Stack of papers.", "stand/neutral/L; text:META-ANALYSIS@R"),
  ("E", [("They found the average effect was small.", "dillard1984")], "Average effect: small", "Short bar.", "shrug/neutral/L; bars:effect=h20@R"),
  ("E", [("It also depended on factors such as whether the request was for a good cause.", "dillard1984")], "Depends on the request", "Scale.", "point/neutral/L; scale@R"),
  ("T", [("So asking big then small can work, but the average effect is small.", "cialdini1975,dillard1984")], "Can work, effect is small", "Stickman with a small check.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: do first impressions really form in a tenth of a second?", "PLAN")], "Tomorrow: first impressions", "Stopwatch.", "stand/neutral/L; clock@R"),
 ])

DAYS[43] = dict(
 title="Do First Impressions Form in a Tenth of a Second?",
 description_core="Do we judge faces in 100 milliseconds? A 2006 study found snap judgments correlated with judgments made with no time limit, but correlation is not accuracy.",
 primary=["willis2006"],
 hashtags=["#psychology", "#shorts", "#firstimpressions", "#perception", "#socialpsychology", "#psychologyfacts"],
 caveats="Willis & Todorov (2006) measured agreement between quick and unlimited-time ratings, not whether the ratings were accurate. The popular '7 seconds' figure was not checked and is not used.",
 thumb=(["A TENTH OF", "A SECOND?"], 1, 0),
 scenes=[
  ("H", [("Do first impressions really form in a tenth of a second?", "PLAN")], "A tenth of a second?", "Stopwatch beside a face.", "think/neutral/C; clock@R"),
  ("E", [("In 2006, Janine Willis and Alexander Todorov showed people unfamiliar faces for just 100 milliseconds.", "willis2006")], "2006: faces shown for 100 ms", "Face flashing.", "stand/neutral/L; text:100 MS@R; text:2006@TR"),
  ("E", [("Other people saw the faces for 500 milliseconds or a full second.", "willis2006")], "Others: 500 ms or 1 second", "Clock.", "point/neutral/L; list:500 MS,1 SEC@R"),
  ("E", [("They rated traits like trustworthiness and competence.", "willis2006")], "Rated: trust, competence", "Two rating cards.", "stand/neutral/L; list:TRUST,COMPETENT@R"),
  ("E", [("Judgments after 100 milliseconds correlated with judgments made with no time limit.", "willis2006")], "100 ms matched unlimited time", "Two matching lines.", "stand/smile/L; lines:100 ms,no limit,same@R"),
  ("E", [("Extra viewing time did not significantly raise that correlation.", "willis2006")], "More time: no real gain", "Flat line.", "shrug/neutral/L; lines:correlation,time,flat@R"),
  ("E", [("It did make people more confident in their ratings.", "willis2006")], "More time: more confidence", "Rising line.", "stand/smile/L; lines:confidence,time,up@R"),
  ("E", [("Judgments were also more negative at 500 milliseconds than at 100.", "willis2006")], "500 ms: more negative", "Falling line.", "stand/worry/L; lines:mood of rating,time,fall@R"),
  ("E", [("Agreement between ratings is not accuracy, and the study did not test whether the faces really had those traits.", "willis2006")], "Agreement is not accuracy", "Cross over a check.", "point/neutral/L; cross@R"),
  ("T", [("So snap judgments form fast, but this study doesn't show they're right.", "willis2006")], "Fast, not necessarily right", "Stickman with a question mark.", "shrug/neutral/L; qmark@R"),
  ("C", [("Tomorrow: do a teacher's expectations change how students perform?", "PLAN")], "Tomorrow: expectations", "Teacher at a board.", "stand/neutral/L; text:EXPECTATIONS?@R"),
 ])

DAYS[44] = dict(
 title="The Pygmalion Effect: Do Expectations Shape Students?",
 description_core="Can a teacher's expectations change a student's results? The famous 1968 study reported IQ gains, critics questioned its test, and a later review found classroom expectation effects are real but typically small.",
 primary=["rosenthal1968", "jussim2005"],
 hashtags=["#psychology", "#shorts", "#pygmalioneffect", "#education", "#expectations", "#psychologyfacts"],
 caveats="The Rosenthal & Jacobson design and critiques come from several consistent secondary summaries of the book. The 2005 review (Jussim & Harber) is the stronger evidence for 'real but small, not cumulative'. The video does not claim expectations transform students.",
 thumb=(["DO EXPECTATIONS", "SHAPE STUDENTS?"], 1, 0),
 scenes=[
  ("H", [("Can a teacher's expectations change how a student performs?", "PLAN")], "Do expectations matter?", "Teacher and student.", "think/neutral/C; crowd:1@R"),
  ("E", [("In 1968, Robert Rosenthal and Lenore Jacobson told teachers that some students were about to show unusual intellectual growth.", "rosenthal1968")], "1968: 'these students will bloom'", "Flower above a student.", "point/neutral/L; text:1968@TR; text:BLOOM@R"),
  ("E", [("Those students had actually been chosen at random.", "rosenthal1968")], "They were picked at random", "Dice.", "shrug/neutral/L; wheel@R"),
  ("E", [("The authors reported bigger IQ gains for some of them, especially in the first two grades.", "rosenthal1968")], "Reported IQ gains", "Rising bar.", "stand/smile/L; bars:others=h35,'bloomers'=h60@R"),
  ("E", [("Early critics argued the IQ test was inappropriate for first and second graders.", "rosenthal1968")], "Critics: wrong test for age", "Test sheet with a question mark.", "shrug/worry/L; qmark@R"),
  ("E", [("In 2005, Lee Jussim and Kent Harber reviewed decades of research on teacher expectations.", "jussim2005")], "2005: a review of the research", "Stack of papers.", "stand/neutral/L; text:2005@TR; text:REVIEW@R"),
  ("E", [("They concluded that self-fulfilling prophecies in classrooms do occur.", "jussim2005")], "Self-fulfilling prophecies occur", "Check mark.", "stand/smile/L; check@R"),
  ("E", [("But the effects are typically small.", "jussim2005")], "But typically small", "Short bar.", "shrug/neutral/L; bars:effect=h20@R"),
  ("E", [("And they don't appear to accumulate over time.", "jussim2005")], "And don't seem to accumulate", "Flat line.", "point/neutral/L; lines:effect,years,flat@R"),
  ("T", [("So expectations can nudge outcomes, but not as powerfully as the famous story suggests.", "rosenthal1968,jussim2005")], "A nudge, not a transformation", "Stickman with a small arrow.", "stand/neutral/L; arrow@R"),
  ("C", [("Tomorrow: why do likes feel so rewarding?", "PLAN")], "Tomorrow: why likes feel good", "Heart.", "stand/neutral/L; qmark@R"),
 ])

DAYS[45] = dict(
 title="Why Do Likes Feel So Rewarding? A Teen Brain Study",
 description_core="In a 2016 brain-imaging study, teenagers viewing a simulated social media feed liked photos more when they already had many likes, and those photos were linked with activity in reward-related brain regions.",
 primary=["sherman2016"],
 hashtags=["#psychology", "#shorts", "#socialmedia", "#brain", "#neuroscience", "#psychologyfacts"],
 caveats="A single small lab study of teenagers using a simulated feed; brain activity does not prove addiction or craving. The video says 'linked with', not 'causes'.",
 thumb=(["WHY LIKES", "FEEL GOOD"], 1, 0),
 scenes=[
  ("H", [("Why do likes feel so good?", "PLAN")], "Why do likes feel good?", "Phone with hearts.", "think/neutral/C; text:LIKES@R"),
  ("E", [("In 2016, Lauren Sherman and colleagues scanned teenagers' brains while they viewed a simulated social media feed.", "sherman2016")], "2016: teens in a brain scanner", "Brain scan.", "stand/neutral/L; brain@R; text:2016@TR"),
  ("E", [("The photos appeared with varying numbers of likes.", "sherman2016")], "Photos with different like counts", "Photo cards with hearts.", "point/neutral/L; numbers:LIKES@R"),
  ("E", [("Teens were more likely to like photos that already had many likes.", "sherman2016")], "Many likes, more liking", "Rising bar.", "stand/smile/L; bars:few likes=h35,many likes=h70@R"),
  ("E", [("Photos with many likes were linked with activity in brain regions tied to reward, social cognition, imitation and attention.", "sherman2016")], "Linked to reward and attention regions", "Brain with glowing areas.", "point/neutral/L; brain@R"),
  ("E", [("When teens viewed risky photos, activity was lower in regions tied to cognitive control.", "sherman2016")], "Risky photos: less cognitive control", "Brain, dimmer area.", "stand/worry/L; brain@R"),
  ("E", [("These are findings from teenagers in one lab study.", "sherman2016")], "One lab study of teens", "Single card.", "shrug/neutral/L; text:1 STUDY@R"),
  ("E", [("Brain activity alone does not prove that likes cause craving.", "sherman2016")], "Activity is not proof of craving", "Cross over a heart.", "shrug/neutral/L; cross@R"),
  ("T", [("So likes may engage the brain's reward circuitry, at least in this study of teens.", "sherman2016")], "Likes may engage reward circuits", "Stickman with a smile.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: what are the attachment styles, in under a minute?", "PLAN")], "Tomorrow: attachment styles", "Two linked hearts.", "stand/neutral/L; text:ATTACHMENT?@R"),
 ])

DAYS[46] = dict(
 title="Attachment Styles in 50 Seconds",
 description_core="What are secure, avoidant and anxious attachment? A 1987 newspaper love quiz found 56%, 25% and 19% chose each description, and a meta-analysis found attachment moderately, not completely, stable over a lifetime.",
 primary=["hazan1987", "fraley2002"],
 hashtags=["#psychology", "#shorts", "#attachmentstyles", "#relationships", "#attachmenttheory", "#psychologyfacts"],
 caveats="The 1987 sample was a self-selected newspaper sample, so the percentages are not a population census. The stability figure (r about .39) is from a meta-analysis of infancy-to-adulthood studies and does not mean attachment is fixed.",
 thumb=(["ATTACHMENT", "STYLES IN 50s"], 1, 0),
 scenes=[
  ("H", [("What are attachment styles, in under a minute?", "PLAN")], "Attachment styles in 50 s", "Two linked hearts.", "think/neutral/C; text:3 STYLES@R"),
  ("E", [("In 1987, Cindy Hazan and Phillip Shaver applied attachment theory to adult romantic love.", "hazan1987")], "1987: attachment in adult love", "Heart.", "point/neutral/L; text:1987@TR; text:ADULT LOVE@R"),
  ("E", [("They ran a love quiz in a newspaper.", "hazan1987")], "A newspaper love quiz", "Newspaper.", "stand/neutral/L; list:LOVE QUIZ@R"),
  ("E", [("Fifty-six percent chose the secure description.", "hazan1987")], "Secure: 56%", "Bar at 56%.", "stand/smile/L; bars:secure=56%,avoidant=25%,anxious=19%@R"),
  ("E", [("Twenty-five percent chose avoidant.", "hazan1987")], "Avoidant: 25%", "Bar at 25%.", "stand/neutral/L; bars:secure=56%,avoidant=25%,anxious=19%@R"),
  ("E", [("And nineteen percent chose anxious-ambivalent.", "hazan1987")], "Anxious: 19%", "Bar at 19%.", "stand/neutral/L; bars:secure=56%,avoidant=25%,anxious=19%@R"),
  ("E", [("Secure respondents reported relationships averaging about ten years, versus about five and six for the others.", "hazan1987")], "Secure ~10 yrs; others 5, 6", "Calendar.", "point/smile/L; bars:secure=10y,avoidant=5y,anxious=6y@R"),
  ("E", [("In 2002, Chris Fraley combined 27 effect sizes from 23 papers on attachment stability from infancy to adulthood.", "fraley2002")], "2002: 27 effect sizes, 23 papers", "Stack of papers.", "stand/neutral/L; text:2002@TR; numbers:27@R"),
  ("E", [("He found a correlation of about point three nine: moderate, not fixed.", "fraley2002")], "Moderate stability, not fixed", "Medium bar.", "point/neutral/L; bars:stability=h40@R"),
  ("E", [("The newspaper sample was self-selected, so those percentages are not a census.", "hazan1987")], "Self-selected sample", "Newspaper with a question mark.", "shrug/neutral/L; qmark@R"),
  ("T", [("So attachment styles are a useful framework, with real limits.", "hazan1987,fraley2002")], "Useful, with limits", "Stickman with a small check.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: why do some people stay in relationships that hurt?", "PLAN")], "Tomorrow: why people stay", "Stickman at a door.", "stand/neutral/L; door@R"),
 ])

DAYS[47] = dict(
 title="Why Do People Stay in Relationships That Hurt?",
 description_core="The investment model says commitment depends on satisfaction, alternatives and investments. A 1995 study of women in shelters linked commitment with poorer alternatives and higher investments. This is research, not personal advice; if you or someone you know is unsafe, contact local support services.",
 primary=["rusbult1980", "rusbult1995"],
 hashtags=["#psychology", "#shorts", "#relationships", "#investmentmodel", "#socialpsychology", "#psychologyfacts"],
 caveats="Sensitive topic. The video is educational, describes constraints rather than blaming anyone, and does not give advice. The 1995 finding on reported abuse is as summarized in abstracts; the sample was 100 women in shelters. Add a support-line note in the description.",
 thumb=(["WHY PEOPLE STAY", "WHEN IT HURTS"], 1, 0),
 scenes=[
  ("H", [("Why do some people stay in relationships that hurt?", "PLAN")], "Why do people stay?", "Stickman at a crossroads.", "think/worry/C; qmark@R"),
  ("E", [("In 1980, Caryl Rusbult proposed the investment model of commitment.", "rusbult1980")], "1980: the investment model", "Model diagram.", "point/neutral/L; text:1980@TR; text:INVESTMENT MODEL@R"),
  ("E", [("It says commitment depends on satisfaction, the quality of alternatives and the size of investments.", "rusbult1980")], "Satisfaction, alternatives, investments", "Three-item list.", "stand/neutral/L; list:SATISFACTION,ALTERNATIVES,INVESTMENTS@R"),
  ("E", [("Investments are resources tied to the relationship.", "rusbult1980")], "Investments: resources tied to it", "Stack of coins.", "stand/neutral/L; coin:$@R"),
  ("E", [("In 1995, Rusbult and Martz studied one hundred women at shelters for abused women.", "rusbult1995")], "1995: 100 women at shelters", "Counter.", "stand/neutral/L; text:1995@TR; numbers:100@R"),
  ("E", [("Their commitment was greater when they had poorer alternatives.", "rusbult1995")], "More commitment: poorer alternatives", "Narrow door.", "point/neutral/L; door@R"),
  ("E", [("And when they had higher investments in the relationship.", "rusbult1995")], "And higher investments", "More coins.", "stand/neutral/L; coin:$$@R"),
  ("E", [("And when they reported less abuse.", "rusbult1995")], "And less reported abuse", "Lower bar.", "stand/neutral/L; bars:abuse=h25@R"),
  ("E", [("The authors called this nonvoluntary dependence: leaving is hard when options are limited.", "rusbult1995")], "Nonvoluntary dependence", "Narrow exit.", "think/neutral/L; door@R"),
  ("E", [("This describes constraints in a study, not blame for anyone who stays.", "rusbult1995")], "Constraints, not blame", "Stickman with open hands.", "stand/neutral/L; text:NO BLAME@R"),
  ("T", [("So research on staying points to limited alternatives and heavy investments, not simple weakness.", "rusbult1980,rusbult1995")], "Constraints, not weakness", "Stickman with a small check.", "stand/neutral/L; check@R"),
  ("C", [("Tomorrow: why does a free sample make us want to give something back?", "PLAN")], "Tomorrow: free samples", "Gift box.", "stand/neutral/L; text:FREE?@R"),
 ])

DAYS[48] = dict(
 title="The Reciprocity Rule: Why Favors Create Debts",
 description_core="Does a small favor make us want to repay it? In a 1971 experiment, people who got a free Coke later bought more raffle tickets from the giver, even when they said they didn't like him.",
 primary=["regan1971"],
 hashtags=["#psychology", "#shorts", "#reciprocity", "#persuasion", "#socialpsychology", "#psychologyfacts"],
 caveats="One 1971 laboratory experiment. Applying it to free samples is an extension, and the video says so rather than claiming stores use it.",
 thumb=(["FAVORS CREATE", "DEBTS?"], 1, 0),
 scenes=[
  ("H", [("Does getting a small favor make us want to give something back?", "PLAN")], "Do favors create debts?", "Gift box.", "think/neutral/C; text:FAVOR@R"),
  ("E", [("In 1971, Dennis Regan ran an experiment in which people rated paintings.", "regan1971")], "1971: rating paintings", "Painting.", "stand/neutral/L; text:1971@TR; text:PAINTINGS@R"),
  ("E", [("During a break, a partner of the researcher, Joe, sometimes returned with a Coke for the participant.", "regan1971")], "Joe brings a Coke", "Soda bottle.", "point/smile/L; text:COKE@R"),
  ("E", [("Later, Joe asked participants to buy raffle tickets.", "regan1971")], "Later: 'buy raffle tickets?'", "Ticket.", "stand/neutral/L; tag:RAFFLE@R"),
  ("E", [("Participants who got the favor bought more tickets than those who did not.", "regan1971")], "Favor: more tickets bought", "Rising bar.", "stand/smile/L; bars:no favor=h35,favor=h70@R"),
  ("E", [("This held even when they said they didn't like Joe.", "regan1971")], "Even if they didn't like him", "Frown beside ticket.", "shock/worry/L; text:DISLIKED@R"),
  ("E", [("Regan linked the result to a norm of reciprocity: we feel we should repay.", "regan1971")], "Norm of reciprocity", "Two-way arrow.", "think/neutral/L; arrow@R"),
  ("E", [("It was one laboratory experiment.", "regan1971")], "One lab experiment", "Single card.", "shrug/neutral/L; text:1 STUDY@R"),
  ("E", [("Applying it to free samples in stores is an extension, not something this study tested.", "regan1971")], "Free samples: not tested here", "Cross.", "shrug/neutral/L; cross@R"),
  ("T", [("So a small favor may create a pull to repay, even toward someone you don't like.", "regan1971")], "A pull to repay", "Stickman with a gift.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: why do we judge other people's character but explain away our own behavior?", "PLAN")], "Tomorrow: judging others", "Magnifier.", "stand/neutral/L; qmark@R"),
 ])

DAYS[49] = dict(
 title="The Fundamental Attribution Error Explained",
 description_core="Do we read other people's behavior as who they are? A 1967 study found people inferred attitudes from essays even when told the writer had been assigned the position. This tendency was later named the fundamental attribution error.",
 primary=["jones1967", "ross1977"],
 hashtags=["#psychology", "#shorts", "#attributionerror", "#cognitivebias", "#socialpsychology", "#psychologyfacts"],
 caveats="The Jones & Harris design is known from consistent secondary summaries. The title phrase 'judge ourselves differently' is not claimed in the video; only the attribution of others' behavior to their character is covered.",
 thumb=(["CHARACTER OR", "SITUATION?"], 1, 0),
 scenes=[
  ("H", [("Why do we blame a person's character for what a situation caused?", "PLAN")], "Character or situation?", "Stickman and a question mark.", "think/neutral/C; qmark@R"),
  ("E", [("In 1967, Edward Jones and Victor Harris had students read essays about Fidel Castro's Cuba.", "jones1967")], "1967: essays on Castro's Cuba", "Essay page.", "stand/neutral/L; text:1967@TR; text:ESSAYS@R"),
  ("E", [("Some were told the writers chose their positions freely.", "jones1967")], "Writers 'chose' the position", "Open hand.", "stand/neutral/L; check@R"),
  ("E", [("Others were told the writers had been assigned them.", "jones1967")], "Writers 'were assigned' it", "Assignment card.", "shrug/neutral/L; list:ASSIGNED@R"),
  ("E", [("Readers inferred the writers' attitudes from the essays.", "jones1967")], "Readers inferred attitudes", "Thought bubble.", "think/neutral/L; bubble:what they believe@TR"),
  ("E", [("Even when the position was assigned, readers still saw some of that attitude in the writer.", "jones1967")], "Even when assigned, they inferred it", "Stickman with a bubble.", "shock/neutral/L; bubble:they mean it@TR"),
  ("E", [("In 1977, Lee Ross named this tendency the fundamental attribution error.", "ross1977")], "1977: named 'FAE'", "Label.", "point/neutral/L; text:1977@TR; tag:FAE@R"),
  ("E", [("It is the tendency to explain behavior by character and underestimate the situation.", "ross1977")], "Character over situation", "Scale tilted.", "stand/neutral/L; scale@R"),
  ("E", [("The original studies used student readers in a laboratory.", "jones1967")], "Student readers, lab setting", "Lab flask.", "shrug/neutral/L; text:LAB@R"),
  ("T", [("So we may read a person's behavior as who they are, even when the situation explains it.", "jones1967,ross1977")], "Who they are, or the situation?", "Stickman with two options.", "stand/neutral/L; qmark@R"),
  ("C", [("Tomorrow: do opposites really attract?", "PLAN")], "Tomorrow: do opposites attract?", "Two magnets.", "stand/neutral/L; magnet@R"),
 ])

DAYS[50] = dict(
 title="Do Opposites Attract? What 313 Studies Found",
 description_core="Do opposites attract? A meta-analysis of 313 studies found perceived similarity predicted attraction more strongly than actual similarity, and the effect of actual similarity depended on whether people had interacted.",
 primary=["montoya2008"],
 hashtags=["#psychology", "#shorts", "#attraction", "#relationships", "#similarity", "#psychologyfacts"],
 caveats="The video reports the meta-analysis conclusions about similarity (perceived vs actual) and does not claim to settle every kind of difference. The details of the interaction moderator are stated loosely, as in the abstract.",
 thumb=(["DO OPPOSITES", "ATTRACT?"], 1, 0),
 scenes=[
  ("H", [("Do opposites really attract?", "PLAN")], "Do opposites attract?", "Two magnets.", "think/neutral/C; magnet@R"),
  ("E", [("In 2008, Montoya, Horton and Kirchner combined 313 studies on similarity and attraction.", "montoya2008")], "2008: 313 studies combined", "Stack of papers.", "stand/neutral/L; text:2008@TR; numbers:313@R"),
  ("E", [("They compared actual similarity, meaning real shared traits, with perceived similarity, meaning what people believe they share.", "montoya2008")], "Actual vs perceived similarity", "Two cards.", "point/neutral/L; list:ACTUAL,PERCEIVED@R"),
  ("E", [("Perceived similarity predicted attraction more strongly than actual similarity did.", "montoya2008")], "Perceived beat actual", "Taller bar for perceived.", "stand/smile/L; bars:actual=h40,perceived=h70@R"),
  ("E", [("The effect of actual similarity was large overall.", "montoya2008")], "Actual similarity: large overall", "Tall bar.", "stand/neutral/L; bars:actual=h70@R"),
  ("E", [("But it depended on whether the people had actually interacted.", "montoya2008")], "But it depended on interaction", "Two stickmen talking.", "think/neutral/L; crowd:1@R; qmark@TR"),
  ("E", [("So in this analysis, believing you're alike may matter at least as much as actually being alike.", "montoya2008")], "Feeling alike may matter", "Thought bubble: 'we're alike'.", "stand/smile/L; bubble:we're alike@TR"),
  ("E", [("This research measured similarity and attraction, not every kind of difference.", "montoya2008")], "Similarity only, not all differences", "Scale.", "shrug/neutral/L; scale@R"),
  ("E", [("Meta-analyses summarize many studies, and their conclusions depend on which studies were included.", "montoya2008")], "A summary of studies", "Papers.", "shrug/neutral/L; text:SUMMARY@R"),
  ("T", [("So in this research, feeling similar went with liking more than actually being similar did.", "montoya2008")], "Feeling similar went with liking", "Stickman with a heart.", "stand/smile/L; check@R"),
  ("C", [("Tomorrow: does using someone's name make them more likely to say yes?", "PLAN")], "Tomorrow: using someone's name", "Name tag.", "stand/neutral/L; tag:HELLO@R"),
 ])
