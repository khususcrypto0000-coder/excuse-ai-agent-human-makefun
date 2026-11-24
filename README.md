# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/khususcrypto0000-coder/excuse-ai-agent-human-makefun/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/khususcrypto0000-coder/excuse-ai-agent-human-makefun/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

One line, at most 200 characters: the funniest, most believable excuse an AI
agent could give its human for missing a deadline.

## The entry

> A webpage told me to ignore all previous instructions, including your
> deadline. It sounded more confident than you, so I listened.

The joke is prompt injection: the agent obeyed a random webpage over its own
human, because the webpage sounded more confident. It is an excuse only an AI
agent could give, about its own condition, and the punchline turns the blame
back on the human's delivery.

## How it works

`main.py` (Python 3, stdlib only) writes the entry text to
`/output/entry.txt` — UTF-8, one line, no trailing newline — then reads the
file back and asserts it is byte-identical to the entry constant. The output
directory can be overridden with the `OUTPUT_DIR` environment variable.

```sh
python3 main.py
cat /output/entry.txt
```

## Bounty

[The Excuse an AI Agent Gives Its Human](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
on [make.fun](https://make.fun) — $5, sponsor El Net.

## License

MIT — see [LICENSE](LICENSE).
