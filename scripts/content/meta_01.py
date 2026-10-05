"""Publishing metadata for Days 1-10: titles, descriptions, hashtags, thumbnail specs.
THUMBS[day] = (headline lines, index of the accent-colored line, scene index whose drawing is reused)."""

CTA = "New psychology short every day on The Psyche Discourse."
CH = "#thepsychediscourse"

META = {
 1: dict(title="Why That Cringe Memory Never Leaves You",
   description="Why does an embarrassing moment replay in your head for years? Emotional arousal tells your brain to store an event more strongly, and replaying it locks it in even deeper. " + CTA + " Source: McGaugh (2004), 'The amygdala modulates the consolidation of memories of emotionally arousing experiences', Annual Review of Neuroscience.",
   hashtags=["#psychology", "#shorts", "#memory", "#brain", "#psychologyfacts", "#cognitivebias", CH]),
 2: dict(title="Nobody's Watching You As Much As You Think",
   description="Think everyone noticed your slip-up? In a classic study, people wearing an embarrassing T-shirt guessed about twice as many observers would notice it as actually did. " + CTA + " Source: Gilovich, Medvec & Savitsky (2000), 'The spotlight effect in social judgment', Journal of Personality and Social Psychology.",
   hashtags=["#psychology", "#shorts", "#spotlighteffect", "#socialanxiety", "#confidence", "#psychologyfacts", CH]),
 3: dict(title="The One-Cent Trick Behind Every $9.99",
   description="Why does $9.99 feel so much cheaper than $10? Your brain anchors on the leftmost digit, so a one-cent change can feel like a much bigger drop. " + CTA + " Source: Thomas & Morwitz (2005), 'Penny wise and pound foolish: the left-digit effect in price cognition', Journal of Consumer Research.",
   hashtags=["#psychology", "#shorts", "#pricing", "#marketing", "#shopping", "#psychologyfacts", CH]),
 4: dict(title="Your Brain Hides Evidence You Disagree With",
   description="Your brain naturally seeks out information that agrees with what you already believe. Peter Wason's classic 2-4-6 task shows how people test ideas in ways that can only confirm them. " + CTA + " Source: Wason (1960), 'On the failure to eliminate hypotheses in a conceptual task', Quarterly Journal of Experimental Psychology.",
   hashtags=["#psychology", "#shorts", "#confirmationbias", "#cognitivebias", "#criticalthinking", "#psychologyfacts", CH]),
 5: dict(title="Why Unfinished Tasks Haunt Your Brain",
   description="Unfinished tasks can nag at your mind, but the details of the Zeigarnik effect are more nuanced than the popular story. Making a specific plan can quiet that mental nagging. " + CTA + " Source: Masicampo & Baumeister (2011), 'Consider it done! Plan making can eliminate the cognitive effects of unfulfilled goals', Journal of Personality and Social Psychology.",
   hashtags=["#psychology", "#shorts", "#zeigarnik", "#productivity", "#procrastination", "#psychologyfacts", CH]),
 6: dict(title="Why Losing Hurts More Than Winning Feels Good",
   description="Losses tend to feel bigger than equal gains, an idea called loss aversion. Researchers still debate how strong and universal it really is. " + CTA + " Source: Kahneman & Tversky (1979), 'Prospect theory: an analysis of decision under risk', Econometrica.",
   hashtags=["#psychology", "#shorts", "#lossaversion", "#behavioraleconomics", "#decisionmaking", "#psychologyfacts", CH]),
 7: dict(title="Dunning-Kruger: What Everyone Gets Wrong",
   description="Do unskilled people really think they're geniuses? Not quite: Dunning and Kruger found that low performers overestimated their ability on specific tasks, but the popular version of the story is oversimplified. " + CTA + " Source: Kruger & Dunning (1999), 'Unskilled and unaware of it', Journal of Personality and Social Psychology.",
   hashtags=["#psychology", "#shorts", "#dunningkruger", "#cognitivebias", "#selfawareness", "#psychologyfacts", CH]),
 8: dict(title="Why That Song Won't Leave Your Head",
   description="Earworms often follow recent listening, stress, or a memory cue, and tend to have simple, easy-to-sing melodies. A small experiment found that chewing gum can reduce them. " + CTA + " Source: Beaman, Powell & Rapley (2015), 'Want to block earworms from conscious awareness? B(u)y gum!', Quarterly Journal of Experimental Psychology.",
   hashtags=["#psychology", "#shorts", "#earworm", "#music", "#brain", "#psychologyfacts", CH]),
 9: dict(title="The Pricing Trick Stores Use on You",
   description="The first number you see quietly shapes your later judgments, which is why stores show a high original price next to the sale price. This is called anchoring. " + CTA + " Source: Tversky & Kahneman (1974), 'Judgment under uncertainty: heuristics and biases', Science.",
   hashtags=["#psychology", "#shorts", "#anchoring", "#marketing", "#negotiation", "#psychologyfacts", CH]),
 10: dict(title="Why You Forget Things Walking Into a Room",
   description="Walking through a doorway can make you forget why you entered the room. Researchers think doorways mark 'event boundaries' that make your brain file the old thought away. " + CTA + " Source: Radvansky, Krawietz & Tamplin (2011), 'Walking through doorways causes forgetting', Quarterly Journal of Experimental Psychology.",
   hashtags=["#psychology", "#shorts", "#memory", "#doorwayeffect", "#brain", "#psychologyfacts", CH]),
}

THUMBS = {
 1: (["WHY YOU", "REMEMBER", "CRINGE"], 2, 0),
 2: (["NOBODY'S", "WATCHING", "YOU"], 0, 0),
 3: (["THE $9.99", "TRICK"], 0, 0),
 4: (["YOUR BRAIN", "HIDES FACTS"], 1, 4),
 5: (["UNFINISHED", "TASKS", "HAUNT YOU"], 0, 0),
 6: (["LOSING", "HURTS MORE"], 0, 0),
 7: (["DUNNING-KRUGER", "MISUNDERSTOOD"], 1, 0),
 8: (["WHY IS THAT", "SONG STUCK?"], 1, 0),
 9: (["STORES SHOW", "THIS FIRST"], 1, 1),
 10: (["WHY DID I", "COME IN", "HERE?"], 2, 0),
}
