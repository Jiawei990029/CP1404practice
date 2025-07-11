"""
languages
Estimate: 10 minutes
Actual:   30 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    for language in languages:
        if language.is_dynamic(language.typing):
            print(language.name)

main()