from drafter import *
from dataclasses import dataclass


@dataclass
class State:
    count: int


@route
def index(state: State) -> Page:
    if state.count < 0:
        state.count = 0
    return Page(state, [
        Image(url='bana.jpg', width=None, height=None),
        "Bananas: " + str(state.count) + "\n",
        Button("+1", "increment"),
        Button("-1", "decrement"),
        Button("+5", "add_five"),
        Button("Reset", "reset_count")
    ])

@route
def increment(state: State) -> Page:
    state.count = state.count + 1
    return index(state)
@route
def decrement(state: State) -> Page:
    state.count = state.count - 1
    return index(state)
@route
def reset_count(state: State) -> Page:
    state.count = 0
    return index(state)
@route
def add_five(state:State) -> Page:
    state.count = state.count + 5
    return (index(state))


set_website_title("Counting Bananas")
set_site_information(
    author="James Wu",
    description="",
    sources="",
    planning="",
    links=[]
)
hide_debug_information()
set_website_framed(False)
start_server(State(5))
