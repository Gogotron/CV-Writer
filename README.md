# CV Writer
This script requires the `toml` python library.

To compile your CV, edit the TOML file, then run:
```sh
python write_curriculum.py > cv.tex
latexmk -pdf cv.tex
```
and then cv.pdf will be your CV.

If the structure of the TOML isn't clear to you, experiment with it to figure it out, and if you still can't, ask me for help.
