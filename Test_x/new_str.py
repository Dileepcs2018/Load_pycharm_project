file = open("python_text")
line = file.read()
new_line = line.strip()

c_backslash = '\\'
c_dquote = '"'
c_comment = '#'


def chop_comment(line):
    # a little state machine with two state varaibles:
    in_quote = False  # whether we are in a quoted string right now
    backslash_escape = False  # true if we just saw a backslash

    for i, ch in enumerate(line):
        if not in_quote and ch == c_comment:
            # not in a quote, saw a '#', it's a comment.  Chop it and return!
            return line[:i]
        elif backslash_escape:
            # we must have just seen a backslash; reset that flag and continue
            backslash_escape = False
        elif in_quote and ch == c_backslash:
            # we are in a quote and we see a backslash; escape next char
            backslash_escape = True
        elif ch == c_dquote:
            in_quote = not in_quote

    return line

x= chop_comment(new_line)
print(x)