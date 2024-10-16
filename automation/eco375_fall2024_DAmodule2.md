---
geometry: "left=1in,right=1in,top=1.5in,bottom=1in"
fontsize: 10pt
linestretch: 1
colorlinks: true
header-includes:
  - \usepackage{fancyvrb}
  - \usepackage{fvextra}
  - \usepackage{xcolor}
  - \usepackage{enumitem}
  - \usepackage{graphicx}
  - \usepackage[export]{adjustbox}
  - \setlistdepth{20}
  - \renewlist{itemize}{itemize}{20}
  - \renewlist{enumerate}{enumerate}{20}
  - \setlist[itemize]{label=$\cdot$}
  - \setlist[itemize,1]{label=\textbullet}
  - \setlist[itemize,2]{label=--}
  - \setlist[itemize,3]{label=*}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \renewcommand{\headrulewidth}{0pt}
  - \renewcommand{\footrulewidth}{0pt}
  - \fancyhf{}
emoji: true
mustache:
- ./results/module2.yaml
- ./results/validation.yaml.log
---


<!-- Title Page, divided into vertical boxes with a blank space for Crowdmark auto-matching -->
```{=latex}

% First box: 2" high for writing
\vskip -3mm  % Remove extra space between boxes
\textcolor{white}{\frame{
    \minipage[t][2in][t]{\textwidth}
        \vspace{0pt} % Ensures top alignment
        \textcolor{black}{
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %%%%% Content ABOVE the auto-matching region goes here %%%%%
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            \section*{Data Analytics Module 2}
            \subsection*{ECO375 Applied Econometrics}
            \subsection*{Prof. Courtney Ward, University of Toronto, Fall 2024}
        }
    \endminipage
}}

% Second box: 3.5" high, left blank, placeholder for crowdmark automated matching
\vskip -3mm  % Remove extra space between boxes
\textcolor{white}{\frame{
    \minipage[t][3.5in][t]{\textwidth}
        \vspace{0pt}
        % Left intentionally blank
    \endminipage
}}

% Third box: 3" high for writing
\vskip -3mm  % Remove extra space between boxes
\textcolor{white}{\frame{
    \minipage[t][3in][t]{\textwidth}
        \vspace{0pt} % Ensures top alignment
        \textcolor{black}{
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %%%%% Content BELOW the auto-matching region goes here %%%%%
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            This PDF document is automatically generated when you submit your work on Github.
            \vspace{5mm}
            \begin{itemize}
                \item 🔗 Link to the \href{https://github.com/{{GITHUB_REPO}}/}{Github Repository}.
            \end{itemize}
        }
    \endminipage
}}
```


\clearpage

# Data Analytics Module 2: Submitted Answers

\vspace{1cm}

```{=latex}
\color{blue}
\Large
```

Numbers validated: {{VALIDATED_COUNT}} / 6

```{=latex}
\color{black}
\normalsize
```

\vspace{5mm}

- {{VALIDATED_avg_test_score}} The average test score in this sample of districts is **{{avg_test_score}}**.

- {{VALIDATED_avg_student_teacher_ratio}} The average students per teacher in this sample is **{{avg_student_teacher_ratio}}**.

- {{VALIDATED_gap_test_score}} The test score in the 90th percentile is **{{gap_test_score}}** higher than districts in the 10th percentile.

- {{VALIDATED_gap_student_teacher_ratio}} The 90th percentile of student teacher ratio is **{{gap_student_teacher_ratio}}** higher than districts in the 10th percentile.

- {{VALIDATED_ols_slope}} One more student-per-teacher is associated with a **{{ols_slope}}** increase in test score.

- {{VALIDATED_ols_constant}} The constant in this model is **{{ols_constant}}**.

\clearpage

# Data Analytics Module 2: Submitted YAML file

\fvset{fontsize=\scriptsize, frame=single, framesep=2mm, label=results/module2.yaml, numbers=left, breaklines=true, samepage=true}
\VerbatimInput{results/module2.yaml}

\clearpage

# Data Analytics Module 2: Submitted Code

\fvset{fontsize=\scriptsize, frame=single, framesep=2mm, label=submission.do, numbers=left, breaklines=true}
\VerbatimInput{submission.do}

\clearpage
