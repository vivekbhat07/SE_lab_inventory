<!-- HTML styled table: paste into README.md -->
<table cellpadding="8" cellspacing="0" border="0" style="border-collapse:collapse; width:100%; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;">
  <thead>
    <tr>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa; font-size:14px;">🧠 <strong>Issue</strong></th>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa; font-size:14px;">🧾 <strong>Type</strong></th>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa; font-size:14px;">🔢 <strong>Line(s)</strong></th>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa; font-size:14px;">🧍‍♂️ <strong>Description</strong></th>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa; font-size:14px;">🛠️ <strong>Fix Approach</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🌀 <strong>Mutable default argument</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">⚙️ Bug</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">12</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Used <code>logs=[]</code> which shares the same list across function calls.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Change default to <code>None</code> and initialize inside the function.</td>
    </tr>

    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🐍 <strong>Non-snake_case function names</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">💅 Style</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Multiple</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Functions like <code>addItem</code>, <code>removeItem</code> did not follow PEP8 naming.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Rename to snake_case: <code>add_item</code>, <code>remove_item</code>, <code>get_qty</code>.</td>
    </tr>

    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">📏 <strong>Missing blank line between functions</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">💅 Style</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Multiple</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Functions were not separated by an empty line, reducing readability and PEP 8 compliance.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Added one blank line between top-level functions.</td>
    </tr>

    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🗒️ <strong>Missing docstrings/comments</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🧾 Documentation</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Multiple</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Functions lacked descriptions, making intent unclear.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Added descriptive triple-quote docstrings to each function and the module header.</td>
    </tr>

    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🧱 <strong>Bare try-except block</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">⚙️ Code Quality</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">24</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Used <code>except:</code> without specifying exception types, which hides errors.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Replace with specific handlers (e.g., <code>except KeyError</code>, <code>except TypeError</code>) and show messages or re-raise.</td>
    </tr>

    <tr>
      <td style="padding:10px 8px;">🔤 <strong>Unsafe string formatting</strong></td>
      <td style="padding:10px 8px;">💡 Readability</td>
      <td style="padding:10px 8px;">14</td>
      <td style="padding:10px 8px;">Used old `%` formatting or concatenation instead of f-strings.</td>
      <td style="padding:10px 8px;">Replaced legacy formatting with f-strings (e.g., <code>f\"{var}\"</code>) for clarity and performance.</td>
    </tr>
  </tbody>
</table>


Question and Answer
1. Which issues were the easiest to fix, and which were the hardest? Why?
Ans: The issue in the flake8 (issue like adding line between fucntion and reomving module which are not in use )report were easy to fix and the pylint was moderate to difficult (issue like using appropriate try expect block and writing the appropriate comment for the fucntiona and converting ) were comapritvly difficult and converting to snake case was bit easy

2.Did the static analysis tools report any false positives? If so, describe one example.
Ans:I think there were no such cases

3.How would you integrate static analysis tools into your actual software development
workflow? Consider continuous integration (CI) or local development practices.
Ans. integrate static tools like pylint(in python ) or linter in javascript so that the file is understandable to other devloper and easy to read and to avoid bad coding practice 
in cicd by enforcing minimum cutoff score to enshore that good quality of code is  depeloyed.


4. What tangible improvements did you observe in the code quality, readability, or potential
robustness after applying the fixes?
Converting function names to snake_case and fixing spacing made the code consistent with Python conventions, speeding peer reviews and onboarding increased readability and Added docstrings and lightweight type hints clarified function contracts and expected behavior, improving maintainability and serving as inline documentation.liminated shared mutable-default bugs: Replacing mutable default arguments with None initialization prevented unexpected state sharing across function calls, removing a class of hard-to-find runtime bugs.
