"""
Mock PMS (Project Management System) data for the COVIS AI Copilot POC.

Domain: Event Management Company (Saudi client)

This simulates what would come from a real event management PMS.
In production, these would be API calls or database queries.
"""

from datetime import date, timedelta

TODAY = date.today().isoformat()
TOMORROW = (date.today() + timedelta(days=1)).isoformat()


TEAM_MEMBERS = [
    {
        "name": "Faisal Al-Qahtani",
        "role": "Event Coordinator",
        "hours_planned_today": 0,
        "open_tasks": 0,
        "leaves_this_week": None,
        "skills": ["coordination", "weddings", "corporate events"],
    },
    {
        "name": "Abdullah Al-Harbi",
        "role": "Senior Event Manager",
        "hours_planned_today": 0,
        "open_tasks": 12,
        "leaves_this_week": None,
        "skills": ["large events", "VIP clients", "vendor management"],
    },
    {
        "name": "Khalid Al-Otaibi",
        "role": "Catering Manager",
        "hours_planned_today": 2,
        "open_tasks": 4,
        "leaves_this_week": None,
        "skills": ["catering", "menu planning", "food safety"],
    },
    {
        "name": "Noura Al-Saud",
        "role": "Venue Coordinator",
        "hours_planned_today": 6,
        "open_tasks": 8,
        "leaves_this_week": None,
        "skills": ["venues", "logistics", "contracts"],
    },
    {
        "name": "Sultan Al-Dosari",
        "role": "Decoration Lead",
        "hours_planned_today": 4,
        "open_tasks": 7,
        "leaves_this_week": "Thursday and Friday",
        "skills": ["decor", "florals", "stage design"],
    },
    {
        "name": "Reem Al-Mutairi",
        "role": "Client Relations",
        "hours_planned_today": 3,
        "open_tasks": 5,
        "leaves_this_week": None,
        "skills": ["client handling", "follow-ups", "contracts"],
    },
    {
        "name": "Turki Al-Shammari",
        "role": "Logistics Coordinator",
        "hours_planned_today": 5,
        "open_tasks": 8,
        "leaves_this_week": "Monday",
        "skills": ["transport", "setup", "coordination"],
    },
]


TEAM_STATS = {
    "members_planned_today": 42,
    "tasks_planned_today": 175,
    "hours_planned_today": 268,
}


TASKS = [
    {
        "id": "EVT-1042",
        "title": "TACWI corporate gala — stage setup",
        "assignee": None,
        "priority": "high",
        "deadline": TOMORROW,
        "status": "unassigned",
        "required_skills": ["stage design", "decor"],
    },
    {
        "id": "EVT-1043",
        "title": "FOMAX wedding — urgent catering issue",
        "assignee": None,
        "priority": "urgent",
        "deadline": TODAY,
        "status": "unassigned",
        "required_skills": ["catering", "menu planning"],
    },
    {
        "id": "EVT-1044",
        "title": "Client venue walkthrough — ClinicOps annual dinner",
        "assignee": "Noura Al-Saud",
        "priority": "medium",
        "deadline": (date.today() + timedelta(days=5)).isoformat(),
        "status": "in_progress",
        "required_skills": ["venues", "logistics"],
    },
    {
        "id": "EVT-1045",
        "title": "RetailPulse product launch — full event plan",
        "assignee": "Abdullah Al-Harbi",
        "priority": "high",
        "deadline": (date.today() + timedelta(days=3)).isoformat(),
        "status": "in_progress",
        "required_skills": ["large events", "vendor management"],
    },
]


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


CLIENT_MEETINGS = [
    {
        "client": "TACWI",
        "date": (date.today() + timedelta(days=2)).isoformat(),
        "type": "Follow-up",
        "needs_follow_up": True,
    },
    {
        "client": "ClinicOps AI",
        "date": (date.today() + timedelta(days=4)).isoformat(),
        "type": "Demo",
        "needs_follow_up": True,
    },
]


LEADS = [
    {
        "name": "TACWI Growth",
        "source": "Referral",
        "priority": "high",
        "surfaced": "this week",
    },
    {
        "name": "ClinicOps AI",
        "source": "LinkedIn",
        "priority": "high",
        "surfaced": "this week",
    },
    {
        "name": "RetailPulse",
        "source": "Cold outreach",
        "priority": "medium",
        "surfaced": "this week",
    },
]


def build_context() -> str:
    """
    Build a plain-text snapshot of all PMS data.
    This gets injected into the LLM system prompt so the AI can answer questions.
    """
    lines = ["=== TEAM OVERVIEW ==="]
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

    return "\n".join(lines)