class formatter:
    def __init__(self, input_string):
        self.input_string = input_string
        self.result_dict = {'html': '', 'css': '', 'js': ''}

    def split_and_recognize(self):
        if not self.input_string:
            return self.result_dict

        delimiter = "///"
        parts = self.input_string.split(delimiter)

        html_part = ""
        css_part = ""
        js_part = ""

        for part in parts:
            if "HTML" in part:
                html_part = part.replace("HTML", "")
            elif "CSS" in part:
                css_part = part.replace("CSS", "")
            elif "JS" in part:
                js_part = part.replace("JS", "")

        self.result_dict['html'] = html_part
        self.result_dict['css'] = css_part
        self.result_dict['js'] = js_part

        return self.result_dict
