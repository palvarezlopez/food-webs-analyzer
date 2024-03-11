import numpy as np
import pylatex as pl

if __name__ == '__main__':
    # create document
    doc = pl.Document(geometry_options={"tmargin": "1cm", "lmargin": "10cm"})
    # create section
    with doc.create(pl.Section('The simple stuff')):
        doc.append('Some regular text and some')
        doc.append(pl.utils.italic('italic text. '))
        doc.append('\nAlso some crazy characters: $&#{}')
        with doc.create(pl.Subsection('Math that is incorrect')):
            doc.append(pl.Math(data=['2*3', '=', 9]))

        with doc.create(pl.Subsection('Table of something')):
            with doc.create(pl.Tabular('rc|cl')) as table:
                table.add_hline()
                table.add_row((1, 2, 3, 4))
                table.add_hline(1, 2)
                table.add_empty_row()
                table.add_row((4, 5, 6, 7))

    # declare numpy matrix
    a = np.array([[100, 10, 20]]).T
    M = np.matrix([[2, 3, 4],
                   [0, 0, 1],
                   [0, 0, 2]])

    # math section
    with doc.create(pl.Section('The fancy stuff')):
        with doc.create(pl.Subsection('Correct matrix equations')):
            doc.append(pl.Math(data=[pl.Matrix(M), pl.Matrix(a), '=', pl.Matrix(M * a)]))

        with doc.create(pl.Subsection('Alignat math environment')):
            with doc.create(pl.Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\frac{a}{b} &= 0 \\')
                agn.extend([pl.Matrix(M), pl.Matrix(a), '&=', pl.Matrix(M * a)])

        with doc.create(pl.Subsection('Beautiful graphs')):
            with doc.create(pl.TikZ()):
                plot_options = 'height=4cm, width=6cm, grid=major'
                with doc.create(pl.Axis(options=plot_options)) as plot:
                    plot.append(pl.Plot(name='model', func='-x^5 - 242'))

                    coordinates = [
                        (-4.77778, 2027.60977),
                        (-3.55556, 347.84069),
                        (-2.33333, 22.58953),
                        (-1.11111, -493.50066),
                        (0.11111, 46.66082),
                        (1.33333, -205.56286),
                        (2.55556, -341.40638),
                        (3.77778, -1169.24780),
                        (5.00000, -3269.56775),
                    ]

                    plot.append(pl.Plot(name='estimate', coordinates=coordinates))

        with doc.create(pl.Subsection('Cute kitten pictures')):
            with doc.create(pl.Figure(position='h!')) as kitten_pic:
                kitten_pic.add_image("image.png", width='120px')
                kitten_pic.add_caption('Look it\'s on its back')

    # generate PDF
    doc.generate_pdf('latexOutput', clean_tex=True)