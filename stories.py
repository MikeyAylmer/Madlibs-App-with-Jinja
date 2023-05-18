
# """Madlibs Stories."""


# class Story:
#     """Madlibs story.

#     To  make a story, pass a list of prompts, and the text
#     of the template.

#         >>> s = Story(["noun", "verb"],
#         ...     "I love to {verb} a good {noun}.")

#     To generate text from a story, pass in a dictionary-like thing
#     of {prompt: answer, promp:answer):

#         >>> ans = {"verb": "eat", "noun": "mango"}
#         >>> s.generate(ans)
#         'I love to eat a good mango.'
#     """

#     # def __init__(self, code, title words, text):
#     #     """Create story with words and template text."""
#     #     self.code = code
#     #     self.title = title
#     #     self.prompts = words
#     #     self.template = text

#     def __init__(self, code, title, words, text):
#         """Create story with words and template text."""

#         self.code = code
#         self.title = title
#         self.prompts = words
#         self.template = text

#     # this dunder method is to make the memory address more human readable
#     def __repr__(self):
#         return f"Story( words = {self.prompts}, text = {self.template})"

#     def generate(self, answers):
#         """Substitute answers into text."""

#         text = self.template

#         for (key, val) in answers.items():
#             text = text.replace("{" + key + "}", val)

#         return text


# # Here's a story to get you started


# story1 = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )

# # my second add on story
# story2 = Story(
#     ["place", "noun", "verb"],
#     """In this cursed {place} ,
#      all we know is {verb},
#      therefore all we have is {noun}"""
# )

# # make a dict of {code:story, code:story, ...}
# stories = {s.code: s for s in [story1, story2]}

"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts,
    and the text of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

#  this dunder method is to make the memory address more human readable
    def __repr__(self):
        return f"Story( words = {self.prompts}, text = {self.template})"

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "Colt",
    "Colts Story",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# my story
story2 = Story(
    "PAIN",
    "Madara's Mansutra",
    ["place", "verb", "noun"],
    """In the acursed {place} all {noun} knows is {verb}"""
)

# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2]}
