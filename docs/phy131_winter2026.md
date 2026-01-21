[Back to main README](../README.md)
# PHY131, Winter 2026 Quickstart

As of Winter 2026, the automatic Quercus marks upload is broken. So you would have to manually upload them in `Grades > Import` section.

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
PRA_no = 1

[QUERCUS]
quercus_grading = False
login = usrname
password = passwd
browser = Chrome
TFA = None
webpg_course = https://q.utoronto.ca/courses/12345
student_group = R9-MP124

[FILES]
file_in = Pods.xlsx
file_out = Marks.csv
xlsx_colors = FFFFFF, D3D3D3

[GRADING]
PRA_name_prefix = PRA
GradingScheme = PHY131_Practical_W2026
```

Note that all QUERCUS parts are irrelevant, since automatic upload is broken for now...
The only exception is `quercus_grading`, which MUST be set to `False`

## Grading a practical

1. Create a directory with files for that practical of the form `PRA#`, i.e. `PRA2`
2. Change the number of the assignment in `config.txt` (`PRA_no`) variable. i.e. `2` for the 2nd practical.
3. Place `Pods.xlsx` into your practical directory, i.e. `PRA2`. 1st sheet of it is the attendance sheet, and 2nd sheet should contain Pod-specific marks. Make sure that the pods on the 1st sheet correspond to the marks on the 2nd sheet!
4. Run `Marking.py` with `python Marking.py` or using a play button in GUI. It should create a `Marks.csv` file in the directory of your practical.
5. Check that marks make sense!
6. Upload the `Marks.csv` to Quercus in ` Grades > Import `

## Notes on LABs vs DATs
For PRAs, make sure to have students in numerical pods (i.e. "1" or "7").
For DATs, since the students separate into 2 "sub-pods", create a/b variants for
each of the pods (i.e. "1a" and "1b"), and grade each separately.

THE CODE DOES NOT KNOW IF WE ARE DOING LAB/DAT. The only way to differentiate
between those for it is to have pods' numbers being strictly numeric or 
alpha-numeric a/b variants.

As of Jan 20th, you cannot use "Marks" sheet with "1a, 1b" for LABs' grading.
So you will have to put in the grades for pods whose name matches the ones
on the Attendance sheet EXACTLY. i.e. either go full "1, 2, ..." or 
"1a, 1b, 2a,...", you cannot mix between the sheets!
It will be fixed soon (hopefully by the time PRA2 arrives), 
make sure to track the updates in the code!

## Notes on the grading scheme

The script automatically sets individual mark for all attending students as 1. You would have to change that manually if you want to adjust it.
