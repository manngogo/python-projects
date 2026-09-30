# Home workout generator with progression tracking. Run: python workout_generator.py
import json, random, re
from pathlib import Path
 
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
LOG_FILE = Path(__file__).with_name("workout_log.json")
LOG = json.loads(LOG_FILE.read_text()) if LOG_FILE.exists() else {}
LOWER = {"squat", "hinge", "single", "glute", "calf"}  # these get +5 lb jumps, upper gets +2.5
 
# Add your own: style|slot|name|sets x reps (or time)
RAW = '''
weights|push|Barbell bench/floor press|4x5-8
weights|push|Dumbbell floor press|3x8-12
weights|push|Incline dumbbell press|3x8-12
weights|push|Close-grip barbell press|3x6-10
weights|push|Single-arm dumbbell floor press|3x8-12
weights|push|Dumbbell floor fly|3x10-15
weights|push|Band chest press|3x12-15
weights|pull|One-arm dumbbell row|3x8-12
weights|pull|Bent-over barbell row|4x6-10
weights|pull|Pendlay row|4x5-8
weights|pull|Dumbbell pullover|3x10-12
weights|pull|Band lat pulldown (over pull-up bar)|3x12-15
weights|pull|Rear-delt dumbbell fly|3x12-15
weights|pull|Band face pulls|3x15-20
weights|pull|Barbell shrugs|3x10-15
weights|shoulder|Standing overhead press|3x6-10
weights|shoulder|Arnold press|3x8-12
weights|shoulder|Lateral raises|3x12-15
weights|shoulder|Seated dumbbell press|3x8-12
weights|shoulder|Dumbbell push press|3x5-8
weights|shoulder|Front raises|3x10-12
weights|shoulder|Band Y raises|3x15
weights|arms|Dumbbell curls|3x10-12
weights|arms|Barbell curls|3x8-12
weights|arms|Hammer curls|3x10-12
weights|arms|Concentration curls|3x10-12
weights|arms|Overhead triceps extension|3x10-12
weights|arms|Floor skull crushers|3x8-12
weights|arms|Band triceps pushdown (over pull-up bar)|3x12-15
weights|arms|Zottman curls|3x8-10
weights|squat|Barbell back squat|4x5-8
weights|squat|Front squat|3x8-10
weights|squat|Goblet squat|3x10-12
weights|squat|Pause squat (2s at bottom)|3x5-8
weights|squat|Tempo squat (3s down)|3x6-8
weights|squat|Dumbbell squat|3x10-12
weights|hinge|Romanian deadlift|3x8-10
weights|hinge|Conventional deadlift|4x4-6
weights|hinge|Sumo deadlift|4x5-8
weights|hinge|Stiff-leg deadlift|3x8-10
weights|hinge|Barbell good mornings|3x8-10
weights|hinge|Dumbbell RDL|3x10-12
weights|single|Bulgarian split squat|3x8-10/leg
weights|single|Walking lunges|3x10/leg
weights|single|Single-leg RDL|3x8-10/leg
weights|single|Reverse lunges|3x8-10/leg
weights|single|Dumbbell step-ups (sturdy chair)|3x8-10/leg
weights|single|Lateral lunges|3x8-10/leg
weights|single|Cossack squats|3x8/side
weights|glute|Barbell hip thrust|3x8-12
weights|glute|Dumbbell glute bridge|3x10-15
weights|glute|Band-resisted glute bridge|3x15-20
weights|glute|Banded lateral walks|3x15/side
weights|glute|Banded kickbacks|3x15/leg
weights|glute|Frog pumps|3x20
weights|calf|Standing calf raises|4x12-20
weights|calf|Single-leg dumbbell calf raise|3x12-15/leg
weights|calf|Barbell seated calf raise|3x15-20
weights|calf|Band calf raise|3x20
weights|core|Barbell rollout|3x8-10
weights|core|Pallof press (band)|3x12/side
weights|core|Russian twist with dumbbell|3x12/side
weights|core|Band woodchop|3x12/side
weights|core|Suitcase hold|3x30s/side
weights|cardio|Light barbell complex (deadlift, row, squat, press)|5 rounds
weights|cardio|Dumbbell swing/thruster circuit|10 min EMOM
calisthenics|push|Push-ups|4x max
calisthenics|push|Feet-elevated push-ups|3x near failure
calisthenics|push|Archer push-ups|3x6-10/side
calisthenics|push|Wide push-ups|3x12-20
calisthenics|push|Tempo push-ups (3s down)|3x8-12
calisthenics|push|Pseudo planche push-ups|3x8-12
calisthenics|push|Explosive clap push-ups|3x5-8
calisthenics|push|Dips (chairs/parallel supports)|3x8-15
calisthenics|push|Hindu push-ups|3x10-12
calisthenics|pull|Pull-ups|4x6-10
calisthenics|pull|Chin-ups|4x6-10
calisthenics|pull|Wide-grip pull-ups|3x5-8
calisthenics|pull|Commando pull-ups|3x5-8/side
calisthenics|pull|Archer pull-ups|3x3-5/side
calisthenics|pull|Slow negative pull-ups|3x5
calisthenics|pull|Inverted rows (low barbell, sturdy setup)|3x8-15
calisthenics|pull|Scapular pull-ups|3x10-12
calisthenics|shoulder|Pike push-ups|3x8-12
calisthenics|shoulder|Elevated pike push-ups|3x6-10
calisthenics|shoulder|Wall walks|3x5-8
calisthenics|shoulder|Handstand wall hold|4x20-30s
calisthenics|shoulder|Plank shoulder taps|3x30s
calisthenics|arms|Diamond push-ups|3x8-15
calisthenics|arms|Close-grip chin-ups|3x6-10
calisthenics|arms|Bench dips|3x10-15
calisthenics|arms|Bodyweight triceps extensions (elevated surface)|3x8-12
calisthenics|arms|Chin-up isometric hold|3x15-20s
calisthenics|squat|Tempo bodyweight squats (4s down)|3x12-15
calisthenics|squat|Jump squats|3x12
calisthenics|squat|Sissy squats (hold support)|3x8-12
calisthenics|squat|Wall sit|3x45-60s
calisthenics|squat|Broad jumps|4x5
calisthenics|squat|Box jumps (sturdy step)|4x5
calisthenics|hinge|Nordic curl negatives (feet anchored)|3x4-6
calisthenics|hinge|Bodyweight good mornings|3x15
calisthenics|hinge|Single-leg hip hinge reach|3x10/leg
calisthenics|single|Pistol squat progression|3x5/leg
calisthenics|single|Reverse lunges|3x12/leg
calisthenics|single|Jumping lunges|3x10/leg
calisthenics|single|Step-ups (sturdy chair)|3x12/leg
calisthenics|single|Skater squats|3x8/leg
calisthenics|single|Shrimp squat progression|3x5/leg
calisthenics|glute|Single-leg glute bridge|3x12/leg
calisthenics|glute|Feet-elevated glute bridge|3x15
calisthenics|glute|Donkey kicks|3x15/leg
calisthenics|glute|Fire hydrants|3x15/leg
calisthenics|glute|Glute bridge march|3x20
calisthenics|calf|Single-leg calf raise|3x15/leg
calisthenics|calf|Calf raises off a step|4x15-20
calisthenics|calf|Tip-toe walks|3x30s
calisthenics|core|Hanging leg raises|3x8-12
calisthenics|core|Hanging knee raises|3x10-15
calisthenics|core|Hollow body hold|3x30-45s
calisthenics|core|L-sit tuck hold|3x15-20s
calisthenics|core|Plank|3x45-60s
calisthenics|core|Side plank|3x30s/side
calisthenics|core|V-ups|3x12-15
calisthenics|core|Dragon flag negatives|3x3-5
calisthenics|core|Mountain climbers|3x40s
calisthenics|cardio|Burpee intervals (40s on / 20s off)|8 rounds
calisthenics|cardio|Bodyweight AMRAP (squat, push-up, lunge)|10-15 min
calisthenics|cardio|Mountain climber + burpee ladder|10 min
calisthenics|cardio|Jumping jack / high-knee circuit|4 rounds
pilates|core|The Hundred|1x100 beats
pilates|core|Roll-ups|3x8-10
pilates|core|Single-leg stretch|3x10/side
pilates|core|Double-leg stretch|3x10
pilates|core|Criss-cross|3x12/side
pilates|core|Scissors|3x10/side
pilates|core|Teaser|3x6-8
pilates|core|Saw|3x6/side
pilates|core|Spine twist|3x8/side
pilates|core|Corkscrew|3x6/side
pilates|core|Leg pull front|3x8
pilates|core|Pilates plank series|3x45s
pilates|core|Dead bug|3x10/side
pilates|core|Rolling like a ball|3x10
pilates|glute|Pilates bridge series|3x12
pilates|glute|Shoulder bridge|3x8/side
pilates|glute|Side-lying leg series|3x15/side
pilates|glute|Clamshells (band)|3x20/side
pilates|glute|Single-leg bridge|3x10/side
pilates|push|Pilates push-ups|3x8-10
pilates|push|Plank to pike|3x10
pilates|pull|Swimming|3x30s
pilates|pull|Swan prep|3x8
pilates|pull|Superman pulls|3x10
pilates|shoulder|Band arm circles|3x12
pilates|shoulder|Pilates band arm series|3x10
pilates|arms|Pilates triceps push-ups|3x8-10
pilates|arms|Band biceps curl (Pilates stance)|3x12
pilates|squat|Wall squat hold|3x45s
pilates|squat|Pilates squat with heel lift|3x12
pilates|hinge|Standing hip hinge (Pilates)|3x12
pilates|hinge|Spine stretch forward|3x8
pilates|single|Standing single-leg balance series|3x30s/leg
pilates|single|Side-lying leg lifts|3x15/leg
pilates|calf|Parallel heel raises|3x15
pilates|calf|Band footwork on the floor|3x15
run|cardio|Run/walk intervals (1 min jog / 2 min walk)|8 rounds
run|cardio|Run/walk intervals (2 min jog / 1 min walk)|6 rounds
run|cardio|Run/walk intervals (3 min jog / 1 min walk)|5 rounds
run|cardio|Easy conversational run|20-30 min
run|cardio|Long easy run/walk|30-45 min
run|cardio|Strides after an easy jog|15 min + 6x20s
run|cardio|Tempo run (comfortably hard)|5 min warm-up + 10-15 min
run|cardio|Fartlek (random surges)|20 min
run|cardio|Hill or stair repeats|8 rounds
run|cardio|Progression run (finish faster)|25 min
run|cardio|5K practice at easy pace|20-35 min
rope|cardio|Rope intervals 30s on / 30s off|10 rounds
rope|cardio|Rope 2-min rounds|6 rounds
rope|cardio|Rope ladder (1-2-3-2-1 min)|1 ladder
rope|cardio|Double-under practice|10 min
rope|cardio|Boxer skip, steady|10-15 min
rope|cardio|Tabata rope (20s on / 10s off)|8 rounds
rope|cardio|Criss-cross / high-knee intervals|8 rounds
rope|cardio|Single-leg hop rope|6 rounds
'''
EX = []
for line in RAW.strip().splitlines():
    style, slot, name, rx = line.split("|")
    EX.append((name, style, slot, rx))
 
TEMPLATES = {
    "upper": ["push", "pull", "shoulder", "pull", "push", "arms"],
    "lower": ["squat", "hinge", "single", "glute", "calf"],
    "core": ["core", "core", "glute", "core", "cardio"],
}
CYCLE = ["upper", "lower", "upper", "lower", "core"]
 
 
# ---------- progression ----------
def tracked(e):
    # Only rep-based weights/calisthenics moves get weight & rep tracking.
    _, style, slot, rx = e
    return style in ("weights", "calisthenics") and slot != "cardio" \
        and bool(re.match(r"\d+x", rx)) and not re.search(r"\d+s\b", rx)
 
 
def top_reps(rx):
    m = re.match(r"\d+x(\d+)(?:-(\d+))?", rx)
    return int(m.group(2) or m.group(1)) if m else None
 
 
def next_goal(e, w, reps):
    # Double progression: hit the top of the rep range, then add weight.
    slot, rx = e[2], e[3]
    top, inc = top_reps(rx), (5 if slot in LOWER else 2.5)
    if e[1] == "calisthenics":
        if top and reps >= top:
            return "slow the tempo (3 seconds down), then add weight or try a harder variation"
        return f"bodyweight, aim for {reps + 1}+ reps"
    if top and reps >= top:
        return f"{w + inc:g} lb, rebuild from the bottom of the range" if w else "add weight or a harder variation"
    return f"{f'{w:g} lb' if w else 'bodyweight'}, aim for {reps + 1}+ reps"
 
 
def save():
    LOG_FILE.write_text(json.dumps(LOG, indent=2))
 
 
def log_workout(plan):
    days = [d for d, (_, rows) in plan.items() if any(tracked(r) for r in rows)]
    if not days:
        return print("\nNo trackable lifts in this plan.")
    day = ask("Which day did you just do?", days)
    for e in plan[day][1]:
        if not tracked(e):
            continue
        raw = input(f"\n{e[0]} ({e[3]})\n  weight in lb (0 = bodyweight, Enter = skip): ").strip()
        if not raw:
            continue
        try:
            w = float(raw)
            set_reps = [int(value) for value in input("  reps for each set, separated by commas: ").replace(" ", "").split(",")]
            if not set_reps or any(value < 0 for value in set_reps):
                raise ValueError
            reps = min(set_reps)
        except ValueError:
            print("  Skipped (enter a weight and non-negative reps separated by commas).")
            continue
        LOG[e[0]] = {"w": w, "reps": reps, "next": next_goal(e, w, reps)}
        print(f"  Next time: {LOG[e[0]]['next']}")
    save()
    print("\nSaved!")
 
 
def progress():
    if not LOG:
        return print("\nNothing logged yet.")
    print("\nYour progress:")
    for name, d in LOG.items():
        print(f"  {name}: last {d['w']:g} lb x {d['reps']} -> next: {d['next']}")
 
 
# ---------- plan building ----------
def pick(styles, slot, used):
    pool = [e for e in EX if e[1] in styles and e[2] == slot and e not in used]
    return random.choice(pool) if pool else None
 
 
def build(styles, rest_days, level):
    plan, i = {}, 0
    for day in DAYS:
        if day in rest_days:
            plan[day] = ("Rest (optional 20-30 min walk)", [])
            continue
        kind = CYCLE[i % len(CYCLE)]
        i += 1
        slots = TEMPLATES[kind][:-1] if level == "beginner" else TEMPLATES[kind]
        if kind != "core" and styles & {"run", "rope"}:
            slots = slots + ["cardio"]  # cardio finisher for fat loss
        used, rows = [], []
        for s in slots:
            e = pick(styles, s, used)
            if e:
                used.append(e)
                rows.append(e)
        plan[day] = (kind.upper() + (" + cardio" if "cardio" in slots else ""), rows)
    return plan
 
 
def show(plan):
    for day, (title, rows) in plan.items():
        heading = title.replace("UPPER", "Upper").replace("LOWER", "Lower").replace("CORE", "Core")
        print(f"\n**{day}: {heading}**")
        if not rows:
            print("- " + ("Rest (optional 20-30 min walk)" if "Rest" in title else "Nothing matched your interests"))
            continue
        for e in rows:
            exercise = f"{e[0]}: {e[3].replace('x', ' x ', 1)}"
            if tracked(e) and e[0] in LOG:
                exercise += f" (target: {LOG[e[0]]['next']})"
            print(f"- {exercise}")
        if "cardio" in title.lower():
            print("\n    • *Then:* 15-20 min run/walk intervals after your workout.")
 
 
def ask(prompt, options, multi=False):
    print(f"\n{prompt}")
    for n, o in enumerate(options, 1):
        print(f"  {n}. {o}")
    raw = input("Enter number(s) separated by commas: ")
    idx = [int(x) - 1 for x in raw.replace(" ", "").split(",") if x.isdigit()]
    chosen = [options[i] for i in idx if 0 <= i < len(options)]
    return chosen if multi else (chosen[0] if chosen else options[0])


def yn(prompt, default=False):
    default_text = "y/n"
    raw = input(f"\n{prompt} [{default_text}]: ").strip().lower()
    if not raw:
        return default
    return raw in {"y", "yes"}
 
 
def setup():
    styles = set()
    for style in ["weights", "calisthenics", "pilates", "run", "rope"]:
        if yn(f"Do you want {style} workouts?", style == "weights"):
            styles.add(style)
    styles = styles or {"weights", "calisthenics", "pilates", "run", "rope"}
    level = "beginner" if yn("Are you a beginner?", True) else "intermediate"

    while True:
        raw = input("\nHow many rest days do you want? ").strip()
        if not raw:
            print("  Please enter a number from 0 to 7.")
            continue
        try:
            rest_count = int(raw)
            if 0 <= rest_count <= len(DAYS):
                break
        except ValueError:
            pass
        print("  Please enter a number from 0 to 7.")

    if rest_count == 0:
        rest = set()
    else:
        while True:
            print(f"\nChoose {rest_count} rest day(s) from the list below:")
            for n, day in enumerate(DAYS, 1):
                print(f"  {n}. {day}")
            raw = input("Enter numbers separated by commas: ").strip()
            if raw:
                idx = [int(x) - 1 for x in raw.replace(" ", "").split(",") if x.isdigit()]
                rest = {DAYS[i] for i in idx if 0 <= i < len(DAYS)}
                if len(rest) != rest_count:
                    print(f"  You selected {len(rest)} day(s), but you asked for {rest_count}. Please choose exactly {rest_count} day(s).")
                    continue
                break

    return styles, level, rest
 
 
if __name__ == "__main__":
    styles, level, rest = setup()
    plan = build(styles, rest, level)
    while True:
        show(plan)
        c = input("\n[r] reroll  [l] log a workout  [p] track workout progression  [s] change setup  [q] quit: ").lower()
        if c == "q":
            break
        elif c == "l":
            log_workout(plan)
        elif c == "p":
            log_workout(plan)
        elif c == "s":
            styles, level, rest = setup()
            plan = build(styles, rest, level)
        else:
            plan = build(styles, rest, level)