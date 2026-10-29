# THE FIRST 90 DAYS — Scenario 21: “The Relapse Report”

*Human-readable script. This document and `scenario-21.json` are generated from a single source and match node-for-node: same IDs, same order, same choices, same effects.*

**The family is fictional — a composite. No real person's story appears here.**

**Content note:** This scenario depicts a reported positive drug screen at month eight of a dependency case, safety planning, a possible emergency removal, and a shelter care hearing — told through procedure and paperwork. There is no graphic content. Players may skip any scene or use the quick exit at any time.

**How to read effects:** `cash −40` changes the player's cash. `FLAG: name` sets a flag the engine tracks. `HIDDEN + item` means the case file quietly records that item at this choice — the player does not see it when it happens. `NOTE:` is text shown to the player right after choosing.

Start date: Monday, November 2, 2026 (month eight of the case; the child has had expanded trial-home time for six weeks). Day offsets are days since the scenario's start date. The 48-hour documentation window ends Wednesday, November 4, 2026.

## [start] The Monday Call
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

Eight months into this case, the shape of your life had finally changed. Sam, seven years old, has been home full-time for six weeks on expanded trial-home time: sleeping in his own bed, going to school from your kitchen table in the morning, with the agency's supervision continuing around that arrangement — scheduled caseworker visits, screens through your treatment program, and a review hearing coming in December that will look at how the home time has gone.

The months behind that arrangement were clean ones, and they are in the file: screens attended, treatment sessions kept, a sponsor named Rae who knows Sam's bedtime routine because she has sat through it.

At 9:12 this morning your caseworker, Ms. Bell, calls with a result instead of a question. A screen you gave on Friday has been reported back positive. She does not raise her voice and she does not use the word emergency. She says two things, in this order: she has to talk with you today about immediate safety planning for Sam, and what happens in the next two days will be part of the record the court reads. The 48-hour window she is describing ends Wednesday, November 4. It starts now.

**Choices:**
- Call your treatment program first, then Rae — before you call anyone else, before you rehearse anything → **first_calls**  _(HIDDEN + Treatment contact — parent reported the result to the program the same morning it reached her)_
  - NOTE (shown after choosing): The two people whose job is your recovery hear it from you, first, today. In files, that order matters, because it usually is the truth about priorities.
- Take an hour. Shower, breathe, decide what this means before you talk to anyone → **delay**
  - NOTE (shown after choosing): An hour feels like care. On a clock that ends Wednesday, an hour is also a document: it will be the first blank space in the record of these two days.

## [first_calls] Two Calls, Made
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

The program's intake line keeps you on hold for eleven minutes, which you spend pacing with the phone on speaker so your hands can make tea neither of you will drink. When a counselor comes on, you say the sentence exactly once, without decorating it: a screen has been reported positive, and you are calling the morning you heard.

The program offers what programs can offer on a Monday: an assessment appointment tomorrow, Tuesday, at 9 a.m., and a note in your treatment file that you self-reported before anyone asked. Rae answers on the second ring. She does not do shock and she does not do comfort that requires lying. She says: “Assessment tomorrow. I'm coming over tonight. Who else is on the list?”

The list, when you say it aloud, has a third name on it: your sister Lou, twenty minutes away, who has kept Sam overnight a dozen times this fall and is listed in your case paperwork as a family support.

**Choices:**
- Call Lou now, while Rae is still on the line — ask if she can be part of a safety plan starting tonight → **kin_call**
  - NOTE (shown after choosing): Support stops being a description and starts being a schedule: a named person, a phone that answered, a night she can cover.
- Keep this between you and the program for now — Lou has enough on her plate this month → **solo_plan**
  - NOTE (shown after choosing): Privacy feels like loyalty. It also means that when the agency asks who can be with Sam tonight, the honest answer will be: no one they can call.

## [delay] The Quiet Hour
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

The hour does what hours do. The tea goes cold. Sam's school shoes sit by the door where he left them Friday, and the apartment is very clean, because cleaning is the thing your hands know how to do when your mind will not sit down.

At 11:40 the phone lights up with a text from Ms. Bell: she will need to see you and Sam today, and she is asking — her word — whether treatment has been in touch yet. It is not a trick question. It is worse than that. It is a question with a true answer that gets less true-feeling the longer it sits unanswered.

Nothing has been decided. That is precisely the problem the text is describing.

**Choices:**
- Call the program now — late is a fact, but it is a smaller fact than never → **late_calls**
  - NOTE (shown after choosing): 11:47 a.m. The call log will show the gap and the recovery in the same line. Files contain both; people who work in this system know how to read both.
- Reply that you're handling it, and put the phone face-down until her visit → **visit_unprepared**
  - NOTE (shown after choosing): “Handling it” is not a plan anyone can verify. By evening, the only version of today in the file will be the one other people wrote.

## [kin_call] Lou Answers
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

Lou answers the way she has answered since you were both children: mid-task, slightly out of breath, already solving. She can take Sam at her house tonight and tomorrow night, or sleep on your couch — her words — “whichever makes the paperwork happier.” She can do school pickup Tuesday and Wednesday. She says it plainly enough that you write it down word for word, with the time of the call beside it.

Rae will be at your kitchen table by six. The assessment is tomorrow at nine. For the first time since 9:12 this morning, the next forty-eight hours have names and times attached to them instead of weather.

Ms. Bell calls back at two, as she said she would. This is the conversation the whole day has been walking toward.

**Choices:**
- Tell her exactly what is arranged — assessment Tuesday at nine, Rae tonight, Lou available for overnights starting tonight, all of it with names and times → **caseworker_strong**  _(HIDDEN + Safety supports — sister confirmed by phone for overnights and school pickup, named and timed)_
  - NOTE (shown after choosing): She repeats it back while she writes. A plan she can repeat is a plan that exists outside your kitchen.
- Tell her family is rallying and you'll sort the details out tonight → **caseworker_vague**
  - NOTE (shown after choosing): True, and unusable. She cannot write “rallying” in a safety plan, and both of you can hear that as you say it.

## [solo_plan] A List of One
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

By early afternoon the apartment contains a complete plan with a staff of one. You will go to the assessment. You will not miss a screen. You will be fine, because you have been fine for months, and the months should count for something.

They do count — they are counted, in the file, in exactly the same ink as everything else. But a safety plan is not an argument about the past. It is an answer to a specific question — who is with this child, and who else can be, tonight and tomorrow night — and a staff of one is the answer that fails the night you get sick, or stuck, or overwhelmed at exactly the wrong hour.

Ms. Bell calls back at two, as she said she would.

**Choices:**
- While she is still ringing, text Lou: “I need you on the plan. Call me now.” → **kin_call**
  - NOTE (shown after choosing): Lou calls back in four minutes, slightly out of breath, already solving. The list has a second name while there is still daylight to use it.
- Answer, and give her the plan as it stands: you, the assessment, and your word → **visit_unprepared**
  - NOTE (shown after choosing): She listens to all of it without interrupting, which experienced parents have learned is not the same thing as agreement.

## [late_calls] Late, But Dialed
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

The program's afternoon counselor is brisker than the morning one and just as unshocked. Tuesday at nine is still open — assessments, it turns out, are offered to people who call at noon, too. She notes the time of your call in the file without commentary, which you decide to take as a professional courtesy and a warning in the same gesture.

Rae's phone goes to voicemail. Lou's does not. Between the two of them, by one o'clock, tomorrow has an assessment in it and tonight has a possible second adult — if you finish the job of asking properly.

**Choices:**
- Leave Rae a full voicemail — the result, the assessment time, tonight's need — then confirm Lou's nights out loud and write them down → **kin_call**
  - NOTE (shown after choosing): A voicemail with facts in it is a document. Rae calls back inside the hour, and the plan closes like a zipper.
- Leave your name and “call me” — you'll explain everything in person tonight → **visit_unprepared**
  - NOTE (shown after choosing): In person never quite arrives on schedule. What arrives, at five, is Ms. Bell, with a notebook and no confirmed names in it.

## [caseworker_strong] A Plan She Can Repeat
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

Ms. Bell does something you did not expect: she builds with what you hand her instead of starting over. The arrangement that comes out of the call has a name she uses twice — a voluntary kin safety arrangement — and a shape simple enough to fit on one page.

Tonight and tomorrow night, Sam sleeps at Lou's, ten minutes away, with his school clothes and his library book in his own backpack. You attend the assessment Tuesday at nine and whatever the program recommends after it. Rae is at your table tonight and checks in daily. Ms. Bell will visit Lou's house this evening, visit you Wednesday, and write the arrangement down for both households to sign. No court filing starts today. She is also plain about the other side of the page: the arrangement exists because the supports are confirmed, and it holds only while they do.

The page is not a verdict on the screen. It is a supervision answer to it.

**Choices:**
- Agree, and ask her to put the whole arrangement in writing tonight — you'll sign at Lou's → **voluntary**  _(HIDDEN + Voluntary kin safety arrangement — agreed on day one, in writing, before any court filing)_
  - NOTE (shown after choosing): A signature turns a good phone call into a plan another worker, or a judge, can find later without you in the room.
- Ask for the night to think it over — sending Sam to Lou's feels like admitting something → **visit_unprepared**
  - NOTE (shown after choosing): She says she understands, and that she still has to see Sam this evening either way. Thinking time and safety time run on different clocks tonight.

## [caseworker_vague] “Rallying” Is Not a Schedule
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

There is a pause on the line that you have learned to recognize across eight months: the sound of a caseworker deciding how much of the machinery to describe to you.

“I believe you,” she says, and you can hear that she does. “But I can't write belief in a safety plan. I need a person, a place, and nights. If your sister can be those, I need to hear it from her, today, and I need to see Sam. I'll come at five. If she's there, we have something to build with. If it's just us, we have a much shorter list of options, and I don't want that list and neither do you.”

It is the most useful threat you have ever received, because it is not one. It is directions.

**Choices:**
- Call Lou the second you hang up and ask her to be at your door at five with her answer ready → **caseworker_strong**
  - NOTE (shown after choosing): She is there at 4:40 with a casserole and a yes. Ms. Bell arrives to find the plan's hardest part — a second adult — already standing in the kitchen.
- Let five o'clock come as it comes — Lou works late, and you won't beg → **visit_unprepared**
  - NOTE (shown after choosing): Pride, in this file, will be recorded as an empty chair. The record does not have a column for why the chair was empty.

## [visit_unprepared] Five O'Clock, Unprepared
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

Ms. Bell arrives at five with a colleague, which tells you before anyone speaks that this visit has more than one possible ending. Sam is at the kitchen table with homework and the particular alertness of a child who can read weather in adults.

She asks her questions kindly and in order: Has treatment been contacted? Is there an assessment? Who can be with Sam tonight, and tomorrow night, that the agency can speak to? The answers, in order, are the ones the day has produced. She writes them down without enjoying it. A plan with no second adult, no assessment, and no confirmed support is not a plan she can leave a seven-year-old inside tonight — and she tells you, in so many words, that the decision she has to make in this room is about tonight's supervision, not about the last eight months and not about your worth.

The room is very quiet. There is still one door open in it, and it is the size of a phone call.

**Choices:**
- Make the calls here, now, on speaker at this table — Lou first, then the program's evening line → **evening_rescue**
  - NOTE (shown after choosing): It is not graceful and it is not early. It is, however, in the room, in front of witnesses, before the decision is made instead of after.
- Tell her no one is rearranging their life on one day's notice over one result — she can write what she wants → **removal_night**  _(FLAG: removed)_
  - NOTE (shown after choosing): She writes, in fact, exactly what happened: a safety plan was needed tonight, none could be confirmed, and the parent declined to contact the supports in her own file. The sentence will be read aloud in rooms you are not in.

## [evening_rescue] The Speakerphone Rescue
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

Lou, on speaker, slightly out of breath, already solving: yes, tonight; yes, tomorrow night; yes, she can be here in twenty minutes and yes, Ms. Bell can visit her house after. The program's evening line confirms a Tuesday nine o'clock assessment in a tone that suggests people arrange their recoveries at kitchen tables under supervision more often than you would think.

Ms. Bell closes her notebook on a different page than the one she opened. The voluntary kin safety arrangement will be the same one she described this afternoon — written at Lou's tonight, signed by both households, built entirely out of a phone call you almost didn't make in front of her.

Sam, who has been listening the way children listen, asks if Lou's house means the good cereal. It does. It always did.

**Choices:**
- Go with Sam to Lou's, sign the arrangement there, and be at the assessment at nine tomorrow → **voluntary**
  - NOTE (shown after choosing): Rescued is not the same as ready — but tonight, the paper says what the evening actually was: late, witnessed, and real.

## [voluntary] Signed at Lou's Table
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

The arrangement is one page, and you read all of it before you sign, because eight months have taught you to read pages before signing them. Sam sleeps at Lou's Monday and Tuesday nights. You attend Tuesday's assessment and follow its recommendations. Rae has a key to your apartment and a daily check-in time. Ms. Bell visits both houses Wednesday — the day the 48-hour window closes — and the arrangement is reviewed then, with the assessment paperwork in hand.

There is no court date in it. There is also no promise in it beyond Wednesday, and Ms. Bell does not pretend otherwise when you ask. What it is, is a bridge built out of confirmed people, with a review standing on the far side of it.

Sam inspects Lou's guest room, approves the cereal situation, and falls asleep faster than either adult expected. Bridges, it turns out, are easier to cross at seven.

**Choices:**
- Sleep at home, set two alarms, and go to the assessment the way you go to everything that matters: early → **assessment_day**
  - NOTE (shown after choosing): Tomorrow the question changes. It stops being “is there a plan for tonight” and becomes “what does the record of the next two days show.”

## [assessment_day] Tuesday, Nine O'Clock
*Day 1 — Tuesday, November 3, 2026 — Tuesday, November 3, 2026 (dayOffset 1)*

The assessment takes ninety minutes and covers the ground assessments cover: the months of clean screens, Friday's result, sleep, stress, the week your hours at work were cut, what support actually surrounds you on an ordinary Tuesday rather than a good one. The counselor is neither a judge nor a friend. She is a person building a treatment document, and she tells you its shape before she builds it.

Her recommendation, written while you watch: step up, don't start over. Additional sessions each week for the next stretch, group twice a week, screens on the program's schedule including a follow-up this week, daily contact with Rae, and a written relapse-response note in your treatment plan that names Lou's role. Nothing in it is a punishment. All of it is more paper, of the kind that has carried you for eight months.

On your way out she mentions, because you are standing near the results binder, that Friday's screen report came to the program as a lab report — a page with collection and reporting details on it, not just a word in a phone call.

**Choices:**
- Ask the process questions now, and write the answers down: who collected the sample, when it was reported, what paperwork accompanies the result, and how a person sees that page → **lab_questions**  _(cash −14; HIDDEN + Assessment — attended Tuesday, recommendations accepted: stepped-up sessions, group, scheduled screens, daily sponsor contact)_
  - NOTE (shown after choosing): Questions about process are not accusations. Asked today, in this room, they become part of how the file describes you: a parent checking the paperwork, not fighting it.
- Sign the updated plan, thank her, and get to work — the paperwork about the result can keep → **records_request**  _(cash −14; HIDDEN + Assessment — attended Tuesday, stepped-up treatment plan signed)_
  - NOTE (shown after choosing): The plan is signed and real. The page behind Friday's result stays a page you have never seen, described to you secondhand.

## [lab_questions] Questions About a Page
*Day 1 — Tuesday, November 3, 2026 — Tuesday, November 3, 2026 (dayOffset 1)*

The counselor answers the way careful people answer: some of it she knows, some of it is the lab's, and all of it she will put in the treatment note. The sample was collected Friday at the program, logged with a date and time, and reported Monday as a written lab report, which is why Ms. Bell's call said “reported” so precisely. The report page itself sits in the case record, she says — the agency's file, not the program's binder — and questions about how it was produced belong in writing, to the people who hold that file.

She is careful about one more thing, and you are grateful for the care even as it disappoints you: she cannot order anything redone, promise what any reviewer will make of the page, or tell you the result means more or less than it says. What she can do — and does, before you leave — is note in your treatment record that you asked, what you asked, and that you accepted the stepped-up plan in the same visit.

You write the date, the time, and her name at the top of your notebook page. Eight months in, your handwriting for this kind of page has gotten very neat.

**Choices:**
- Go home and build Wednesday's folder: the assessment note, Rae's check-in times, Lou's nights — and one written request still to send → **records_request**
  - NOTE (shown after choosing): A folder is an argument about the future: everything in it says what will happen next, with names on it.

## [records_request] Wednesday Morning, in Writing
*Day 2 — Wednesday, November 4, 2026 — Wednesday, November 4, 2026 (dayOffset 2)*

Wednesday, November 4 — the day the 48-hour window closes. Your counsel's advice from the last review, which you wrote on the folder in marker, was: anything you need from the file, ask for in writing, and keep the copy.

There is a regulation for exactly this. A party to the case may ask for the case record, and under 55 Pa. Code § 3130.44(d) it “shall be released upon request.” Your written request, dated today, asks for the record material around Friday's result: the screen report itself and the related case notes from these two days — the assessment note, the safety arrangement, the visit notes — so that what you, your counsel, and eventually the court are reading from is the same page.

The request does not argue with the result. It does something quieter and, in this system, rarer: it insists that the result travel with its paperwork and with everything that happened after it.

**Choices:**
- Send the written request today, keep your stamped copy in the folder, and text Ms. Bell that it is sent → **supervision_plan**  _(cash −6; FLAG: recordsRequested; HIDDEN + Case record — written request sent Wednesday for the screen report and related case notes (55 Pa. Code § 3130.44(d)))_
  - NOTE (shown after choosing): Requested, dated, copied. The screen report will arrive — whenever it arrives — into a file that already contains your response to it.
- Hold the request — you'll ask for the record verbally at the December review instead → **supervision_plan**  _(cash −0)_
  - NOTE (shown after choosing): Verbal asks live in other people's notes. December is a long way for a page to travel on memory alone.

## [supervision_plan] The Plan, With Names On It
*Day 2 — Wednesday, November 4, 2026 — Wednesday, November 4, 2026 (dayOffset 2)*

The last piece of Wednesday's folder is the one Ms. Bell will ask about at today's visit: the supervision plan for the days ahead, while the stepped-up treatment runs. Not the crisis version from Monday — the ordinary-days version. Who is with Sam after school. Who covers the evenings you are at group. What happens on the night a session runs long, or a shift changes, or you are simply having the kind of day that used to be dangerous.

Plans like this fail in a specific way: not in the intentions, which are always good, but in the unnamed hours. The folder is open. Lou's number is in your phone. Rae's check-in time is already set.

**Choices:**
- Write it with names, nights, and a backup for the backup — Lou after school, Rae's daily check-in, Lou's couch as the standing fallback — and have Lou confirm it by text today → **wed_visit**  _(HIDDEN + Supervision plan — written, named cover for after-school and treatment evenings, kin confirmed same day)_
  - NOTE (shown after choosing): Confirmed means a second phone, answered. When Ms. Bell calls Lou this afternoon, she will hear the plan from its other author.
- Write it in general terms — “family support as needed” — so there's flexibility if the week changes → **wed_visit**
  - NOTE (shown after choosing): Flexibility reads, on paper, exactly like its opposite. The plan goes into the folder with no name a caseworker can call to check it.

## [wed_visit] Wednesday, Both Houses
*Day 2 — Wednesday, November 4, 2026 — Wednesday, November 4, 2026 (dayOffset 2)*

Ms. Bell visits Lou's first, then yours, with the folder's contents effectively walking beside her: the signed safety arrangement, the assessment note with its stepped-up plan, your record request with its stamped copy, the supervision plan. Sam is at Lou's kitchen table doing homework with the concentration of a child whose week has been unusual but not frightening, which — though no form has a box for it — everyone in both kitchens can see is the point of the whole exercise.

She is plain about what she is writing: the reported result stands in the record as reported. Beside it now stand two days of documented response — treatment contacted the same morning, assessment attended, supports confirmed by name, a plan with a backup. The December review will read both. The trial-home arrangement continues while the stepped-up treatment runs, with visits on the schedule she hands you.

“This,” she says, tapping the folder once, “is what a response looks like when it's written down.”

**Choices:**
- Ask what the program needs from you this week, and put the follow-up screen on the calendar before she leaves → **followup_week**
  - NOTE (shown after choosing): The window is closed. The record it produced is not. It is, starting now, the thing the rest of the case will be read through.

## [followup_week] The Follow-Up Screen
*Day 8 — Tuesday, November 10, 2026 — Tuesday, November 10, 2026 (dayOffset 8)*

Tuesday again, a week later, at the program's window — not because anyone ordered this exact visit in a courtroom, but because the stepped-up plan you signed put screens on a schedule and schedules are kept or they are nothing.

You attend. Rae's check-ins have happened daily; the log of them is unglamorous and complete. Group met twice. Lou covered Thursday's long session and wrote her initials on the supervision plan's margin the way people sign for packages. The follow-up screen is collected, logged with its date and time, and sent wherever such pages go. Whatever it reports when it comes back, this much is already true and already written: it was attended, on schedule, inside a plan other people can confirm.

Eight months of this case have taught you the difference between a result and a record. A result is a line. A record is a line with a life around it.

**Choices:**
- Keep the folder current — every attendance, every check-in, every page — and take it to counsel before December → **december_review**  _(cash −14; HIDDEN + Follow-up screen — attended on schedule under the stepped-up plan; attendance documented)_
  - NOTE (shown after choosing): Paper kept weekly is a habit. Paper assembled the night before a hearing is a hope. The folder has become the first kind.

## [december_review] The December Review
*Day 30 — Wednesday, December 2, 2026 — Wednesday, December 2, 2026 (dayOffset 30)*

The review hearing is smaller than its reputation. Your counsel — provided under 42 Pa.C.S. § 6337, and in possession of the folder because you sent the record request in November and shared what came back — does not argue that Friday's result never happened. She argues from the whole record: eight months of progress, one reported positive screen at month eight, and a documented forty-eight hours that answered it, followed by weeks of a stepped-up plan actually being lived.

Ms. Bell's report says what her Wednesday note said, longer. The treatment provider's letter confirms the assessment, the attendance, the screens on schedule. Lou is in the gallery, because confirmed supports turn out to be people, and people can be in rooms.

The judge reads the folder the way judges read: the result first, because it is flagged, and then everything that was built around it, because it is there.

**Choices:**
- Listen for the order with Sam's backpack already packed for home either way — and hear it whole → **end_home**
  - NOTE (shown after choosing): Whatever it says, it will say it about a record, not a rumor. You made sure of the difference in November.

## [removal_night] The Emergency Decision
*Day 0 — Monday, November 2, 2026 — Monday, November 2, 2026 (dayOffset 0)*

It happens the way these things happen in the published cases and in life: not with shouting, but with forms. Ms. Bell makes a call from your kitchen. Her colleague makes another from the doorway. Sam is told, in the practised language of kind professionals, that he will sleep at a new house tonight — an emergency placement, because Lou could not be reached through the agency's process in time to be the plan tonight, and no confirmed plan existed when the decision had to be made.

At the door, Ms. Bell hands you a paper with the information the law makes sure you have: there will be a shelter care hearing, and it will be held within 72 hours — for a child taken into custody on Monday, November 2, that hearing falls on Thursday, November 5, 2026 (42 Pa.C.S. § 6332; 23 Pa.C.S. § 6315(d)). You are also told about counsel: under 42 Pa.C.S. § 6337, you have the right to be represented, and counsel will be provided if you cannot afford one.

Then the apartment is quiet in the particular way it will be quiet for days. On the table, the notebook from today is open to a page with almost nothing on it. Thursday is three days away. What those three days contain on paper is now the entire case.

**Choices:**
- Sit down tonight, while it is worst, and write down the names: Rae, Lou, the program's number, counsel's number from the paper → **morning_after**
  - NOTE (shown after choosing): Grief and paperwork are not enemies. Tonight, each is the only company the other has.

## [morning_after] Tuesday Morning, After
*Day 1 — Tuesday, November 3, 2026 — Tuesday, November 3, 2026 (dayOffset 1)*

Tuesday arrives with the flat light of a day after. The assessment the program offered yesterday is, you learn when you call, still bookable today. Rae answers on the first ring and her voice does something complicated when she hears where Sam slept.

Two clocks are now running where yesterday there was one. The shelter care hearing is Thursday — inside the 72-hour window the statutes set. And the forty-eight-hour documentation window Ms. Bell described on Monday closes Wednesday. Everything you do today and tomorrow either enters the record the court will read on Thursday, or doesn't.

Counsel's number is on the paper from last night. The program's number is in your phone. The order in which you use them is, itself, a fact about you that will be visible later.

**Choices:**
- Call counsel first, then the program — and do exactly the unglamorous list both of them give you → **counsel_call**
  - NOTE (shown after choosing): Two phone calls before ten o'clock. In the record of this week, they will be the first two entries that point forward.
- Wait for Thursday — the hearing is where you'll explain, in person, what one result doesn't prove → **wait_hearing**
  - NOTE (shown after choosing): Explanation is a real thing, and you are good at it. It is also the only thing you are currently scheduled to bring to a hearing that runs on documents.

## [counsel_call] Counsel, and a List
*Day 1 — Tuesday, November 3, 2026 — Tuesday, November 3, 2026 (dayOffset 1)*

Your counsel — the lawyer provided under 42 Pa.C.S. § 6337 after last night's paper — has a voice like a person who makes lists for a living. Hers has four items, and she reads them in order of the clock, not of importance.

One: attend the assessment today, and accept what it recommends — Thursday's court will ask what treatment says now, not what it said in October. Two: Rae and Lou, contacted today, in ways that can be confirmed. Three: a written request for the case record under 55 Pa. Code § 3130.44(d) — the screen report and the related case notes — sent by Wednesday, copy kept. Four: a written supervision plan for Sam's return, with named cover, that Lou has actually agreed to — not described, agreed.

“The screen result will be in the room Thursday either way,” she says. “The question the judge will actually be deciding is what surrounds it. Build the surroundings.”

**Choices:**
- Start with item one — call the program from counsel's office and take today's assessment slot → **removal_assessment**  _(cash −14)_
  - NOTE (shown after choosing): The list shrinks by its hardest item before lunch. Momentum, in a two-day window, is a form of evidence.
- Start with the result itself — spend today calling the program and the lab's number on the report to demand the screen be done again → **dispute_only**
  - NOTE (shown after choosing): The urge is honest. The hours are also real, and they are the same hours items one through four were going to use.

## [wait_hearing] Waiting for Thursday
*Day 1 — Tuesday, November 3, 2026 — Tuesday, November 3, 2026 (dayOffset 1)*

Tuesday passes the way waiting passes: in rooms that are too quiet, at a phone that does not ring with news, in rehearsals of a speech that improves every time you give it to the kitchen.

The speech is good. That is the trap of it. It explains the clean months, the unfairness of a week judged by one line, the kind of parent Sam's school thinks you are. Everything in it is true. None of it is a document, and Thursday's hearing — like every hearing in the eight months behind you — will be conducted substantially out of documents: reports, notes, plans, records of attendance and contact.

By Wednesday morning, the speech is polished to a shine, and the folder is exactly as empty as it was Monday night. There is still one day left in the window. It is not much. It is also not nothing — Wednesdays have built records before.

**Choices:**
- Spend Wednesday on counsel's list after all — assessment if the program can fit you, record request sent, Lou confirmed in writing → **removal_records**
  - NOTE (shown after choosing): A one-day record is thin. It is also, on Thursday, the difference between “nothing” and “begun, in writing, before the hearing.”
- Keep faith with the speech — Thursday, in person, is where you'll be believed → **wed_thin**
  - NOTE (shown after choosing): Wednesday closes the way Tuesday did. The window the caseworker described on Monday is now a closed door with your speech standing in front of it.

## [removal_assessment] The Assessment, From the Other Side of Removal
*Day 1 — Tuesday, November 3, 2026 — Tuesday, November 3, 2026 (dayOffset 1)*

The assessment is the same ninety minutes it would have been yesterday — the clean months, Friday's result, sleep, stress, the cut hours at work — with one difference: you are answering from an apartment Sam is not in, and everyone in the room knows it, and the counselor's kindness about that fact is professional and complete.

Her recommendation is the stepped-up plan, not a restart: added sessions, group twice a week, screens on the program's schedule, daily sponsor contact, and a written relapse-response note naming Lou's role — the same document that was on offer Monday. You sign it. She notes, because these notes are her job, that you attended the day after removal, accepted the recommendations, and asked — in writing, on the program's form — what paperwork accompanies Friday's result and how a person obtains that page.

“Through the case record,” she says. “Ask the agency in writing. Keep your copy.” It is the second time in two days a professional has said that sentence to you. You decide to treat repetition as instruction.

**Choices:**
- Go home and do items three and four tonight, while the assessment note is still warm: the record request and the supervision plan → **removal_records**  _(HIDDEN + Assessment — attended Tuesday after removal; stepped-up plan accepted; provider/lab process questions asked and noted)_
  - NOTE (shown after choosing): Two items left, one day left, and for the first time since Monday the arithmetic feels possible.

## [dispute_only] A Day Spent on the Result
*Day 1 — Tuesday, November 3, 2026 — Tuesday, November 3, 2026 (dayOffset 1)*

The lab's number, when you finally reach a human, belongs to a person whose entire job is explaining that she cannot explain. Results are released through the ordering program and the case record. Questions about a report go in writing to the agency that holds the file. There is no desk, at the end of any phone tree you climb today, where a screen gets argued with, withdrawn, or redone on a parent's say-so — and the people telling you this are not unkind about it. They are describing the shape of the process, the way Ms. Bell described the shape of Monday.

By evening you know a great deal about how the paperwork moves and have moved none of it. The assessment slot you didn't take was given to someone else; the program can try again Wednesday morning, maybe. Rae has called twice. Lou has texted once: “Tell me what to sign.”

Counsel's list is still on the table. Four items. One day of the window remains, and Wednesday has a reputation in this case for being the day records get built or don't.

**Choices:**
- Wednesday, work the list top to bottom — assessment if they'll fit you, record request sent, Lou's signature on a real plan → **removal_records**
  - NOTE (shown after choosing): A day late and a day real. What Wednesday produces will be in Thursday's room; what Tuesday produced is a story about phone trees.
- Call the lab once more Wednesday — if the result falls, everything else was a distraction → **wed_thin**
  - NOTE (shown after choosing): It does not fall, because phone calls are not the mechanism by which results fall. Wednesday ends with the list untouched.

## [removal_records] Wednesday: The Request and the Plan
*Day 2 — Wednesday, November 4, 2026 — Wednesday, November 4, 2026 (dayOffset 2)*

Wednesday, November 4 — the last day of the window. Two documents get built at your kitchen table, and they are built differently, which is the day's whole lesson.

The first is the written case-record request, sent today under 55 Pa. Code § 3130.44(d), asking for the screen report and the related case notes — the assessment note, the removal-night notes, the visit records — with your stamped copy kept. The second is the supervision plan for Sam's return: after-school cover, treatment-evening cover, the standing fallback, each with a name on it. A plan, counsel said, that Lou has actually agreed to.

Lou is twenty minutes away and has been waiting since Monday to be handed something she can sign. The request is ready to send either way. The plan is where the day will be decided.

**Choices:**
- Send the request, then drive the plan to Lou's and come home with her signature and her confirmed nights on it → **shelter_strong**  _(cash −6; FLAG: recordsRequested; HIDDEN + Case record — written request sent Wednesday for the screen report and related case notes (55 Pa. Code § 3130.44(d)); HIDDEN + Supervision plan — written, named cover, kin signed and confirmed inside the 48-hour window)_
  - NOTE (shown after choosing): Requested, dated, copied — and confirmed, by a second person, in writing, inside the window. Thursday's folder has a spine.
- Send the request, and describe the plan to Ms. Bell by phone — Lou's word is good and everyone knows it → **shelter_partial**  _(cash −6; FLAG: recordsRequested; HIDDEN + Case record — written request sent Wednesday for the screen report and related case notes (55 Pa. Code § 3130.44(d)))_
  - NOTE (shown after choosing): Lou's word is good. It is also, as of Wednesday night, a thing one caseworker heard described on a phone — which is where unconfirmed things live.

## [wed_thin] Wednesday, Unbuilt
*Day 2 — Wednesday, November 4, 2026 — Wednesday, November 4, 2026 (dayOffset 2)*

Wednesday is a day you will later be able to describe in detail and evidence hardly at all. The speech got better. The apartment got cleaner. A call was made to a number that turned out to be a fax line, and that call — like most of the week's effort — happened in a way that left nothing behind it that another person could point to.

No assessment was attended. No record was requested. Rae was not called; Lou was not asked for anything she could sign. None of this means you did nothing, and none of it means you do not love your son, and both of those truths will be in the room Thursday — carried by you, in person, in a speech.

What will also be in the room is a file. In the file, Friday's reported result currently travels alone, accompanied only by Monday night's notes. Tomorrow, a judge reads the file.

**Choices:**
- Sleep badly, dress carefully, and go to the shelter care hearing with the only record there is → **shelter_thin**
  - NOTE (shown after choosing): Thursday does not ask whether you suffered this week. It asks what the week contains that a court can rely on.

## [shelter_strong] Thursday: Shelter Care, With a Folder
*Day 3 — Thursday, November 5, 2026 — Thursday, November 5, 2026 (dayOffset 3)*

The shelter care hearing falls on Thursday, November 5, 2026 — within the 72 hours that 42 Pa.C.S. § 6332 and 23 Pa.C.S. § 6315(d) allow between a child being taken into custody and this hearing. It is a small room with a specific, limited job: not to decide the case, but to decide where Sam sleeps while the case goes on, and on what the court can rely on right now.

Your counsel, provided under 42 Pa.C.S. § 6337, does not argue that Friday's result is imaginary. She walks the court through the folder the forty-eight hours built: the assessment attended and its stepped-up plan, signed; the record request, sent Wednesday, for the screen report and the case notes; the supervision plan with Lou's signature and confirmed nights; Rae's daily contact, confirmed. Ms. Bell's own report, to her credit and your counsel's use, confirms the timeline: the supports the arrangement names are the supports who answered.

The judge asks the questions judges ask about tonight and tomorrow night — who, where, what happens if — and for once, every answer is a name that has already agreed.

**Choices:**
- Answer the last question yourself, briefly, the way counsel rehearsed: what changed Monday, and what is in place now → **end_shelter_return**
  - NOTE (shown after choosing): Short, factual, and finished before it becomes a speech. The folder does the rest, because folders are what it was built for.

## [shelter_partial] Thursday: Shelter Care, With a Gap
*Day 3 — Thursday, November 5, 2026 — Thursday, November 5, 2026 (dayOffset 3)*

The shelter care hearing falls on Thursday, November 5, 2026 — within the 72 hours that 42 Pa.C.S. § 6332 and 23 Pa.C.S. § 6315(d) allow. Your counsel, provided under 42 Pa.C.S. § 6337, has real material to work with, and she works it: the assessment attended, the stepped-up plan signed, the record request sent Wednesday under § 3130.44(d) for the screen report and the case notes.

Then the court reaches the supervision plan — the document that answers where Sam sleeps and who is with him on the hard nights — and the room finds the gap. The plan was described by phone. Lou, who would sign it today if handed it, was never handed it. A court deciding tonight's placement on tonight's record cannot confirm a support from a description of her willingness, and the judge — who says, on the record, that the week's treatment response is documented and credited — continues the placement and sets the next review, with the path back written into the order: a confirmed, signed plan.

You leave with the path in writing. It is a better thing to leave with than most people get. It is not Sam.

**Choices:**
- Take the order home and read the path back the way it is written: confirmed, signed, filed — this time before the review, not at it → **january_review**
  - NOTE (shown after choosing): The court has told you, in an order, exactly what the record is missing. Orders like that are instructions wearing formal clothes.

## [shelter_thin] Thursday: Shelter Care, With a Speech
*Day 3 — Thursday, November 5, 2026 — Thursday, November 5, 2026 (dayOffset 3)*

The shelter care hearing falls on Thursday, November 5, 2026 — within the 72 hours that 42 Pa.C.S. § 6332 and 23 Pa.C.S. § 6315(d) allow. Your counsel, provided under 42 Pa.C.S. § 6337, stands beside you in a small room whose entire business is what can be relied on right now.

You are given your say, and you give the speech, and it is everything it was in the kitchen: true, complete, and moving in the way true things are. The clean months are described. The unfairness of one line is described. Then the court turns, as courts turn, to the file — for an assessment that was attended, a support that was contacted, a record that was requested, a plan that exists on paper — and the file, this week, has almost nothing in it to turn to. The reported result sits in it unaccompanied.

The judge continues the placement and sets the next review. It is not a ruling that you are a bad parent, and the judge does not say it is. It is a ruling about what Thursday could rely on, which is a colder thing and, this week, an accurate one.

**Choices:**
- Hear the review date on your way out, and understand — fully, for the first time — what has to exist by then → **january_review**
  - NOTE (shown after choosing): Understanding arrives the way it often does in this system: one hearing too late to be early, and in plenty of time to matter next.

## [january_review] The Next Review
*Day 65 — Wednesday, January 6, 2027 — Wednesday, January 6, 2027 (dayOffset 65)*

Weeks have passed the way weeks pass in placement: visits kept, sessions attended in rising numbers, a treatment file that has begun, late, to accumulate the paper it should have had in November. You did much of what counsel's list asked — after the window in which it would have changed Thursday.

What the record still does not contain, on the morning of this review, is the thing both Thursday hearings circled: a supervision plan confirmed the hard way, by the people named in it, in writing, in the file — and a response to the November result that was documented when the result was fresh rather than assembled afterward. Lou's availability, described many times, was never confirmed in the form the court asked for. The November screen report was never requested in writing, so the questions about its paperwork were never answered in the record either.

The court credits what has been built since. It also reads dates. Placement continues past this review, with the path — the same path, still open, still paper — stated again.

**Choices:**
- Leave with the path memorized this time, and a folder that is finally, actually started → **end_continues**
  - NOTE (shown after choosing): The case is not over. Cases like this rarely end at a review. But the review has ended, and Sam goes back to the placement, and the folder goes home with you.

## [end_home] Ending — Home, Under a Documented Plan
*Day 30 — Wednesday, December 2, 2026 — Wednesday, December 2, 2026 (dayOffset 30)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD: One reported positive screen, at month eight, after months of clean ones — and, around it, a record: treatment contacted the morning the result arrived; an assessment attended Tuesday and its stepped-up plan signed; a written case-record request sent Wednesday, November 4, under 55 Pa. Code § 3130.44(d), for the screen report and the related case notes; a voluntary kin safety arrangement, signed at Lou's table, that covered the two nights nobody could leave uncovered; a supervision plan with named cover and a confirmed backup; and follow-up screens attended on schedule. The result never left the file. It simply stopped travelling alone.
- THE ROLES, AS THEY ACTUALLY WORKED: The treatment provider documented what treatment could document — attendance, recommendations, the response to the result — and decided nothing about placement. The caseworker built the safety arrangement out of supports she could confirm, and wrote both the result and the response into the record she carried to court. Kin — Lou — turned “family support” from a phrase into nights, pickups, and a signature. Counsel, provided under 42 Pa.C.S. § 6337, made sure the folder, not the rumour of the folder, was what the court read. And the court decided the only question before it, on the record in front of it. A screen result is a laboratory report about one sample on one day. Follow-up documentation is what a parent did next, made checkable. The court's record is what of all that was actually in the room — and cases are decided from the third thing, not the first.
- THE HONEST PART: This ending is prompt and it is conditional, and both halves matter. Sam is home under a documented safety and treatment plan — with stepped-up sessions, scheduled screens, and a review structure still standing around the family — not declared finished, and not cleared of the result, which remains in the record where results live. Another judge, reading the same folder with a different sense of risk, could have tightened the arrangement further; a week in which Lou's phone went unanswered could have rewritten Monday entirely. What you controlled was the next forty-eight hours on paper. This time, they were enough — and “this time” is the most honest phrase in family court.

## [end_shelter_return] Ending — Returned at Shelter Care
*Day 3 — Thursday, November 5, 2026 — Thursday, November 5, 2026 (dayOffset 3)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD: A removal on Monday night, November 2 — and then a forty-eight-hour record built from inside that fact: counsel contacted Tuesday morning; an assessment attended and its stepped-up plan signed; provider and lab-process questions asked and noted, without anyone inventing a right to have the result redone; a written case-record request sent Wednesday under 55 Pa. Code § 3130.44(d) for the screen report and the related case notes; and a supervision plan carrying Lou's signature and her confirmed nights. At Thursday's shelter care hearing — held November 5, within the 72 hours required by 42 Pa.C.S. § 6332 and 23 Pa.C.S. § 6315(d) — that record is what supported Sam's return at the shelter-care stage, under the documented safety and treatment plan.
- THE ROLES, AS THEY ACTUALLY WORKED: The treatment provider's contribution was documentation: attendance, a current recommendation, a plan with dates. The caseworker's Monday decision and her Thursday report were both in the record, and her report confirmed the timeline of your response — workers' notes carry the facts they carry, in whichever direction they point. Kin made return physically possible: a return plan is only as real as the person who signed it. Counsel, provided under 42 Pa.C.S. § 6337, kept the hearing on its actual question — what tonight's supervision can rely on — and put the folder, item by item, in front of the court. The distinction the whole scenario turns on held: a screen result is one reported line about one sample; follow-up documentation is the checkable account of what happened next; the court's record is the part of both that a judge could actually read on Thursday, and it is the third thing that decided the outcome.
- THE HONEST PART: Sam was removed, and three nights of a seven-year-old's life were spent in an emergency placement because Monday's safety plan did not exist when it was needed. This ending does not give those nights back, and it does not pretend the return was guaranteed: a different judge could have wanted the plan lived under for longer before trusting it, and if Lou had not answered, there would have been no plan to sign. What the record did was narrower and real — it made return the decision the evidence in the room best supported, at the first hearing the law provides. The removal happened because of an empty page. The return happened because the next two days filled it.

## [end_continues] Ending — Placement Continues Past Review
*Day 65 — Wednesday, January 6, 2027 — Wednesday, January 6, 2027 (dayOffset 65)*

**Ending.**

**Debrief:**
- WHAT THE RECORD HELD: At the hearings that decided Sam's placement, the record held a reported positive screen — and, around it, far too little that anyone else could check. No assessment attended inside the window when it would have answered Thursday's questions. No written case-record request under 55 Pa. Code § 3130.44(d), so the screen report's own paperwork was never obtained or examined in the record. No supervision plan confirmed in writing by the people named in it; supports that existed in life — Lou's willingness, Rae's loyalty — stayed unconfirmed in the only form a court can rely on. Later work was real and was credited. It was also dated, and courts read dates: a response assembled after the hearings cannot retroactively surround a result at the hearings.
- THE ROLES, AND WHERE THE GAPS SAT: The treatment provider can only document attendance that happens; an assessment never attended generates a page that says so. The caseworker's file carried Monday's events essentially unaccompanied, because little else was given to it — workers write what occurs, and absence occurs too. Kin cannot confirm a plan they were never handed to sign. Counsel, provided under 42 Pa.C.S. § 6337, argued what existed — and the honest limit of advocacy is that it cannot introduce a record that was never built. The court decided, at shelter care and again at review, from the record in front of it. That is the distinction to keep: a screen result is a reported line about one sample. Follow-up documentation is the checkable account of the response. The court's record is what judges are permitted to act on — and in this path, the second of those three things was thin, so the third was thin, whatever the first one did or did not truly mean.
- THE HONEST PART: This ending is not a finding that one screen proved a parent's worth, and nothing in this scenario treats it as one. Placement continues because the paper record was thin and the supports remained unconfirmed at the moments decisions had to be made — a statement about timing and documentation, not about love, effort in other weeks, or who this parent is across eight months. Judges, workers, and luck all held pieces of this: a different caseworker might have pressed harder on Monday; a confirmed Lou on Wednesday could have changed Thursday outright. The part that belonged to the parent was the next forty-eight hours on paper. They are still buildable — the path in the order remains open, the folder has been started, and reviews recur. But they will now be built across a separation that did not have to last this long, and a seven-year-old will measure that in his own units, which are not days.
