"""
TEACHABLE SNIPPET: Perceive -> Reason -> Act agent loop
--------------------------------------------------------
This illustrates the *shape* of an agentic loop, not a working flight
booking system. The flight search API call below is a stub — swap
search_flights_api() for a real provider (Amadeus, Skyscanner, Duffel,
etc.) and it'll behave the same way.

The point of the exercise: an agent isn't one function call. It's a
loop that alternates between:
  PERCEIVE - take in new information (user input, tool output)
  REASON   - decide what to do next based on everything perceived so far
  ACT      - take an action (call a tool, ask the user, etc.)

Each step below is tagged with which phase it represents.
"""

from dataclasses import dataclass, field
from datetime import date


# ---------------------------------------------------------------------------
# Fake "world" — stand-ins for real tools/APIs. Replace with real integrations.
# ---------------------------------------------------------------------------

def search_flights_api(origin: str, destination: str, depart_date: date) -> list[dict]:
    """Stub for a real flight search API call."""
    return [
        {"flight_no": "BA112", "airline": "British Airways", "price": 612, "stops": 0},
        {"flight_no": "VS021", "airline": "Virgin Atlantic", "price": 549, "stops": 0},
        {"flight_no": "UA929", "airline": "United",         "price": 480, "stops": 1},
    ]


def ask_user_to_confirm(option: dict) -> str:
    """Stub for surfacing a confirmation prompt to the user."""
    return (
        f"I found {option['airline']} flight {option['flight_no']} "
        f"for ${option['price']} ({option['stops']} stop(s)). "
        f"Shall I book it? (yes/no)"
    )


# ---------------------------------------------------------------------------
# Agent state — the "memory" the agent carries across loop iterations.
# In a real system this might be a message history, a scratchpad, etc.
# ---------------------------------------------------------------------------

@dataclass
class AgentState:
    request: str
    origin: str
    destination: str
    depart_date: date
    max_price: int
    search_results: list = field(default_factory=list)
    chosen_flight: dict | None = None
    pending_confirmation: str | None = None


# ---------------------------------------------------------------------------
# The loop itself
# ---------------------------------------------------------------------------

def run_agent(user_request: str, origin: str, destination: str,
              depart_date: date, max_price: int) -> AgentState:

    # 1. PERCEIVE — take in the initial request + relevant context (today's date)
    state = AgentState(
        request=user_request,
        origin=origin,
        destination=destination,
        depart_date=depart_date,
        max_price=max_price,
    )
    print(f"[PERCEIVE] Got request: '{state.request}' (today={date.today()})")

    # 2. REASON — decide that finding an answer requires a tool call
    print("[REASON] I don't have flight prices in my head — I need to search.")

    # 3. ACT — call the flight search tool
    print(f"[ACT] Calling search_flights_api({origin!r}, {destination!r}, {depart_date})")
    raw_results = search_flights_api(origin, destination, depart_date)

    # 4. OBSERVE — take in the tool's output
    state.search_results = raw_results
    print(f"[OBSERVE] Got {len(raw_results)} flight options back.")

    # 5. REASON — apply the user's constraint (price) to narrow the results
    print(f"[REASON] Filtering results to price <= ${max_price}...")
    affordable = [f for f in state.search_results if f["price"] <= max_price]

    if not affordable:
        print("[REASON] Nothing fits the budget — loop would branch here "
              "(e.g. ask user to raise budget, or widen dates).")
        return state

    # 6. ACT — select the best option from what's left (cheapest, in this case)
    best = min(affordable, key=lambda f: f["price"])
    state.chosen_flight = best
    print(f"[ACT] Selected {best['airline']} {best['flight_no']} at ${best['price']}")

    # 7. REASON — booking is irreversible/costs money, so confirm before acting
    print("[REASON] This action spends money — I should not book without "
          "explicit user approval.")

    # 8. ACT — surface the confirmation request (and stop; the loop would
    #    resume on the NEXT perceive step once the user replies)
    state.pending_confirmation = ask_user_to_confirm(best)
    print(f"[ACT] {state.pending_confirmation}")

    return state


if __name__ == "__main__":
    run_agent(
        user_request="Find me a flight from LHR to JFK next month under $600",
        origin="LHR",
        destination="JFK",
        depart_date=date(2026, 9, 15),
        max_price=600,
    )
