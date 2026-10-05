"""Days 1-10 (Month 1: How your brain tricks you). Every sentence carries source ids; 'PLAN' only for questions."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common_sources import S, SEC, SECOND

SOURCES = {
 "mcgaugh2004": S("McGaugh, J. L.", 2004, "The amygdala modulates the consolidation of memories of emotionally arousing experiences", "Annual Review of Neuroscience, 27, 1-28", "https://annualreviews.org/content/journals/neuro/27/1", SEC + " (amygdala engages adrenergic and cortisol stress-hormone systems that promote memory storage)"),
 "talarico2003": S("Talarico, J. M., & Rubin, D. C.", 2003, "Confidence, not consistency, characterizes flashbulb memories", "Psychological Science, 14(5), 455-461", "https://doi.org/10.1111/1467-9280.02453", SEC + " (54 students, retested after 1/6/32 weeks)"),
 "gilovich2000": S("Gilovich, T., Medvec, V. H., & Savitsky, K.", 2000, "The spotlight effect in social judgment: An egocentric bias in estimates of the salience of one's own actions and appearance", "Journal of Personality and Social Psychology, 78(2), 211-222", "https://www.kellogg.northwestern.edu/academics-research/research/detail/2000/the-spotlight-effect-in-social-judgment-an-egocentric-bias", SECOND + " (46% predicted vs 23% observed)"),
 "thomas2005": S("Thomas, M., & Morwitz, V. G.", 2005, "Penny wise and pound foolish: The left-digit effect in price cognition", "Journal of Consumer Research, 32(1), 54-64", "https://ideas.repec.org/a/oup/jconrs/v32y2005i1p54-64.html", SEC),
 "stiving2000": S("Stiving, M.", 2000, "Price-endings when prices signal quality", "Management Science, 46(12), 1617-1629", "https://ideas.repec.org/a/inm/ormnsc/v46y2000i12p1617-1629.html", SEC),
 "wason1960": S("Wason, P. C.", 1960, "On the failure to eliminate hypotheses in a conceptual task", "Quarterly Journal of Experimental Psychology, 12(3), 129-140", "https://doi.org/10.1080/17470216008416717", SEC + " (29 subjects; 6 reached the correct rule without a prior wrong one); rule wording 'any ascending sequence' from secondary summaries"),
 "lord1984": S("Lord, C. G., Lepper, M. R., & Preston, E.", 1984, "Considering the opposite: A corrective strategy for social judgment", "Journal of Personality and Social Psychology, 47(6), 1231-1243", "https://causeweb.org/cause/node/7638", SEC),
 "zeigarnik1927": S("Zeigarnik, B.", 1927, "Über das Behalten von erledigten und unerledigten Handlungen", "Psychologische Forschung, 9, 1-85", "https://en.wikipedia.org/wiki/Zeigarnik_effect", "web search 2026-10-05: original claim (interrupted tasks recalled better) confirmed via reference article and later meta-analysis abstract; original paper not read"),
 "vanbergen1968": S("Van Bergen, A.", 1968, "Task interruption", "North-Holland (monograph)", "https://en.wikipedia.org/wiki/Zeigarnik_effect", "web search 2026-10-05: replication attempt that found no advantage for interrupted tasks (ratio 0.88), per reference article and a science-news summary"),
 "ghibellini2025": S("Ghibellini, R., & Meier, B.", 2025, "Interruption, recall and resumption: A meta-analysis of the Zeigarnik and Ovsiankina effects", "Humanities and Social Sciences Communications (Palgrave Communications), 12", "https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05000-w.html", SEC + " (abstract: no memory advantage for unfinished tasks; general tendency to resume)"),
 "masicampo2011": S("Masicampo, E. J., & Baumeister, R. F.", 2011, "Consider it done! Plan making can eliminate the cognitive effects of unfulfilled goals", "Journal of Personality and Social Psychology, 101(4), 667-683", "https://supp.apa.org/psycarticles/supplemental/a0024192/a0024192_supp.html", SEC + " (full abstract quoted in search results)"),
 "kahneman1979": S("Kahneman, D., & Tversky, A.", 1979, "Prospect theory: An analysis of decision under risk", "Econometrica, 47(2), 263-291", "https://stafforini.com/works/kahneman-1979-prospect-theory-analysis/", SEC),
 "tversky1992": S("Tversky, A., & Kahneman, D.", 1992, "Advances in prospect theory: Cumulative representation of uncertainty", "Journal of Risk and Uncertainty, 5(4), 297-323", "https://ideas.repec.org/a/kap/jrisku/v5y1992i4p297-323.html", SEC + " (loss-aversion coefficient 2.25 in their model)"),
 "gal2018": S("Gal, D., & Rucker, D. D.", 2018, "The loss of loss aversion: Will it loom larger than its gain?", "Journal of Consumer Psychology, 28(3), 497-516", "https://papers.ssrn.com/abstract=3049660", SEC + " (full abstract quoted)"),
 "kruger1999": S("Kruger, J., & Dunning, D.", 1999, "Unskilled and unaware of it: How difficulties in recognizing one's own incompetence lead to inflated self-assessments", "Journal of Personality and Social Psychology, 77(6), 1121-1134", "https://www.altmetric.com/details/464305", SEC + " (abstract incl. 12th vs 62nd percentile and training result)"),
 "gignac2020": S("Gignac, G. E., & Zajenkowski, M.", 2020, "The Dunning-Kruger effect is (mostly) a statistical artefact: Valid approaches to testing the hypothesis with individual differences data", "Intelligence, 80, 101449", "https://www.Gwern.net/doc/iq/2020-gignac.pdf", SEC + " (929 participants)"),
 "liikkanen2012": S("Liikkanen, L. A.", 2012, "Musical activities predispose to involuntary musical imagery", "Psychology of Music, 40(2), 236-256", "https://journals.sagepub.com/doi/10.1177/0305735611406578", SEC + " (N = 12,519 Finnish internet users; 89.2% weekly)"),
 "jakubowski2016": S("Jakubowski, K., Finkel, S., Stewart, L., & Müllensiefen, D.", 2017, "Dissecting an earworm: Melodic features and song popularity predict involuntary musical imagery", "Psychology of Aesthetics, Creativity, and the Arts, 11(2), 122-135 (online 2016)", "https://research.gold.ac.uk/19405", SEC + " (tunes named by 3,000 survey participants)"),
 "beaman2015": S("Beaman, C. P., Powell, K., & Rapley, E.", 2015, "Want to block earworms from conscious awareness? B(u)y gum!", "Quarterly Journal of Experimental Psychology, 68(6), 1049-1057", "https://centaur.reading.ac.uk/40114/", SEC + " (Experiment 1: 98 participants)"),
 "tversky1974": S("Tversky, A., & Kahneman, D.", 1974, "Judgment under uncertainty: Heuristics and biases", "Science, 185(4157), 1124-1131", "https://pubmed.ncbi.nlm.nih.gov/17835457/", SEC + " (wheel of fortune; medians 25 and 45)"),
 "galinsky2001": S("Galinsky, A. D., & Mussweiler, T.", 2001, "First offers as anchors: The role of perspective-taking and negotiator focus", "Journal of Personality and Social Psychology, 81(4), 657-669", "https://pubmed.ncbi.nlm.nih.gov/11642352", SEC + " (full abstract quoted)"),
 "radvansky2011": S("Radvansky, G. A., Krawietz, S. A., & Tamplin, A. K.", 2011, "Walking through doorways causes forgetting: Further explorations", "Quarterly Journal of Experimental Psychology, 64(8), 1632-1645", "https://bps.org.uk/research-digest/how-walking-through-doorway-increases-forgetting", SEC + " (real and virtual environments)"),
 "mcfadyen2021": S("McFadyen, J., Nolan, C., Pinocy, E., Buteri, D., & Baumann, O.", 2021, "Doorways do not always cause forgetting: A multimodal investigation", "BMC Psychology, 9", "https://discovery-pp.ucl.ac.uk/id/eprint/10123784", SEC + " (four experiments; abstract quoted)"),
}

C = lambda s: s  # readability

DAYS = {}

DAYS[1] = dict(
 title="Why That Cringe Memory Never Leaves You",
 description_core="Why does an embarrassing moment replay in your head for years? Research suggests emotional arousal helps your brain store memories more strongly, but a vivid memory is not necessarily an accurate one.",
 primary=["mcgaugh2004", "talarico2003"],
 hashtags=["#psychology", "#shorts", "#memory", "#brain", "#psychologyfacts", "#cognitivebias"],
 caveats="Flashbulb-memory study (Talarico & Rubin 2003) had 54 students at one university. The amygdala works with other brain regions; the video simplifies. McGaugh's account concerns emotional arousal in general, not embarrassment specifically.",
 thumb=(["WHY YOU", "REMEMBER", "CRINGE"], 2, 0),
 scenes=[
  ("H", [("Why do you still cringe at that embarrassing moment?", "PLAN")], "Still cringing", "Stickman clutches head, wincing, as a small cloud labeled 'that moment' hovers above.", "shock/worry/C; bubble:that moment@TR"),
  ("E", [("After an emotional experience, a brain region called the amygdala activates your stress-hormone systems.", "mcgaugh2004")], "Amygdala + stress hormones", "Cutaway brain with the amygdala highlighted in the accent color and wavy stress lines.", "think/neutral/L; brain:amygdala@R; waves@TR"),
  ("E", [("Neuroscientist James McGaugh argued that this signal helps the brain store the memory more strongly.", "mcgaugh2004")], "Stronger storage", "Memory file stamped with a bold SAVE tag.", "point/neutral/L; tag:SAVE@R"),
  ("E", [("But a strong memory is not always an accurate one.", "talarico2003")], "Strong is not accurate", "Two cards: 'vivid' with a check, 'accurate' with a question mark.", "shrug/neutral/L; qmark@R"),
  ("E", [("On September 12, 2001, researchers asked 54 students to record how they heard about the attacks, then retested them up to 32 weeks later.", "talarico2003")], "54 students, retested later", "A calendar with three marks: 1, 6 and 32 weeks.", "stand/neutral/L; clock@R; text:54 STUDENTS@TR"),
  ("E", [("Their memories of the attacks became just as inconsistent as their memories of an everyday event.", "talarico2003")], "Same inconsistency", "Two matching downward lines labeled 'attacks' and 'everyday'.", "stand/neutral/L; lines:attacks,everyday@R"),
  ("E", [("Yet only for the everyday memories did vividness and belief in accuracy fade.", "talarico2003")], "Confidence stayed high", "Confidence line stays high while the everyday line falls.", "think/worry/L; lines:flashbulb,everyday@R"),
  ("T", [("So when a cringe memory feels crystal clear, remember that clarity is not proof of accuracy.", "talarico2003")], "Clear is not accurate", "Stickman pauses and peers at a clear memory bubble.", "point/smile/L; bubble:clear?@TR"),
  ("C", [("Tomorrow: did everyone else notice that moment as much as you think?", "PLAN")], "Tomorrow: who noticed?", "Crowd of tiny stickmen, none looking at ours.", "stand/neutral/L; crowd:5@R; text:TOMORROW@TR"),
 ])

DAYS[2] = dict(
 title="Nobody's Watching You As Much As You Think",
 description_core="Do you think everyone noticed your slip-up? In a classic study, people wearing an embarrassing T-shirt guessed about twice as many classmates would notice it as actually did.",
 primary=["gilovich2000"],
 hashtags=["#psychology", "#shorts", "#spotlighteffect", "#socialanxiety", "#confidence", "#psychologyfacts"],
 caveats="Percentages (46% predicted vs 23% observed) come from secondary summaries of the paper; the PDF could not be opened from this environment. The effect was shown with college students in a lab. Egocentrism is the authors' proposed explanation.",
 thumb=(["NOBODY'S", "WATCHING", "YOU"], 0, 0),
 scenes=[
  ("H", [("Do you think everyone noticed that mistake?", "PLAN")], "Did everyone notice?", "Stickman cowering under a harsh spotlight.", "shock/worry/C; spotlight@C"),
  ("E", [("In 2000, psychologist Thomas Gilovich and colleagues published the first empirical evidence of the spotlight effect.", "gilovich2000")], "The spotlight effect, 2000", "Title card 'SPOTLIGHT EFFECT' above a stickman in a light cone.", "stand/neutral/L; spotlight@L; text:SPOTLIGHT EFFECT@TR"),
  ("E", [("Students wore an embarrassing Barry Manilow T-shirt into a room of other students.", "gilovich2000")], "The embarrassing T-shirt", "Stickman in a goofy T-shirt entering a room of tiny stickmen.", "walk/worry/L; tshirt:BARRY@R; crowd:4@B"),
  ("E", [("The wearers guessed that about 46 percent of the others would notice the shirt.", "gilovich2000")], "They guessed 46%", "Tall bar labeled 'guessed 46%'.", "think/worry/L; bars:guessed=46%,actual=23%@R"),
  ("E", [("In reality, only about 23 percent did.", "gilovich2000"), ("That means they overestimated by about double.", "gilovich2000")], "Actually: 23%", "Short bar labeled 'noticed 23%' next to the tall one.", "point/neutral/L; bars:guessed=46%,actual=23%@R"),
  ("E", [("Researchers call this the spotlight effect: we overestimate how much others notice us.", "gilovich2000")], "We overestimate attention", "Stickman in a spotlight; crowd looks elsewhere.", "stand/smile/L; spotlight@L"),
  ("E", [("They attribute it to egocentrism: you experience your own flaws so intensely that you assume others do too.", "gilovich2000")], "Egocentrism", "Stickman is the big star of his own show; others are small.", "shrug/neutral/L; crowd:5@R"),
  ("T", [("Next time you feel watched, remember the shirt study: people notice you roughly half as much as you expect.", "gilovich2000")], "Roughly half as much", "Two bars side by side, expected and real.", "walk/smile/L; bars:expected=46%,real=23%@R"),
  ("C", [("Tomorrow: why does $9.99 feel so much cheaper than $10?", "PLAN")], "Tomorrow: $9.99", "A price tag reading $9.99 with a sly eye.", "stand/smile/L; tag:$9.99@R; text:TOMORROW@TR"),
 ])

DAYS[3] = dict(
 title="The One-Cent Trick Behind Every $9.99",
 description_core="Why does $9.99 feel so much cheaper than $10? Experiments show a nine-ending price looks smaller than a price one cent higher, but only when the leftmost digits differ.",
 primary=["thomas2005", "stiving2000"],
 hashtags=["#psychology", "#shorts", "#pricing", "#marketing", "#shopping", "#psychologyfacts"],
 caveats="Thomas & Morwitz (2005) identify when the effect occurs; its size varies. Stiving (2000) is an economic model plus empirical evidence that firms use round prices more for higher-quality products; the model is debated (a 2003 comment exists).",
 thumb=(["THE $9.99", "TRICK"], 0, 0),
 scenes=[
  ("H", [("Why does $9.99 feel so much cheaper than $10?", "PLAN")], "$9.99 vs $10", "Two price tags side by side, one cent apart.", "stand/neutral/L; tag:$9.99@TR; tag:$10@R"),
  ("E", [("Researchers call it the left-digit effect.", "thomas2005")], "The left-digit effect", "Magnifying glass over the leftmost digit.", "point/neutral/L; numbers:9 . 9 9@R"),
  ("E", [("In five experiments, Manoj Thomas and Vicki Morwitz found that a nine-ending price looks smaller than a price one cent higher.", "thomas2005")], "Nine-ending looks smaller", "Two tags: $2.99 looks smaller than $3.00.", "think/neutral/L; tag:$2.99@TR; tag:$3.00@R"),
  ("E", [("But only when the leftmost digits differ, like $2.99 versus $3.00.", "thomas2005")], "Only if the left digit changes", "$2.98 vs $2.99 crossed out; $2.99 vs $3.00 circled.", "point/smile/L; numbers:2 3@R; check@TR"),
  ("E", [("They also found the effect was stronger when the two prices being compared were close together.", "thomas2005")], "Stronger when prices are close", "Two tags drawn close together.", "stand/neutral/L; tag:$2.99@TR; tag:$3.00@R"),
  ("E", [("And it appeared with other multi-digit numbers, not just prices.", "thomas2005")], "Not only prices", "Random multi-digit numbers floating around.", "shock/neutral/L; numbers:4 0 0 0@R"),
  ("E", [("A separate analysis found that firms tend to use more round prices for higher-quality products.", "stiving2000")], "Round prices, higher quality", "A luxury watch with a round price tag.", "stand/neutral/L; coin:$500@R"),
  ("E", [("Researcher Mark Stiving argued that firms signaling quality are more likely to use round prices.", "stiving2000")], "Round can signal quality", "Premium shelf with round tags vs sale shelf with 9s.", "stand/smile/L; list:$500,$99.99@R"),
  ("T", [("So when a price ends in nine, try rounding it up to the next number before you decide.", "thomas2005")], "Round it up first", "Stickman rounds $9.99 up to $10 with an eraser.", "point/smile/L; tag:$9.99@TR; arrow:right@R; tag:$10@B"),
  ("C", [("Tomorrow: why do you test only the ideas you already believe?", "PLAN")], "Tomorrow: your beliefs", "Stickman with blinders in front of a fact sheet.", "stand/worry/L; list:FACT,FACT,FACT@R; text:TOMORROW@TR"),
 ])

DAYS[4] = dict(
 title="Your Brain Hides Evidence You Disagree With",
 description_core="Do you really look at all the evidence? In Peter Wason's classic 2-4-6 task, most people tested only examples that fit their own guess, and a simple 'consider the opposite' strategy reduced bias in later experiments.",
 primary=["wason1960", "lord1984"],
 hashtags=["#psychology", "#shorts", "#confirmationbias", "#cognitivebias", "#criticalthinking", "#psychologyfacts"],
 caveats="Wason's task is a simplified lab model of hypothesis testing; the sample was 29 people. The rule wording ('any ascending sequence') and the 'most tested only fitting examples' summary come from secondary descriptions of the 1960 paper. Lord, Lepper & Preston tested consider-the-opposite on biased assimilation and impression formation, not every decision.",
 thumb=(["YOUR BRAIN", "HIDES FACTS"], 1, 4),
 scenes=[
  ("H", [("Do you really look at all the evidence?", "PLAN")], "All the evidence?", "Stickman wearing blinders in front of a pile of papers.", "stand/neutral/C; list:YES,YES,NO@R"),
  ("E", [("In 1960, psychologist Peter Wason gave 29 people the numbers 2, 4, 6.", "wason1960")], "Wason's 2-4-6 puzzle", "Three big numbers: 2, 4, 6.", "point/neutral/L; numbers:2 4 6@R; qmark@TR"),
  ("E", [("Their task was to discover the hidden rule by proposing their own sets of three numbers.", "wason1960")], "Find the hidden rule", "Stickman writes three-number guesses.", "think/neutral/L; numbers:? ? ?@R"),
  ("E", [("The actual rule was simply any ascending sequence.", "wason1960")], "Rule: any ascending numbers", "Numbers climbing upward like stairs.", "stand/smile/L; numbers:1 5 9@R; arrow:right@TR"),
  ("E", [("Most people tested only examples that fit their own guess.", "wason1960")], "They tested what fit", "A row of green checks next to matching guesses.", "think/smile/L; list:FIT,FIT,FIT@R; check@TR"),
  ("E", [("Only 6 of the 29 announced the correct rule without first announcing a wrong one.", "wason1960")], "Only 6 of 29", "Counter showing 6 of 29 lit up.", "shock/neutral/L; text:6 OF 29@R"),
  ("E", [("Wason concluded people tend to seek only confirming evidence.", "wason1960")], "Confirmation bias", "Magnet pulling only 'agree' papers.", "point/neutral/L; magnet@R; text:CONFIRMATION@TR"),
  ("T", [("Psychologists Lord, Lepper and Preston tested a fix: consider the opposite.", "lord1984")], "Consider the opposite", "Stickman flipping a card to its other side.", "stand/smile/L; arrow:right@R"),
  ("T", [("In two experiments, asking people to consider the opposite reduced bias more than telling them to be fair and unbiased.", "lord1984")], "Beats 'be fair'", "Two bars: 'be fair' short, 'consider the opposite' tall.", "stand/smile/L; bars:be fair,opposite@R"),
  ("T", [("So before a big decision, ask yourself: what would prove me wrong?", "lord1984")], "What would prove me wrong?", "Stickman holding a magnifying glass toward a red NO paper.", "think/smile/L; qmark@R; text:PROVE ME WRONG@TR"),
  ("C", [("Tomorrow: do unfinished tasks really haunt your memory?", "PLAN")], "Tomorrow: unfinished tasks", "Open to-do list glowing.", "stand/worry/L; list:TODO,TODO,TODO@R; text:TOMORROW@TR"),
 ])

DAYS[5] = dict(
 title="Why Unfinished Tasks Haunt Your Brain",
 description_core="Do unfinished tasks really stick in memory? A 2025 meta-analysis found no memory advantage, but unfinished goals can still intrude on your thoughts, and a specific plan can quiet them.",
 primary=["masicampo2011", "ghibellini2025"],
 hashtags=["#psychology", "#shorts", "#zeigarnik", "#productivity", "#procrastination", "#psychologyfacts"],
 caveats="Zeigarnik's original memory claim has failed to replicate (Van Bergen 1968; Ghibellini & Meier 2025 meta-analysis). Masicampo & Baumeister (2011) studied goal-related intrusive thoughts in lab tasks, not everyday to-do lists.",
 thumb=(["UNFINISHED", "TASKS", "HAUNT YOU"], 0, 0),
 scenes=[
  ("H", [("Why do unfinished tasks nag at you?", "PLAN")], "Why won't it let go?", "Stickman at a desk surrounded by half-done checklists.", "think/worry/C; list:TODO,TODO@R"),
  ("E", [("In the 1920s, psychologist Bluma Zeigarnik reported that people remembered interrupted tasks better than completed ones.", "zeigarnik1927")], "The Zeigarnik effect", "Vintage portrait frame with the name ZEIGARNIK.", "stand/neutral/L; text:ZEIGARNIK@R; text:1920s@TR"),
  ("E", [("That became known as the Zeigarnik effect.", "zeigarnik1927")], "Interrupted = remembered?", "Interrupted vs finished task cards.", "think/neutral/L; list:DONE,STOPPED@R"),
  ("E", [("But a 2025 meta-analysis found no memory advantage for unfinished tasks.", "ghibellini2025")], "2025: no memory advantage", "Scale balanced evenly.", "shrug/neutral/L; scale@R; text:2025@TR"),
  ("E", [("An earlier replication attempt by Annie van Bergen in 1968 had also failed to find one.", "vanbergen1968")], "1968 replication failed too", "A crossed-out check next to 1968.", "shrug/worry/L; cross@R; text:1968@TR"),
  ("E", [("Unfinished goals can still keep intruding on your thoughts, though.", "masicampo2011")], "Goals still intrude", "Little TODO bubbles popping up over the stickman's head.", "think/worry/L; bubble:TODO@TR; bubble:TODO@R"),
  ("E", [("Psychologists Masicampo and Baumeister showed that making a specific plan for a goal eliminated those effects.", "masicampo2011")], "A specific plan helped", "Stickman writes a plan; TODO bubbles fade.", "point/smile/L; check@R; text:PLAN@TR"),
  ("E", [("In one study, the people who later carried out their plans were the ones whose intrusive thoughts stopped.", "masicampo2011")], "Real plans quiet the mind", "Check mark next to a calm brain.", "stand/smile/L; brain:@R; check@TR"),
  ("T", [("So instead of just listing a task, decide exactly when and where you will start.", "masicampo2011")], "Decide when and where", "Clock and map pin next to a task.", "point/smile/L; clock@R; text:WHEN + WHERE@TR"),
  ("C", [("Tomorrow: why does losing hurt more than winning feels good?", "PLAN")], "Tomorrow: why losing stings", "Two coins: one lost, one won.", "stand/worry/L; coin:+$20@R; text:TOMORROW@TR"),
 ])

DAYS[6] = dict(
 title="Why Losing Hurts More Than Winning Feels Good",
 description_core="Do losses really hurt about twice as much as equal gains? That's the classic prospect-theory idea, but a 2018 review argued the evidence doesn't support it as a general rule.",
 primary=["kahneman1979", "gal2018"],
 hashtags=["#psychology", "#shorts", "#lossaversion", "#behavioraleconomics", "#decisionmaking", "#psychologyfacts"],
 caveats="CONTESTED. 'About twice' reflects a model parameter (2.25) fitted to certain gambling choices (Tversky & Kahneman 1992). Gal & Rucker (2018) argue evidence does not support losses being more impactful on balance and that context matters; defenders of loss aversion disagree. Video presents it as a debated rule of thumb.",
 thumb=(["LOSING", "HURTS MORE"], 0, 0),
 scenes=[
  ("H", [("Why does losing feel worse than winning feels good?", "PLAN")], "Losing hurts more?", "Stickman holding a lost coin next to a smaller won coin.", "shock/worry/C; coin:-$20@R"),
  ("E", [("In 1979, Daniel Kahneman and Amos Tversky proposed prospect theory.", "kahneman1979")], "Prospect theory, 1979", "Title card PROSPECT THEORY 1979.", "stand/neutral/L; text:PROSPECT THEORY@TR; text:1979@R"),
  ("E", [("One key idea is loss aversion: losses loom larger than equivalent gains.", "kahneman1979")], "Losses loom larger", "Balance scale tipping toward the loss side.", "point/neutral/L; scale@R"),
  ("E", [("In 1992, Tversky and Kahneman estimated a loss-aversion coefficient of about 2.25.", "tversky1992")], "Estimated coefficient: 2.25", "Big number 2.25.", "think/neutral/L; numbers:2.25@R"),
  ("E", [("Roughly speaking, that means a loss counts about twice as much as a gain of the same size.", "tversky1992")], "Loss counts about 2x", "Coin -$100 vs coin +$200.", "stand/neutral/L; coin:-$100@R; coin:+$200@B"),
  ("E", [("But the idea is contested.", "gal2018")], "But it's contested", "Two stickmen arguing with a question mark between.", "shrug/neutral/L; qmark@R"),
  ("E", [("In 2018, David Gal and Derek Rucker reviewed the evidence and concluded that losses, on balance, are not more impactful than gains.", "gal2018")], "2018 review disagrees", "Scale balanced evenly.", "stand/neutral/L; scale@R; text:2018@TR"),
  ("E", [("They argue the impact of losses versus gains depends on context.", "gal2018")], "It depends on context", "Different scenes: shop, casino, job.", "shrug/smile/L; list:SHOP,JOB,GAME@R"),
  ("T", [("So treat 'losses hurt twice as much' as a debated rule of thumb, not a law.", "gal2018")], "Debated rule of thumb", "Rule-of-thumb ruler with a question mark.", "stand/smile/L; qmark@R; text:NOT A LAW@TR"),
  ("T", [("When you hear it, ask: in which situation, and compared with what?", "gal2018")], "Which situation? Compared to what?", "Stickman asking two questions.", "point/smile/L; text:WHEN? VS WHAT?@R"),
  ("C", [("Tomorrow: do unskilled people really think they're geniuses?", "PLAN")], "Tomorrow: Dunning-Kruger", "Quote bubble with a crown.", "stand/neutral/L; text:GENIUS?@R; text:TOMORROW@TR"),
 ])

DAYS[7] = dict(
 title="Dunning-Kruger: What Everyone Gets Wrong",
 description_core="Do unskilled people really think they're geniuses? Not quite: in the original study the lowest scorers overestimated their rank, but a 2020 analysis argued much of the classic pattern is a statistical artefact.",
 primary=["kruger1999", "gignac2020"],
 hashtags=["#psychology", "#shorts", "#dunningkruger", "#cognitivebias", "#selfawareness", "#psychologyfacts"],
 caveats="CONTESTED. Gignac & Zajenkowski (2020) used intelligence tests in 929 community participants; their critique applies to that way of testing, and Dunning and others dispute it. The popular 'Mount Stupid' graph is not from the 1999 paper (not used here).",
 thumb=(["DUNNING-KRUGER", "MISUNDERSTOOD"], 1, 0),
 scenes=[
  ("H", [("Do unskilled people really think they're geniuses?", "PLAN")], "Do they think they're geniuses?", "Stickman wearing a paper crown.", "stand/smile/C; text:GENIUS?@R"),
  ("E", [("In 1999, Justin Kruger and David Dunning tested people on humor, grammar and logic.", "kruger1999")], "Kruger & Dunning, 1999", "Quiz sheets: humor, grammar, logic.", "point/neutral/L; list:HUMOR,GRAMMAR,LOGIC@R"),
  ("E", [("Those who scored in the bottom quarter guessed they'd done much better than they had.", "kruger1999")], "Lowest scorers overestimated", "Two bars: low actual, higher guessed.", "stand/smile/L; bars:actual=12%,guessed=62%@R"),
  ("E", [("They scored around the 12th percentile but estimated themselves near the 62nd.", "kruger1999")], "12th vs 62nd percentile", "Numbers 12 and 62.", "think/neutral/L; numbers:12 62@R"),
  ("E", [("The researchers argued that skill and the ability to judge your skill are linked.", "kruger1999")], "Skill and self-judging linked", "Two linked gears: DO and JUDGE.", "think/neutral/L; text:DO + JUDGE@R"),
  ("E", [("When they trained participants in logic, those participants became better at recognizing their own limits.", "kruger1999")], "Training helped self-judgment", "Stickman studying, then checking a score.", "stand/smile/L; check@R"),
  ("E", [("But here's the catch: a 2020 study of 929 people argued that the classic pattern is mostly a statistical artifact.", "gignac2020")], "2020: mostly a statistical artifact?", "Graph stamped 'DEBATED'.", "shrug/neutral/L; lines:myth,test@R; text:DEBATED@TR"),
  ("E", [("It found that self-rated and measured intelligence rose together in almost a straight line.", "gignac2020")], "Almost a straight line", "Straight upward line.", "stand/neutral/L; lines:rated,measured@R"),
  ("T", [("So when you're learning something new, building skill may also improve your ability to judge your own work.", "kruger1999")], "Skill helps you judge your work", "Stickman holding up his work next to a ruler.", "point/smile/L; check@R; text:SKILL + JUDGMENT@TR"),
  ("C", [("Tomorrow: why is that song stuck in your head?", "PLAN")], "Tomorrow: stuck songs", "Musical notes floating from the stickman's head.", "stand/neutral/L; notes@R; text:TOMORROW@TR"),
 ])

DAYS[8] = dict(
 title="Why That Song Won't Leave Your Head",
 description_core="Why does a song get stuck in your head? A large survey found nearly nine in ten people get an earworm weekly, earworm tunes tend to be faster with common melodic shapes, and chewing gum reduced them in a small lab experiment.",
 primary=["beaman2015", "liikkanen2012"],
 hashtags=["#psychology", "#shorts", "#earworm", "#music", "#brain", "#psychologyfacts"],
 caveats="Survey figure (89.2% weekly, N=12,519) is from Finnish internet users and may not generalize. The gum result is from small lab experiments (Experiment 1: 98 people) and is not a guaranteed cure. Jakubowski et al. compared tunes named as earworms with other songs; it describes tendencies, not rules.",
 thumb=(["WHY IS THAT", "SONG STUCK?"], 1, 0),
 scenes=[
  ("H", [("Why is that song stuck in your head?", "PLAN")], "Stuck song?", "Stickman holding head as notes swirl.", "shock/worry/C; notes@R"),
  ("E", [("Scientists call it involuntary musical imagery, or an earworm.", "liikkanen2012")], "Earworm = involuntary imagery", "Worm with headphones.", "stand/neutral/L; notes@R; text:EARWORM@TR"),
  ("E", [("In a survey of 12,519 Finnish adults, 89 percent reported having one at least once a week.", "liikkanen2012")], "89% get one weekly", "Big 89% label with notes.", "think/neutral/L; text:89%@R; notes@TR"),
  ("E", [("A 2016 study compared tunes that people named as earworms with other songs.", "jakubowski2016")], "2016: earworm tunes vs others", "Two song lists side by side.", "point/neutral/L; list:EARWORMS,OTHERS@R"),
  ("E", [("Earworm tunes tended to have faster tempos.", "jakubowski2016")], "Faster tempos", "Metronome ticking fast.", "stand/smile/L; clock@R; notes@TR"),
  ("E", [("They also followed common melodic shapes, with unusual steps between turning points.", "jakubowski2016")], "Common shapes, odd steps", "A melody line with a few odd jumps.", "think/neutral/L; lines:shape,steps@R"),
  ("E", [("In 2015, Beaman and colleagues had 98 people try not to think about two pop songs for three minutes.", "beaman2015")], "2015: 98 people, 3 minutes", "Stopwatch at three minutes.", "stand/neutral/L; clock@R; text:98 PEOPLE@TR"),
  ("E", [("People chewing gum reported hearing the songs less often than people who did nothing or tapped their fingers.", "beaman2015")], "Gum reduced earworms", "Bars: gum low, nothing high, tapping high.", "stand/smile/L; bars:gum,tapping@R"),
  ("E", [("The authors suggest gum interferes with the motor planning behind imagining the song.", "beaman2015")], "Gum blocks 'inner singing'", "Mouth and note with a blocked arrow.", "point/neutral/L; notes@R; cross@TR"),
  ("T", [("So chewing gum might help next time, though this was a small lab experiment.", "beaman2015")], "Gum might help (small study)", "Stickman chewing gum, notes shrinking.", "stand/smile/L; text:GUM@R; notes@TR"),
  ("C", [("Tomorrow: why do stores show you a number before the price?", "PLAN")], "Tomorrow: the first number", "Big crossed-out price tag.", "stand/smile/L; tag:$200@R; text:TOMORROW@TR"),
 ])

DAYS[9] = dict(
 title="The Pricing Trick Stores Use on You",
 description_core="Why do stores show a big number first? In a classic experiment, a random number changed people's estimates, a result known as anchoring.",
 primary=["tversky1974", "galinsky2001"],
 hashtags=["#psychology", "#shorts", "#anchoring", "#marketing", "#negotiation", "#psychologyfacts"],
 caveats="Figures are medians from the original wheel-of-fortune experiment (25 and 45). Anchoring is a robust finding, but effect size varies by task. Galinsky & Mussweiler studied simulated negotiations. The video does not claim that stores' 'original prices' work exactly this way; it presents the lab result and the negotiation research.",
 thumb=(["STORES SHOW", "THIS FIRST"], 1, 1),
 scenes=[
  ("H", [("Why do stores show you a big number first?", "PLAN")], "The number they show first", "Big price tag looming over a small stickman.", "stand/worry/L; tag:$200@R"),
  ("E", [("In 1974, Tversky and Kahneman had volunteers watch a wheel spin to a random number.", "tversky1974")], "Tversky & Kahneman, 1974", "Wheel of fortune stopping on 10, then 65.", "point/neutral/L; wheel:10@R"),
  ("E", [("Then they asked what percentage of African countries are in the United Nations.", "tversky1974")], "Then a question", "Question mark above a globe.", "think/neutral/L; qmark@R; text:% IN THE UN?@TR"),
  ("E", [("People who saw the number 10 guessed about 25 percent.", "tversky1974")], "Saw 10: guessed ~25%", "Bar at 25%.", "stand/neutral/L; bars:saw 10=25%,saw 65=45%@R"),
  ("E", [("People who saw 65 guessed about 45 percent.", "tversky1974")], "Saw 65: guessed ~45%", "Bar at 45%.", "point/neutral/L; bars:saw 10=25%,saw 65=45%@R"),
  ("E", [("A random, irrelevant number pulled their estimates toward it.", "tversky1974")], "A random number pulled answers", "Rope pulling a thought bubble toward a number.", "shock/neutral/L; text:ANCHOR@R"),
  ("E", [("This is called anchoring.", "tversky1974")], "Anchoring", "Anchor drawn in the accent color.", "stand/smile/L; text:ANCHORING@R"),
  ("E", [("Anchors matter in negotiations too.", "galinsky2001")], "Negotiations too", "Two stickmen across a table.", "stand/neutral/L; crowd:1@R"),
  ("E", [("In three experiments, whoever made the first offer got a better outcome.", "galinsky2001")], "First offer wins", "Flag planted on a number line.", "walk/smile/L; arrow:right@R"),
  ("E", [("But when the other side thought about their own alternatives, the first-offer advantage disappeared.", "galinsky2001")], "Unless they think of alternatives", "Alternatives list cancelling the anchor.", "think/smile/L; list:ALT 1,ALT 2@R; cross@TR"),
  ("T", [("So when someone makes the first offer, think about your own target and their alternatives before you answer.", "galinsky2001")], "Think target + alternatives", "Stickman with a target and two options.", "point/smile/L; text:MY TARGET@R"),
  ("C", [("Tomorrow: why do you forget why you walked into a room?", "PLAN")], "Tomorrow: doorways", "Doorway with a fading thought bubble.", "stand/neutral/L; door@R; text:TOMORROW@TR"),
 ])

DAYS[10] = dict(
 title="Why You Forget Things Walking Into a Room",
 description_core="Does walking through a doorway really make you forget? A 2011 study found people forgot more after passing through a door, but a 2021 set of experiments mostly did not find a clean effect.",
 primary=["radvansky2011", "mcfadyen2021"],
 hashtags=["#psychology", "#shorts", "#memory", "#doorwayeffect", "#brain", "#psychologyfacts"],
 caveats="CONTESTED / MIXED. Radvansky et al. (2011) found the effect in real and virtual rooms; McFadyen et al. (2021) found no significant overall effect across four experiments, only increased memory errors under a working-memory load. No 'fix' is claimed, because later research found the effect even after returning to the original room (not claimed here for lack of a single verified primary source).",
 thumb=(["WHY DID I", "COME IN", "HERE?"], 2, 0),
 scenes=[
  ("H", [("Why do you forget why you walked into this room?", "PLAN")], "Why did I come in here?", "Stickman confused in a doorway.", "shrug/worry/C; door@R"),
  ("E", [("In 2011, Gabriel Radvansky's team studied students moving through real and virtual rooms.", "radvansky2011")], "Radvansky, 2011", "Virtual room with a box being carried.", "walk/neutral/L; text:2011@TR; door@R"),
  ("E", [("People forgot more after walking through a doorway than after walking the same distance within one room.", "radvansky2011")], "More forgetting after doors", "Bars: room low, door high.", "stand/neutral/L; bars:room,door@R"),
  ("E", [("The researchers proposed that a doorway creates a new memory episode, an event boundary, making the old information harder to retrieve.", "radvansky2011")], "Doors = event boundaries", "Thought bubble packed into a box as the stickman steps through.", "think/neutral/L; door@R; bubble:old thought@TR"),
  ("E", [("But in 2021, Jessica McFadyen and colleagues ran four experiments across virtual reality, video and real-life movement.", "mcfadyen2021")], "2021: four experiments", "Four panels: VR, VR+load, video, real.", "stand/neutral/L; list:VR,VR+LOAD,VIDEO,REAL@R"),
  ("E", [("They found no significant effect of doorways on forgetting.", "mcfadyen2021")], "No significant effect", "Check replaced by cross.", "shrug/neutral/L; cross@R"),
  ("E", [("Only when people had to hold information in mind did doorways increase certain memory errors.", "mcfadyen2021")], "Only under mental load", "Brain carrying heavy load near a door.", "think/worry/L; brain:@R; door@TR"),
  ("E", [("So the doorway effect looks real in some conditions, but not guaranteed.", "radvansky2011,mcfadyen2021")], "Real in some conditions", "Scale tipping slightly.", "shrug/smile/L; scale@R"),
  ("T", [("So if you blank in a doorway, it's a documented memory quirk studied in healthy students.", "radvansky2011")], "A documented memory quirk", "Smiling stickman with a healthy brain icon.", "stand/smile/L; brain:@R"),
  ("C", [("Tomorrow: why does something you just learned seem to appear everywhere?", "PLAN")], "Tomorrow: it's everywhere", "Many identical objects behind the stickman.", "stand/shock/L; crowd:5@R; text:TOMORROW@TR"),
 ])
