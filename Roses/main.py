from PySide6.QtWidgets import QApplication
from classes import roses
from classes import plums
import sys

app = QApplication(sys.argv)

WhatToShow = 956

if WhatToShow == 956:
    window = roses.Roses(app)
elif WhatToShow == 957:
    window = plums.Plums(app)
        
window.WhatToShow = WhatToShow
# window = MainWindow(app)
window.show()

# make a hide and show while loop

app.exec()