[Back to main README](../README.md)
# PHY131, Winter 2025 Quickstart

As of Winter 2025, the automatic Quercus marks upload is broken. So you would have to manually upload them in `Grades > Import` section.

## First-time setup

Here are the steps you should follow when setting up this repo:
1. git clone this repository and navigate into it.
2. Install all required libraries. For that, use GUI and install libraries listed in [main README](../README.md), or do:
```
pip install -r requirements.txt
```
3. Add the config.txt file with the following contents:

```
[PRA]
PRA_no = 2

[QUERCUS]
login = user
password = passwd
browser = Chrome
TFA = None
webpg_course = https://q.utoronto.ca/courses/12345
student_group = R9-MP124

[QUERCUS]
quercus_grading = False
login = usrname
password = passwd
browser = Chrome
TFA = None
webpg_course = https://q.utoronto.ca/courses/12345

[FILES]
file_in = Pods.xlsx
file_out = Marks.csv
xlsx_colors = FFFFFF, D3D3D3

[GRADING]
PRA_name_prefix = PRA
GradingScheme = PHY131_Practical_W2025
```

Note that all QUERCUS parts are irrelevant, since automatic upload is broken for now...

## Grading a practical

1. Create a directory with files for that practical of the form `PRA#`, i.e. `PRA2`
2. Change the number of the assignment in `config.txt` (`PRA_no`) variable. i.e. `2` for the 2nd practical.
3. Place `Pods.xlsx` into your practical directory, i.e. `PRA2`. 1st sheet of it is the attendance sheet, and 2nd sheet should contain Pod-specific marks. Make sure that the pods on the 1st sheet correspond to the marks on the 2nd sheet!
4. Run `Marking.py` with `python Marking.py` or using a play button in GUI. It should create a `Marks.csv` file in the directory of your practical.
5. Check that marks make sense!
6. Upload the `Marks.csv` to Quercus in ` Grades > Import `

## Notes on the grading scheme

The script automatically sets individual mark for all attending students as 1. You would have to change that manually if you want to adjust it.
