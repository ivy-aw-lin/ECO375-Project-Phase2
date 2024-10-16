* Define a variable ${root} which points to the root folder of the repository
setroot

* Erase our YAML results file (if it exists) so the code writes it from scratch
capture erase "${root}/results/example.yaml"

* Load the data
use "${root}/data/raw/auto.dta", clear

* List the first 3 observations
list in 1/3

* Calculate descriptive statistics like the mean
sum mpg, d
return list
yamlout using "${root}/results/example.yaml", key(average_mpg) value(`=r(mean)')

* Run an OLS regression
reg price mpg foreign
reg price mpg foreign, coeflegend
di "Coefficient and Standard Error for mpg: `=_b[mpg]' (`=_se[mpg]')"
di "Coefficient and Standard Error for foreign: `=_b[foreign]' (`=_se[foreign]')"
di "Coefficient and Standard Error for constant: `=_b[_cons]' (`=_se[_cons]')"
ereturn list
yamlout using "${root}/results/example.yaml", key(ols_slope_mpg) value(`=_b[mpg]')
