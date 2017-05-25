# Nearby_Strings

<p>To run with the default output of 10 words: <code>python nearby_strings.py ahead</code></p>
<p>To run with a specified number of outputs (e.g. 20): <code>python nearby_strings.py ahead -n 20</code></p> 
<br>
<ul>
    <li>Allow about 30 seconds for the program to execute - there are many words in /usr/share/dict/words !</li>
    <li>This program uses argparse, which requires Python 2.7 and above</li>
    <li>The input word will never be outputed, even when it technically does have the shortest levenshtein distance.</li>
</ul>
