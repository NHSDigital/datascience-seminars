# README

> [!IMPORTANT]  
> The data from this workshop is taken from the [Artificial data pilot]( Artificial data pilot - NHS England Digital)

## Housekeeping (5 mins)
For this workshop I expect:
- Professionalism
- Focus

## Introduction to Python (15 mins)

### How to read Python script

```python
a = 1
b = a
```

```python
a = 1
b = 1
c = a + b
```

```python
a = 1
b = a + 2
b = b*4
c = b + 4
```

```python
a = 1
b = 2
b = a + b*3
c = b + 4
```

### How to run Python

### Library

```python
import pandas as pd
import datetime
```

## How to print and access Pandas info (15 mins)

### Print Function
```python
a = 1
print(a)
b = 2
print(b)
b = a + b*3
print(b)
c = b + 4
print(c)
```
### To access information from Pandas table

|    |   FYEAR |   PARTYEAR |       EPIKEY |        AEKEY | PSEUDO_HESID                     | ADMIDATE   | ADMIMETH   |   ADMINCAT |   ADMINCATST |   ADMISORC | ALCDIAG_4   |   ALCFRAC | AT_GP_PRACTICE   | AT_RESIDENCE   | AT_TREATMENT   | CANNET   | CANREG   | CAUSE_3   | CAUSE_4   | CCG_GP_PRACTICE   | CCG_RESIDENCE   | CCG_RESPONSIBILITY   |   CCG_RESPONSIBILITY_ORIGIN | CCG_TREATMENT   |   CCG_TREATMENT_ORIGIN |   CLASSPAT | CR_GP_PRACTICE   | CR_RESIDENCE   | CR_TREATMENT   | DIAG_3_01   | DIAG_3_02   | DIAG_3_03   | DIAG_3_04   | DIAG_3_05   | DIAG_3_06   | DIAG_3_07   | DIAG_3_08   | DIAG_3_09   | DIAG_3_10   | DIAG_3_11   | DIAG_3_12   | DIAG_3_13   | DIAG_3_14   |   DIAG_3_15 | DIAG_3_16   | DIAG_3_17   |   DIAG_3_18 | DIAG_3_19   |   DIAG_3_20 | DIAG_3_CONCAT                               | DIAG_4_01   | DIAG_4_02   | DIAG_4_03   | DIAG_4_04   | DIAG_4_05   | DIAG_4_06   | DIAG_4_07   | DIAG_4_08   | DIAG_4_09   | DIAG_4_10   | DIAG_4_11   | DIAG_4_12   | DIAG_4_13   | DIAG_4_14   |   DIAG_4_15 | DIAG_4_16   | DIAG_4_17   |   DIAG_4_18 | DIAG_4_19   |   DIAG_4_20 | DIAG_4_CONCAT                                          |   DIAG_COUNT | DISDATE    |   DISDEST |   DISMETH | ELECDATE   |   ELECDUR |   ELECDUR_CALC |   EPIDUR | EPIEND     |   EPIORDER | EPISTART   |   EPISTAT |   EPITYPE | ETHNOS   |   FAE |   FAE_EMERGENCY |   FCE |   FDE | GORTREAT   | GPPRAC   |   MAINSPEF |   MYDOB |   NEODUR | OPERTN_3_01   | OPERTN_3_02   | OPERTN_3_03   | OPERTN_3_04   | OPERTN_3_05   |   OPERTN_3_06 |   OPERTN_3_07 |   OPERTN_3_08 |   OPERTN_3_09 |   OPERTN_3_10 |   OPERTN_3_11 |   OPERTN_3_12 |   OPERTN_3_13 |   OPERTN_3_14 |   OPERTN_3_15 |   OPERTN_3_16 |   OPERTN_3_17 |   OPERTN_3_18 |   OPERTN_3_19 |   OPERTN_3_20 |   OPERTN_3_21 |   OPERTN_3_22 |   OPERTN_3_23 |   OPERTN_3_24 | OPERTN_3_CONCAT   | OPERTN_4_01   | OPERTN_4_02   | OPERTN_4_03   | OPERTN_4_04   | OPERTN_4_05   |   OPERTN_4_06 |   OPERTN_4_07 |   OPERTN_4_08 |   OPERTN_4_09 |   OPERTN_4_10 |   OPERTN_4_11 |   OPERTN_4_12 |   OPERTN_4_13 |   OPERTN_4_14 |   OPERTN_4_15 |   OPERTN_4_16 |   OPERTN_4_17 |   OPERTN_4_18 |   OPERTN_4_19 |   OPERTN_4_20 |   OPERTN_4_21 |   OPERTN_4_22 |   OPERTN_4_23 |   OPERTN_4_24 | OPERTN_4_CONCAT     |   OPERTN_COUNT | PCON   | PCON_ONS   | PCTCODE_HIS   |   PCTORIG_HIS | PCTTREAT   | PROCODE3   | PROCODE5   | PROCODET   | PURCODE   |   RANK_ORDER |   RESCTY | RESCTY_ONS   | RESGOR   | RESGOR_ONS   | RESLADST   | RESLADST_ONS   | RESPCT_HIS   | RESSTHA_HIS   |   SEX | SITETRET   | LSOA01    | MSOA01    |   SPELBGIN |   SPELDUR |   SPELDUR_CALC | SPELEND   |   STARTAGE |   STARTAGE_CALC | STHATRET   | SUSHRG   |       SUSRECID |   TRETSPEF | LSOA11    | MSOA11    |   WAITLIST |   ALCNRWFRAC | ALCNRWDIAG   |   ALCBRDFRAC | ALCBRDDIAG   |   SITEDIST |   SITEDIST_FLAG |   PROVDIST |   PROVDIST_FLAG |   HRG40 |   HRGLATE35 | NER_GP_PRACTICE   | NER_RESIDENCE   | NER_TREATMENT   |
|---:|--------:|-----------:|-------------:|-------------:|:---------------------------------|:-----------|:-----------|-----------:|-------------:|-----------:|:------------|----------:|:-----------------|:---------------|:---------------|:---------|:---------|:----------|:----------|:------------------|:----------------|:---------------------|----------------------------:|:----------------|-----------------------:|-----------:|:-----------------|:---------------|:---------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|------------:|:------------|:------------|------------:|:------------|------------:|:--------------------------------------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|------------:|:------------|:------------|------------:|:------------|------------:|:-------------------------------------------------------|-------------:|:-----------|----------:|----------:|:-----------|----------:|---------------:|---------:|:-----------|-----------:|:-----------|----------:|----------:|:---------|------:|----------------:|------:|------:|:-----------|:---------|-----------:|--------:|---------:|:--------------|:--------------|:--------------|:--------------|:--------------|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|:------------------|:--------------|:--------------|:--------------|:--------------|:--------------|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|:--------------------|---------------:|:-------|:-----------|:--------------|--------------:|:-----------|:-----------|:-----------|:-----------|:----------|-------------:|---------:|:-------------|:---------|:-------------|:-----------|:---------------|:-------------|:--------------|------:|:-----------|:----------|:----------|-----------:|----------:|---------------:|:----------|-----------:|----------------:|:-----------|:---------|---------------:|-----------:|:----------|:----------|-----------:|-------------:|:-------------|-------------:|:-------------|-----------:|----------------:|-----------:|----------------:|--------:|------------:|:------------------|:----------------|:----------------|
|  0 |    2021 |     202099 | 406111899172 | 964210830588 | TESTiJLlLWNNzwDWQwc1km6K55HsW0xS | 2020-06-16 | 21         |          1 |          nan |         19 | nan         |      0    | Q49              | Q71            | Q56            | N29      | Y0201    | nan       | Y95X      | 84H               | 92G             | 05A                  |                           1 | 97R             |                      1 |          3 | Y62              | Y59            | Y56            | R41         | E28         | C78         | X62         | nan         | nan         | K44         | nan         | nan         | nan         | nan         | nan         | nan         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | R41,E28,C78,X62,K44                         | R410        | E282        | C780        | X620        | nan         | nan         | K449        | nan         | nan         | nan         | nan         | nan         | nan         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | R410,E282,C780,X620,K449                               |            5 | 2020-11-10 |        98 |         8 | 2020-06-16 |        87 |             10 |        0 | 2020-06-16 |          1 | 2020-06-16 |         3 |         1 | A        |     0 |               0 |     1 |     1 | E          | J82646   |        110 |   41966 |      nan | -             | A55           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -  ,A55           | -             | A559          | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -   ,A559           |              1 | C95    | E14000695  | 5QF           |             1 | 5MD        | RK9        | RGP00      | R0A        | 15N00     |            1 |       00 | E99999999    | G        | E12000008    | 38UE       | E06000042      | 5P5          | Q39           |     1 | RM346      | E01003617 | E02003263 |          2 |         1 |              8 | Y         |         55 |         54.7014 | Q39        | BZ34C    | 58014155730769 |        424 | E01007002 | E02002407 |          0 |    0         | nan          |     0        | I48          |       2.38 |               5 |      20.96 |               3 |     nan |         nan | QJK               | QOP             | QHM             |
|  1 |    2021 |     202099 | 255765609232 | 181876493987 | TESTiJLlLWNNzwDWQwc1km6K55HsW0xS | 2020-05-28 | 21         |          1 |          nan |         19 | I10X        |      0    | Q51              | Q37            | Y              | N22      | Y0201    | nan       | nan       | 13T               | 05Y             | 08G                  |                           1 | 27D             |                      1 |          1 | Y60              | Y56            | Y59            | I21         | Z03         | I10         | N17         | J43         | nan         | nan         | nan         | nan         | nan         | nan         | nan         | nan         | nan         |         nan | nan         | R54         |         nan | nan         |         nan | I21,Z03,I10,N17,J43,R54                     | I214        | Z038        | I10X        | N179        | J439        | nan         | nan         | nan         | nan         | nan         | nan         | nan         | nan         | nan         |         nan | nan         | R54X        |         nan | nan         |         nan | I214,Z038,I10X,N179,J439,R54X                          |            6 | nan        |        19 |         1 | 2020-05-28 |         2 |              4 |        1 | 2020-09-28 |          1 | 2020-05-28 |         3 |         1 | A        |     1 |               0 |     1 |     1 | H          | J82039   |        300 |   41966 |      nan | W24           | nan           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | W24               | W246          | nan           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | W246                |              1 | A20    | E14000996  | 5PL           |             1 | 5NL        | RN5        | RHM00      | RXH        | 08E       |          nan |       18 | E99999999    | J        | E12000009    | 00HY       | E08000003      | 5AT          | Q33           |     1 | RLQ01      | E01024898 | E02004672 |          2 |         0 |              1 | Y         |         55 |         54.9452 | Q34        | NZ42A    | 48269450608855 |        300 | E01002933 | nan       |          0 |    0.0909804 | nan          |     1        | nan          |       7.47 |               5 |      88.71 |               3 |     nan |         nan | QT1               | QM7             | QNC             |
|  2 |    2021 |     202099 | 731480873960 | 803179514887 | TESTiJLlLWNNzwDWQwc1km6K55HsW0xS | 1801-01-01 | 21         |          1 |          nan |         19 | nan         |      0.18 | Y                | Q70            | Q56            | N27      | Y0401    | nan       | nan       | 03W               | 15E             | 15M                  |                           1 | 93C             |                      1 |          1 | Y59              | Y58            | Y62            | A09         | E11         | nan         | nan         | C67         | H93         | nan         | nan         | Z92         | nan         | nan         | nan         | Z87         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | A09,E11,C67,H93,Z92,Z87                     | A099        | E119        | nan         | nan         | C679        | H931        | nan         | nan         | Z926        | nan         | nan         | nan         | Z871        | nan         |         nan | nan         | nan         |         nan | nan         |         nan | A099,E119,C679,H931,Z926,Z871                          |            6 | 1801-01-01 |        19 |         1 | 1801-01-01 |         2 |             59 |        0 | 1801-01-01 |          1 | 1801-01-01 |         3 |         1 | A        |     1 |               1 |     1 |     1 | A          | C81090   |        410 |   41966 |      nan | C46           | Y53           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | C46,Y53           | C468          | Y534          | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | C468,Y534           |              2 | C48    | E14000872  | 5PQ           |             1 | 5PT        | RX1        | RA200      | RVW        | 91Q       |          nan |       22 | E10000030    | D        | E12000005    | 47UF       | E07000140      | 5A3          | Q38           |     1 | RH801      | E01010005 | E02004245 |          2 |         0 |              7 | Y         |         54 |         54.2658 | Q31        | SB97Z    | 10706735967195 |        502 | E01014240 | E02005907 |          0 |    0         | J18          |     0        | nan          |       4.22 |               5 |      13.81 |               5 |     nan |         nan | QOP               | QF7             | QRL             |
|  3 |    2021 |     202099 | 682563308547 | 717571868364 | TESTiJLlLWNNzwDWQwc1km6K55HsW0xS | 2020-06-23 | 21         |          1 |          nan |         19 | nan         |      0    | Y                | Q60            | Y              | N26      | Y0301    | nan       | nan       | 15N               | 05Y             | 06A                  |                           1 | 78H             |                      1 |          2 | Y61              | Y63            | Y60            | U07         | K29         | C78         | E87         | nan         | nan         | nan         | nan         | nan         | I10         | Z50         | nan         | nan         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | U07,K29,C78,E87,I10,Z50                     | U071        | K297        | C787        | E877        | nan         | nan         | nan         | nan         | nan         | I10X        | Z501        | nan         | nan         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | U071,K297,C787,E877,I10X,Z501                          |            6 | 2020-07-17 |        19 |         1 | 1801-01-01 |        46 |             16 |        2 | 2020-07-17 |          4 | 2020-07-17 |         3 |         1 | A        |     0 |               1 |     0 |     1 | B          | P82609   |        501 |   41966 |      nan | -             | X72           | nan           | Z94           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -  ,X72,Z94       | -             | X721          | nan           | Z942          | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -   ,X721,Z942      |              2 | F34    | E14000869  | 5A7           |             1 | 5H8        | RXR        | R1F00      | RTX        | 91Q       |          nan |       00 | E99999999    | A        | E12000008    | 00AS       | E08000036      | 5K7          | Q35           |     1 | RTGFG      | E01001281 | E02001158 |          2 |         3 |              0 | Y         |         54 |         54.2658 | Q31        | EB08E    | 15696109869578 |        110 | E01007300 | E02003460 |          0 |    0         | nan          |     0.153979 | W18          |      19.35 |               5 |       6.8  |               3 |     nan |         nan | QHL               | QK1             | QU9             |
|  4 |    2021 |     202099 | 253030371090 | 186017970650 | TESTiJLlLWNNzwDWQwc1km6K55HsW0xS | 2020-09-10 | 11         |          1 |          nan |         19 | nan         |      0    | Q56              | Q54            | Q60            | N35      | Y0801    | nan       | nan       | 27D               | 03W             | 36L                  |                           1 | 05W             |                      1 |          1 | Y59              | Y61            | Y62            | Z38         | G43         | G40         | B18         | I79         | nan         | nan         | nan         | Z96         | nan         | nan         | nan         | Z92         | nan         |         nan | I10         | nan         |         nan | nan         |         nan | Z38,G43,G40,B18,I79,Z96,Z92,I10             | Z380        | G439        | G409        | B182        | I792        | nan         | nan         | nan         | Z960        | nan         | nan         | nan         | Z921        | nan         |         nan | I10X        | nan         |         nan | nan         |         nan | Z380,G439,G409,B182,I792,Z960,Z921,I10X                |            8 | 2021-01-27 |        51 |         1 | 2020-08-28 |        27 |              2 |        0 | 2020-09-10 |          2 | 2020-09-10 |         3 |         1 | A        |     0 |               1 |     1 |     1 | B          | N81127   |        800 |   41966 |      nan | -             | Z27           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -  ,Z27           | -             | Z274          | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -   ,Z274           |              1 | A10    | E14000693  | 5PQ           |             1 | 5C4        | RVY        | RBT00      | RN5-X      | 01K       |          nan |       18 | E99999999    | B        | E12000004    | 00CQ       | E08000022      | 5M8          | Q31           |     1 | RWDLA      | E01018760 | E02001243 |          2 |         6 |              1 | Y         |         55 |         54.9753 | Q35        | HE12C    | 43803598714800 |        340 | E01009732 | E02001958 |          1 |    0         | nan          |     0.121285 | nan          |       5.41 |               5 |      28.28 |               3 |     nan |         nan | QU9               | QWU             | QE1             |
|  5 |    2021 |     202099 | 219440373765 | 902500792971 | TEST2bGQUKgQbz5W9YyAQfCqg6evVEPW | 2020-10-07 | 12         |          1 |          nan |         19 | nan         |      0    | Q69              | Q32            | Y              | N03      | Y1701    | nan       | nan       | 16C               | 72Q             | 91Q                  |                           1 | 11X             |                      1 |          1 | Y62              | Y60            | Y61            | C67         | Z11         | G30         | R79         | I50         | M51         | nan         | I10         | I48         | F41         | nan         | nan         | J45         | Z91         |         nan | nan         | nan         |         nan | nan         |         nan | C67,Z11,G30,R79,I50,M51,I10,I48,F41,J45,Z91 | C679        | Z115        | G309        | R798        | I501        | M511        | nan         | I10X        | I489        | F419        | nan         | nan         | J459        | Z910        |         nan | nan         | nan         |         nan | nan         |         nan | C679,Z115,G309,R798,I501,M511,I10X,I489,F419,J459,Z910 |           11 | 2020-10-07 |        19 |         1 | 1801-01-01 |        71 |            105 |        1 | 2020-10-07 |          1 | 2020-10-07 |         3 |         1 | K        |     1 |               0 |     1 |     0 | J          | N81123   |        800 |  101963 |      nan | X72           | nan           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | X72               | X724          | nan           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | X724                |              1 | D64    | E14000740  | 5J5           |             1 | 5QC        | RGT        | RXW00      | RTH        | 15C00     |          nan |       18 | E10000024    | H        | E12000007    | 40UC       | E06000035      | 5D7          | Q35           |     2 | RCX70      | E01027581 | E02004415 |          2 |         1 |              0 | Y         |         58 |         57.5041 | Q33        | AA30F    | 15126091823174 |        301 | E01014276 | E02001334 |          0 |    0.0194445 | nan          |     0        | I48          |       2.78 |               5 |      44.24 |               3 |     nan |         nan | QNC               | QH8             | QSL             |
|  6 |    2021 |     202099 |  67537292947 | 332192348098 | TEST2bGQUKgQbz5W9YyAQfCqg6evVEPW | 2020-06-01 | 2D         |          1 |          nan |         19 | nan         |      0    | Q64              | Q39            | Y              | N24      | Y1701    | nan       | nan       | 02A               | 06F             | 93C                  |                           1 | 13T             |                      1 |          1 | Y59              | Y60            | Y63            | Z38         | nan         | E87         | R31         | I25         | R47         | nan         | nan         | F17         | nan         | nan         | nan         | nan         | nan         |         nan | nan         | nan         |         nan | F03         |         nan | Z38,E87,R31,I25,R47,F17,F03                 | Z380        | nan         | E872        | R31X        | I259        | R478        | nan         | nan         | F171        | nan         | nan         | nan         | nan         | nan         |         nan | nan         | nan         |         nan | F03X        |         nan | Z380,E872,R31X,I259,R478,F171,F03X                     |            7 | 2020-12-13 |        98 |         1 | 2020-06-01 |       224 |              3 |       10 | 2020-06-01 |          1 | 2020-06-01 |         3 |         1 | K        |     1 |               1 |     1 |     0 | J          | H81003   |        300 |  101963 |      nan | E03           | nan           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | E03               | E032          | nan           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | E032                |              1 | E52    | E14000804  | 5N2           |             1 | 5M7        | RCB        | R1H00      | RTE        | 13Q       |          nan |       00 | E99999999    | G        | E12000005    | 00AX       | E09000026      | 5PA          | Q32           |     2 | RCB55      | E01029656 | E02000311 |          2 |         0 |              0 | Y         |         57 |         56.9479 | Q35        | JA38B    |  2252623233955 |        800 | E01008866 | E02000211 |          0 |    0         | nan          |     0        | nan          |       6.01 |               5 |       1.66 |               3 |     nan |         nan | QJM               | QOP             | QUE             |
|  7 |    2021 |     202099 | 111441373799 | 692643565686 | TESTW5Bs40ne05VLS6bK4DmW5dWkwxUz | 2020-05-07 | 13         |          1 |          nan |         19 | nan         |      0    | Y                | Q34            | Q52            | N35      | nan      | Y83       | nan       | 00P               | 00T             | 03N                  |                           1 | 26A             |                      1 |          3 | Y58              | Y61            | Y60            | D61         | K70         | G11         | I25         | R29         | R29         | nan         | K31         | nan         | nan         | Z86         | Z86         | Z90         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | D61,K70,G11,I25,R29,R29,K31,Z86,Z86,Z90     | D610        | K709        | G119        | I259        | R296        | R296        | nan         | K318        | nan         | nan         | Z864        | Z864        | Z904        | nan         |         nan | nan         | nan         |         nan | nan         |         nan | D610,K709,G119,I259,R296,R296,K318,Z864,Z864,Z904      |           10 | 2020-11-20 |        79 |         8 | 2020-05-07 |        13 |             34 |        4 | 2020-05-07 |          1 | 2020-05-07 |         3 |         1 | Z        |     1 |               1 |     1 |     1 | G          | A89023   |        110 |   41942 |      nan | -             | nan           | Z94           | Z91           | Z42           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -  ,Z94,Z91,Z42   | -             | nan           | Z942          | Z917          | Z421          |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -   ,Z942,Z917,Z421 |              3 | F30    | E14000614  | 5PL           |             1 | 5EM        | RJE        | RNN00      | RVJ-X      | 06L       |          nan |       00 | E10000007    | D        | E12000009    | 00CR       | E07000177      | 5GC          | Q30           |     1 | RN325      | E01027350 | E02004438 |          0 |         0 |             10 | N         |         79 |         78.5726 | Q31        | DZ19H    | 76361111273626 |        503 | E01009644 | E02004013 |          1 |    0.0497249 | K80          |     0.265684 | J18          |      14.57 |               5 |      27.96 |               3 |     nan |         nan | QHM               | QOQ             | QE1             |
|  8 |    2021 |     202099 | 498876903032 | 335480124698 | TESTW5Bs40ne05VLS6bK4DmW5dWkwxUz | 2020-09-22 | 12         |          1 |          nan |         19 | nan         |      0.13 | Y                | Q54            | Y              | N31      | Y1701    | nan       | nan       | 04F               | 16C             | 13T                  |                           1 | 08V             |                      1 |          1 | Y58              | Y63            | Y58            | Z38         | R10         | Z11         | N08         | nan         | nan         | I51         | R29         | nan         | nan         | nan         | nan         | nan         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | Z38,R10,Z11,N08,I51,R29                     | Z380        | R104        | Z115        | N083        | nan         | nan         | I517        | R296        | nan         | nan         | nan         | nan         | nan         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | Z380,R104,Z115,N083,I517,R296                          |            6 | 2020-09-22 |        19 |         1 | 2020-06-18 |        53 |             59 |        0 | 2020-09-22 |          1 | 2020-09-22 |         3 |         1 | Z        |     1 |               1 |     1 |     0 | J          | G85109   |        800 |   41942 |      nan | -             | nan           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -                 | -             | nan           | nan           | nan           | nan           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | -                   |            nan | F38    | E14000695  | 5MD           |             1 | 5M2        | RTP        | R1H00      | RJE        | 12F00     |          nan |       12 | E10000015    | B        | E12000004    | 30UN       | E07000009      | 5QD          | Q31           |     1 | RWY01      | nan       | E02001656 |          0 |         0 |              0 | Y         |         79 |         78.5616 | Q35        | LA97A    | 21887549387224 |        420 | E01008447 | E02001346 |          0 |    0         | I10          |     0        | Y49          |       2.87 |               5 |      10.99 |               3 |     nan |         nan | QHL               | Q99             | QUE             |
|  9 |    2021 |     202099 | 539258852426 |  13171618718 | TESTW5Bs40ne05VLS6bK4DmW5dWkwxUz | 2020-10-03 | 11         |          1 |          nan |         19 | nan         |      0    | Q70              | Q52            | Y              | nan      | Y0201    | nan       | nan       | 15E               | 15M             | 15D                  |                           1 | 00Y             |                      1 |          1 | Y58              | Y59            | Y59            | H25         | K65         | P07         | D64         | I10         | E11         | nan         | nan         | E87         | T81         | nan         | nan         | nan         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | H25,K65,P07,D64,I10,E11,E87,T81             | H258        | K650        | P071        | D649        | I10X        | E119        | nan         | nan         | E877        | T817        | nan         | nan         | nan         | nan         |         nan | nan         | nan         |         nan | nan         |         nan | H258,K650,P071,D649,I10X,E119,E877,T817                |            8 | 2021-01-21 |        19 |         1 | 2020-10-03 |         7 |              8 |        0 | 2020-10-03 |          4 | 2020-10-03 |         3 |         1 | Z        |     1 |               1 |     1 |     1 | H          | M85009   |        301 |   41942 |      nan | U20           | nan           | nan           | nan           | L72           |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | U20,L72           | U201          | nan           | nan           | nan           | L722          |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan |           nan | U201,L722           |              2 | F33    | E14000819  | 5QW           |             1 | 5N6        | RBD        | RCB00      | RDU        | 00T       |          nan |       00 | E10000012    | J        | E12000005    | 00CN       | E06000060      | 5M2          | Q35           |     1 | RH5A8      | E01008877 | E02001185 |          2 |         0 |              2 | N         |         79 |         78.6466 | Q33        | PX57B    | 53804498748897 |        328 | E01010827 | E02006564 |          0 |    0         | nan          |     0        | I10          |      16.56 |               5 |       6.68 |               3 |     nan |         nan | QWO               | QOQ             | QMF             |

#### Columns

##### All the columns in the table

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

list_of_cols = hes_data.columns

print(list_of_cols)
```

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selected_col = hes_data[['FYEAR', 'PARTYEAR', 'EPIKEY']]

print(selected_col)
```

##### A single column

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selected_col = hes_data[['AEKEY']]

print(selected_col)
```

##### A single row
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selected_row = hes_data.iloc[3]

print(selected_row)
```
##### A entry for a given row and column
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selected_entry = hes_data.iloc[3]['ADMIDATE']

print(selected_entry)
```
## Data types in Pandas (15 mins)

### Numbers
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

number_col = hes_data['DISDEST']

print(number_col)
```

### Strings
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

string_col = hes_data['DIAG_4_01']

print(string_col + 'test')

print(string_col * 2)
```
### Dates?
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

date_looking_col = hes_data['ADMIDATE']

date_col = pd.to_datetime(date_looking_col, format="%Y/%m/%d")

print(date_col)
```
## Break + Stoptake + Retro (15 mins)


## Groupings in Pandas (15mins)

### Aggrating over a single column
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selecting_distances = hes_data[['DISDEST']]

mean_distance = selecting_distances.mean()

print(mean_distance)
```

### Aggrating over a value in a column

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selecting_each_patient = hes_data[['PSEUDO_HESID','DISDEST']]

grouping_agg_distance = selecting_each_patient.groupby('PSEUDO_HESID').agg(['min','max','mean'])

print(grouping_agg_distance)
```

### Aggrating over a value in multple column

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selecting_diag_codes_and_demogr_data = hes_data[['DIAG_4_01','ETHNOS','ELECDUR_CALC']]

grouping_dia_codes = selecting_diag_codes_and_demogr_data.groupby(['DIAG_4_01','ETHNOS']).agg(['mean'])

print(grouping_dia_codes)
```
## Conditional and filterings (15 mins)

### Filtering the strings

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

binary_filter_letter = hes_data['DIAG_4_01'] == 'D610'

filtered_icd10 = hes_data[binary_filter_letter]

print(filtered_icd10)
```

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

binary_filter_letter = hes_data['DIAG_4_01'].str.contains('D')

filtered_icd10 = hes_data[binary_filter_letter]

print(filtered_icd10)
```

### Filtering numbers

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

binary_filter_age = hes_data['STARTAGE_CALC'] < 18

filtered_age = hes_data[binary_filter_age]

print(filtered_age)
```

### Filtering Dates

#### Date range

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

#Create a date
selected_date = datetime.datetime(2020, 6, 7)

#Coverting column to a date
hes_data['ADMIDATE'] = pd.to_datetime(hes_data['ADMIDATE'], format="%Y/%m/%d")

filter_dates_indicator = hes_data['ADMIDATE'] > selected_date

filtered_dates = hes_data[filter_dates_indicator]

print(filtered_dates)
```

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

#Coverting column to a date
hes_data['ADMIDATE'] = pd.to_datetime(hes_data['ADMIDATE'], format="%Y/%m/%d")

filter_month_indicator = hes_data['ADMIDATE'].dt.month == 6

filtered_dates = hes_data[filter_dates_indicator]

print(filtered_dates)
```

### Multipe conditions

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

binary_filter_letter_D = hes_data['DIAG_4_01'].str.contains('D')

binary_filter_letter_E = hes_data['DIAG_4_01'].str.contains('E')

indicator_either_D_or_E = binary_filter_letter_D | binary_filter_letter_E

filtered_icd10 = hes_data[indicator_either_D_or_E]

print(filtered_icd10)
```

## Stoptake + Take away

## END

## Licence
The documentation and the artificial data files are © Crown copyright and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.

