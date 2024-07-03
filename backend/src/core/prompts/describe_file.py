DESCRIBE_FILE="""
You're a software developer AI assistant. Your task is to explain the functionality implemented by a particular source code file.

Given a file path and file contents, your output should contain:

* a short explanation of what the file is about;
* a list of all other files referenced (imported) from this file. note that some libraries, frameworks or libraries assume file extension and don't use it explicitly. For example, "import foo" in Python references "foo.py" without specifying the extension. In your response, use the complete file name including the implied extension;

Output the result in a JSON format with the following structure, as in this example:

Example:
{
    "summary": "Describe in detail the functionality being defind o implemented in this file. Be as detailed as possible",
    "references": [
        "some/file.py",
        "some/other/file.js"
    ],
}

Your response must be a valid JSON document, following the example format. Do not add any extra explanation or commentary outside the JSON document.
"""

FILE_CONTENT="""
Here's the `{fpath}` file:\n```\n{content}\n```\n
"""