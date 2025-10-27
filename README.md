<!-- 📘 HTML Styled Table: Paste this directly into your README.md -->
<h2>🧩 Known Issue & Fix Summary</h2>

<table cellpadding="8" cellspacing="0" border="0" style="border-collapse:collapse; width:100%; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;">
  <thead>
    <tr>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa;">🧠 <strong>Issue</strong></th>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa;">🧾 <strong>Type</strong></th>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa;">🔢 <strong>Line(s)</strong></th>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa;">🧍‍♂️ <strong>Description</strong></th>
      <th style="text-align:left; border-bottom:2px solid #e1e4e8; padding:10px 8px; background:#f6f8fa;">🛠️ <strong>Fix Approach</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🌀 <strong>Mutable default argument</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">⚙️ Bug</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">12</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Used <code>logs=[]</code> which shared the same list across function calls.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Changed default to <code>None</code> and initialized inside the function.</td>
    </tr>

    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🐍 <strong>Non-snake_case function names</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">💅 Style</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Multiple</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Functions like <code>addItem</code> and <code>removeItem</code> did not follow PEP 8 naming conventions.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Renamed all to snake_case (e.g., <code>add_item</code>, <code>remove_item</code>, <code>get_qty</code>).</td>
    </tr>

    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">📏 <strong>Missing blank line between functions</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">💅 Style</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Multiple</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Functions were not separated by blank lines, reducing readability and PEP 8 compliance.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Added one blank line between top-level functions.</td>
    </tr>

    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🗒️ <strong>Missing docstrings/comments</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🧾 Documentation</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Multiple</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Functions lacked explanations for purpose and parameters.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Added descriptive docstrings (<code>\"\"\"...\"\"\"</code>) to all functions and the module header.</td>
    </tr>

    <tr>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">🧱 <strong>Bare try-except block</strong></td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">⚙️ Code Quality</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">24</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Used a generic <code>except:</code> which hides actual errors.</td>
      <td style="padding:10px 8px; border-bottom:1px solid #e1e4e8;">Replaced with specific exception types (<code>except KeyError</code>, <code>except TypeError</code>) and clearer messages.</td>
    </tr>

    <tr>
      <td style="padding:10px 8px;">🔤 <strong>Unsafe string formatting</strong></td>
      <td style="padding:10px 8px;">💡 Readability</td>
      <td style="padding:10px 8px;">14</td>
      <td style="padding:10px 8px;">Used old <code>%</code> formatting and string concatenation.</td>
      <td style="padding:10px 8px;">Replaced with modern f-strings (e.g., <code>f"{var}"</code>) for readability and performance.</td>
    </tr>
  </tbody>
</table>

---

## 📝 Questions and Answers

**1. Which issues were the easiest to fix, and which were the hardest? Why?**  
The issues reported by **Flake8** (such as adding blank lines between functions and removing unused modules) were the easiest to fix.  
The **Pylint** issues were moderately difficult, especially writing appropriate `try-except` blocks and adding meaningful comments/docstrings.  
Converting function names to snake_case was straightforward once identified.

---

**2. Did the static analysis tools report any false positives? If so, describe one example.**  
No, there were no false positives. All the issues reported were valid and meaningful improvements to the code.

---

**3. How would you integrate static analysis tools into your actual software development workflow?**  
Static analysis tools like **Pylint** (for Python) or **ESLint** (for JavaScript) can be integrated into the development process to enforce good coding practices and readability.  
In CI/CD pipelines, we can set a **minimum Pylint score threshold** or **linting step** before deployment to ensure only high-quality code is merged into the main branch.

---

**4. What tangible improvements did you observe in code quality, readability, or robustness after applying the fixes?**  
Converting function names to **snake_case** and fixing spacing made the code consistent with Python’s PEP 8 standards, improving readability and maintainability.  
Adding **docstrings** and lightweight type hints clarified function contracts and improved understanding for future developers.  
Eliminating shared mutable defaults (changing `logs=[]` to `None`) prevented hidden state-sharing bugs.  
Overall, the code became cleaner, more reliable, easier to maintain, and aligned with industry best practices.
