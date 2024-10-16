setroot

use "${root}/data/raw/caschool.dta", clear

sum testscr, detail
return list

yamlout using "${root}/results/module2.yaml", key(avg_test_score) value(`=r(mean)') replace
yamlout using "${root}/results/module2.yaml", key(gap_test_score) value(`=r(p90)-r(p10)') 

sum str, detail
return list

yamlout using "${root}/results/module2.yaml", key(avg_student_teacher_ratio) value(`=r(mean)') 
yamlout using "${root}/results/module2.yaml", key(gap_student_teacher_ratio) value(`=r(p90)-r(p10)') 

reg testscr str
di "Coefficient and Standard Error for test score: `=_b[str]' (`=_se[str]')"
di "Coefficient and Standard Error for constant: `=_b[_cons]' (`=_se[_cons]')"

yamlout using "${root}/results/module2.yaml", key(ols_slope) value(`=_b[str]')
yamlout using "${root}/results/module2.yaml", key(ols_constant) value(`=_b[_cons]')


