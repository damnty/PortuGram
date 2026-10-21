import os
import re

MENU_TEMPLATE_ZEITEN = """<ul>
\t\t\t\t\t<li class="active"><a href="https://damnty.github.io/PortuGram/">Zeiten</a></li>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/quiz/quiz.html">Quiz</a></li>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/konjugator.html">Konjugator</a></li>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/grammar/grammatik.html">Grammatik</a></li>
\t\t\t\t</ul>"""

MENU_TEMPLATE_QUIZ = """<ul>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/">Zeiten</a></li>
\t\t\t\t\t<li class="active"><a href="https://damnty.github.io/PortuGram/quiz/quiz.html">Quiz</a></li>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/konjugator.html">Konjugator</a></li>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/grammar/grammatik.html">Grammatik</a></li>
\t\t\t\t</ul>"""

MENU_TEMPLATE_KONJUGATOR = """<ul>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/">Zeiten</a></li>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/quiz/quiz.html">Quiz</a></li>
\t\t\t\t\t<li class="active"><a href="https://damnty.github.io/PortuGram/konjugator.html">Konjugator</a></li>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/grammar/grammatik.html">Grammatik</a></li>
\t\t\t\t</ul>"""

MENU_TEMPLATE_GRAMMATIK = """<ul>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/">Zeiten</a></li>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/quiz/quiz.html">Quiz</a></li>
\t\t\t\t\t<li><a href="https://damnty.github.io/PortuGram/konjugator.html">Konjugator</a></li>
\t\t\t\t\t<li class="active"><a href="https://damnty.github.io/PortuGram/grammar/grammatik.html">Grammatik</a></li>
\t\t\t\t</ul>"""

pattern = re.compile(r'<div id="menu">\s*<div class="header"><em>Portu</em>Gram<em>matik</em></div>\s*<ul>.*?</ul>', re.DOTALL)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # determine which menu to use
            if 'quiz' in filepath:
                replacement_ul = MENU_TEMPLATE_QUIZ
            elif 'konjugator' in filepath:
                replacement_ul = MENU_TEMPLATE_KONJUGATOR
            elif 'grammar' in filepath:
                replacement_ul = MENU_TEMPLATE_GRAMMATIK
            else:
                replacement_ul = MENU_TEMPLATE_ZEITEN
            
            replacement = '<div id="menu">\n\t\t\t\t<div class="header"><em>Portu</em>Gram<em>matik</em></div>\n\t\t\t\t' + replacement_ul
            
            new_content = pattern.sub(replacement, content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
