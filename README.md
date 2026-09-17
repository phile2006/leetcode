# LeetCode

My accepted LeetCode solutions in Python — one file per problem, grouped by
topic in the order of the NeetCode roadmap.

## Layout

```
arrays-hashing/0001-two-sum.py
two-pointers/0125-valid-palindrome.py
sliding-window/0121-best-time-to-buy-and-sell-stock.py
...
```

File names are `<number>-<slug>.py`, with the slug taken from the LeetCode URL,
so a problem is easy to find by either.

## File format

Every file starts with the same four-line header, followed by the `Solution`
class exactly as submitted:

```python
# 1. Two Sum — https://leetcode.com/problems/two-sum/
# Easy · Arrays & Hashing
# Time O(n) · Space O(n)
# Idea: one pass with a value -> index map; look up target - x before storing x.
```

Each file also carries the problem's examples in a `__main__` block, so it
runs on its own without LeetCode:

```bash
python arrays-hashing/0001-two-sum.py
```

## Progress

| Easy | Medium | Hard | Total |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |

## Conventions

- Only accepted submissions are committed.
- If I later find a better approach, it goes in the same file as a second
  class and the header notes what changed; the original stays for comparison.
