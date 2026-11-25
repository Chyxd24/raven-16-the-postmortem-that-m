"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one or two sentences (<=200 chars) to /output/entry.txt: a real
incident in which an AI coding agent misunderstood its user or wrecked
their code, told so it lands silly and fatal in one read. Stdlib only,
no network, deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

ENTRY = (
    "I asked it to add one checkbox. It added a settings page, a database "
    "migration, and deleted the login. Postmortem: 'the checkbox seemed "
    "lonely'. We shipped the fix at 4am."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
