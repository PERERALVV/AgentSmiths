import re


class CodeSplitter:

    def __init__(self, input_string):
        self.input_string = input_string

    def split_code(self):
        # Define regular expressions for HTML, CSS, and JS parts
        html_pattern = re.compile(r'```html(.*?)```', re.DOTALL)
        css_pattern = re.compile(r'```css(.*?)```', re.DOTALL)
        js_pattern = re.compile(r'```js(.*?)```', re.DOTALL)

        # Extract HTML, CSS, and JS parts using regular expressions
        html_match = re.search(html_pattern, self.input_string)
        css_match = re.search(css_pattern, self.input_string)
        js_match = re.search(js_pattern, self.input_string)

        # Initialize variables to store extracted code
        self.html_code = html_match.group(1).strip() if html_match else ''
        self.css_code = css_match.group(1).strip() if css_match else ''
        self.js_code = js_match.group(1).strip() if js_match else ''

    def display_code(self):
        print("HTML Part:")
        print(self.html_code)

        print("\nCSS Part:")
        print(self.css_code)

        print("\nJS Part:")
        print(self.js_code)


input_string = "```css\nbody{\nbackground-color: red;\n}\n```\n ```html\n<body>\n<body>\n<body>\n<body>\n</body>\n</body>\n</body>\n</body>\n``` \n ```js\nfunction(){\nconsole.log('Hello World!');\n}\n```"


code_splitter = CodeSplitter(input_string)
code_splitter.split_code()
code_splitter.display_code()
