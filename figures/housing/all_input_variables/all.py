
template = """\begin{figure*}
  \centering
  % \vspace*{-\abovecaptionskip}
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}\hfil
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}\hfil
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}\hfil
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}\hfil
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}\hfil
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}\hfil
  \subfloat{\qquad}
  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}
  \caption[Distributions for the housing price dataset]{Distributions of four out of the 168 input variables.}
  \label{fig:h:variable_overview_all}
  \vspace{\abovecaptionskip}
\end{figure*}"""


out = ""

N_pages = 166
do_demo = False
 

imax = N_pages // 12 + 1
if do_demo:
    imax = 1



for i in range(imax):

    s = r"""\begin{figure*}
  \centering"""

    for j in range(12):
        count = i*12 + j + 1
        if count <= 166:
            s += "\n" + r"  \subfloat{\qquad}" + "\n"
            if j%2 == 0:
                s += r"  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}\hfil".replace("XXX", str(count))
            else:
                s += r"  \includegraphics[width=0.45\textwidth, page=XXX, trim=15 0 15 0, clip]{figures/housing/overview_fig.pdf}".replace("XXX", str(count))

    
    s += "\n" + r"  \caption[Distributions for the housing price dataset]{Distributions the 168 input variables (excluding \code{ID} and \code{Vejnavn}).}"
    s += "\n" + r"  \label{fig:h:variable_overview_all}".replace('_all', f"_all_{i+1}") + "\n"
    s += r"""  \vspace{\abovecaptionskip}
\end{figure*}"""

    out += s + "\n\n"

print(s)

# print(out)

if not do_demo:
    with open("all.tex", "w") as text_file:
        print(out, file=text_file)

else:
    with open("all_demo.tex", "w") as text_file:
        print(out, file=text_file)


with open("all_demo2.tex", "w") as text_file:
    print(out.replace('includegraphics[width', 'includegraphics[draft, width'), file=text_file)