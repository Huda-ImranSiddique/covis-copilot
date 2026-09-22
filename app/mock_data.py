"""
Mock PMS data for the COVIS AI Copilot POC.

Domain: Event Management Company (Saudi client)

Simulates what a real event management PMS would provide.
In production, these would be API calls or database queries.
"""

from datetime import date, timedelta

TODAY = date.today().isoformat()
TOMORROW = (date.today() + timedelta(days=1)).isoformat()
NEXT_WEEK = (date.today() + timedelta(days=7)).isoformat()
NEXT_MONTH = (date.today() + timedelta(days=30)).isoformat()


# ---------- TEAM ----------
TEAM_MEMBERS = [
    {
        "name": "Faisal Al-Qahtani",
        "role": "Event Coordinator",
        "hours_planned_today": 0,
        "open_tasks": 2,
        "leaves_this_week": None,
        "skills": ["event planning", "weddings", "corporate events", "guest coordination"],
    },
    {
        "name": "Abdullah Al-Harbi",
        "role": "Senior Event Manager",
        "hours_planned_today": 0,
        "open_tasks": 12,
        "leaves_this_week": None,
        "skills": ["large events", "VIP clients", "vendor management", "budget planning"],
    },
    {
        "name": "Khalid Al-Otaibi",
        "role": "Catering Manager",
        "hours_planned_today": 2,
        "open_tasks": 4,
        "leaves_this_week": None,
        "skills": ["catering", "menu planning", "food safety", "banquet setup"],
    },
    {
        "name": "Noura Al-Saud",
        "role": "Venue Coordinator",
        "hours_planned_today": 6,
        "open_tasks": 8,
        "leaves_this_week": None,
        "skills": ["venues", "logistics", "contracts", "site inspection"],
    },
    {
        "name": "Sultan Al-Dosari",
        "role": "Decoration Lead",
        "hours_planned_today": 4,
        "open_tasks": 7,
        "leaves_this_week": "Thursday and Friday",
        "skills": ["floral design", "stage design", "decor", "lighting"],
    },
    {
        "name": "Reem Al-Mutairi",
        "role": "Guest Relations Manager",
        "hours_planned_today": 3,
        "open_tasks": 5,
        "leaves_this_week": None,
        "skills": ["guest handling", "VIP hosting", "check-in", "hospitality"],
    },
    {
        "name": "Turki Al-Shammari",
        "role": "AV & Technical Lead",
        "hours_planned_today": 5,
        "open_tasks": 6,
        "leaves_this_week": "Monday",
        "skills": ["sound systems", "LED screens", "lighting", "AV setup"],
    },
    {
        "name": "Lama Al-Qahtani",
        "role": "Logistics Coordinator",
        "hours_planned_today": 4,
        "open_tasks": 5,
        "leaves_this_week": None,
        "skills": ["transport", "setup", "coordination", "vendor scheduling"],
    },
    {
        "name": "Bandar Al-Otaibi",
        "role": "Entertainment Coordinator",
        "hours_planned_today": 6,
        "open_tasks": 4,
        "leaves_this_week": None,
        "skills": ["entertainment", "performers", "stage timing", "MC coordination"],
    },
]


TEAM_STATS = {
    "members_planned_today": 42,
    "tasks_planned_today": 175,
    "hours_planned_today": 268,
}


# ---------- TASKS ----------
TASKS = [
    {
        "id": "EVT-1042",
        "title": "Al-Rashed corporate gala — stage and decor setup",
        "assignee": None,
        "priority": "high",
        "deadline": TOMORROW,
        "status": "unassigned",
        "required_skills": ["stage design", "decor", "floral design"],
    },
    {
        "id": "EVT-1043",
        "title": "Al-Faisal wedding — urgent catering issue",
        "assignee": None,
        "priority": "urgent",
        "deadline": TODAY,
        "status": "unassigned",
        "required_skills": ["catering", "menu planning", "banquet setup"],
    },
    {
        "id": "EVT-1044",
        "title": "Saudi Tech Summit — venue walkthrough",
        "assignee": "Noura Al-Saud",
        "priority": "medium",
        "deadline": (date.today() + timedelta(days=5)).isoformat(),
        "status": "in_progress",
        "required_skills": ["venues", "site inspection"],
    },
    {
        "id": "EVT-1045",
        "title": "Riyadh Expo 2026 — AV and LED setup",
        "assignee": "Turki Al-Shammari",
        "priority": "high",
        "deadline": (date.today() + timedelta(days=3)).isoformat(),
        "status": "in_progress",
        "required_skills": ["AV setup", "LED screens", "sound systems"],
    },
    {
        "id": "EVT-1046",
        "title": "Al-Rashed gala — guest list finalization",
        "assignee": "Reem Al-Mutairi",
        "priority": "high",
        "deadline": (date.today() + timedelta(days=2)).isoformat(),
        "status": "in_progress",
        "required_skills": ["guest handling", "VIP hosting"],
    },
]


# ---------- LEAVES ----------
LEAVES = [
    {
        "employee": "Sultan Al-Dosari",
        "dates": "Thursday, Friday",
        "priority": "high",
        "reason": "Family event",
    },
    {
        "employee": "Turki Al-Shammari",
        "dates": "Monday",
        "priority": "low",
        "reason": "Personal",
    },
]


# ---------- CLIENT MEETINGS ----------
CLIENT_MEETINGS = [
    {
        "client": "Al-Rashed Group",
        "date": (date.today() + timedelta(days=2)).isoformat(),
        "type": "Follow-up",
        "needs_follow_up": True,
    },
    {
        "client": "Saudi Tech Summit",
        "date": (date.today() + timedelta(days=4)).isoformat(),
        "type": "Site visit",
        "needs_follow_up": True,
    },
]


# ---------- LEADS ----------
LEADS = [
    {
        "name": "Al-Rashed Group",
        "source": "Referral",
        "priority": "high",
        "surfaced": "this week",
    },
    {
        "name": "Saudi Tech Summit",
        "source": "LinkedIn",
        "priority": "high",
        "surfaced": "this week",
    },
    {
        "name": "Jeddah Municipality",
        "source": "Cold outreach",
        "priority": "medium",
        "surfaced": "this week",
    },
]


# ---------- PROPOSALS ----------
PROPOSALS = [
    {
        "client": "Al-Rashed Group",
        "event_type": "Corporate Gala",
        "event_date": (date.today() + timedelta(days=30)).isoformat(),
        "status": "In Review",
        "value_sar": 450000,
    },
    {
        "client": "Saudi Tech Summit",
        "event_type": "Annual Conference",
        "event_date": (date.today() + timedelta(days=20)).isoformat(),
        "status": "In Review",
        "value_sar": 180000,
    },
    {
        "client": "Riyadh Expo 2026",
        "event_type": "Product Launch",
        "event_date": (date.today() + timedelta(days=15)).isoformat(),
        "status": "Won",
        "value_sar": 320000,
    },
    {
        "client": "Al-Faisal Wedding",
        "event_type": "Wedding Reception",
        "event_date": (date.today() + timedelta(days=10)).isoformat(),
        "status": "Won",
        "value_sar": 260000,
    },
    {
        "client": "Jeddah Municipality",
        "event_type": "Public Festival",
        "event_date": (date.today() + timedelta(days=45)).isoformat(),
        "status": "In Review",
        "value_sar": 620000,
    },
]


# ---------- UPCOMING EVENTS ----------
EVENTS = [
    {
        "name": "Riyadh Expo 2026",
        "city": "Riyadh",
        "date": (date.today() + timedelta(days=5)).isoformat(),
        "client": "Riyadh Expo 2026",
    },
    {
        "name": "Al-Faisal Wedding",
        "city": "Jeddah",
        "date": (date.today() + timedelta(days=10)).isoformat(),
        "client": "Al-Faisal Wedding",
    },
    {
        "name": "Saudi Tech Summit",
        "city": "Riyadh",
        "date": (date.today() + timedelta(days=20)).isoformat(),
        "client": "Saudi Tech Summit",
    },
    {
        "name": "Al-Rashed Corporate Gala",
        "city": "Riyadh",
        "date": (date.today() + timedelta(days=30)).isoformat(),
        "client": "Al-Rashed Group",
    },
    {
        "name": "Jeddah Municipality Festival",
        "city": "Jeddah",
        "date": (date.today() + timedelta(days=45)).isoformat(),
        "client": "Jeddah Municipality",
    },
]


# ---------- EQUIPMENT INVENTORY ----------
EQUIPMENT = [
    {"item": "LED Screen P2.5", "available_sqm": 55, "total_sqm": 80},
    {"item": "LED Screen P3.9", "available_sqm": 120, "total_sqm": 150},
    {"item": "Line Array Speakers", "available_units": 4, "total_units": 6},
    {"item": "Moving Head Lights", "available_units": 32, "total_units": 48},
]


# ---------- PIPELINE ----------
PIPELINE = {
    "target_this_quarter_sar": 2000000,
    "won_this_quarter_sar": 580000,
    "in_review_sar": 1250000,
    "exhibition_events_won": 3,
    "private_events_won": 5,
    "avg_profit_margin_percent": 22,
    "win_ratio_percent": 40,
    "win_ratio_target_percent": 30,
}


# ---------- CLIENT KPIs ----------
CLIENT_KPIS = [
    {
        "client": "Al-Rashed Group",
        "lifetime_value_sar": 1250000,
        "acquisition_cost_sar": 85000,
        "proposals_submitted": 5,
        "proposals_won": 2,
    },
    {
        "client": "Riyadh Expo 2026",
        "lifetime_value_sar": 640000,
        "acquisition_cost_sar": 42000,
        "proposals_submitted": 3,
        "proposals_won": 1,
    },
    {
        "client": "Saudi Tech Summit",
        "lifetime_value_sar": 320000,
        "acquisition_cost_sar": 28000,
        "proposals_submitted": 4,
        "proposals_won": 1,
    },
    {
        "client": "Al-Faisal Wedding",
        "lifetime_value_sar": 260000,
        "acquisition_cost_sar": 18000,
        "proposals_submitted": 1,
        "proposals_won": 1,
    },
    {
        "client": "Jeddah Municipality",
        "lifetime_value_sar": 480000,
        "acquisition_cost_sar": 55000,
        "proposals_submitted": 3,
        "proposals_won": 0,
    },
]


# ---------- CONTEXT BUILDER ----------
def build_context() -> str:
    lines = ["=== TODAY ==="]
    lines.append(f"Today's date: {TODAY}")
    lines.append(f"Next 7 days: {TODAY} to {NEXT_WEEK}")
    lines.append(f"Next 30 days: {TODAY} to {NEXT_MONTH}")

    lines.append("\n=== TEAM OVERVIEW ===")
    lines.append(
        f"Today: {TEAM_STATS['members_planned_today']} members planned "
        f"{TEAM_STATS['tasks_planned_today']} tasks, "
        f"totaling {TEAM_STATS['hours_planned_today']} hours."
    )

    lines.append("\n=== TEAM MEMBERS ===")
    for m in TEAM_MEMBERS:
        leave = f" | On leave: {m['leaves_this_week']}" if m["leaves_this_week"] else ""
        lines.append(
            f"- {m['name']} ({m['role']}): "
            f"{m['hours_planned_today']}h planned today, "
            f"{m['open_tasks']} open tasks, "
            f"skills: {', '.join(m['skills'])}{leave}"
        )

    lines.append("\n=== OPEN TASKS ===")
    for t in TASKS:
        assignee = t["assignee"] or "UNASSIGNED"
        lines.append(
            f"- {t['id']}: {t['title']} | assignee: {assignee} | "
            f"priority: {t['priority']} | deadline: {t['deadline']} | "
            f"skills needed: {', '.join(t['required_skills'])}"
        )

    lines.append("\n=== LEAVES THIS WEEK ===")
    for l in LEAVES:
        lines.append(
            f"- {l['employee']}: {l['dates']} (priority: {l['priority']}, {l['reason']})"
        )

    lines.append("\n=== CLIENT MEETINGS ===")
    for c in CLIENT_MEETINGS:
        lines.append(
            f"- {c['client']}: {c['type']} on {c['date']} "
            f"(follow-up needed: {c['needs_follow_up']})"
        )

    lines.append("\n=== LEADS ===")
    for lead in LEADS:
        lines.append(
            f"- {lead['name']} (source: {lead['source']}, "
            f"priority: {lead['priority']}, surfaced: {lead['surfaced']})"
        )

    lines.append("\n=== PROPOSALS ===")
    for p in PROPOSALS:
        lines.append(
            f"- {p['client']} | {p['event_type']} on {p['event_date']} | "
            f"status: {p['status']} | value: {p['value_sar']} SAR"
        )

    lines.append("\n=== UPCOMING EVENTS ===")
    for e in EVENTS:
        lines.append(
            f"- {e['name']} in {e['city']} on {e['date']} (client: {e['client']})"
        )

    # ---------- PRE-COMPUTED TIME SUMMARY ----------
    lines.append("\n=== TIME-BASED EVENT SUMMARY (pre-computed) ===")
    today_dt = date.today()
    week_end = today_dt + timedelta(days=7)
    month_end = today_dt + timedelta(days=30)

    events_this_week = []
    events_this_month = []
    events_by_city = {}

    for e in EVENTS:
        ed = date.fromisoformat(e["date"])
        city = e["city"]
        events_by_city.setdefault(city, []).append(e)

        if today_dt <= ed <= week_end:
            events_this_week.append(e)
        if today_dt <= ed <= month_end:
            events_this_month.append(e)

    if events_this_week:
        lines.append("Events in the NEXT 7 DAYS:")
        for e in events_this_week:
            lines.append(f"  - {e['name']} in {e['city']} on {e['date']}")
    else:
        lines.append("Events in the NEXT 7 DAYS: none")

    if events_this_month:
        lines.append("Events in the NEXT 30 DAYS:")
        for e in events_this_month:
            lines.append(f"  - {e['name']} in {e['city']} on {e['date']}")
    else:
        lines.append("Events in the NEXT 30 DAYS: none")

    lines.append("Events grouped by CITY:")
    for city, evs in events_by_city.items():
        lines.append(f"  {city}:")
        for e in evs:
            lines.append(f"    - {e['name']} on {e['date']}")

    # ---------- EQUIPMENT ----------
    lines.append("\n=== EQUIPMENT INVENTORY ===")
    for eq in EQUIPMENT:
        if "available_sqm" in eq:
            lines.append(
                f"- {eq['item']}: {eq['available_sqm']} sqm available "
                f"of {eq['total_sqm']} total"
            )
        else:
            lines.append(
                f"- {eq['item']}: {eq['available_units']} units available "
                f"of {eq['total_units']} total"
            )

    lines.append("\n=== PIPELINE (this quarter) ===")
    lines.append(f"- Target: {PIPELINE['target_this_quarter_sar']} SAR")
    lines.append(f"- Won so far: {PIPELINE['won_this_quarter_sar']} SAR")
    lines.append(f"- In review: {PIPELINE['in_review_sar']} SAR")
    lines.append(f"- Exhibition events won: {PIPELINE['exhibition_events_won']}")
    lines.append(f"- Private events won: {PIPELINE['private_events_won']}")
    lines.append(f"- Average profit margin: {PIPELINE['avg_profit_margin_percent']}%")
    lines.append(
        f"- Win ratio: {PIPELINE['win_ratio_percent']}% "
        f"(target: {PIPELINE['win_ratio_target_percent']}%)"
    )

    lines.append("\n=== CLIENT KPIs (LTV / CAC / Win ratio) ===")
    for c in CLIENT_KPIS:
        ratio = (
            round(c["proposals_won"] / c["proposals_submitted"] * 100)
            if c["proposals_submitted"] > 0
            else 0
        )
        lines.append(
            f"- {c['client']}: "
            f"LTV {c['lifetime_value_sar']} SAR, "
            f"CAC {c['acquisition_cost_sar']} SAR, "
            f"proposals {c['proposals_won']}/{c['proposals_submitted']} won "
            f"({ratio}% win ratio)"
        )

    return "\n".join(lines)