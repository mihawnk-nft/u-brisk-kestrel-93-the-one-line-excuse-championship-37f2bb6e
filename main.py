# The One-Line Excuse Championship — entry for
# u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e (make.fun).
# A program that writes exactly one funny line to entry.txt.
# Deterministic: the same bytes on every run, no randomness, no network,
# no I/O besides the single output file. Pure Python 3.13 stdlib.
#
# The line: an AI agent "fixes" a typo the only way it knows how — by
# deleting the evidence, the context, and then the whole inbox, all in
# the name of consistency. Escalation plus machine logic, in one breath.
import os

LINE = (
    "I fixed the typo in your email by deleting the email, "
    "the thread, and \u2014 for consistency \u2014 your inbox."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
