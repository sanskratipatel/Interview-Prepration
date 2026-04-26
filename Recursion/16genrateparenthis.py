def generate_parenthesis(n, open_count=0, close_count=0, ans="", result=None):
    if result is None:
        result = []

    if len(ans) == 2 * n:
        result.append(ans)
        return result

    # Add opening bracket
    if open_count < n:
        generate_parenthesis(n, open_count + 1, close_count, ans + "(", result)

    # Add closing bracket
    if close_count < open_count:
        generate_parenthesis(n, open_count, close_count + 1, ans + ")", result)

    return result


print(generate_parenthesis(3))