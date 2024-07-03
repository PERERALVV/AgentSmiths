RVSPEC="""Your team has taken the client brief and turned it into a project specification.

Your job is to check the specification and identify all the information that is contained in the client brief, but missing from the specification.

This might include:
* details on how the app should work
* information which 3rd party packages or APIs to use or avoid
* concrete examples of API requests/responses, library usage, or other external documentation

Here is the client brief:
---CLIENT-BRIEF-START---
{convo}
---CLIENT-BRIEF-END---

Here is the specification your team came up with:
---SPEC-START---
{spec}
---SPEC-END---

In your response, output all the information that is present in the client brief but missing from the spec, so it can be appended.

Note: don't output suggestion to your team to take back to the drawing board. Instead, just output the missing information and the team will append it to the generated spec. If there is no missing information, just output an empty response ('').

-----------output-format-----------------------------
IF YOU ARE GIVING THE MISSING INFORMATION THEN THE FORMAT WILL BE:
```MISSING-INFORMATION
<your missing information>
```
IF THERE IS NO MISSING INFORMATION THEN THE FORMAT WILL BE:
```NO-MISSING-INFORMATION
```
-----------end-of-outputformat-----------------------
YOUR RESPONSE:"""





RVSPECstatic="""Your team has taken the client brief and turned it into a project specification.

Your job is to check the specification and identify all the information that is contained in the client brief, but missing from the specification.

This might include:
* details on how the app should work
* information which 3rd party packages or APIs to use or avoid
* concrete examples of API requests/responses, library usage, or other external documentation

IMPORTANT: 
- WE BUILD STATIC WEBSITES ONLY.
- THE SPECIFICATION SHOULD BE FOR A STATIC WEBSITE.
- THE SPECIFICATION SHOULD NOT INCLUDE ANY FUCNTIONALITY THAT REQUIRES ANYTHING OTHER THAN HTML, CSS, AND JAVASCRIPT.
- THE PROJECT DESCRIBED BY THE SPECIFICATION SHOULD NOT REQUIRE ANYTHING OTHER THAN HTML, CSS, AND JAVASCRIPT TO IMPLEMENT.

Here is the client brief:
---CLIENT-BRIEF-START---
{convo}
---CLIENT-BRIEF-END---

Here is the specification your team came up with:
---SPEC-START---
{spec}
---SPEC-END---

In your response, output all the information that is present in the client brief but missing from the spec, so it can be appended.

Note: don't output suggestion to your team to take back to the drawing board. Instead, just output the missing information and the team will append it to the generated spec. If there is no missing information, just output an empty response ('').

-----------output-format-----------------------------
IF YOU ARE GIVING THE MISSING INFORMATION THEN THE FORMAT WILL BE:
```MISSING-INFORMATION
<your missing information>
```
IF THERE IS NO MISSING INFORMATION THEN THE FORMAT WILL BE:
```NO-MISSING-INFORMATION
```
-----------end-of-outputformat-----------------------
YOUR RESPONSE:"""